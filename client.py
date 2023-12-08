import socket
c=socket.socket()
print("wating for connection....")
c.connect(('localhost',9999))
print(c.recv(1024).decode())
