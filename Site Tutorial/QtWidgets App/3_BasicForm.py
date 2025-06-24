import sys
from PySide6.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QVBoxLayout
from PySide6.QtCore import Slot

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")

        self.edit = QLineEdit("Meu nome aqui...")
        self.button = QPushButton("Sei lá")
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
    
        self.button.clicked.connect(self.ola)
    
    @Slot()
    def ola(self):
        print(f"Hello {self.edit.text()}")
        

if __name__ == '__main__':
    app = QApplication([])
    
    form = Form()
    form.show()
    
    sys.exit(app.exec())