for i in range(1,10):
    for x in range(0,10-i):
        print(end=  " ")
    for j in range(1,1+i):
        print(i ,end=" ")   #end=" " 不換行
    print()