from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Диспетчерский журнал")
        self.setGeometry(0, 0, 1920, 1080)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Журнал заявок")
        self.main_text.move(0, 0)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(0, 20)
        self.btn.setText("Открыть")
        self.btn.setFixedWidth(200)


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
