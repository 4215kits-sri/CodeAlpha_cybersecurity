import socket
target = input("Enter IP address: ")
port=int(input("Enter port : "))
s = socket.socket()
s.connect((target, port))
banner = s.recv(1024)
print("Banner: ", banner.decode())
s.close()