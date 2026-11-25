import random
import sys
from PySide6.QtWidgets import QApplication, QFormLayout, QGridLayout, QHBoxLayout, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class Contenedor(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        form = QFormLayout()

        FIELDS = ["orange", "purple", "magenta", "gray", "red"]
        for i,field in enumerate(FIELDS, start=1):
            form.addRow(f"Campo {i}", Contenedor(field))

        widget = QWidget()
        widget.setLayout(form)

        self.setCentralWidget(widget)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())