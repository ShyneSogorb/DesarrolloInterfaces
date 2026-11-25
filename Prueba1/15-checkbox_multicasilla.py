import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QVBoxLayout, QWidget
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.check1 = QCheckBox("Opcion 1")
        self.check2 = QCheckBox("Opcion 2")
        self.check3 = QCheckBox("Opcion 3")

        casillas = [self.check1, self.check2, self.check3]

        for check in casillas:
            check.stateChanged.connect(self.estado_cambiado)
            layout.addWidget(check)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)



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