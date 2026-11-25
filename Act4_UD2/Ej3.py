from pathlib import Path
import sys
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QMainWindow, QVBoxLayout
from PySide6.QtGui import QIcon, QPixmap, Qt

# Título de la ventana
TITLE = "3-Ejercicio3.py"

# Pasa de ruta relativa a absoluta
def abspath(path):
    return str(Path(__file__).parent.absolute() / path)

# Carga una imagen local como icono
def loadImg(path):
    path = abspath(path)
    print(path)
    return QIcon(path)

class imgDialog(QDialog):
    def __init__(self, parent, title, image):
        super().__init__(parent)

        # Establece el título de la ventana y el tamaño de la ventana
        self.setWindowTitle(title)
        self.resize(600,600)

        # Crea un pixel map para la imagen
        pixelMap = QPixmap(abspath(f"img/{image}"))
        pixelMap = pixelMap.scaled(580, 580, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Crea un label con el pixelmap como imagen
        label = QLabel()
        label.setPixmap(pixelMap)

        # Crea un layout con el label y lo usa
        layout = QVBoxLayout()
        layout.addWidget(label)
        
        self.setLayout(layout)
        

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Establece el nombre de la ventana
        self.setWindowTitle(TITLE)

        # Crea el menu
        self.build_menu()

    def build_menu(self):

        # Crea la barra de menu y la opción menú
        menu = self.menuBar()
        arch = menu.addMenu("&Archivo")

        # Crea la primera opción de salir aislada
        arch.addAction(loadImg("img/exit"), "&Salir", self.close, "Ctrl+S")
        arch.addSeparator()

        # Crea la imagen en una nueva ventana
        def show(title, img):
            dg = imgDialog(self, title, img)
            dg.exec()

        # Crea un submenú para mostrar el pato o el pingüino con titulo de ventana e imagen
        subMenu = arch.addMenu("Submenú")
        subMenu.addAction("&Patito", lambda: show("Patito", "duck.jpg"))
        subMenu.addAction("&Pingüino", lambda: show("Pingüino", "penguin.jpeg"))

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
