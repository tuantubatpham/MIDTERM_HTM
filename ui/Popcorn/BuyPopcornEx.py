from PyQt6.QtWidgets import QMainWindow

from ui.Popcorn.BuyPopcorn import Ui_MainWindow


class BuyPopcornEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Initialize UI

    def showWindow(self):
        self.show()  # Show this window properly