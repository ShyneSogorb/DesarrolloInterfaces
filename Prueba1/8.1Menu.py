from posixpath import abspath
import random
import sys
from PySide6.QtWidgets import QApplication, QDialogButtonBox, QFontDialog, QFormLayout, QGridLayout, QHBoxLayout, QInputDialog, QMainWindow, QLabel, QPushButton, QStatusBar, QToolBar, QVBoxLayout, QWidget
from PySide6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.construir_menu()
        self.construir_herramientas()


    def construir_menu(self):
        menu = self.menuBar()

        menu_archivo = menu.addMenu("&Menu")

        menu_archivo.addAction("&Prueba")

        submenu_archivo = menu_archivo.addMenu("&Submenu")

        submenu_archivo.addAction("&Subopcion &1")
        submenu_archivo.addAction("&Subopcion &2")

        menu_archivo.addSeparator()
        menu_archivo.addAction(QIcon(abspath("exit.png")), "&Salir", self.close, "Ctrl+Q")

        menu_archivo.addSeparator()

        menu_archivo = menu.addMenu("&Ayuda")
        
        self.setStatusBar(QStatusBar(self))

        

    def construir_herramientas(self):

        self.actionInfo = action = QAction("&Information", self)
        action.setShortcut("Ctrl+I")
        action.triggered.connect(lambda: print("Info irrelevante"))


        tools = QToolBar("Barra de herramientas principal")

        tools.addAction(QIcon(abspath("./imagenes/exit.png")), "S&alir", self.close)

        tools.addAction(self.actionInfo)
        self.addToolBar(tools)

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())