import pandas_datareader.data as web
import datetime

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2018, 6, 26)

df = web.DataReader('TSLA', 'google', start, end)
df.show()
print(df.head())