import random
def lotto(n):
    for i in range(1,n+1):
        for j in range(1,7):
            LottoNum = random.randint(1,49)
            print('%3d' % (LottoNum),end=' ')
            print()
            
def main():
    num=eval(input("請輸入要產生幾組樂透號碼:"))#eval()函數用來執行一個字符串表達式，並返回表達式的值   
    lotto(num)
    
main()