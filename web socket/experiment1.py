import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.getaddrinfo('localhost',3000)
# mysock.connect(('data.pr4e.org', 80))
mysock.connect(('localhost:3000', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
cmd = 'GET http://127.0.0.1:3000/ HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()