import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi


class CirclePainter(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for circle in self.circles:
            color = QColor(Qt.yellow)
            painter.setBrush(color)
            painter.drawEllipse(*circle)

    def add_circle(self, x, y, diameter):
        self.circles.append((x, y, diameter, diameter))
        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = loadUi("UI.ui", self)
        self.circle_painter = CirclePainter(self.ui.centralwidget)
        self.ui.verticalLayout.addWidget(self.circle_painter)

        self.ui.pushButton.clicked.connect(self.draw_circle)

    def draw_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.circle_painter.width() - diameter)
        y = random.randint(0, self.circle_painter.height() - diameter)
        self.circle_painter.add_circle(x, y, diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
