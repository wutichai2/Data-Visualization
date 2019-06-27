import pandas as pd

data = pd.read_csv("nba.csv", index_col="Name")

first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]

print(first, "\n\n\n", second)