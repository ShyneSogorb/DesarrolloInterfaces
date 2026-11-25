import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QRadioButton, QVBoxLayout, QWidget
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        
        radial1 = QRadioButton("Boton radial")
        radial2 = QRadioButton("Boton radial 2")

        radials = [radial1, radial2]

        for radial in radials:
            radial.toggled.connect(self.estado_cambiado)
            layout.addWidget(radial)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def estado_cambiado(self, estado):
        if estado == 1:
            print("Casilla marcada")
        else:
            print("Casilla desmarcada")

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())