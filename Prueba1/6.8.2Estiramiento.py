from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys


class Contenedor(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        btn1 = QPushButton("Fijo")
        btn1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        btn2 = QPushButton("Expansivo")
        btn2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout.addWidget(btn1, alignment=Qt.AlignRight | Qt.AlignCenter)
        layout.addWidget(btn2)
        

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())