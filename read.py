import pandas as pd

column=[]
n = int(input('Enter number of colums needed'))
for i in range(n):
    print(i+1,' column name : ')
    col=input()
    column.append(col);
v= int(input('Enter number of rows needed')) 

df=pd.read_csv("test.csv",usecols=column)
final=df.head(v)
final.to_csv('result.csv')