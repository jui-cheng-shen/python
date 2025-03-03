#求ax2+bx+c=0的根
import math

a,b,c=map(int,input().split())

def solve(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("No real root")
            else:
                print("Not a quadratic equation")
        else:
            x = -c / b
            print("x:.2f")
    else:
        delta = b **2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print("Two different roots , x1 ={x1:.2f} , x2 = {x2:.2f}")
        elif delta == 0:
            x = -b / (2*a)
            print("Two same roots , x = {x:.2f}")
        else:
            print("No real root")

solve(a,b,c) # 傳入參數 a,b,c