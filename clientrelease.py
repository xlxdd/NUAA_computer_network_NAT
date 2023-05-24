import sys
import json
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from clientui import Ui_MainWindow
from client import client
from PyQt5.QtCore import pyqtSignal

class UtilWindowUI(QtWidgets.QMainWindow, Ui_MainWindow):
    mysignal = pyqtSignal(str)
    def __init__(self):
        super(UtilWindowUI,self).__init__()
        self.setupUi(self)
        self.mysignal.connect(self.myupdate)
        self.s = ""

    def sendandrcvmessage(self):
        self.c = client()
        str = self.lineEdit.text()#获取输入框文本
        id = self.chooseIDbox.currentText()#获取进程标识符
        if str == "exit":
            self.close()
        if id == "A":
            self.c.set(id,"10.0.0.1","4000")
        elif id == "B":
            self.c.set(id,"10.0.0.2","4000")
        elif id == "C":
            self.c.set(id,"10.0.0.3","4000")

        self.c.setaim("10000")

        self.c.message = {
            "id": self.c.id,  # 进程标识符
            "ip": self.c.ip,  # 源ip
            "port": self.c.port,  # 源端口
            "text": str  # 文本内容
        }

        self.s = self.s+"进程"+self.c.id+"向S"+"发送了"+str+"\n"
        self.showtext.setText(self.s)
        connect_thread = threading.Thread(target=self.start_connecting)
        connect_thread.start()

    def start_connecting(self):
        print("1")
        try:
            print("2")
            self.c.datasocket.connect(("127.0.0.1", int(self.c.realAimPort)))
            sendbytes = json.dumps(self.c.message).encode('utf8')
            self.c.datasocket.send(sendbytes)
            rcvbytes = self.c.datasocket.recv(1024)
            self.c.message = json.loads(rcvbytes.decode('utf8'))
            t = "收到了进程S返回的信息："+self.c.message["text"]+"\n"
            self.mysignal.emit(t)
        except ConnectionRefusedError:
            print("3")
            self.mysignal.emit("ConnectionRefusedError\n")

    def myupdate(self,str):
        self.s += str
        self.showtext.setText(self.s)

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    widget=UtilWindowUI()
    widget.show()
    sys.exit(app.exec_())