import pandas as pd
import os

d = {}

for file in os.listdir('data'):
    d[file.split('.')[0]] = pd.read_csv(f'data/{file}')

