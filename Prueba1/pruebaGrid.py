from itertools import product
import random
import sys
from PySide6.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QMainWindow, QLabel, QVBoxLayout, QWidget

class Contenedor(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        grid = QGridLayout()

        GRID_SIZE = 100
        
        for i in range(GRID_SIZE*GRID_SIZE):
            f = GRID_SIZE // i if i != 0 else 0
            c = GRID_SIZE % i if i != 0 else 0
            color = str(hex(random.randint(0, 16777215)))[2:].zfill(6)
            print(f"[{f}][{c}][{GRID_SIZE*f + c}/{GRID_SIZE*GRID_SIZE}] {color} color --> {color[2:]}")
            grid.addWidget(Contenedor(f"#{color}"), f,c)
        
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())