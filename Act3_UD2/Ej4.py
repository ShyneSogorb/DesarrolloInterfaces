import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QTabWidget

#Define constantes para fácil acceso y modificación en código
TITLE = "Layout vertical con botones"

class Container(QLabel):
    def __init__(self, color):
        super().__init__()

        self.setStyleSheet(f"background-color: {color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        COLORS = ["red","green","blue","yellow"]

        #Asigna el titulo de la ventana
        self.setWindowTitle(TITLE)

        #Crea el widget tab con las opciones a la izquierda
        wdg = QTabWidget()
        wdg.setTabPosition(QTabWidget.TabPosition.West)

        #Por cada color, lo asigna de fondo y usa el nombre de color en mayuscula
        for color in COLORS:
            wdg.addTab(Container(color), color.capitalize())
        
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

