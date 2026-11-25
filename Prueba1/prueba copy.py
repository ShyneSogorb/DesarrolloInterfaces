import sys
from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QLabel, QVBoxLayout, QWidget

class Contenedor(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        RESOLUTION = 256
        SCALE = 256 / RESOLUTION


        toHex = lambda x: ("00" + hex(int(x*SCALE)).split("x")[1])[-2:]

        HLayout = QHBoxLayout()
        HLayout.setSpacing(0)
        for i in range(RESOLUTION):
            VLayout = QVBoxLayout()
            VLayout.setSpacing(0)
            red = toHex(i)
            print(red)
            print(int(i*SCALE))
            for j in range(RESOLUTION):
                color = f"#{red}{toHex(j)}00"
                VLayout.addWidget(Contenedor(color))

                print(f"{i*RESOLUTION + j}/{(RESOLUTION)*(RESOLUTION)} ({color})")
            HLayout.addLayout(VLayout)


        widget = QWidget()
        widget.setLayout(HLayout)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())