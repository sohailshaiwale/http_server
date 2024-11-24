import socket
from dotenv import load_dotenv
import os
import time

load_dotenv()

class TCP:
    def __init__(self):
        self.sock = None

    def make_socket(self, socket_family, socket_type):
        if self.sock:
            return
        self.sock = socket.socket(socket_family, socket_type)
        self.sock.bind((socket.gethostname(), 8080))
        self.sock.listen(5)
        return self.sock


if __name__ == "__main__":
    TCP_connection = TCP()
    sock = TCP_connection.make_socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        client_socket, addr = sock.accept() 
        print(f"got a connection from {str(addr)}")
        current_time = time.ctime(time.time()) + "\r\n"
        client_socket.send(current_time.encode('ascii'))
        client_socket.close()
