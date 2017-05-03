from socket import *
import threading
from time import ctime

HOST='127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)
threads = []
addrs = []
all_port = []
tcpCliSerSocks = {}
def listen(tcpCliSerSock,addr):
    print('...connected from',addr)
    all_port = list(tcpCliSerSocks.keys())
    all_port_str = ",".join(str(x) for x in all_port)
    send_data = 'there is ports:'+all_port_str
    tcpCliSerSock.send(send_data.encode('UTF-8'))
    while True:
        data = tcpCliSerSock.recv(BUFSIZ)
        data = eval(data.decode())
        print(data)
        if not data:
            break
        tcpCliSerSocks[data['port']].send(data['data'].encode('UTF-8'))
    tcpCliSerSock.close()



if __name__ == '__main__':
    tcpSerSock = socket(AF_INET,SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)
    while True:
        print('Waiting for connection...')
        tcpCliSerSock, addr = tcpSerSock.accept()
        tcpCliSerSocks[str(addr[1])]=tcpCliSerSock
        addrs.append(addr)
        t = threading.Thread(target=listen,args=(tcpCliSerSocks[str(addr[1])],addr))
        threads.append(t)
        t.start()

    tcpSerSock.close()