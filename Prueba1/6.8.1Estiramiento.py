from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QMainWindow, QLabel, QStackedLayout, QTabWidget, QVBoxLayout, QWidget)
from PySide6.QtCore import Qt
import sys


class Contenedor(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        layout.addStretch(1)
        layout.addWidget(QLabel("A"))
        layout.addStretch(3)
        layout.addWidget(QLabel("B"))



        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())