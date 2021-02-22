
import pandas as pd
pd.set_option('expand_frame_repr', False)

# df = pd.read_csv(filepath_or_buffer=r'D:\pyc-wk\pt-test\data\test.csv', encoding='gbk')

df = pd.read_csv(filepath_or_buffer=r'D:\pyc-wk\pt-test\data\sh600000.csv',
                 encoding='gbk',
                 index_col='交易日期'
                 )


# ========================================================== print
# print(df)
# print(df.shape)  # Number of rows , Number of column
# print(df.shape[0])  # row count

# print(df.columns)
# for col in df.columns:
#     print(col)

# print(df.index)
# print(df.head(3))
# print(df.tail(3))
# print(df.sample(n=3))
# print(df.sample(frac=0.3))  # sample sample(frac=0.3)
# print(df.describe())



# ========================================================== loc、iloc
# print(df[['开盘价', '最高价']])

# print(df.loc[['2016-01-06', '2017-12-25']])
# print(df.loc['2016-01-06': '2017-12-25'])
# print(df.loc['2017-01-01': '2017-01-31', '开盘价': '前收盘价'])
# print(df.loc[:, :])  # all row and column

# print(df.iloc[0])
# print(df.iloc[1, 3])

# ========================================================== operation
# print(df['交易日期'] + ' 12:00')
# print(df['开盘价'] * 10)
# df['交易日期2'] = df['交易日期'] + ' 10:00'  # create new col


# ========================================================== statistic
# print(df['收盘价'].mean())  # average
# print(df[['收盘价', '成交量']].mean())  # 分别求两列的平均值
# print(df[['开盘价', '收盘价']].mean(axis=1))  # 求两列每行的平均值
# print(df[['开盘价', '收盘价']].mean(axis=1).mean())  # 求两列的平均值

# print(df['收盘价'].std())  # 标准差
# print(df['收盘价'].count())  # 非空值数量
# print(df['收盘价'].median())  # 中位数
# print(df['收盘价'].quantile(0.25))  # 25% 中位数


# ========================================================== shift、 diff、 pct_change
# df['前一周期收盘价'] = df['收盘价'].shift(1)  # 取上一行的值
# del df['前一周期收盘价']
# df['未来3周期收盘价'] = df['收盘价'].shift(2)  # 取下两行的值
# print(df[['开盘价', '最高价', '最低价', '收盘价', '前收盘价', '前一周期收盘价', '未来2周期收盘价']])

# df['涨跌'] = df['收盘价'].diff(1)
# df['涨跌幅'] = df['收盘价'].pct_change(1)
# print(df[['收盘价', '涨跌', '涨跌幅']])

# df['累计成交量'] = df['成交量'].cumsum()  # 累加
# print((df['涨跌幅'] + 1).cumprod())  # 累乘
# print(df[['成交量', '累计成交量']])

df['收盘价排名'] = df['收盘价'].rank(ascending=True, pct=True)  # 显示百分比
print(df[['收盘价', '收盘价排名']])

