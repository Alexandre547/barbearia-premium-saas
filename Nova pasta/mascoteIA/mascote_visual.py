import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MascoteWindow(QWidget):
    def __init__(self, image_path="mascote.png"):
        super().__init__()
        self.setWindowTitle("Mascote IA")
        self.setFixedSize(200,200)

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.mascote_label = QLabel(self)
        self.pixmap = QPixmap(image_path)
        if self.pixmap.isNull():
            print(f"Erro: Não foi possivel carregar a imagem em '{image_path}'.Verifique o caminho e o formato")
            self.mascote_label.setText("Erro: imagem não encontrada")
            self.mascote_label.setStyleSheet("color: red; font-size: 10px; qproperty-alignment: AlignCenter;")
            self.mascote_label.adjustSize()
        else:
            self.mascote_label.setPixmap(self.pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.mascote_label.setAlignment(Qt.AlignCenter)
            self.move(QApplication.desktop().screenGeometry().width() - self.width() - 15, QApplication.desktop().screenGeometry().height() - self.height() - 18)

def iniciar_mascote_visual():
        app = QApplication(sys.argv)
        mascote_window = MascoteWindow()
        mascote_window.show()
        sys.exit(app.exec_())
    
if __name__ == '__main__':
    iniciar_mascote_visual()
