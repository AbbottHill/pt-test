import pandas as pd

df = pd.read_csv(filepath_or_buffer=r'D:\pyc-wk\pt-test\data\test.csv', encoding='gbk')

print(df)

print(df['price'].quantile(0.01))
