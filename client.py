import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 6800
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while 1:
    data = s.recv(BUFFER_SIZE)
    print data
    inp = raw_input("> ")
    if inp == "q":
        s.send("/quit")
        break
    if inp == "\n" or inp == "":
        continue
    s.send(inp)
s.close()

print "Connection Closed!"
