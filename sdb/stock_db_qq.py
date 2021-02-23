
from urllib.request import urlopen
import pandas as pd
from datetime import datetime
import time
import re
import os
import json

pd.set_option('expand_frame_repr', False)  # 当列显示太多
pd.set_option('display.max_rows', 5000)  #


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

    rename_dict = {1: 'open', 2: 'pre_close', 3: 'close', 4: 'high', 5: 'low', 6: 'buy1', 7: 'sell1',
                   8: 'amount', 9: 'volume', 32: 'status'}
    df.rename(columns=rename_dict, inplace=True)
    # print(df)
    # df['status'] = df['status'].str.strip('";')

    return df


print(get_today_date_from_sinajs(['sh600285', 'sh600273']))
exit()


def is_today_trading_day():
    df = get_today_date_from_sinajs(code_list=['sh000001'])
    sh_date = df.iloc[0]['candle_end_time']

    return datetime.now().date == sh_date.date()


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


###################
if is_today_trading_day() is False:
    print('not trading day, exit')
    exit()

if datetime.now().hour < 16:
    print('tody trading is not close')
    exit()

df = get_all_today_stock_data_from_sina_marketcenter()
df.to_csv(
    'C:\\Users\\Administrator\\Desktop\\sdb_qq\\all_stock\\all_' + str(datetime.now().date()).replace('-', '') + '.csv')

for i in df.index:
    t = df.iloc[i:i + 1, :]
    stock_code = t.iloc[0]['symbol']
    # print(stock_code)
    path = 'C:\\Users\\Administrator\\Desktop\\sdb_qq\\single\\' + stock_code + '.csv'
    # path = 'C:\\Users\\Administrator\\Desktop\\all_stock.csv'

    if os.path.exists(path):
        t.to_csv(path, header=None, index=False, mode='a', encoding='gbk')
    else:
        pd.DataFrame(columns=['data by cd']).to_csv(path, index=False, encoding='gbk')
        t.to_csv(path, header=None, index=False, mode='a', encoding='gbk')
