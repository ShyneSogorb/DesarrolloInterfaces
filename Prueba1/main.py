import sys
from PySide6.QtWidgets import QApplication, QWidget

# Creamos una aplicación para gestionar la interfaz
app = QApplication(sys.argv)

# Creamos un widget para gestionar la ventana
window = QWidget()

# Mostramos la ventana que se encuentra oculta por defecto
window.show()

# Iniamos el Bucle del programa
sys.exit(app.exec())