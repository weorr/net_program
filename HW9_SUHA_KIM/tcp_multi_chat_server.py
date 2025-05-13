import socket
import threading
import time

clients = {}  # {socket: ID}

def broadcast(message, sender_sock):
    for client_sock in list(clients.keys()):
        if client_sock != sender_sock:
            try:
                client_sock.send(message.encode())
            except:
                client_sock.close()
                del clients[client_sock]

def handle_client(sock, addr):
    try:
        id_msg = sock.recv(1024).decode().strip()
        clients[sock] = id_msg
        print(f"new client {addr}, ID: {id_msg}")
        broadcast(f"{id_msg} 입장", sock)

        while True:
            data = sock.recv(1024).decode().strip()
            if not data or "quit" in data.lower():
                print(f"{addr} exited")
                break
            timestamp = time.asctime()
            print(f"{timestamp} {addr}: {data}")
            broadcast(data, sock)

    except:
        pass
    finally:
        sock.close()
        if sock in clients:
            left_id = clients[sock]
            del clients[sock]
            broadcast(f"{left_id} 퇴장", None)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 2500))
    server.listen(5)
    print('🚀 TCP Chat Server Started')

    while True:
        client_sock, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(client_sock, addr), daemon=True)
        t.start()

if __name__ == "__main__":
    main()
