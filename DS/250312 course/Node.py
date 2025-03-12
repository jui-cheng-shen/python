class Node:
    def __init__(self,new_data): #建構函數，用來初始化節點的資料和 next 指標。
        self.data = new_data #儲存資料
        self.next = None #指向下一個節點
