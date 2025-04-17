from socket import *
import time

port = 3353
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    reTx = 0
  
    while reTx <= 5:
        send_msg = str(reTx) + ' ' + msg
        sock.sendto(send_msg.encode(), ('localhost', port))
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            print(f'[타임아웃] 재전송 {reTx + 1}회')
            reTx += 1
            continue
        else:
            break

    sock.settimeout(None)
    data, addr = sock.recvfrom(BUFF_SIZE)
    print('<-', data.decode())
