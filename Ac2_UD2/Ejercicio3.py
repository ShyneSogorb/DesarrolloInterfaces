import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
from random import choice

#Lista de refranes. El último será el que deshabilite el texto
SAYING = [
    "Haz el bien sin mirar a quien",
    "Más vale prevenir que curar",
    "Al mal tiempo, buena cara",
    "Quien tiene un amigo tiene un tesoro",
    "La avaricia rompe el saco",
    "De los errores se aprende" #NOTE para que este refran deshabilite el texto debe ser el último
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Crea el boton con texto y tamaño inicial
        button = self.sayingBtn = QPushButton()
        button.setText("Refrán")
        button.resize(300, 50)


        #Añade el widget a la ventana
        self.setCentralWidget(button)

        #Delega el evento cuando se le llama
        button.clicked.connect(self.DisplayRandomSaying)


    def DisplayRandomSaying(self):
        #Elige un refran aleatorio y lo pone como titulo
        saying = choice(SAYING)
        self.setWindowTitle(saying)

        # Deshabilito el botón? = Es el ultimo refrán?
        self.sayingBtn.setDisabled(saying == SAYING[-1])
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())