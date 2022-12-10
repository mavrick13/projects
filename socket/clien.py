import socket

c=socket.socket()
name= input("entere your name - ")


c.connect(("localhost",9999))

print(c.recv(1024).decode())

c.send(bytes(name,"utf-8"))

print("connecting")








