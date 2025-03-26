queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)

queue.pop(0) #pop 是用來移除list中的元素
print(queue)

queue.append('d') #append d into list
queue.pop(0) #remove b in the list
queue.pop(0) #remove c in the list
queue.append('e') #append e into list()
queue.pop(0)#remove d in the list
queue.append('f') #append f into list
queue.append('g') #append g into list
print(queue)