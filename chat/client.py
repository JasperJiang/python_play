from socket import *
from time import ctime
import threading
HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
print('welcom to our chat')
data = tcpCliSock.recv(BUFSIZ)
data = data.decode()
print(data)
Threads = {}

def send_mes():
    while True:
        data = input()
        send_data = {'port':port,'data':data}
        if not data:
            break
        tcpCliSock.send(str(send_data).encode('UTF-8'))

def recv_mes():
    while True:
        data2 = tcpCliSock.recv(BUFSIZ)
        # Threads['send'].join(0)
        print(data2.decode())
        # Threads['send'].start()

port = input('witch port would you want to chat with:')
t = threading.Thread(target=send_mes)
Threads['send'] = t
t.start()
t = threading.Thread(target=recv_mes)
Threads['recv'] = t
t.start()

# tcpCliSock.close()