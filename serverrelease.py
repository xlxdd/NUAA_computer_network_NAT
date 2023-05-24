import sys
import json
import threading
from socket import *
from PyQt5 import QtCore, QtGui, QtWidgets
from serverui import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal

class UtilWindowUI(QtWidgets.QMainWindow, Ui_MainWindow):
    mysignal = pyqtSignal(str)

    def __init__(self):
        super(UtilWindowUI,self).__init__()
        self.setupUi(self)
        self.mysignal.connect(self.myupdate)
        self.s = ""

    def start(self):
        self.startButton.setEnabled(False)

        self.s += '开始工作\n'
        self.showtext.setText(self.s)

        listen_thread = threading.Thread(target=self.start_listening)
        listen_thread.start()

    def start_listening(self):
        server_socket = socket(AF_INET, SOCK_STREAM)
        #服务器端口号设为10002
        server_socket.bind(('localhost', 10002))
        server_socket.listen(1)
        while True:
            client_socket, client_address = server_socket.accept()
            data = client_socket.recv(1024)
            message = json.loads(data.decode('utf8'))
            id = message["id"]
            ip = message["ip"]
            port = message["port"]
            t = message["text"]
            text = f"收到{id}发送的请求分组，源地址{ip}，端口号{port}，内容为{t}\n"
            self.mysignal.emit(text)

            message["text"] = "我收到了！"

            response_data = json.dumps(message).encode('utf8')
            text = f"返回给{id}应答分组，内容为：我收到了！\n"
            self.mysignal.emit(text)

            client_socket.sendall(response_data)
            client_socket.close()

    def myupdate(self,text):
        self.s += text
        self.showtext.setText(self.s)




if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    widget=UtilWindowUI()
    widget.show()
    sys.exit(app.exec_())