#可多次連線的Socket Server
import socket
sock = socket.socket() # 創建socket對象
sock.bind(('127.0.0.1',12345)) # 綁定地址和端口
sock.listen(5) # 監聽TCP連接，最大數量為5

while True:
    client,addr = sock.accept() # 等待傳入連接並返回表示連接的新套接字對象和客戶端的地址
    client.setblocking(False) # 設置socket為非阻塞模式
    print(f'用戶端位置：{addr[0]}, 埠號:{addr[1]}') # 顯示客戶端和地址
    print(client,addr) # 顯示客戶端和地址