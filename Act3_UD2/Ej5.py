import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout

#Define constantes para fácil acceso y modificación en código
TITLE = "Layout cuadrícula"

class Container(QPushButton):
    def __init__(self, row, column, size):
        super().__init__()
        self.setText(f"{row},{column}{f"-{size+column}" if size > 1 else ""}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Asigna el titulo de la ventana
        self.setWindowTitle(TITLE)

        #La tabla representa el tamaño de cada elemento
        TABLE = [
            [1 for _ in range(4)],  #4 de tamaño 1
            [4],                    #1 de tamaño 4
            [2,2]                   #2 de tamaño 2
        ]

        grid = QGridLayout()

        #recorre cada fila con su indice (r) y contenido (row)
        for r, row in enumerate(TABLE):
            offset = 0

            #recorre la información de la fila obteniendo el tamaño de cada elemento
            for size in row:
                #añade el contenedor en la fila y con el offset acumulado de tamaños anteriores
                grid.addWidget(Container(r, offset, size), r, offset, 1, size)
                offset += size

        #crea el widget y asigna el grid
        wdg = QWidget()
        wdg.setLayout(grid)
        
        #Añadir al principal
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

