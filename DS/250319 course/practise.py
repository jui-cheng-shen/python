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

"ADD and Delete and if user input -999,break and print"

queue = [] #建立一個容器

def add(data): #定義一個代名詞叫做add，這個代名詞是用來新增資料的
    queue.append(data) #新增資料

def delete(): #定義一個代名詞叫做delete，這個代名詞是用來刪除資料的
    queue.pop(0) #刪除資料

while True: #如果程式執行
    data = input() #輸入的資料放入data
    if data == "-999": #如果輸入的資料是-999
        print(queue) #印出容器裡面的資料
        break #停止
    elif data.split()[0] == "add": #問電腦:輸入的第一項是不是add
        add(data.split()[1]) #如果是add,就把輸入的第二項加到容器裡面
    elif data == "delete": #問電腦:輸入的是不是delete
        delete() #執行delete這個代名詞