import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QListWidget
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
import sqlite3


class MAIN(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("todo.ui", self)
        self.setWindowTitle("My todo app")
        self.button_handlers()
        self.grab_db_items()

        self.show()

    # get evrything frm db
    def grab_db_items(self):
        conn = sqlite3.connect('my_list.db')
        c = conn.cursor()

        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()

        # commit changes and close
        conn.commit()
        conn.close()

        for record in records:
            self.todo_list.addItem(str(record[0]))

    # saving to db
    def save_to_db(self):
        conn = sqlite3.connect('my_list.db')
        c = conn.cursor()

        # delete all item frm d database table
        # bcos otherwise it'll just append everything we're tryna save unto d list that was prev saved
        c.execute("DELETE FROM todo_list;", )

        # blank list to hold td items
        items = []
        # loop thru widget list n pull out each item
        for index in range(self.todo_list.count()):
            items.append(self.todo_list.item(index))

        for item in items:
            # print(item.text())
            # add stuff to our table
            c.execute("INSERT INTO todo_list VALUES (:item)",
                      {'item': item.text(), }
                      )

        # commit changes and close
        conn.commit()
        conn.close()

        # show pop up after each save
        msg = QMessageBox()
        msg.setWindowTitle("Item saved!")
        msg.setText("Your todo's have been saved!")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def button_handlers(self):
        self.add_btn.clicked.connect(self.addTodo)
        self.clear_btn.clicked.connect(self.clr_all)
        self.del_btn.clicked.connect(self.delItem)
        self.save_btn.clicked.connect(self.save_to_db)

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
