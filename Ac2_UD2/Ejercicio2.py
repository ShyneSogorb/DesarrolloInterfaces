import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QComboBox
from PySide6.QtCore import QSize

#Meses ordenados de enero a diciembre
MONTHS = ["Syczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerpiec", "Lipiec", "Sierpień", "Wrzesień", "Pażdiernik", "Listopad", "Grudzień"]

#Limite de texto en entrada
SIZE = QSize(200, 30)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Crea un combo box con los meses y un tamaño fijo
        comboBox = QComboBox()
        comboBox.addItems(MONTHS)
        comboBox.resize(SIZE)

        #El mes será el indice en el array (0-11) más 1 (1-12), junto con el mes del ínidice
        comboBox.currentIndexChanged.connect(lambda x: print(f"{x+1} - {MONTHS[x]}"))

        #Añade el widget a pantalla
        self.layout().addWidget(comboBox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

