from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtCore import QTimer

app = QApplication([])
table = QTableWidget(0, 6)  # 创建一个0行6列的表格
table.setHorizontalHeaderLabels(['A', 'B', 'C', 'D', 'E', 'Time'])  # 设置表头

# 创建一个按钮来添加行
button = QPushButton('Add Row')
button.clicked.connect(lambda: add_row(table))
button.show()

# 创建一个QTimer来更新表格中的倒计时
timer = QTimer()
timer.timeout.connect(lambda: update_timer(table))
timer.start(1000)

def add_row(table):
    row = table.rowCount()
    table.insertRow(row)
    table.setItem(row, 0, QTableWidgetItem('A'))
    table.setItem(row, 1, QTableWidgetItem('B'))
    table.setItem(row, 2, QTableWidgetItem('C'))
    table.setItem(row, 3, QTableWidgetItem('D'))
    table.setItem(row, 4, QTableWidgetItem('E'))
    table.setItem(row, 5, QTableWidgetItem('5'))

def update_timer(table):
    for row in range(table.rowCount() - 1, -1, -1):
        current_time = int(table.item(row, 5).text())
        if current_time > 0:
            table.item(row, 5).setText(str(current_time - 1))
        else:
            table.removeRow(row)

table.show()
app.exec_()
