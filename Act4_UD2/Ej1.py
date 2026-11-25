import sys
from PySide6.QtWidgets import QApplication, QColorDialog, QMainWindow, QPushButton
from PySide6.QtGui import QColor

# Título de la ventana
TITLE = "Aplicación con diálogos"


class MainWindow(QMainWindow):
    
    _bgColor:QColor


    def __init__(self):
        super().__init__()

        # Establece el título de la ventana
        self.setWindowTitle(TITLE)

        # Crea un botón y lo configura
        self.btn = btn = QPushButton("Haz click para que el dialogo aparezca")
        self.updateBtnColor(QColor("white"))
        btn.clicked.connect(self.onClicked)

        # Establece el botón como el widget central de la ventana
        self.setCentralWidget(btn)


    def onClicked(self):
        # Muestra un diálogo de selección de color y actualiza el color del botón si se selecciona un color válido
        color = QColorDialog.getColor(self._bgColor, self)
        if color.isValid():
            self.updateBtnColor(color)

    def updateBtnColor(self, color: QColor):
        # Actualiza el color de fondo del botón y almacena el color seleccionado
        self._bgColor = color
        self.btn.setStyleSheet(f"background-color: {color.name()}")



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
