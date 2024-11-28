height = int(input("input your height(cm) : "))
weight = int(input("input your weight(kg) : "))
bmi = round(weight / ((height / 100) ** 2), 2)
if(bmi>=27):
    print("肥胖")
elif(bmi>=24):  
    print("過重")
elif(bmi>=18.5):
    print("正常")
else:
    print("過輕")

    