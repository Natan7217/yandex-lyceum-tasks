import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi

conn = sqlite3.connect("coffee.sqlite")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS coffee (
        id INTEGER PRIMARY KEY,
        sort_name TEXT,
        roast_degree TEXT,
        ground_or_whole TEXT,
        taste_description TEXT,
        price REAL,
        package_volume REAL
    )
''')

cursor.execute('''
    INSERT INTO coffee (sort_name, roast_degree, ground_or_whole, taste_description, price, package_volume)
    VALUES (?, ?, ?, ?, ?, ?)
''', ("Арабика", "Средняя", "В зерна", "Фруктово-цветочный", 399.99, 250))

conn.commit()
conn.close()


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)
        self.setWindowTitle("Coffee Information")

        self.connection = sqlite3.connect("coffee.sqlite")
        self.cursor = self.connection.cursor()

        self.display_coffee_info()

    def display_coffee_info(self):
        query = "SELECT * FROM coffee"
        self.cursor.execute(query)
        coffee_data = self.cursor.fetchall()

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Название сорта", "Степень обжарки", "Молотый/в зернах", "Описание вкуса", "Цена", "Объем упаковки"]
        )

        self.tableWidget.setRowCount(len(coffee_data))

        for row_num, row_data in enumerate(coffee_data):
            for col_num, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

        self.connection.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec_())
