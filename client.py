import sys
import socket

# Check args, if nothing is set, use defaults
if(len(sys.argv) == 3):
    TCP_IP = sys.argv[1]
    TCP_PORT = int(sys.argv[2])
elif(len(sys.argv) == 2):
    if ":" in sys.argv[1]:
        print(sys.argv[1])
        # slice up and set vars
        spl = sys.argv[1].split(":")
        TCP_IP = spl[0]
        TCP_PORT = int(spl[1])
else:   
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
