import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# x = np.linspace(-np.pi, np.pi, 100)
# plt.plot(x, np.sin(x))
#
#
# x = np.linspace(-np.pi * 2, np.pi * 2, 100)
# plt.figure(2, dpi=50)  # 创建图表2
# for i in range(1, 5):
#     plt.plot(x, np.sin(x / i))  # 4条线
# plt.show()
#
#
# plt.figure(2, dpi=50)
# data = [1, 1, 1, 2, 2, 3]
# plt.hist(data)
# plt.show()
#
# x = np.arange(1, 10)
# y = x
# fig = plt.figure()
# plt.scatter(x, y, c='r', marker='o')  # c红色， marker 原型
# plt.show()

hp = pd.read_csv('../data/201703.csv')
# print(hp.最高价)
# print(hp.head())
# hp.plot(kind='scatter', x='最低价', y='最高价')
# hp.plot(kind='line', x='交易日期', y='最高价')
# plt.show()


hp = pd.read_csv('../data/201703.csv')
sns.set(style='white', color_codes=True)
# 设置散点图
sns.jointplot(x='交易日期', y='最高价', data=hp, size=5)
# 绘制曲线
sns.displot(hp.最高价)
plt.show()

