"""

    Introdução à Signals e Slots
    
    Signals (sinais) e Slots deixam as widgets gráficas comunicarem entre si

"""

import sys
import random
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Slot, Qt

def rgbAleatorio():
    return tuple(random.randint(0, 255) for _ in range(3))

def convertHex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Random Text Color Button")
        
        self.button = QPushButton("Click me!")
        self.button.setFixedSize(200, 60)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.button.clicked.connect(self.changeTextColor)
    
    @Slot()
    def changeTextColor(self):
        color = convertHex(rgbAleatorio())
        self.setStyleSheet(f"MyWidget {{background-color: {color};}}")
        print(f"Cor definida para: {color}")


if __name__ == "__main__":
    app = QApplication([])
    
    window = MyWidget()
    window.resize(400, 300)
    window.show()
    
    sys.exit(app.exec())