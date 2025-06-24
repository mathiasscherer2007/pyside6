import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication([])

label = QLabel("Hello World!")
label.show()
label2 = QLabel("<font color=red size=40>hon hon hon je suis français</font>")
label2.show()

app.exec()