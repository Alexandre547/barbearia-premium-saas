import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def testar_conexao():
    url = os.getenv('DATABASE_URL')
    
    # ADICIONE ESTA LINHA PARA TESTE:
    print(f"URL carregada: {url}") 

    if not url:
        print("❌ ERRO: A DATABASE_URL não foi encontrada no arquivo .env!")
        return

    try:
        conn = psycopg2.connect(url, sslmode='require')
        print("✅ Conectado ao Render!")
        conn.close()
    except Exception as e:
        print(f"❌ Erro: {e}")

testar_conexao()