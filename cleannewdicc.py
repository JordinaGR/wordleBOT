import pandas as pd
import numpy as np

df = pd.read_csv('newdicc.csv')

# arr = ['a', 'b', 'c', '?', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# arrb = [12.55, 1.32, 3.6, 1.06, 3.94, 13.89, 1, 1.28, 0.72, 6.99, 0.3, 0, 7.74, 3.16, 6.4, 5.71, 2.72, 1.35, 6.76, 8.43, 6.11, 4.18, 1.4, 0, 0.52, 0, 0.01]
# newc = []

# for ind, w in df.iterrows():
#     word = w['paraules']
#     p = 0

#     for i in word:
#         index = arr.index(i)
#         p += arrb[index]
    
#     p = int(100*p)
#     newc.append(p)

# df['prob'] = newc

# df = df.sort_values(by=['prob'], ascending=False)

df = df.drop(columns=['prob'])

print(df)

df.to_csv('newdicc.csv', index=False)
