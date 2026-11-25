import sys
from PySide6.QtWidgets import QApplication, QDoubleSpinBox, QListWidget, QListWidgetItem, QMainWindow, QCheckBox, QRadioButton, QSpinBox, QVBoxLayout, QWidget
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        numero = QDoubleSpinBox()
        numero.setValue(3.1415)
        numero.setPrefix("$")


        self.setCentralWidget(numero)


    def item_cambiado(self, cambiado: QListWidgetItem):
        print(cambiado.text())

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())