"""
 todo:
  1 log
  2 batch update
  3 analysis
"""
from urllib.request import urlopen
from datetime import datetime
from random import randint
from os import walk
import pandas as pd
import time
import re
import os
import json

pd.set_option('expand_frame_repr', False)  # 当列显示太多
pd.set_option('display.max_rows', 5000)  #


def _random(n = 16):
    start = 10 ** (n - 1)
    end = (10 ** n) - 1
    return str(randint(start, end))


def get_content_from_internet(url, max_try_num=10, sleep_time=5):
    get_success = False
    for i in range(max_try_num):
        try:
            content = urlopen(url=url, timeout=10).read()
            get_success = True
            break
        except Exception as e:
            print('抓取数据报错，次数', i + 1, '， exception: ', e)
            time.sleep(sleep_time)

    if get_success:
        return content
    else:
        raise ValueError("max try number over")


def get_his_date_from_qq(s_code, k_type='day', num=1560):
    url = 'https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=%s,%s,,,%s,&r=0.%s'
    url = url % (s_code, k_type, num, _random())

    content = get_content_from_internet(url).decode('utf-8')
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
    # print(df)

    rename_dict = {0: 'candle_end_time', 1: 'open', 2: 'close', 3: 'high', 4: 'low', 5: 'volume', 6: 'info', 7: '换', 8: 'amount'}
    df.rename(columns=rename_dict, inplace=True)
    df['code'] = s_code
    # df['candle_end_time'] = pd.to_datetime(df['candle_end_time'])
    if 'info' not in df:
        df['info'] = None
    df = df[['candle_end_time', 'code', 'open', 'close', 'high', 'low', 'amount', 'volume', 'info']]
    return df

# print(get_his_date_from_qq(s_code='sh600285', k_type='day', num=1560))
# print(get_his_date_from_qq(s_code='sh605133', k_type='day', num=1560))
# exit()

def get_today_date_from_sinajs(code_list):
    # http://hq.sinajs.cn/list=sh600285,sh600273
    url = "http://hq.sinajs.cn/list=" + ",".join(code_list)

    # day data
    content = get_content_from_internet(url)
    content = content.decode('gbk')
    print(content)

    content = content.strip()
    data_line = content.split("\n")
    date_line = [i.replace('var hq_str_', '').split(',') for i in data_line]
    df = pd.DataFrame(date_line, dtype='float')

    df[0] = df[0].str.split('="')
    df['stock_code'] = df[0].str[0].str.strip()
    df['stock_name'] = df[0].str[-1].str.strip()
    df['candle_end_time'] = df[30] + ' ' + df[31]
    df['candle_end_time'] = pd.to_datetime(df['candle_end_time'])

    rename_dict = {1: 'open', 2: 'pre_close', 3: 'close', 4: 'high', 5: 'low', 6: 'buy1', 7: 'sell1',
                   8: 'amount', 9: 'volume', 32: 'status'}
    df.rename(columns=rename_dict, inplace=True)
    print(df)
    # df['status'] = df['status'].str.strip('";')

    return df


# print(get_today_date_from_sinajs(['sh600285', 'sh600273']))
# exit()


def is_today_trading_day():
    df = get_today_date_from_sinajs(code_list=['sh000001'])
    sh_date = df.iloc[0]['candle_end_time']

    return datetime.now().date() == sh_date.date()


# print(is_today_trading_day())
# exit()

def get_all_today_stock_data_from_sina_marketcenter():
    # 新浪财经行情数据
    # http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=2&num=40&sort=changepercent&asc=0&node=hs_a&symbol=&_s_r_a=page
    raw_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=%s' \
              '&num=80&sort=changepercent&asc=0&node=hs_a&symbol=&_s_r_a=page'
    page_num = 1

    all_df = pd.DataFrame()

    while True:
        url = raw_url % (page_num)
        print('page: ', page_num)
        content = get_content_from_internet(url)
        content = content.decode('gbk')
        page_num = page_num + 1

        if '[]' in content:
            break

        content = re.sub(r'(?<={|,)([a-zA-Z][a-zA-Z0-9]*)(?=:)', r'"\1"', content)

        # 将数据装换成dict 格式
        content = json.loads(content)
        df = pd.DataFrame(content)
        print(df)
        all_df = all_df.append(df, ignore_index=True)
        time.sleep(2)

        # if page_num == 4:
        #     break

    return all_df


