from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QStackedLayout, QTabWidget, QWidget)
from PySide6.QtCore import Qt
import sys


class Contenedor(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un layout apilado
        tabs = QTabWidget()

        # Añadimos varios widgets unos sobre otros
        FIELDS = ["orange", "purple", "magenta", "gray", "red"]
        for i,field in enumerate(FIELDS, start=1):
            tabs.addTab(Contenedor(field), field)

        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        self.setCentralWidget(tabs)

        



    # Para ver el funcionamiento de como un widget sustituye al superior en la pila
    # creamos un evento que cuando se pulsen las flechas izquierda y derecha
    # pasemos de un widget a otro, controlando que el proceso sea ciclico e infinito
    def keyPressEvent(self, event):

        # recuperamos el índice
        indice = self.layout.currentIndex()
        # buscamos el indice máximo del layout contando cuantos widgets tiene
        indice_maximo = self.layout.count() - 1

        # dependiendo de la flecha presionada sumamos o restamos
        if event.key() == Qt.Key_Right:
            indice += 1
        elif event.key() == Qt.Key_Left:
            indice -= 1

        # rectificamos el índice para generar el efecto infinito
        if indice > indice_maximo:
            indice = 0
        if indice < 0:
            indice = indice_maximo

        # finalmente establecemos el nuevo índice
        self.layout.setCurrentIndex(indice)

        # continuamos con el evento por defecto
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())