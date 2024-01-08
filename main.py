import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QRectF


class CirclePainter(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for circle in self.circles:
            x, y, diameter, color = circle
            painter.setBrush(QColor(*color))
            painter.drawEllipse(x, y, diameter, diameter)

    def add_circle(self, x, y, diameter, color):
        self.circles.append((x, y, diameter, color))
        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Circles")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.circle_painter = CirclePainter()
        self.layout.addWidget(self.circle_painter)

        self.button = QPushButton("Draw Circle")
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.draw_circle)

    def draw_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.circle_painter.width() - diameter)
        y = random.randint(0, self.circle_painter.height() - diameter)
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.circle_painter.add_circle(x, y, diameter, color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
