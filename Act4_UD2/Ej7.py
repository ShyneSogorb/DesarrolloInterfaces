from pathlib import Path
import sys
from PySide6.QtWidgets import QApplication, QLabel,QMainWindow, QToolBar, QWidget, QLineEdit, QDockWidget
from PySide6.QtGui import QIcon, Qt

# Título de la ventana
TITLE = "7-Ejercicio7.py"

# Pasa de ruta relativa a absoluta
def abspath(path):
    return str(Path(__file__).parent.absolute() / path)

# Carga una imagen local como icono
def loadImg(path):
    path = abspath(path)
    print(path)
    return QIcon(path)

# Crea un widget con el layout indicado y lo devuelve
def createWidgetLayout(layout):
    wdg = QWidget()
    wdg.setLayout(layout)
    return wdg

class ColorContainer(QLabel):
    def __init__(self, color):
        super().__init__()

        self.setStyleSheet(f"background-color:{color}")

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        #Establece el titulo de la ventana
        self.setWindowTitle(TITLE)

        # Construye el contenido completo del widget
        self.buildMenu()
        self.buildTools()
        self.buildContent()
    
    def buildMenu(self):
        #Crea la barra de menú con dos menús
        menu = self.menuBar()
        menu.addMenu("&Archivo")
        menu.addMenu("A&yuda")

        # Añade otro menú que generará el dock especificado
        ver = menu.addMenu("&Ver")
        for i, _ in enumerate(range(3), 1):
            ver.addAction(f"Mostrar DOCK {i}", lambda local_index=i: self.addDockWidget(*self.DockGeneration(local_index)))


    def buildTools(self):
        #Crea una barra de herramientas con dos imagenes cualquiera
        tools = QToolBar("Tools", self)
        tools.addAction(loadImg("img/printer"), "Plus")
        tools.addAction(loadImg("img/duck"), "Info")

        # Añade la barra de herramientas al widget
        self.addToolBar(tools)
        

    def DockGeneration(self, index):

        #Encapsula la creación de un dock
        def CreateDock(Name, Content):
            #Crea el dock con el nombre y contenido indicados
            Dock = QDockWidget(Name)
            Dock.setWidget(Content)
            #Establece las dimensiones por defecto del dock
            Dock.setMinimumWidth(100)
            Dock.setMinimumHeight(100)
            Dock.setMinimumSize(100, 100)
            return Dock

        #Selecciona el docker y su contenido en función del indice indicado
        dock = f"DOCK {index}"
        match index:
            case 1: return Qt.DockWidgetArea.LeftDockWidgetArea,    CreateDock(dock, QLineEdit()),
            case 2: return Qt.DockWidgetArea.RightDockWidgetArea,   CreateDock(dock, ColorContainer("yellow")),
            case 3: return Qt.DockWidgetArea.BottomDockWidgetArea,  CreateDock(dock, ColorContainer("blue"))
            case _: raise # Cualquier otro valor es un error

    def buildContent(self):

        # Crea 3 docker flotantes
        for i, _ in enumerate(range(3), 1):
            self.addDockWidget(*self.DockGeneration(i))

        #Establece un widget central simple
        self.setCentralWidget(ColorContainer("grey"))
        

#equivalente al método main
if __name__ == "__main__":
    #carga la aplicacion con los argumentos
    app = QApplication(sys.argv)

    #crea la ventana principal
    window = MainWindow()

    #muestra la ventana principal
    window.show()

    #Espera a cerrar la app para salir
    sys.exit(app.exec())
