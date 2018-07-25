import sys
import select
import socket
from eventloop import EventLoop


class Connection():
    def __init__(self):
        self.s = socket.socket()
        self.s.connect(('localhost', 1234))
    def fileno(self):
        return self.s.fileno()
    def on_read(self):
        msg = self.s.recv(1000).decode('utf8')
        print msg
    def send(self, msg):
        self.s.send(msg.encode('utf8'))

class Input():
    def __init__(self, sender):
        self.sender = sender
    def fileno(self):
        return sys.stdin.fileno()
    def on_read(self):
        msg = sys.stdin.readline()
        self.sender.send(msg)

connection = Connection()
input_reader = Input(connection)

eventLoop = EventLoop()
eventLoop.add_reader(connection)
eventLoop.add_reader(input_reader)
eventLoop.run_forever()