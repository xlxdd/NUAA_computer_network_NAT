# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:39:56 2023

@author: xlxdd
"""

# 服务端 PORT端口的监听程序
from socket import *

import json

IP = ''

PORT = 8888

BUFLEN = 512

listensocket = socket(AF_INET, SOCK_STREAM)

listensocket.bind((IP, PORT))

listensocket.listen(8)

print(f"服务端启动成功，在{PORT}端口等待链接")

dataSocket, addr = listensocket.accept()

print("接受一个用户请求：", addr)

while True:

    received = dataSocket.recv(BUFLEN)

    if not received:
        break

    message = json.loads(received.decode('utf8'))

    print(message)

    message["action"] = "ok"
    message["name"] = "xlxserver"

    sendbytes = json.dumps(message).encode('utf8')

    dataSocket.send(sendbytes)

dataSocket.close()
listensocket.close()