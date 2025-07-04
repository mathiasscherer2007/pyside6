import sys
import random

from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.hello = ["Olá Mundo", "Hello World", "Bonjour le Monde", "Hola Mundo", "Hei Maailma"]
        
        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.addWidget(self.text)
        self.mainLayout.addWidget(self.button)
        
        self.button.clicked.connect(self.magic)
        
    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()
    
    sys.exit(app.exec())