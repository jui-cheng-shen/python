def agv(*ns): # *回傳值是一个元组
    print(ns)
    for n in ns:
        print(n)

agv(3,4)
agv(3,4,10)
agv(1,4,-1,-8)