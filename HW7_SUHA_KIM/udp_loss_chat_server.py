from socket import *
import random

port = 3353
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    sock.settimeout(None)
    data, addr = sock.recvfrom(BUFF_SIZE)

    if random.random() <= 0.5:
        print("X (ack 생략)")
        continue
    else:
        sock.sendto(b'ack', addr)
        print('<-', data.decode())

    msg = input('-> ')
    sock.sendto(msg.encode(), addr)
