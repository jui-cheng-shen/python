'''
請模擬「佇列」的操作，包括新增和刪除資料
依使用者的輸入判斷要進行的動作，直到 -999 停止
'add' ：進行新增（新增該列的第二項資料）
'delete'：進行刪除（刪除 queue 最前面的資料）
舉例說明：

《輸入》
add 11
add 22
add 33
delete
add 44
delete
add 55
add 66
delete
-999

《輸出》
44
55
66
'''
#add and delete data in queue

queue = []

def add(data):
    queue.append(data)

def delete():
    queue.pop(0)

while True:
    data = input()
    if data == "-999":
        print(queue)
        break
    elif data.split()[0] == "add":
        add(data.split()[1])
    elif data == "delete":
        delete()


