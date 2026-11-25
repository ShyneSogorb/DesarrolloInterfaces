import sys
from PySide6.QtWidgets import QApplication, QCheckBox, QGroupBox, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout
from PySide6.QtCore import Qt

#Define constantes para fácil acceso y modificación en código
TITLE = "Layout con CheckBox"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Asigna el titulo de la ventana
        self.setWindowTitle(TITLE)

        #crea el grupo y layout
        group = QGroupBox()
        layout = QVBoxLayout()

        #indica el nombre de cada checkbox
        CHECKBOXES_NAMES = ["Primer", "Segundo", "Tercer"]

        #Crea un checkbox para cada nombre
        self.checkboxes = [QCheckBox(f"{name} checkbox") for name in CHECKBOXES_NAMES]

        #añade cada checkbox al layout y enlaza el cambio de valor con la función de display
        for cb in self.checkboxes:
            layout.addWidget(cb)
            cb.stateChanged.connect(self.DisplayActiveCheckbox)

        #Añadir al principal
        group.setLayout(layout)
        self.setCentralWidget(group)

    #Muestra que checkboxes están activos
    def DisplayActiveCheckbox(self):
        print("Estado de los CheckBox tras un cambio:")

        #filtra solo los activos
        active_only = [cb for cb in self.checkboxes if cb.checkState() == Qt.CheckState.Checked]
        for cb in active_only:
            print(f"{cb.text()} activado")


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

