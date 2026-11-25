import random
import sys
from PySide6.QtWidgets import QApplication, QFontDialog, QFormLayout, QGridLayout, QHBoxLayout, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btn = btn = QPushButton("Fuente")
        btn.clicked.connect(self.click)


        self.setCentralWidget(btn)

    def click(self):
        confirm, font = QFontDialog.getFont(self)
        if confirm:
            self.btn.setFont(font)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())