import socket
print("hello")
s=socket.socket()   

socket.create_server(("localhost",9999))
print("socket is created")

s.bind(("localhost",9999))
#port no range---0-65535

#connect no, of connections
s.listen(3)
print("waiting for connection")

while True:
    # to accept the connection
    # returns client ip and socket
    c,addr =s.accept()
    

    c.send(bytes("welcome to mav's server","utf-8"))
    name=(c.recv(1024).decode())
    print("connected with", addr,name)

    c.close()
