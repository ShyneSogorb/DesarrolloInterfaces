from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout)
import sys
from PySide6.QtGui import QPalette, QColor  # nuevo
import random


class Subventana(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(240, 120)
        self.setWindowTitle("Subventana")

        # creamos una etiqueta con texto aleatorio que demuestra
        # la persistencia de la subventana
        etiqueta = QLabel(f"Soy una subventana... {random.randint(0, 100)}")

        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # iniciamos la variable de la subventana nula por defecto
        self.subventana = None

        # Le damos un tamaño y un título
        self.setWindowTitle("Ventana principal")
        # dummy widget para un layout
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        OPCIONES = [
            ("Mostrar subventana", self.mostrar_subventana),
            ("Ocultar subventana", self.ocultar_subventana),
            ("Alternar subventana", self.alternar_subventana)
        ]

        for opt in OPCIONES:
            # botón para abrir la subventana
            btn = QPushButton(opt[0])
            btn.clicked.connect(opt[1])
            layout.addWidget(btn)

    def crear_subventana(self):
        # si no hay ninguna instancia la guardamos
        if not self.subventana:
            self.subventana = Subventana()
            paleta = QPalette()
            paleta.setColor(QPalette.Window, QColor(51, 0, 51))
            self.subventana.setPalette(paleta)

    def mostrar_subventana(self):
        self.crear_subventana()

        # y la mostramos
        self.subventana.show()

    def ocultar_subventana(self):
        self.crear_subventana()
    
        # y la mostramos
        self.subventana.hide()

    def alternar_subventana(self):
        self.crear_subventana()
    
        # y la mostramos
        self.subventana.setHidden(not self.subventana.isHidden())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
