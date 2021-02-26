
import pandas as pd

c_file = r'C:\Users\Administrator\Desktop\sdb_cd\single\sh600285.csv'
csv_raw = pd.read_csv(filepath_or_buffer=c_file, index_col='candle_end_time', encoding='gbk')
csv_df = csv_raw.loc['2019-01-01':, :]
# print(csv_df['close'].min(), csv_df['close'].max(), csv_df['close'].median(), csv_df['close'].quantile(0.1))
# print(c_file, csv_df.iloc[-1, 2])
# if csv_df['close'].quantile(0.1) > csv_df.iloc[-1, 2]:
# if csv_df['close'].quantile(0.01) > csv_df.iloc[-1, 2]:

print(c_file, ',  trade:', csv_df.iloc[-1, 2], ',  min:', csv_df['close'].min(), ',  max:', csv_df['close'].max(),
      ',  median:', csv_df['close'].median(), '，  qt：', csv_df['close'].quantile(0.5))

