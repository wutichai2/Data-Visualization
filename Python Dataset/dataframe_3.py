import pandas as pd

data = {'Name':['wut1','wut2','wut3','wut4'],
        'Age':['11','12','13','14'],
        'Addres':['a','b','c','d'],
        'Sex':['m','w','m','m']}
df = pd.DataFrame(data)
print(df[['Name', 'Sex']])