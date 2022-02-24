import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QListWidget
from PyQt5.uic import  loadUi

class MAIN(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("todo.ui", self)
        self.setWindowTitle("My todo app")

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    firstWindow = MAIN()
    sys.exit(app.exec_())