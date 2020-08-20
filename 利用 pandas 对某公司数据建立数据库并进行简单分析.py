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
dr = pd.date_range(start='2019-01-02', periods=100)
data = np.random.randn(100).cumsum()
close = data - np.min(data)
df = pd.DataFrame({"close": close}, index=dr)
# 请计算收盘价的五日平均，并新增一列存储
df['mean'] = df.rolling(5).mean()

# 请将下方表格数据存储在 DataFrame 中，然后按要求完成练习
index2 = ['a', 'b', 'c', 'd']
column2 = ['第1列', '第2列', '第3列', '第4列']
array1 = np.array(range(1,17)).reshape(4,4)
df2 = pd.DataFrame(array1, index= index2, columns= column2)
# 请利用 apply 函数，统计出每一行的总和
df2.apply(lambda x: x.sum(), axis=1)
# 请生成第 5 列数据，使其满足：当第 3 列数据 > 10 时，第 5 列数据等于第 1 、第 2 列数据之和；
# 否则第 5 列数据等于第 3 列数据
df2['第5列'] = df2.apply(lambda x: x[0]+x[1] if x[2]>10 else x[2], axis=1)
