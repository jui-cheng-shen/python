n1,n2=map(int,input().split())
s = (n1*2+n2)%3
if s==0:
    print("普通")
elif s==1:
    print("小吉")
else:
    print("大吉")
