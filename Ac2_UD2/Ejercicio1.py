
import sys
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QWidget
from PySide6.QtCore import QSize

#Tamaño de cada componente
SIZE = QSize(50, 30)

#Limite de texto en entrada
TEXT_LENGTH = 5


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Crea el input con tamaño y longitud
        LineEdit = QLineEdit(
            maxLength=TEXT_LENGTH,
        )
        LineEdit.resize(SIZE)

        #Crea el label con tamaño y offset a la izquierda del tamaño
        Label = QLabel()
        Label.resize(SIZE)
        Label.move(SIZE.width(), 0)

        #Cambiar texto del label al mismo que el input
        LineEdit.textChanged.connect(lambda newText: Label.setText(newText))

        #Añadir los widgets al layout
        self.layout().addWidget(LineEdit)
        self.layout().addWidget(Label)

        #Limitar alto y ancho minimo nde la ventana
        self.setMinimumHeight(SIZE.height()+20)
        self.setMinimumWidth(SIZE.width()*2)


#main de python
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
