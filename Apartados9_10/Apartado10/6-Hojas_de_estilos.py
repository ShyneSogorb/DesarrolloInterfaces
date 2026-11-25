from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel, QRadioButton,
    QCheckBox, QLineEdit, QSpinBox, QPushButton)
from pathlib import Path
import sys


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # estilos QSS, solo una declaración por widget 
        self.setStyleSheet("""
            QMainWindow {background-color: #212121; }
            QLabel {color: #e9e9e9; }
            QPushButton {background-color: orange;
                         font-family: "Arial";
                         font-size: 14px;
                         font-weight: bold; }
            QPushButton:hover {
            background-color: red;
            }
            QPushButton:active {
                        background-color: yellow;
                        }
        """)

        formulario = QFormLayout()
        formulario.addRow("QCheckBox", QCheckBox())
        formulario.addRow("QRadioButton", QRadioButton())
        formulario.addRow("QLabel", QLabel("QLabel"))
        formulario.addRow("QPushButton", QPushButton("QPushButton"))
        formulario.addRow("QLineEdit", QLineEdit("QLineEdit"))
        formulario.addRow("QSpinBox", QSpinBox())
        
        widget = QWidget()
        widget.setLayout(formulario)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())