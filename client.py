# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
send_data = input("Input send data: ")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(send_data, encoding='utf-8'))
    data = s.recv(1024)
print('Received', repr(data))