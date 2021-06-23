import pandas as pd
from os import walk
import datetime

pd.set_option('expand_frame_repr', False)  # 当列显示太多
pd.set_option('display.max_rows', 5000)  #


def ana_all_percentile(quantile_num=0.01):
    dataframe_list = []
    for f, _, i in walk(r"C:\Users\Administrator\Desktop\sdb_cd\single"):
        for j in i:
            dataframe_list.append(f + "\\" + j)

    for c_file in dataframe_list:
        csv_df = pd.read_csv(filepath_or_buffer=c_file, index_col='candle_end_time')
        # print(csv_df['close'].min(), csv_df['close'].max(), csv_df['close'].median(), csv_df['close'].quantile(0.1))
        # print(c_file, csv_df.iloc[-1, 2])
        # if csv_df['close'].quantile(0.1) > csv_df.iloc[-1, 2]:
        trade = csv_df.iloc[-1, 2]
        if csv_df['close'].quantile(quantile_num) > trade and len(csv_df) > 1560 and trade > 5 and trade < 10:
            print(c_file, len(csv_df), ',  trade:', trade, ',  min:', csv_df['close'].min(), ',  max:',
                  csv_df['close'].max(),
                  ',  median:', csv_df['close'].median(), '，  centi-qt：', csv_df['close'].quantile(quantile_num),
                  '，  hqt：', csv_df['close'].quantile(0.5))


def ana_all_trend():
    dataframe_list = []
    now = datetime.datetime.now()
    path = r'C:\Users\Administrator\Desktop\sdb_cd\all_stock\\'
    for i in range(1, 6):
        days_i_ = now - datetime.timedelta(days=i)
        strftime = days_i_.strftime('%Y%m%d')
        print(strftime)
        df_read_csv = pd.read_csv(filepath_or_buffer=(path + 'all_' + strftime + '.csv'))
        df_descend = df_read_csv[df_read_csv['changepercent'] < 0]
        dataframe_list.append(df_descend)
        print(len(df_descend))

    # 在多个列表中存在
    result = None
    for tdf in dataframe_list:
        if result is None:
            result = tdf
            # print(len(result))
            continue
        result = tdf[tdf['symbol'].isin(result['symbol'])]
        print(len(result))
    return result


def info_not_not_empty():
    dataframe_list = []
    for f, _, i in walk(r"C:\Users\Administrator\Desktop\sdb_cd\single"):
        for j in i:
            dataframe_list.append(f + "\\" + j)

    for c_file in dataframe_list:
        csv_df = pd.read_csv(filepath_or_buffer=c_file, index_col='candle_end_time')
        info = csv_df.iloc[-1, 7]
        if info != '{}':
            print(info_not_not_empty, c_file, ',  trade:', csv_df.iloc[-1, 2], ',  info:', info, ',  min:', csv_df['close'].min(), ',  max:', csv_df['close'].max(),
                  ',  median:', csv_df['close'].median(), '，  deci-qt：', csv_df['close'].quantile(0.1), '，  hqt：',
                  csv_df['close'].quantile(0.5))



def ana_single(file_nm):
    bpath = r'C:\Users\Administrator\Desktop\sdb_cd\single\\'
    c_file = bpath + file_nm + '.csv'
    csv_df = pd.read_csv(filepath_or_buffer=c_file, index_col='candle_end_time')
    print(file_nm, ',  trade:', csv_df.iloc[-1, 2], ',  min:', csv_df['close'].min(), ',  max:', csv_df['close'].max(),
          ',  median:', csv_df['close'].median(), '，  deci-qt：', csv_df['close'].quantile(0.1), '，  centi-qt：', csv_df['close'].quantile(0.01), '，  hqt：',
          csv_df['close'].quantile(0.5))


ana_single('sz002419')
# exit()

# info_not_not_empty()
#
# ana_all_percentile(quantile_num=0.005)

# trend = ana_all_trend()
# # print(trend[trend['trade']])
# print(trend)
# exit()
