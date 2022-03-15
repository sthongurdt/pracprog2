from operator import index
import pandas as pd

dic1 = {'a':[1,2,3,4], 'b':[2,3,4,5], 'c':[3,4,5,6]}
dic2 = {'a':[2,3,2], 'b':[3,4,3], 'c':[4,5,4]}

#df1 = pd.DataFrame([[llave, dic1[llave]]] for llave in dic1.keys())
df1 = pd.DataFrame(dic1, columns = ['a', 'b', 'c'])
df2 = pd.DataFrame(dic2, columns=['a', 'b', 'c'])

print(df1)
print('--------')
print(df2)
print('******************************')
#df3 = pd.merge(df1, df2)
df3 = pd.concat([df1,df2])
print(df3)
df4 = df3.drop_duplicates()
print('-----------------')
print(df4)