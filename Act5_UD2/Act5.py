from pathlib import Path
import sys
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QHBoxLayout, QLabel, QLayout, QLineEdit, QMainWindow, QApplication, QMessageBox, QSpinBox, QStatusBar, QTableView, QToolBar, QVBoxLayout, QWidget, QSizePolicy, QDockWidget
from PySide6.QtGui import QIcon, QPixmap, QValidator, Qt
from PySide6.QtCore import Signal, SignalInstance

from User import User

#Titulo inicial de la aplicación
TITLE = "EDITOR DE TEXTO CON PYSIDE6"

#Lista inicial de los contactos
INITIAL_CONTACTS = [
            User(1, "Shyne", "123456789", "correo@gmail.com"),
            User(2, "Pati", "987654321", "mail@gmail.com"),
            User(3, "Azia", "111111111", "cosa@gmail.com")
        ]

#convierte una ruta relativa a ruta absoluta
def abspath(path):
    return str(Path(__file__).parent / path)

#carga un icono desde una ruta relativa a img
def loadIcon(path):
    return QIcon(abspath(f"img/{path}"))

#carga una imagen desde una ruta relativa a img
def loadImage(path):
    return QPixmap(abspath(f"img/{path}"))

#crea un widget usando el layout
def layoutToWidget(layout):
    wd = QWidget()
    wd.setLayout(layout)
    return wd

#Crea un QDialogButtonBox con los botones estandar indicados por parametros.
#Devuelve el widget principal seguido de los botones creados en el mismo orden que la entrada
def createBtnDialog(*btns):
    #define un valor por defecto
    btns = (QDialogButtonBox.StandardButton.Ok, QDialogButtonBox.StandardButton.Cancel) if btns is None else btns

    #Se inicializa res con el primer tipo de botón para que el interprete sepa como tratarlo
    res = btns[0]
    for btn in btns:
        res |= btn

    #Crea el boton con los botones indicados
    btnAcceptance = QDialogButtonBox(res)

    #crea un array con cada boton disponible iniciando desde el dialog box
    res = [btnAcceptance]
    for btn in btns:
        res.append(btnAcceptance.button(btn))

    #convierte el array a tupla para permitir expansion
    return tuple(res)

# ayuda a crear un dialogo rápidamente con título
def createDialog(parent, name):
    dialog = QDialog(parent)

    #crea, asigna el layout y el titulo de ventana
    layout = QVBoxLayout()
    dialog.setLayout(layout)
    dialog.setWindowTitle(name)

    #devuelve el recien creado dialgo
    return dialog

# Aydua a trabajar con un label de entrada de usuario
class InputLabelConstructor:
    #por defecto está preparado para un LineEdit
    def __init__(self, labelType = QLineEdit, editSignalName = "textChanged", getValue = "text"):
        self.type = labelType
        self.editSignalName = editSignalName
        self.getValue = getValue
        pass

#Constructor listo para line edit
InputLineEditConstructor = InputLabelConstructor()
#Constructor listo para spin box
InputSpinBoxEditConstructor = InputLabelConstructor(QSpinBox, "valueChanged", "value")

