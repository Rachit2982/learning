import pandas as pd


d=pd.read_csv("new_data.csv")
print(d)

df=pd.DataFrame([1,2,3],["rachit","btech","cse"])
print(df)
df.to_csv("rachit_data")
print("data saved")

for i in d:
    if d.Name=="Rachit":
        print("data found")