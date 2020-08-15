import pandas as pd
import numpy as np

# 利用 pandas 读取 sh.600000.csv 文件中的数据
csv_data = pd.read_csv('sh.600000.csv')

# 查看前 5 行数据与后 5 行数据
print(csv_data.head(5))
print(csv_data.tail(5))

# 查看该份数据的描述统计
print(csv_data.info())

# 查看该份数据的字段概况
print(csv_data.describe())

# 数据的选取（索引方式）
# (1) 使用 [ ] 位置索引方式，选取出前 3 行数据
csv_data1 = csv_data[0:3]

# (2) 使用 [ ] 标签索引方式，选取出 “date” 一列，并用 type 查看返回的数据类型
csv_data2 = csv_data['date']
print(type(csv_data2))

# (3) 使用 [ ] 标签索引方式，取出 “date”、“open” 列和 “colse” 列，并用 type 查看返回的数据类型
csv_data3 = csv_data[['date', 'open', 'close']]
print(type(csv_data3))

# (4) 使用 [ ] 标签索引方式，选取收盘价大于 11.08 的所有数据
csv_data4 = csv_data[csv_data['close'] > 11.08]

# (5) 将 date 设置为索引，并重新命名数据库为 df1，使用 df.loc[] 标签定位方式，
# 选取 df1 数据库中 2017-12-11 至 2017-12-20 的所有数据
df1 = csv_data.set_index('date')
df2 = df1.loc['2017-12-11':'2017-12-20']

# (6) 使用 df.loc[] 标签定位方式，选取 df1 数据库中 open 至 close 间的所有列
index1 = [i for i in df1.columns].index('open')
index2 = [i for i in df1.columns].index('close')
df3 = df1.loc[:, [i for i in df1.columns][index1:index2+1]]

# (7) 使用 df.loc[] 标签定位方式，选取 df1 数据库中时间从 2018-07-01 至 2018-07-08，open 至 close 间的所有列
df4 = df1.loc['2018-07-01':'2018-07-08', [i for i in df1.columns][index1:index2+1]]
