dic = {"apple":"頻果","bug":"蟲蟲"}
print(dic["apple"])
dic["apple"]="青蘋果"
print(dic["apple"])
print("apple" in dic)
print("test" not in dic)
del dic["apple"]
print(dic)
dic = {x:x*2 for x in [3,4,5]}
print(dic)