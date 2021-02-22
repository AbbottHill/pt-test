
import pandas as pd

history_dir = r'C:\Users\Administrator\Desktop\历史数据'

df = pd.read_csv(filepath_or_buffer=r'D:\pyc-wk\pt-test\data\sh600000.csv',
                 encoding='gbk',
                 # index_col='交易日期'
                 )

df1 = pd.read_csv(filepath_or_buffer=r'C:\Users\Administrator\Desktop\历史数据\历史基础交易数据_样本(2016 2017年数据)\basic_trading_data\stock_data\sz300274.csv',
                 encoding='gbk',
                 # skiprows=1
                  )

print(df.shape, df1.shape)
print(df1)


date_cond = (df['交易日期'] >= '2017-03-01') & (df['交易日期'] <= '2017-03-31')
date_cond1 = (df1['交易日期'] >= '2017-3-1') & (df1['交易日期'] <= '2017-3-31')
df_ = df[date_cond]
df_1 = df1[date_cond1]
print(df_1)

append = df_.append(df_1)
append.to_csv(path_or_buf=r'D:\pyc-wk\pt-test\data\201703.csv')




