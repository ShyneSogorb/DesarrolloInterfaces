from pathlib import Path
import sys
from PySide6.QtWidgets import QApplication, QDialogButtonBox, QGridLayout, QGroupBox, QHBoxLayout, QLabel,QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QTextEdit
from PySide6.QtGui import QIcon

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


class Container(QWidget):
    def __init__(self, label):
        super().__init__()
        layout = QVBoxLayout()

        #Crea un grupo con un label principal
        self._group = QGroupBox(label)
        layout.addWidget(self._group)
        self.setLayout(layout)
        

    def group(self):
        return self._group


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Establece el título de la ventana
        self.setWindowTitle(TITLE)

        # Crea el widget
        self.buildMenu()        
        self.buildContent()
        

    def buildMenu(self):
        #Crea el menú
        menu = self.menuBar()
        arch = menu.addMenu("Archivo")
        arch.addAction(loadImg("img/exit.png"), "&Salir", "Ctrl+S", self.close)


    def buildContent(self):

        layout = QVBoxLayout()

        # Crea el contenedor y el layout para los botones
        HContainer = Container("Layout Horizontal")
        HLayout = QHBoxLayout()
        HContainer.group().setLayout(HLayout)


        # Genera N_BUTTONS de botones y los añade al layout
        N_BUTTONS = 4
        for i, _ in enumerate(range(N_BUTTONS), 1):
            HLayout.addWidget(QPushButton(f"Botón {i}"))

        #Crea un contenedor y el grid para los textos
        gridContainer = Container("Layout Grid")
        grid = QGridLayout()
        gridContainer.group().setLayout(grid)

        #Encapsula la creación de una linea de Label+LineEdit
        def AddLineInput(NLine):
            lineLayout = QHBoxLayout()
            lineLayout.addWidget(QLabel(f"Línea {NLine}"))
            lineLayout.addWidget(QLineEdit())
            return createWidgetLayout(lineLayout)

        #Crea una linea por cada N_LINES
        N_LINES = 2
        for i, _ in enumerate(range(N_LINES), 1):
            grid.addWidget(AddLineInput(i), i, 1)

        #Añade un text edit en la segunda columna tan alto como lineas haya
        grid.addWidget(QTextEdit("Esto es un QTextEdit"), 1, 2, N_LINES, 1)

        # Añade los contenedores al widget junto con botones de Ok y Cancel
        layout.addWidget(HContainer)
        layout.addWidget(gridContainer)
        layout.addWidget(QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel))

        # Aplica el layout como principal
        self.setCentralWidget(createWidgetLayout(layout))

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
