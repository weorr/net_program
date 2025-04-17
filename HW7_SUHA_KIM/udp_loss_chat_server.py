from socket import *
import random

port = 3353
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    sock.settimeout(None)
    data, addr = sock.recvfrom(BUFF_SIZE)

    # 50% 확률로 ACK 누락
    if random.random() <= 0.5:
        print("X (ack 생략)")
        continue
    else:
        sock.sendto(b'ack', addr)
        print('<-', data.decode())

    # 서버 응답
    msg = input('-> ')
    sock.sendto(msg.encode(), addr)
