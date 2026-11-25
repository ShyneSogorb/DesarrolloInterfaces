import random
import sys
from PySide6.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class Contenedor(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        grid = QGridLayout()

        main = QWidget()
        main.setLayout(grid)

        grid.addWidget(QPushButton("0,0"), 0, 0)
        grid.addWidget(QPushButton("0,1"), 0, 1)

        grid.addWidget(QPushButton("1,0-3"), 1, 0, 1, 2)
        
        self.setCentralWidget(main)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())