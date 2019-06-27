import pandas as pd

data = {'Name':['wut1', 'wut2', 'wut3', 'wut4', 'wut5'],
        'Age':['10', '20', '30', '40', '59'],
        'Addresss':['11', 'ab', '12', 'abd', 'aaa'],
        'LV':['s', 's', 's', 's', 's']}
df = pd.DataFrame(data)
print(df[['Name', 'LV']])