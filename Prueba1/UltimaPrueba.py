from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QMainWindow, QLabel, QStackedLayout, QTabWidget, QVBoxLayout, QWidget)
from PySide6.QtCore import Qt
import sys


class Contenedor(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Contendor principal
        layout = QHBoxLayout()

        #Mapa de distribucion de contenedores. 
        #Representa el contenido de cada layout, cada array contiene el contenido del layout vertical en la posicion horizontal que se encuentra
        SLOTS_COLOR = [
            ["red", "yellow", "purple"],
            ["green"],
            ["red", "purple"]
        ]


        for colors in SLOTS_COLOR:
            #Crea un nuevo vertical layout para cada lista
            HSlot = QVBoxLayout()
            layout.addLayout(HSlot)

            #añade el un contenedor por cada elemento
            for color in colors:
                HSlot.addWidget(Contenedor(color))

        #añade el contenido a la ventana principal
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())