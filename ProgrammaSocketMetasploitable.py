import socket
SRV_ADDR = "192.168.2.7"
port_str = 80

port = int(port_str)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, port))
s.listen(1)
print("Server started, waiting for connections")
connection, address= s.accept()
print("Client connected with address ", address)
while 1:
	data = connection.recv(1024)
	if not data: break
	print(data.decode('utf-8'))
connection.close()