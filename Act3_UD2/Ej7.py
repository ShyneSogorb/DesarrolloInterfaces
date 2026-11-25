from itertools import product
import sys
from PySide6.QtWidgets import QApplication, QCheckBox, QGroupBox, QLabel, QMainWindow, QPushButton, QSizePolicy, QVBoxLayout, QWidget, QGridLayout
from PySide6.QtCore import QMargins, QSize, Qt

#Define constantes para fácil acceso y modificación en código
TITLE = "Tablero de Ajedrez"

#Define el tamaño del tablero
TILES = 2
SIZE = 128

class Container(QLabel):
    def __init__(self, color):
        super().__init__()
        #Asigna el color de fondo
        self.setStyleSheet(f"background-color: {color}")

#asegura que el número de elementos sea par
TILES = TILES & ~0x01

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Asigna el titulo de la ventana
        self.setWindowTitle(TITLE)

        #Array de colores de rango binario (0-1)
        COLORS = ["black", "white"]

        #Elimina espacio y márgenes
        grid = QGridLayout()
        grid.setSpacing(0)
        grid.setContentsMargins(QMargins())

        #recorre por cada casilla de  
        for i in range(TILES*TILES):

            #si el índice es par y coincide con el par de la fila será blanco, si no coinciden será negro
            color = COLORS[(i & 0x01) == (i // TILES & 0x01)]

            #Set container at row and column
            grid.addWidget(Container(color), i // TILES, i % TILES)

        
        self.setMinimumSize(QSize(SIZE, SIZE))

        #Añade el grid a la ventana principal
        wdg = QWidget()
        wdg.setLayout(grid)
        self.setCentralWidget(wdg)

#si la ejecucion es la principal
if __name__ == "__main__":
    #Crea la app con los argumentos del comando
    app = QApplication(sys.argv)
    #Crea la ventana principal
    mainWindow = MainWindow()
    #Muestra la ventana en pantalla
    mainWindow.show()
    #termina la ejecución de la aplicacion
    sys.exit(app.exec())

