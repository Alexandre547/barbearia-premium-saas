import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

# 1. CONFIGURAÇÕES INICIAIS
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'birigui_premium_key_2026')

# 2. CONEXÃO COM POSTGRESQL (RENDER)
DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        return conn
    except Exception as e:
        print(f"Erro de conexão: {e}")
        return None

# 3. ROTAS DO CLIENTE
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/horarios_disponiveis', methods=['POST'])
def horarios_disponiveis():
    dados = request.json
    data_str = dados['data']
    dt_escolhida = datetime.strptime(data_str, '%Y-%m-%d')
    dt_agora = datetime.now()

    # TRAVA 2: Se a data for anterior a hoje, retorna vazio
    if dt_escolhida.date() < dt_agora.date():
        return jsonify([])

    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT hora_inicio, hora_fim FROM expediente WHERE dia_semana = %s", (dt_escolhida.weekday(),))
    exp = cursor.fetchone()
    
    if not exp:
        conn.close()
        return jsonify([])

    cursor.execute("SELECT to_char(data_hora, 'HH24:MI') as h FROM agendamentos WHERE data_hora::date = %s", (data_str,))
    ocupados = [i['h'] for i in cursor.fetchall()]
    conn.close()

    disponiveis = []
    atual = datetime.combine(dt_escolhida.date(), exp['hora_inicio'])
    fim = datetime.combine(dt_escolhida.date(), exp['hora_fim'])

    while atual <= fim:
        h_str = atual.strftime('%H:%M')
        # TRAVA 3: Se a data for HOJE, só mostra horários posteriores à hora atual
        if dt_escolhida.date() == dt_agora.date():
            if atual > dt_agora + timedelta(minutes=10): # Margem de 10 min para o cliente preencher
                if h_str not in ocupados:
                    disponiveis.append(h_str)
        else:
            if h_str not in ocupados:
                disponiveis.append(h_str)
        
        atual += timedelta(minutes=30)

    return jsonify(disponiveis)

@app.route('/agendar', methods=['POST'])
def agendar():
    d = request.json
    dt_agendamento = datetime.strptime(d['data'], '%Y-%m-%dT%H:%M')
    
    # TRAVA FINAL: Bloqueio total de datas passadas no banco
    if dt_agendamento < datetime.now():
        return jsonify({"status": "erro", "mensagem": "Não é possível agendar no passado!"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO agendamentos (cliente, telefone, servico, valor, data_hora, forma_pagamento) VALUES (%s, %s, %s, %s, %s, %s)",
                (d['cliente'], d['telefone'], d['servico'], d['valor'], d['data'], d['pagamento']))
    conn.commit()
    conn.close()
    return jsonify({"status": "sucesso"})

# 4. ROTAS ADMINISTRATIVAS
ADMIN_HASH = generate_password_hash("1234")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('usuario') == "admin" and check_password_hash(ADMIN_HASH, request.form.get('senha')):
            session['logado'] = True
            return redirect(url_for('admin'))
        return "Acesso negado."
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear() # Limpa os dados de login da sessão
    return redirect(url_for('login')) # Redireciona para a tela de login

@app.route('/admin')
def admin():
    if not session.get('logado'): return redirect(url_for('login'))
    conn = get_db_connection()
    if not conn:
        return "Erro ao conectar ao banco de dados no Render."
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM agendamentos ORDER BY data_hora DESC")
    agendamentos = cursor.fetchall()
    
    cursor.execute("SELECT SUM(valor) as total FROM agendamentos WHERE data_hora::date = CURRENT_DATE")
    res_dia = cursor.fetchone()
    lucro_dia = float(res_dia['total']) if res_dia['total'] else 0.0

    # CÁLCULO DE LUCRO DA SEMANA (PostgreSQL Syntax)
    cursor.execute("SELECT SUM(valor) as total FROM agendamentos WHERE data_hora >= NOW() - INTERVAL '7 days'")
    res_sem = cursor.fetchone()
    lucro_semana = float(res_sem['total']) if res_sem['total'] else 0.0
    
    conn.close()
    return render_template('admin.html', 
                        agendamentos=agendamentos, 
                        lucro_dia=lucro_dia, 
                        lucro_semana=lucro_semana)
@app.route('/deletar/<int:id>', methods=['DELETE'])
def deletar(id):
    # Verifica se o administrador está logado antes de permitir a exclusão
    if not session.get('logado'): 
        return jsonify({"erro": "Não autorizado"}), 403
    
    conn = get_db_connection()
    if not conn:
        return jsonify({"erro": "Erro de conexão"}), 500
        
    try:
        cursor = conn.cursor()
        # Executa o comando de exclusão no PostgreSQL
        cursor.execute("DELETE FROM agendamentos WHERE id = %s", (id,))
        conn.commit()
        return jsonify({"status": "sucesso"})
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)}), 500
    finally:
        cursor.close()
        conn.close()
if __name__ == '__main__':
    app.run(debug=True)

