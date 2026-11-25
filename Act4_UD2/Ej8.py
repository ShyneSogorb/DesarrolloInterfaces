from pathlib import Path
import sys
from PySide6.QtWidgets import QApplication, QColorDialog, QDialog, QDialogButtonBox, QFontDialog, QHBoxLayout, QLabel,QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit
from PySide6.QtGui import QColor, QFont, QIcon, Qt

# Título de la ventana
TITLE = "Preferencias de Usuario"

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

class Settings:
    def __init__(self):
        self.bgColor = QColor("white")
        self.font = QFont()

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        #Crea los ajustes definitivos y temporales
        self._settings = Settings()
        self._tmp_settings = Settings()

        #Establece el titulo de la ventana
        self.setWindowTitle(TITLE)

        # Construye el contenido completo del menú
        self.buildMenu()
        self.buildContent()

    
    def buildMenu(self):
        # Crea la barra de menú con un único menú
        menu = self.menuBar()
        menu.addMenu("&Configuración")

    def buildContent(self):
        # Crea un layout simple
        layout = QVBoxLayout()

        # Crea el texto principal, lo añade al layout y da el formato por defecto
        self.mainText = mainText = QLabel("Hola")
        layout.addWidget(mainText, 1, Qt.AlignmentFlag.AlignHCenter)
        MainWindow.updateWidget(mainText, self._settings)
        
        # Crea el botón de preferencias, lo conecta y añade al layout
        btn = QPushButton("Preferencias")
        btn.clicked.connect(self.setupPreferences)
        layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        # Establece el layout como central
        self.setCentralWidget(createWidgetLayout(layout))

    def updateWidget(widget: QWidget, settings: Settings):
        # Establece la fuente y el color de fondo
        widget.setFont(settings.font)
        widget.setStyleSheet(f"background-color: {settings.bgColor.name()}")

    def LineTable(*elements):
        # Añade elementos a un layout horizontal
        layout = QHBoxLayout()
        for elem in elements:
            layout.addWidget(elem)

        # Devuelve el layout
        return layout

    def setupPreferences(self):
        #Crea un dialogo con un layout principal vertical
        dialog = QDialog()
        layout = QVBoxLayout()
        dialog.setLayout(layout)

        # Crea el texto de previsualización
        preview = QLabel("Previsualización")

        # Define la función a llamar cuando se actualize alguna preferencia
        updatePreview = lambda: MainWindow.updateWidget(preview, self._tmp_settings)

        # Añade el botón de selección de color y lo enlaza a la función de cambio de color y actualización
        colorBtn = QPushButton("Elige color...")
        colorBtn.clicked.connect(self.colorSelect)
        colorBtn.clicked.connect(updatePreview)

        # Añade el botón de selección de fuente y lo enlaza a la función de cambio de color y actualización
        fontBtn = QPushButton("Elige fuente...")
        fontBtn.clicked.connect(self.fontSelect)
        fontBtn.clicked.connect(updatePreview)

        # Añade cada opción en una linea nueva
        layout.addLayout(MainWindow.LineTable(QLabel("Nombre de usuario: "), QLineEdit()))
        layout.addLayout(MainWindow.LineTable(QLabel("Color de fondo: "), colorBtn))
        layout.addLayout(MainWindow.LineTable(QLabel("Tipo de letra: "), fontBtn))

        #Añade el texto de preview y un dialogo de botones OK/Cancel
        layout.addWidget(preview)
        btnBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(btnBox)

        # Enlaza el botón ok a aceptar
        okBtn = btnBox.button(QDialogButtonBox.StandardButton.Ok)
        okBtn.clicked.connect(dialog.accept)

        # Enlaza el botón cancela a rechazar
        cancelBtn = btnBox.button(QDialogButtonBox.StandardButton.Cancel)
        cancelBtn.clicked.connect(dialog.reject)

        # Establece los ajustes actuales a los seleccionados si se ha aceptado
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self._settings = self._tmp_settings

        #Actualiza el texto principal con los ajustes actuales
        MainWindow.updateWidget(self.mainText, self._settings)

    def colorSelect(self):
        #Establece el color temporal como el seleccionado
        self._tmp_settings.bgColor = QColorDialog.getColor(self._tmp_settings.bgColor, self)

    def fontSelect(self):
        #Establece la fuente temporal como la seleccionada
        self._tmp_settings.font = QFontDialog.getFont(self._tmp_settings.font, self)

    

        
        

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
