import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
sock.connect((host, port))

tm = sock.recv(1024)

sock.close()
print(f"the time is {tm.decode('ascii')}")
