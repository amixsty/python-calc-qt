from email.mime import application
import PySide6
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader

class amixsty(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()

        self.my_ui = loader.load("main.ui")
        self.my_ui.show()
        self.my_ui.btn.clicked.connect(self.show_message)


    def show_message(self):
        self.my_ui.tb1.setText("hello world")


app = QApplication()

mywindow = amixsty()

app.exec()
