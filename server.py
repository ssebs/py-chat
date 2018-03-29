import socket
from threading import Thread
from socketserver import ThreadingMixIn


class ClientThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.name = self.ip + ":" + str(self.port)
        print "New connection at " + self.name

    def process_data(self, inp):
        if(inp.startswith("/name")):
            self.name = inp[6:]
            print("srv|> Name changed to: " + self.name)
            conn.send("srv|> Name changed to: " + self.name)

        elif(inp == "/quit"):
            print("Shuting down connection for " + self.name)
            return 1    # return true to stop thread

        elif(inp == "/help" or inp == "/?" or inp == "/"):
            print("Sending help to " + self.name)
            conn.send(
                "srv|> You can enter text and everyone will hear it. You can also type commands, such as /who, /help, /msg, <name>, /quit")
       
        else:
            print(self.name + "|> " + inp)
            conn.send(self.name + "|> " + inp)

    def run(self):
        conn.send("srv|> Welcome to the server, " + self.name + ". You can Change your name by typing /name <name>.\nsrv|> Need help? try: /help")
        while True:
            data = conn.recv(2048)
            if not data:
                break
            # if method returns true, stop thread
            if self.process_data(str(data)):
                break


TCP_IP = '0.0.0.0'
TCP_PORT = 6800
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpSock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpSock.listen(4)
    print "Waiting for incoming connections..."
    (conn, (ip, port)) = tcpSock.accept()
    newThread = ClientThread(ip, port)
    newThread.daemon = True
    newThread.start()
    threads.append(newThread)

for t in threads:
    t.join()
