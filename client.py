from socket import *
import json
class client:
    def __init__(self):
        self.id = ""
        self.ip = ""
        self.port = ""
        self.realAimPort = ""

        self.message = dict()
        self.datasocket = socket(AF_INET, SOCK_STREAM)

    def set(self, id, ip, port):
        self.id = id
        self.ip = ip
        self.port = port

    def setaim(self, realaimport):
        self.realAimPort = realaimport

'''
    def connect(self):
        self.datasocket.connect(("127.0.0.1", self.aimPort))

    def disconnect(self):
        self.datasocket.close()
        return

    def sendandrcv(self):
        if self.textToSend == "exit":
            self.disconnect()
        self.message = {
            "id":self.id,  #进程标识符
            "ip": self.ip,  #源ip
            "port": self.port,  #源端口
            "aimIp": self.aimIp,    #目的ip
            "aimPort": self.aimPort,    #目的端口
            "text": self.textToSend #文本内容
        }
        self.datasocket.bind(("", self.realPort))
        self.datasocket.connect(("127.0.0.1", self.realAimPort))
        sendbytes = json.dumps(self.message).encode('utf8')
        self.datasocket.send(sendbytes)
        rcvbytes  = self.datasocket.recv(BUFLEN)
        self.message = json.loads(rcvbytes.decode('utf8'))
'''