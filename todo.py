import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QListWidget
from PyQt5.uic import  loadUi

class MAIN(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("todo.ui", self)
        self.setWindowTitle("My todo app")
        self.button_handlers()

        self.show()

    def button_handlers(self):
        self.add_btn.clicked.connect(self.addTodo)
        self.clear_btn.clicked.connect(self.clr_all)
        self.del_btn.clicked.connect(self.delItem)

    def addTodo(self):
        # first we grab d td item from input
        item = self.todo_input.text()

        # then add it to d listwidget
        self.todo_list.addItem(item)

        # then again clr input box
        self.todo_input.setText("")

    def delItem(self):
        # get selected item
        selected = self.todo_list.currentRow()

        # del selected item
        # print(selected)
        self.todo_list.takeItem(selected)

    def clr_all(self):
        self.todo_list.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    firstWindow = MAIN()
    sys.exit(app.exec_())