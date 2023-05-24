# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:52:40 2023

@author: xlxdd
"""

# 客户端 向 地址IP 端口 SERVER_PORT请求建立连接

from socket import *
import json

IP = "127.0.0.2"

SERVER_PORT = 8888

BUFLEN = 1024

dataSocket = socket(AF_INET, SOCK_STREAM)

#dataSocket.bind(("", 1000))

dataSocket.connect((IP, SERVER_PORT))

while True:

    textToSend = input(">>>")

    if textToSend == "exit": break

    message = {
        'action': textToSend,
        'name': 'xlxclient'
    }

    sendbytes = json.dumps(message).encode('utf8')

    dataSocket.send(sendbytes)

    receive = dataSocket.recv(BUFLEN)

    message = json.loads(receive.decode('utf8'))

    if not receive: break

    print(receive)

dataSocket.close()