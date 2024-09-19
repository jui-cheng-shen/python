# 這是一個計算 BMI 值的程式
#5b1g0012

height = int(input("input your height(cm) : "))
weight = int(input("input your weight(kg) : "))
bmi = round(weight / ((height / 100) ** 2), 2)
print("Your BMI is: ", bmi)