import sys
from PySide6.QtWidgets import QApplication, QFontDialog, QMainWindow, QPushButton
from PySide6.QtGui import QFont

# Título de la ventana
TITLE = "Aplicación con diálogos"

class MainWindow(QMainWindow):
    _font:QFont


    def __init__(self):
        super().__init__()

        # Establece el título de la ventana
        self.setWindowTitle(TITLE)

        # Crea un botón y lo configura
        self.btn = btn = QPushButton("Haz click para que el dialogo aparezca")
        btn.clicked.connect(self.onClicked)

        # Establece el botón como el widget central de la ventana
        self.setCentralWidget(btn)

    def onClicked(self):
        # Obtiene la nueva fuente a tratar junto con una confirmación y lo actualiza
        confirm, font = QFontDialog.getFont(self.btn.font(), self)
        if confirm:
            self.updateBtnFont(font)

    # Cambia la fuente al botón
    def updateBtnFont(self, font: QFont):
        self.btn.setFont(font)
        



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
