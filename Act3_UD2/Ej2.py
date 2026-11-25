import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget

#Define constantes para fácil acceso y modificación en código
TITLE = "Layout horizontal con botones"
TEXTS_BUTTON = ["Uno", "Dos", "Tres", "Cuatro"]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Asigna el titulo de la ventana
        self.setWindowTitle(TITLE)

        layout = QHBoxLayout()

        #Por cada entrada del array añade un boton con ese nombre
        for btn_text in TEXTS_BUTTON:
            btn = QPushButton()
            layout.addWidget(btn)
            btn.setText(btn_text)

        #crea y muestra el widget
        wdg = QWidget()
        wdg.setLayout(layout)
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

