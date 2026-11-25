from pathlib import Path
import sys
from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QLayout, QLineEdit, QMainWindow, QApplication, QMessageBox, QToolBar, QVBoxLayout, QWidget, QSizePolicy
from PySide6.QtGui import QIcon, QPixmap, QValidator, Qt

from User import User

TITLE = "EDITOR DE TEXTO CON PYSIDE6"

def abspath(path):
    return str(Path(__file__).parent / path)

def loadIcon(path):
    return QIcon(abspath(f"img/{path}"))

def loadImage(path):
    return QPixmap(abspath(f"img/{path}"))

def layoutToWidget(layout):
    wd = QWidget()
    wd.setLayout(layout)
    return wd

class InputLabel(QLabel):
    def __init__(self, name, validator, placeHolder: str | None = None):
        super().__init__()
        self.setMinimumSize(200, 40)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.validator = validator

        line = QHBoxLayout()
        label = QLabel(name)
        label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        line.addWidget(label)
        self.inputLine = inputLine = QLineEdit()
        
        line.addWidget(inputLine)

        inputLine.setPlaceholderText(placeHolder if placeHolder else f"Introducir aquí {name}")
        
        inputLine.textChanged.connect(self.validate)

        self.setLayout(line)

    def validate(self):
        self._valid = self.validator(self.inputLine.text())

    def isValid(self):
        return self._valid



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(TITLE)

        self.contacts = [
            User(1, "Shyne", "123456789", "correo@gmail.com"),
            User(2, "Pati", "987654321", "mail@gmail.com"),
            User(3, "Azia", "111111111", "cosa@gmail.com")
        ]

        self.buildContent()
        self.buildMenu()
        self.buildTools()

    def buildContent(self):
        layout = QVBoxLayout()
        
        for contact in self.contacts:
            label = QLabel(str(contact))
            label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            layout.addWidget(label, 1)

        layout.addStretch()
        self.setCentralWidget(layoutToWidget(layout))

        

    def buildMenu(self):
        menu = self.menuBar()
        menu.addMenu("Fichero").addAction("Salir", self.close)
        
        menuContacts = menu.addMenu("Contactos")
        menuContacts.addAction("Añadir", self.addContact, "Ctrl+A")
        menuContacts.addAction("Eliminar", self.removeContact, "Ctrl+E")
    
        menu.addMenu("Ayuda").addAction("Inforamción", self.displayInfo)

    def addContact(self):
        dialog = QDialog(self)

        layout = QVBoxLayout()
        dialog.setWindowTitle("Añadir nuevo usuario")

        
        layout.addWidget(InputLabel("Nombre", "nameInput"))
        layout.addWidget(InputLabel("Teléfono", "phoneInput"))
        layout.addWidget(InputLabel("Correo", "mailInput"))

        #layout.addStretch()
        
        dialog.setLayout(layout)
        dialog.exec()



    def removeContact(self):
        QMessageBox(QMessageBox.Icon.Information, "Elimar", "Eliminar usuario").exec()
        pass

    def displayInfo(self):
        msg = QMessageBox(QMessageBox.Icon.Information, "Information", "Información de la aplicación")
        msg.exec()

    def buildTools(self):
        tools = QToolBar()

        tools.addAction(loadIcon("new_user"), "New User", self.addContact)
        tools.addAction(loadIcon("delete_user"), "Delete User", self.removeContact)

        self.addToolBar(tools)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
