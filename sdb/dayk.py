
from urllib.request import urlopen
import json
from random import  randint
import pandas as pd
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 5000)


def _random(n = 16):
    start = 10 ** (n - 1)
    end = (10 ** n) - 1
    return str(randint(start, end))


s_code = 'sh600285'
k_type = 'day'
num = 1560

## qfq
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newfqkline/get?_var=kline_dayqfq&param=sh600285,day,,,320,qfq&r=0.6339201167665203
# url = 'https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newfqkline/get?_var=kline_dayqfq&param=%s,%s,,,%s,qfq&r=0.%s'

## bfq
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sh600285,day,,,320,&r=0.8772604251160292
url = 'https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=%s,%s,,,%s,&r=0.%s'
url = url % (s_code, k_type, num, _random())

content = urlopen(url).read().decode('utf-8')
content = content.split('=', maxsplit=1)[-1]
content = json.loads(content)

k_data = content['data'][s_code]
if k_type in k_data:
    k_data = k_data[k_type]
elif 'qfq' + k_type in k_data:
    k_data = k_data['qfq' + k_type]
else:
    raise ValueError('key type not found')

df = pd.DataFrame(k_data)
#print(df)

rename_dict = {0: 'candle_end_time', 1: 'open', 2: 'close', 3: 'high', 4: 'low', 5: 'amount', 6: 'info', 7: '换', 8: '额'}
df.rename(columns=rename_dict, inplace=True)
df['candle_end_time'] = pd.to_datetime(df['candle_end_time'])
if 'info' not in df:
    df['info'] = None
df = df[['candle_end_time', 'open', 'close', 'high', 'low', 'amount', 'info']]
print(df)

path = 'C:\\Users\\Administrator\\Desktop\\test\\' + s_code + '.csv'
df.to_csv(path, header=None, index=False, mode='a', encoding='gbk')

