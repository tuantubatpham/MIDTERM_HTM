from PyQt6.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QScroller

class WebLikePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Tạo nội dung dài
        for i in range(50):
            layout.addWidget(QLabel(f"Nội dung {i+1}"))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smooth Scroll Demo")
        self.resize(600, 400)

        # QScrollArea với hiệu ứng cuộn trớn
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Tạo nội dung trang
        web_page = WebLikePage()
        scroll_area.setWidget(web_page)

        # Kích hoạt QScroller để cuộn mượt
        QScroller.grabGesture(scroll_area.viewport(), QScroller.)

        self.setCentralWidget(scroll_area)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
