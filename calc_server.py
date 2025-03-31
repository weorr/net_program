import socket

def calculate(expr):
    expr = expr.replace(' ', '') 
    try:
        if '+' in expr:
            op1, op2 = expr.split('+')
            return str(int(op1) + int(op2))
        elif '-' in expr:
            op1, op2 = expr.split('-')
            return str(int(op1) - int(op2))
        elif '*' in expr:
            op1, op2 = expr.split('*')
            return str(int(op1) * int(op2))
        elif '/' in expr:
            op1, op2 = expr.split('/')
            return f"{int(op1) / int(op2):.1f}" 
        else:
            return "지원하지 않는 연산입니다."
    except Exception as e:
        return f"오류: {e}"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 9003))
server_socket.listen(1)
print("서버가 시작되었습니다. 연결을 기다리는 중...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"클라이언트 {addr} 접속됨")

    while True:
        data = client_socket.recv(1024).decode()
        if not data or data == 'q':
            print("클라이언트가 연결을 종료했습니다.")
            break

        print(f"받은 계산식: {data}")
        result = calculate(data)
        client_socket.send(result.encode())

    client_socket.close()
