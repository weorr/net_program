import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9003)
sock.connect(addr)

print("서버에 연결되었습니다. (종료하려면 'q' 입력)")

while True:
    expression = input("계산식 입력(예: 20 + 17): ")
    if expression == 'q':
        sock.send(expression.encode())
        break

    sock.send(expression.encode())
    result = sock.recv(1024).decode()
    print("계산 결과:", result)

sock.close()
print("연결이 종료되었습니다.")
