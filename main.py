import pandas as pd

d = {}

for i in range(1900, 2025):
    try:
        d[i] = pd.read_csv(f'./data/{i}.csv')
    except Exception as e:
        continue
print(len(d))