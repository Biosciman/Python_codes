import numpy as np
import pandas as pd

# 结合 numpy 创建一个 (3, 10) 区间内的包含 5 个随机整数的一维数组 ndarray 为 data1，
# 并以此 data 再创建索引为 a, b, c, d, e 的 Series 为 s1
# Series 是带有标签的一维数组，可以保存任何数据类型（整数，字符串，浮点数，Python对象等）,轴标签统称为索引
data1 = np.random.randint(3, 10, 5)
index = ['a', 'b', 'c', 'd', 'e']
s1 = pd.Series(data1, index)


# 请分别用位置索引和标签索引的方式提取是 s1 的后三个数
print(s1[-3:])
print(s1['c':'e'])

# 请用字典的形式创建一个DataFrame，将下方表格数据存储进去