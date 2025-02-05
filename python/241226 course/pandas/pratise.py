import pandas as pd

data=pd.DataFrame({
    "name":["Amy","Bob","Charles","David","Eric"],
    "money":[46000,150200,30000,12222,40000],
    "income":[6000,12000,3000,5000,10000]
    })

data["CP"]=data["income"]/data["money"]

print(data)