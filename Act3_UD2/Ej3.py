import sys
from PySide6.QtWidgets import QApplication, QDoubleSpinBox, QLabel, QLayout, QLineEdit, QMainWindow, QHBoxLayout, QSpinBox, QVBoxLayout, QWidget

#Define constantes para fácil acceso y modificación en código
TITLE = "Layout formulario"

#Crea una pareja de label + entrada de forma cómoda
class FormEntry(QHBoxLayout):
    def __init__(self, parent: QLayout, labelText, formInput):
        super().__init__()

        #crea el label
        label = QLabel()
        label.setText(f"{labelText}: ")
        label.setStyleSheet("width: 20%")

        
        #añade el label y la entrada al layout
        self.addWidget(label)
        self.addWidget(formInput)


        #se añade al padre
        wd = QWidget()
        wd.setLayout(self)
        parent.addWidget(wd)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        

        #Asigna el titulo de la ventana
        self.setWindowTitle(TITLE)

        layout = QVBoxLayout()

        createdEntries: list[tuple[str, object]] = []

        #Crea y registra la entrada de texto con valor por defecto
        textEntry = QLineEdit()
        textEntry.setText("camilo")
        createdEntries.append(("Texto", textEntry))

        #Crea y registra la entrada de un entero con valor por defecto
        intEntry = QSpinBox()
        intEntry.setValue(56)
        createdEntries.append(("Entero", intEntry))

        #Crea y registra la entrada de un decimal con valor por defecto
        decEntry = QDoubleSpinBox()
        decEntry.setValue(6.55)
        createdEntries.append(("Decimal", decEntry))

        for entry in createdEntries:
            FormEntry(layout, entry[0], entry[1])

        

        wdg = QWidget()
        wdg.setLayout(layout)
        self.setCentralWidget(wdg)

        

        


#si la ejecucion es la principal
if __name__ == "__main__":
    #Crea la app con los argumentos del comando
    app = QApplication(sys.argv)
    #app.setStyle("Fusion")

    #Crea la ventana principal
    mainWindow = MainWindow()
    #Muestra la ventana en pantalla
    mainWindow.show()
    #termina la ejecución de la aplicacion
    sys.exit(app.exec())

