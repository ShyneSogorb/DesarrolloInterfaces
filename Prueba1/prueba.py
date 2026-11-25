import sys
from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QLabel, QVBoxLayout, QWidget

class Contenedor(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layoutH = QHBoxLayout()
        layoutV1 = QVBoxLayout()
        layoutV2 = QVBoxLayout()

        layoutH.addWidget(Contenedor("Green"))

        layoutH.addLayout(layoutV1)
        layoutH.addLayout(layoutV2)

        layoutV1.addWidget(Contenedor("blue"))
        layoutV1.addWidget(Contenedor("red"))

        layoutV2.addWidget(Contenedor("orange"))
        layoutV2.addWidget(Contenedor("magenta"))
        layoutV2.addWidget(Contenedor("purple"))

        widget = QWidget()
        widget.setLayout(layoutH)
        self.setCentralWidget(widget)


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())