# symbol    code   name    trade  pricechange  changepercent      buy     sell settlement     open     high      low     volume      amount  ticktime      per      pb        mktcap           nmc  turnoverratio
# print(get_all_today_stock_data_from_sina_marketcenter())
# exit()



all_path = 'C:\\Users\\Administrator\\Desktop\\sdb_cd\\all_stock\\all_' + str(datetime.now().date()).replace('-', '') + '.csv'
if not os.path.exists(all_path):
    all_df = get_all_today_stock_data_from_sina_marketcenter()
    all_df.to_csv(all_path)
else:
    all_df = pd.read_csv(all_path)


## his
for i in all_df.index:
    t = all_df.iloc[i:i + 1, :]
    stock_code = t.iloc[0]['symbol']
    stock_name = t.iloc[0]['name']
    path = 'C:\\Users\\Administrator\\Desktop\\sdb_cd\\single\\' + stock_code + '.csv'
    if not os.path.exists(path):
        print(i, '->his->', stock_code)
        hdf = get_his_date_from_qq(s_code=stock_code, k_type='day', num=210 * 20)
        hdf['name'] = stock_name
        hdf = hdf[['candle_end_time', 'code', 'name', 'open', 'close', 'high', 'low', 'amount', 'volume', 'info']]
        hdf.to_csv(path, index=False)
        time.sleep(1)
    else:
        continue


###################
if is_today_trading_day() is True and datetime.now().hour < 16:
    print('tody trading is not close')
    exit()


dataframe_list=[]
for f, _, i in walk(r"C:\Users\Administrator\Desktop\sdb_cd\single"):
    for j in i:
        dataframe_list.append(f + "\\" + j)


# todo
for i in all_df.index:
    t = all_df.iloc[i:i + 1, :]
    stock_code = t.iloc[0]['symbol']
    stock_name = t.iloc[0]['name']
    path = 'C:\\Users\\Administrator\\Desktop\\sdb_cd\\single\\' + stock_code + '.csv'
    if os.path.exists(path):
        print(i, 'update->', stock_code)
        his_csv = pd.read_csv(filepath_or_buffer=path, dtype='str')
        # get new data
        hdf = get_his_date_from_qq(s_code=stock_code, k_type='day', num=10)
        hdf['name'] = stock_name
        # merge his and new
        his_csv = pd.merge(his_csv, hdf, on=['candle_end_time', 'code', 'name', 'open', 'close', 'high', 'low', 'amount', 'volume'], how="outer")
        # his_csv['info'] = his_csv['info_x']
        # his_csv = his_csv[['candle_end_time', 'code', 'name', 'open', 'close', 'high', 'low', 'amount', 'volume', 'info_x', 'info_y']]

        # rename_dict = {'info_y': 'info'}
        # his_csv.rename(columns=rename_dict, inplace=True)
        # hdf.index = hdf['candle_end_time']
        # his_csv.sort_index()
        his_csv.sort_values(by=["candle_end_time"])
        his_csv.to_csv(path, index=False, encoding='utf-8')
        time.sleep(1)
    else:
        continue

exit()

## analy
for c_file in dataframe_list:
    csv_df = pd.read_csv(filepath_or_buffer=c_file, index_col='candle_end_time')
    # print(csv_df['close'].min(), csv_df['close'].max(), csv_df['close'].median(), csv_df['close'].quantile(0.1))
    # print(c_file, csv_df.iloc[-1, 2])
    # if csv_df['close'].quantile(0.1) > csv_df.iloc[-1, 2]:
    if csv_df['close'].quantile(0.01) > csv_df.iloc[-1, 2]:
        print(c_file, csv_df.iloc[-1, 2], csv_df['close'].min(), csv_df['close'].max(), csv_df['close'].median(), csv_df['close'].quantile(0.01))

