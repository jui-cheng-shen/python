#只可連線一次
# 伺服器端

import socket
sock = socket.socket()
sock.bind(('127.0.0.1',12345)) # 綁定地址和端口
sock.listen(1) # 監聽TCP連接，最大數量為1
client,addr = sock.accept() # 等待傳入連接並返回表示連接的新套接字對象和客戶端的地址
print(client,addr) # 顯示客戶端和地址