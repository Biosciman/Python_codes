import pandas as pd
import numpy as np

# 请根据上方表格数据创建一个 DataFrame 存储公司的数据，数据源如下所示，数据命名为 df_company
index1 = ['杭州银行', '青农商行', '常熟银行', '工商银行', '上海银行', '江苏银行']
data1 = {
    'marketcap': [449, 371, 237, 21313, 1369, 823],
    'pe': [8.31, 15.36, 16.01, 7.16, 7.59, 6.3],
    'code': ['600926', '002958', '601128', '601398', '601229', '600919']
}
dataframe1 = pd.DataFrame(data1, index = index1)

# 选出市值低于 2000 亿的所有公司
dataframe2A = dataframe1[dataframe1['marketcap'] < 2000]
dataframe2B = dataframe1.loc[dataframe1['marketcap'] < 2000]


# 选出市值 < 2000亿，并且市盈率 < 10 的所有公司
dataframe3A = dataframe1.loc[(dataframe1['marketcap'] < 2000) & (dataframe1['pe'] < 10)]

# 假设其中一家公司股票的每日收盘价数据，如下
# 请计算收盘价的五日平均，并新增一列存储
dr = pd.date_range(start='2019-01-02', periods=100)
data = np.random.randn(100).cumsum()
close = data - np.min(data)
df = pd.DataFrame({"close": close}, index=dr)

