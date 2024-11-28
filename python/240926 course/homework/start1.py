#沈睿晟 5B1G0012
#有序可變動列表 List
grades = [12,60,25,70,90]
print(grades)
print(grades[0])
print(grades[3])
print(grades[1:4])

grades = [12,60,25,70,90]
grades[0]=55
print(grades)

grades = [12,60,25,70,90]
grades[1:4]
print(grades)
grades = [12,60,25,70,90]
grades = grades+[12,33]
print(grades)

grades=[12,60,25,70,90]
length = len(grades)
print(length)
data = [[3,4,5],[6,7,8]]#巢狀列表
print(data[0])
print(data[0][1])
print(data[0][0:2])
print(data)

data[0][0:2]=[5,5,5]
print(data)
data = (3,4,5)
print(data[2])
print(data[0:2])