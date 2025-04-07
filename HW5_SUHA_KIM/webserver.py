from socket import *

s = socket()
s.bind(('', 81))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    request_line = req[0]
    method, path, _ = request_line.split()

    filename = path.lstrip('/')

    if filename == '':
        filename = 'index.html'

    try:
        if filename == 'index.html':
            f = open(filename, 'r', encoding='utf-8')
            mimeType = 'text/html'
            file_data = f.read().encode('euc-kr')

        elif filename == 'iot.png':
            f = open(filename, 'rb')
            mimeType = 'image/png'
            file_data = f.read()

        elif filename == 'favicon.ico':
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'
            file_data = f.read()

        else:
            raise FileNotFoundError

        header = f'HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n'
        c.send(header.encode())
        c.send(file_data)

    except FileNotFoundError:
        header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        body = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'\
               '<BODY>Not Found</BODY></HTML>'
        c.send(header.encode())
        c.send(body.encode())

    c.close()
