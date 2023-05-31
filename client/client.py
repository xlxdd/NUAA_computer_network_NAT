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