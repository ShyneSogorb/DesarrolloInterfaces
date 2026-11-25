from pathlib import Path
import sys
import platform
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel,QMainWindow, QStatusBar, QToolBar, QVBoxLayout, QWidget, QTextEdit
from PySide6.QtGui import QAction, QIcon

# Título de la ventana
TITLE = "Ventana principal con menú, bara de herramientas y barra de estado"

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

class Status(QStatusBar):
    def __init__(self, parent):
        super().__init__(parent)

        #Crea
        label = QLabel()
        self.addPermanentWidget(label)
        label.setText(platform.system())
        



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Establece el título de la ventana
        self.setWindowTitle(TITLE)

        self.buildContent()
        self.buildMenu()
        self.buildTools()

    def buildMenu(self):
        menu = self.menuBar()
        arch = menu.addMenu("&Menú")

    def buildTools(self):
        tools = QToolBar("Tools", self)
        action = QAction("Printer", self,  icon=loadImg("img/printer"), toolTip="Imprimir miedo consuela", shortcut="Ctrl+I")
        #action.
        DISPLAY_TEXT = "Acción lanzada a través del menú, uso del atajo de teclado de la barra de herramientas"
        tools.addAction(loadImg("img/printer"), "Printer", "Ctrkl+I", lambda: print(DISPLAY_TEXT), "Imprimir miedo consuela")

        self.addToolBar(tools)

    def buildContent(self):
        layout = QVBoxLayout()

        main = QHBoxLayout()

        main.addWidget(QLabel("Componente principal"))

        base = QVBoxLayout()
        base.addWidget(QLabel("Componente base 1"))
        base.addWidget(QTextEdit(""))
        main.addLayout(base)


        layout.addLayout(main)
        
        self.setStatusBar(Status(self))
        self.setStatusTip("Listo. Esperando acción ...")


        self.setCentralWidget(createWidgetLayout(layout))
        self.resize(800,800)
        



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
