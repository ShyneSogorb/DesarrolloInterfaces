import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide6.QtCore import *
from PySide6 import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        casilla = QCheckBox("Casilla verificacion")
        self.setCentralWidget(casilla)


        casilla.setCheckState(Qt.  PartiallyChecked)


        casilla.stateChanged.connect(self.estado_cambiado)

    def estado_cambiado(self, estado):
        if estado == 2:
            print("Casilla marcada")
        elif estado == 0:
            print("Casilla desmarcada")
        else:
            print("Casilla neutra")

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())