import sys
from PySide6.QtWidgets import QApplication, QCheckBox, QComboBox, QGroupBox, QHBoxLayout, QLabel, QListWidget, QMainWindow, QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout, QWidget, QGridLayout
from PySide6.QtCore import QMargins, QSize, QUrl, Qt
from PySide6.QtGui import QDesktopServices

#Define constantes para fácil acceso y modificación en código
TITLE = "Menú lateral con QStackedWidget"

#devuelve un nuevo widget con el layout de entrada
def wrapLayout(layout):
    wdg = QWidget()
    wdg.setLayout(layout)
    return wdg

class InitialContainer(QVBoxLayout):
    def __init__(self):
        super().__init__()

        #Crea el label
        label = QLabel()
        label.setText("Benvingudo a la aplicación")

        #Crea un boton y al hacer click cambia el texto del label anterior
        btn = QPushButton()
        btn.setText("Canvia el mensaje")
        btn.clicked.connect(lambda _: label.setText(
            "Has pinchado en el botón de Bienvenida"
        ))

        #Añade el label y el botón al layout principal
        self.addWidget(label)
        self.addWidget(btn)

class InformationContainer(QVBoxLayout):
    def __init__(self):
        super().__init__()

        #Crea el label con el texto inicial
        label = QLabel()
        label.setText("Esta aplicación muestra como usar un QStackedWidget con un menú lateral")

        #Crea el boton con el texto y al hacer click abrirá el enlace al paco mollá
        btn = QPushButton()
        btn.setText("Abrir web del IES Poeta Paco Mollá")
        btn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://iespacomolla.es/")))

        #añade el label y el botón al layout actual
        self.addWidget(label)
        self.addWidget(btn)

class ConfigContainer(QVBoxLayout):
    def __init__(self):
        super().__init__()

        #Indic los ajustes existentes
        OPTIONS = [
            "Activar modo oscuro",
            "Notificaciones activas",
            "Actualizar automaticamente"
        ]

        #Por cada opción crea un checkbox y lo añade al layout
        boxes = self.checkboxes = [QCheckBox(text) for text in OPTIONS]
        for box in boxes:
            self.addWidget(box)

        #Crea un botón enlazado a la función que muesta los ajustes actuales
        btn = QPushButton()
        btn.setText("Mostrar seleción")
        btn.clicked.connect(self.DisplaySelection)

        #añade el boton al layout
        self.addWidget(btn)

    def DisplaySelection(self):
        #Muestra cada checkox por nombre y si está marcado
        print("Configuración actual:")
        for box in self.checkboxes:
            print(f" - {box.text()}: {box.checkState() == Qt.CheckState.Checked}")


class HolderSelector(QHBoxLayout):
    def __init__(self):
        super().__init__()

        #añade la lista de selección al layout
        selector = self.selector = QListWidget()
        self.addWidget(selector)

        #añade el stack al layout
        stack = self.stack = QStackedWidget()
        self.addWidget(self.stack)

        #Cuando se cambia la seleción se cambia el widget del stack
        selector.currentRowChanged.connect(stack.setCurrentIndex)

    #Añade un widget enlazado a un nombre
    def addStack(self, name, widget):
        self.selector.addItem(name)
        self.stack.addWidget(widget)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Asigna el titulo de la ventana
        self.setWindowTitle(TITLE)

        #crea el contenedor que manejará la seleccion de widget
        holder = HolderSelector()

        #crea cada widget independiente enlazado con su texto de selección
        holder.addStack("Inicio", wrapLayout(InitialContainer()))
        holder.addStack("Información", wrapLayout(InformationContainer()))
        holder.addStack("Configuración", wrapLayout(ConfigContainer()))

        #Añadir al principal
        wdg = QWidget()
        wdg.setLayout(holder)
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

