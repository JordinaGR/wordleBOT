import pandas as pd

df = pd.read_csv('newdicc.csv')
df = df.replace(', ', ',\n')

print(df)