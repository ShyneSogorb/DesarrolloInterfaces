from pathlib import Path
import sys
from PySide6.QtWidgets import QApplication, QGroupBox, QHBoxLayout, QMainWindow, QPushButton, QWidget
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

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Establece el nombre de la ventana y el contenido del widget
        self.setWindowTitle(TITLE)
        self.buildContent()

    def buildContent(self):
        #Crea un layout para guardar los botones indicados
        layout = QHBoxLayout()
        N_BUTTONS = 4

        # Se crean tantos botones como se desee y enlazan a la función de establecer color
        for _ in range(N_BUTTONS):
            btn = QPushButton()
            btn.clicked.connect(self.setColor)

            #Establece que se puede checkar, y check por defecto
            btn.setCheckable(True)
            btn.setChecked(True)

            # Simula el click para cambiar el estado a falso a la vez que fuerza llmar a setColor implicitamente
            btn.click()

            #Añade el boton al layout
            layout.addWidget(btn)

        # Añade el layout a un grupo y lo establece como central
        group = QGroupBox("Layout Horizontal")        
        group.setLayout(layout)
        self.setCentralWidget(group)

    def setColor(self):
        # Obtiene el generador del evento y establece el color en función de si está activo
        sender: QPushButton = self.sender()
        sender.setStyleSheet(f"background-color:{"red" if sender.isChecked() else "green"}")
        
        

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
