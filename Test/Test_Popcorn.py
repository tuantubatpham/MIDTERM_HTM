from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.Popcorn.BuyPopcornEx import BuyPopcornEx

app=QApplication([])
mainwindow=QMainWindow()
myui=BuyPopcornEx()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()