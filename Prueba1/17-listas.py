import sys
from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QMainWindow, QCheckBox, QRadioButton, QVBoxLayout, QWidget
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        lista = QListWidget()

        lista.addItems([f"Option {i+1}" for i in range(10)])
        lista.currentItemChanged.connect(self.item_cambiado)

        self.setCentralWidget(lista)


    def item_cambiado(self, cambiado: QListWidgetItem):
        print(cambiado.text())

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())