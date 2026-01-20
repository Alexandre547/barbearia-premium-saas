import sys
import subprocess
import platform
import webbrowser

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer # QTimer será útil para futuras animações ou tarefas em segundo plano

# --- CLASSE DA JANELA DO MASCOTE (VISUAL) ---
class MascoteWindow(QWidget):
    def __init__(self, image_path="mascote.png"):
        super().__init__()
        self.setWindowTitle("Mascote IA")
        self.setFixedSize(200, 200) # Tamanho fixo para a janela do mascote

        # Torna a janela sem bordas, transparente, sempre no topo e transparente para cliques
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground) # Habilita o fundo transparente

        # Carrega e exibe a imagem do mascote
        self.mascote_label = QLabel(self)
        self.pixmap = QPixmap(image_path)
        if self.pixmap.isNull():
            print(f"Erro: Não foi possível carregar a imagem em '{image_path}'. Verifique o caminho e o formato.")
            self.mascote_label.setText("Erro: Imagem não encontrada")
            self.mascote_label.setStyleSheet("color: red; font-size: 10px; qproperty-alignment: AlignCenter;")
            self.mascote_label.adjustSize()
        else:
            self.mascote_label.setPixmap(self.pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.mascote_label.setAlignment(Qt.AlignCenter)

        # Posiciona a janela no canto inferior direito (você pode ajustar isso)
        screen_rect = QApplication.desktop().screenGeometry()
        self.move(screen_rect.width() - self.width() - 50, screen_rect.height() - self.height() - 50) # 50px de margem

        # Adiciona um evento de clique na janela para abrir a caixa de comando
        # Importante: Como a janela é WindowTransparentForInput, precisamos de um truque para capturar cliques.
        # Uma forma mais simples para começar é tirar Qt.WindowTransparentForInput
        # ou adicionar um botão invisível/overlay que capture o clique.
        # Para começar, vamos remover o WindowTransparentForInput temporariamente para que você possa clicar nela.
        # Depois podemos adicionar funcionalidades mais avançadas para clique.
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool) # Removido Qt.WindowTransparentForInput
        self.mascote_label.mousePressEvent = self.abrir_caixa_comando # Conecta o clique à função

    def abrir_caixa_comando(self, event):
        """Abre uma janela de diálogo para o usuário digitar um comando."""
        dialog = ComandoDialog(self) # 'self' passa a janela do mascote como pai
        dialog.exec_() # Executa a janela de diálogo de forma modal (bloqueia o resto da aplicação até fechar)
        comando_digitado = dialog.get_comando() # Pega o comando digitado pelo usuário

        if comando_digitado: # Se o usuário digitou algo
            self.processar_comando(comando_digitado)

    def processar_comando(self, comando):
        """Processa o comando digitado pelo usuário (lógica do mascote_ai.py)."""
        comando = comando.lower().strip()
        print(f"Mascote AI (recebeu): {comando}") # Para ver no terminal o que o mascote recebeu

        if "abrir bloco de notas" in comando:
            print("Mascote AI: Abrindo o Bloco de Notas...")
            try:
                if platform.system() == "Windows":
                    subprocess.Popen(['notepad.exe'])
                elif platform.system() == "Darwin":
                    subprocess.Popen(['open', '-a', 'TextEdit'])
                elif platform.system() == "Linux":
                    subprocess.Popen(['gedit'])
                else:
                    print("Mascote AI: Sistema operacional não reconhecido para abrir o editor de texto.")
            except FileNotFoundError:
                print("Mascote AI: O programa não foi encontrado. Verifique se está instalado ou se o comando está correto.")
            except Exception as e:
                print(f"Mascote AI: Ocorreu um erro ao tentar abrir o programa: {e}")

        elif "abrir google" in comando:
            print("Mascote AI: Abrindo o Google...")
            try:
                webbrowser.open('https://www.google.com/')
            except Exception as e:
                print(f"Mascote AI: Ocorreu um erro ao tentar abrir o Google: {e}")

        elif "abrir youtube" in comando: # Exemplo de como adicionar mais comandos
            print("Mascote AI: Abrindo o YouTube...")
            try:
                webbrowser.open('https://www.youtube.com/')
            except Exception as e:
                print(f"Mascote AI: Ocorreu um erro ao tentar abrir o YouTube: {e}")

        elif "sair" in comando or "desligar" in comando:
            print("Mascote AI: Desligando. Até mais!")
            QApplication.quit() # Fecha a aplicação PyQt5
            # Ou sys.exit(0) se preferir, mas QApplication.quit() é mais "gentil"

        else:
            print("Mascote AI: Não entendi o comando. Tente novamente.")


# --- CLASSE DA JANELA DE COMANDOS (POP-UP) ---
class ComandoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Comando Mascote")
        self.setFixedSize(300, 80)
        self.comando_digitado = ""

        layout = QVBoxLayout()
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Digite seu comando aqui...")
        self.input_field.returnPressed.connect(self.accept_comando) # Conecta Enter para aceitar o comando

        layout.addWidget(self.input_field)
        self.setLayout(layout)

        # Posiciona a caixa de comando no centro da tela
        self.center_on_screen()

    def accept_comando(self):
        self.comando_digitado = self.input_field.text()
        self.accept() # Fecha a janela de diálogo

    def get_comando(self):
        return self.comando_digitado

    def center_on_screen(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

# --- FUNÇÃO PRINCIPAL PARA INICIAR A APLICAÇÃO ---
def iniciar_mascote_integrado():
    app = QApplication(sys.argv)
    mascote_window = MascoteWindow()
    mascote_window.show()
    sys.exit(app.exec_())

# --- INICIA O PROGRAMA QUANDO O ARQUIVO É EXECUTADO ---
if __name__ == '__main__':
    iniciar_mascote_integrado()