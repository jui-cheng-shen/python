#會回應的Socket Server
import socket
server_socket = socket.socket()
server_socket.bind(('127.0.0.1',12345)) #12345是埠號
server_socket.listen(1)
print("Server is listening on 127.0.0.1:12345")

client_socket,addr = server_socket.accept()
print(f"Connected by {addr}")

data = client_socket.recv(1024) #recv() 是接收數據的方法，1024是接收的最大字節數
print(f"Teceived{data.decode()}")

client_socket.send("Hello from Server!".encode()) #send() 是發送數據的方法, encode() 是將字符串轉換為字節

client_socket.close()
server_socket.close()