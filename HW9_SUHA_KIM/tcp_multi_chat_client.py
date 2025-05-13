import socket
import threading

def receive(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print(msg)
        except:
            break

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 2500))

    my_id = input("ID를 입력하세요: ")
    sock.send(my_id.encode())

    threading.Thread(target=receive, args=(sock,), daemon=True).start()

    while True:
        msg = input()
        if msg.lower() == "quit":
            sock.send(msg.encode())
            break
        full_msg = f"[{my_id}] {msg}"
        sock.send(full_msg.encode())

    sock.close()

if __name__ == "__main__":
    main()
