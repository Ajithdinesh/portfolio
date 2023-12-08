# socket programming

# server

import socket
s=socket.socket()
print("socket is created")
s.bind(('localhost',9999))
s.listen(3)
print("waiting for clients...")

while True:
    c,addr=s.accept()
    print("client details:",c,addr)
    c.send(bytes("this is from server side","utf-8"))
    c.close()
