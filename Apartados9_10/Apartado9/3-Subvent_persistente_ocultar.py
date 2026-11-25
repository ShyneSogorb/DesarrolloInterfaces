from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout)
import sys
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
        # botón para abrir la subventana
        boton_mostrar = QPushButton("Mostrar subventana")
        boton_mostrar.clicked.connect(self.mostrar_subventana)
        layout.addWidget(boton_mostrar)

        # botón para cerrar la subventana
        boton_cerrar = QPushButton("Ocultar subventana")
        boton_cerrar.clicked.connect(self.ocultar_subventana)
        layout.addWidget(boton_cerrar)

    def ocultar_subventana(self):
        # si la subventana existe y es visible la escondemos
        if self.subventana and self.subventana.isVisible():
            self.subventana.hide()


    def mostrar_subventana(self):
        # si no hay ninguna instancia la guardamos
        if not self.subventana:
            self.subventana = Subventana()

        # y la mostramos
        self.subventana.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
