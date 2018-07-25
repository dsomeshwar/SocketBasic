import socket
import sys
import select

#
#   listen on port 1234 using command : nc -l 1234
#

conn = socket.socket()
conn.connect(('localhost', 1234))

while True:
    readers, _, _ = select.select([conn, sys.stdin],[],[])
    for reader in readers:
        if reader is conn:
            print(conn.recv(100).decode('utf8'))
        else:
            msg = sys.stdin.readline()
            conn.send(msg.encode('utf8'))