class InputLabel(QLabel):
    #requerido a nivel de clase por QWidgets
    validationChanged = Signal() 

    #inicializa con el texto indicativo, la función de validación, el consejo de entrada y el label que usar
    def __init__(self, name, validator, inputTip: str, editLabel = InputLineEditConstructor):
        super().__init__()

        #Asigna el tamaño y políticas por defecto de tamaño
        self.setMinimumSize(200, 40)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        # asigna los valores que deberán persistir en la clase
        self.validator = validator
        self._valid = False
        self.editLabel = editLabel

        # Crea el layout horizontal principal
        line = QHBoxLayout()
        self.setLayout(line)

        #Crea y muestra el texto indicativo para la entrada del usuario
        label = QLabel(name)
        label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        line.addWidget(label)

        #Crea y muestra el label y texto de ayuda
        self.inputLine = inputLine = editLabel.type()
        line.addWidget(inputLine)
        inputLine.setToolTip(inputTip)

        #Obtiene la señal de cambio del label y lo conecta a la validación de este label
        getattr(inputLine, editLabel.editSignalName).connect(self.validate)


    def validate(self):
        #obtiene si el input es valido actualmente
        newValid = self.validator(self.inputLine.text())

        #si la validación ha cambiado la actualiza y envía la emisión de que la validación ha cambiado
        if self._valid != newValid:
            self._valid = newValid
            self.validationChanged.emit()

    #indica si el label tiene un valor válido
    def isValid(self):
        return self._valid

    #obtiene el valor del label correspondiente
    def value(self):
        return getattr(self.inputLine, self.editLabel.getValue)()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Establece el nombre de la aplicación e initializa contacts como un array
        self.setWindowTitle(TITLE)
        self.contacts = []
        
        #Construye el contenido
        self.buildContent()
        #Construye el menú
        self.buildMenu()
        #Construye las herramientas
        self.buildTools()
        #Construye el dock
        self.buildDock()
        #Construye la barra de estado
        self.buildStatusBar()

    # Construye el contenido
    def buildContent(self):
        #crea el main layout e inserta los contactos iniciales
        self.mainLayout = layout = QVBoxLayout()
        
        for contact in INITIAL_CONTACTS:
            self.insertNewContact(contact)

        # Añade espacio hasta el fin y lo asigna como layout de widget central
        layout.addStretch()
        self.setCentralWidget(layoutToWidget(layout))

    # Construye el menú
    def buildMenu(self):
        #Crea la barra de menu
        menu = self.menuBar()

        #Crea el menú fichero y añade la acción de salir
        menu.addMenu("Fichero").addAction("Salir", self.close)

        #Crea el menú de contactos y añade las acciones de añadir y eliminar usuarios
        menuContacts = menu.addMenu("Contactos")
        menuContacts.addAction("Añadir", self.addContact, "Ctrl+A")
        menuContacts.addAction("Eliminar", self.removeContact, "Ctrl+E")

        #Añade el menú de ayuda con información a mostrar
        menu.addMenu("Ayuda").addAction("Inforamción", self.displayInfo)

    # Añade la ventana de añadir un contacto
    def addContact(self):
        #Crea el dialogo y obtiene su layout
        dialog = createDialog(self, "Añadir nuevo usuario")
        layout = dialog.layout()

        #Lista de las entradas de datos del usuario
        Inputs = [
            InputLabel("Nombre", User.validateName, "El nombre no debe estar vacío"),
            InputLabel("Teléfono", User.validateNumber, "El teléfono debe tener 9 dígitos"),
            InputLabel("Correo", User.validateMail, "El correo debe ser correcto debe tener texto seguido de @ seguido de texto un punto y más texto")
        ]

        #Añade los inputs al layout y rellena el espacio restante
        for inpt in Inputs:
            layout.addWidget(inpt)
        layout.addStretch()

        #crea, obtiene y añade el dialogo de botón y sus botones de aceptar y cancelar
        btnAcceptance, okBtn, cancelBtn = createBtnDialog(QDialogButtonBox.StandardButton.Ok, QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(btnAcceptance)

        # habilita el botón de ok si todos los inputs son válidos
        updateOkEnable = lambda: okBtn.setEnabled(all(inpt.isValid() for inpt in Inputs))
        for inpt in Inputs:
            inpt.validationChanged.connect(updateOkEnable)

       # Conecta los botones de ok y cancel con la aceptación y rechazo del diálogo y establece el estado de disponibilidad del botón ok okBtn.clicked.connect(dialog.accept)
        updateOkEnable()
        cancelBtn.clicked.connect(dialog.reject)
    
        dialog.setLayout(layout)

        dialog.accepted.connect(lambda: self.insertNewContact(User(self.contacts[-1]._id + 1, *[inpt.value() for inpt in Inputs])))

        dialog.exec()

    #Inserta un nuevo usuario a la lista y actualiza la vista, el estado y las últimas acciones
    def insertNewContact(self, user: User):
        self.contacts.append(user)
        self.updateStatusBar(f"Nuevo usuario añadido ({user})")
        self.updateLastActions("Nuevo usuario añadido", user.format())
        label = QLabel(str(user))
        label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.mainLayout.insertWidget(len(self.contacts) - 1, label)

    # Muestra el diálogo para eliminar un usuario de la lista
    def removeContact(self):
        dialog = QDialog(self, "Eliminar usuario")

        layout = dialog.layout()

        existsUser = lambda x: any(user._id == int(x) for user in self.contacts)
        inpt = InputLabel("ID", existsUser, editLabel=InputSpinBoxEditConstructor)

        layout.addWidget(inpt)

        layout.addStretch()

        btnAcceptance, okBtn, cancelBtn = createBtnDialog(QDialogButtonBox.StandardButton.Ok, QDialogButtonBox.StandardButton.Cancel)

        layout.addWidget(btnAcceptance)

        updateOkEnable = lambda: okBtn.setEnabled(inpt.isValid())

        inpt.validationChanged.connect(updateOkEnable)
        #crea la ventana de confirmación de eliminación del usuario
        def ensureDeleition():
            ensureDialog = createDialog(self, "Warning")
            ensureBtns, sureBtn, cancel = createBtnDialog(QDialogButtonBox.StandardButton.Ok, QDialogButtonBox.StandardButton.Cancel)
            sureBtn.clicked.connect(dialog.accept)
            sureBtn.clicked.connect(ensureDialog.accept)

            cancel.clicked.connect(ensureDialog.reject)
            ensureDialog.layout().addWidget(QLabel("¿Seguro que quieres eliminar el usuario?"))
            ensureDialog.layout().addWidget(ensureBtns)
            ensureDialog.exec()

        okBtn.clicked.connect(lambda: ensureDeleition())
        updateOkEnable()
        cancelBtn.clicked.connect(dialog.reject)

        dialog.accepted.connect(lambda: self.removeExistingContact(int(inpt.value())))
    
        dialog.setLayout(layout)

        dialog.exec()

    # Elimina el contacto desde su id junto con su elemento widget y actualiza la información de movimiento y statusBar
    def removeExistingContact(self, id):
        findIndex = -1
        for findIndex, user in enumerate(self.contacts):
            if user._id == id:
                break

        deletedUser = self.contacts.pop(findIndex)
        layout = self.mainLayout.takeAt(findIndex)
        wdg = layout.widget()
        wdg.setParent(None)
        wdg.deleteLater()
        self.updateStatusBar(f"Usuario {deletedUser} eliminado")
        self.updateLastActions("Usuario eliminado", deletedUser.format())

    # Crees un diálogo de texto con información de la aplicación
    def displayInfo(self):
        msg = QMessageBox(QMessageBox.Icon.Information, "Information", "Información de la aplicación")
        msg.exec()

    #Crea y asigna la barra de herramientas
    def buildTools(self):
        tools = QToolBar()

        tools.addAction(loadIcon("new_user"), "New User", self.addContact)
        tools.addAction(loadIcon("delete_user"), "Delete User", self.removeContact)
        tools.addAction(loadIcon("exit"), "Salir", self.close)

        self.addToolBar(tools)

    #Crea y asigna el statusBar de la aplicación 
    def buildStatusBar(self):
        self.estado = statusBar = QStatusBar()
        self.setStatusBar(statusBar)

        self.statusBarLabel = label = QLabel()
        statusBar.addWidget(label)
        self.updateStatusBar()

    #actualiza el statusBar con la cantidad de contactos existentes y opcionalmente un mensaje temporal
    def updateStatusBar(self, msg: str | None = None):
        if not hasattr(self, "statusBarLabel"): return

        self.statusBarLabel.setText(f"Hay {len(self.contacts)} contactos")
        if msg:
            self.statusBar().showMessage(msg, 5000)

    #Construye el dock flotante para la aplicación
    def buildDock(self):
        self.dock = dock = QDockWidget(self)
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Ultima acción realizada"))
        self.lastAction = QLabel("Sin ninguna acción realizada")
        layout.addWidget(self.lastAction)

        layout.addSpacing(10)
        layout.addWidget(QLabel("Ultimos datos modificados"))
        self.lastModification = QLabel("Ningun dato modificado")
        layout.addWidget(self.lastModification)

        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)
        layout.addStretch()

        dock.setWidget(layoutToWidget(layout))

    #actualiza la información del dock con la nueva acción y modificación realizadas
    def updateLastActions(self, action, modified):
        if not hasattr(self, "lastAction"): return

        self.lastAction.setText(action)
        self.lastModification.setText(modified)


        
#equivalente a void main
if __name__ == "__main__":
    #Crea la aplicación con los argumentos de entrada
    app = QApplication(sys.argv)
    #Crea la ventana principal
    window = MainWindow()
    #Muestra la ventana recién creada
    window.show()
    #acaba el script junto a la app su mismo código de salida
    sys.exit(app.exec())
