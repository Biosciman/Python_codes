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
csv_data4 = csv_data['close'] > 11.08
print(csv_data4)
