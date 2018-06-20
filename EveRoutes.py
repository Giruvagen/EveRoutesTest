import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

Ui_MainWindow, QtBaseClass = uic.loadUiType(“tax_calc.ui”)

class MyApp(QMainWindow):
def __init__(self):
super(MyApp, self).__init__()
self.ui = Ui_MainWindow()
self.ui.setupUi(self)
self.ui.calc_tax_button.clicked.connect(self.CalculateTax)
