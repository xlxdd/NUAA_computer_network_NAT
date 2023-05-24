import sys
import json
import threading
from socket import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from routerui import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QTimer

class UtilWindowUI(QtWidgets.QMainWindow, Ui_MainWindow):
    mysignal = pyqtSignal(str)
    tablesignal = pyqtSignal(str,str)

    def __init__(self):
        super(UtilWindowUI,self).__init__()
        self.setupUi(self)
        self.mysignal.connect(self.myupdate)
        self.tablesignal.connect(self.updatetable)
        self.portcount = 8000#公网端口从8000开始分配
        self.s = ""
        #设置计时器
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.update_timer(self.table))
        self.timer.start(1000)

    def start(self):
        self.startButton.setEnabled(False)

        self.s += f'开始工作\n'
        self.showtext.setText(self.s)

        listen_thread = threading.Thread(target=self.start_listening)
        listen_thread.start()

    def start_listening(self):
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.bind(('localhost', 10001))
        server_socket.listen(1)
        while True:
            client_socket, client_address = server_socket.accept()
            data = client_socket.recv(1024)
            message = json.loads(data.decode('utf8'))
            print(message)
            id = message["id"]
            #需要查询ip port是否在地址转换表中已经存在
            ip = message["ip"]
            port = message["port"]
            text = f"收到{id}发送的请求分组\n"
            #更新文本框的信号
            self.mysignal.emit(text)
            self.tablesignal.emit(ip,port)
            forward_socket = socket(AF_INET, SOCK_STREAM)
            forward_socket.connect(('127.0.0.1', 10002))
            forward_socket.sendall(data)

            response_data = forward_socket.recv(1024)
            text = f"收到返回给{id}的应答分组\n"
            # 更新文本框的信号
            self.mysignal.emit(text)
            client_socket.sendall(response_data)

            forward_socket.close()
            client_socket.close()

    def myupdate(self,text):
        self.s += text
        self.showtext.setText(self.s)

    def updatetable(self,ip,port):
        #检测是否已经存在
        for row in range(self.table.rowCount() - 1, -1, -1):
            print("转换表的每一行：")
            print(self.table.item(row,1).text(),self.table.item(row,2).text())
            print(ip,port)
            #已经存在则刷新时间
            if (self.table.item(row,1).text() == ip and self.table.item(row,2).text() == port):
                self.table.setItem(row, 5, QTableWidgetItem("30"))
                return
        #否则加入这一行
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem('TCP'))
        self.table.setItem(row, 1, QTableWidgetItem(ip))
        self.table.setItem(row, 2, QTableWidgetItem(port))
        self.table.setItem(row, 3, QTableWidgetItem("128.10.10.1"))
        self.table.setItem(row, 4, QTableWidgetItem(str(self.portcount)))
        self.portcount += 1
        self.table.setItem(row, 5, QTableWidgetItem("30"))

    def update_timer(self,table):
        for row in range(table.rowCount() - 1, -1, -1):
            current_time = int(table.item(row, 5).text())
            if current_time > 0:
                table.item(row, 5).setText(str(current_time - 1))
            else:
                table.removeRow(row)


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    widget=UtilWindowUI()
    widget.show()
    sys.exit(app.exec_())