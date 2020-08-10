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
data11 = {'year': (2017, 2018, 2019), 'price': (10, 20, 30)}
DataFrame1 = pd.DataFrame(data11, index=list('012'))

# 结合 numpy 创建一个 (5, 15) 区间内，形状为 5 行 3 列的随机整数数组为 data2，
# 并以此为基础创建 index 为 ['a', 'c', 'e', 'f', 'h']，columns 为 ['one', 'two', 'three'] 的 DataFrame，
# 并命名为 df_test
data2 = np.random.randint(5, 15, (5, 3))
index1 = ['a', 'c', 'e', 'f', 'h']
columns = ['one', 'two', 'three']
df_test = pd.DataFrame(data2, index1, columns)

# 运用 loc 索引以及替换的知识，按下列要求对 df_test 进行增、改、替操作。
# 完成上述要求后，将该数据命名为 df_change
# (1) 将 a 行 one 列处替换成空值
# (2) 将 c 行 two 列处替换成 -99
# (3) 将 c 行 three 列处替换成 -99
# (4) 将 a 行 two 列处替换成 -100
# (5) 新增 four 列，值为 test
# (6) 重置索引为 ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(df_test)
df_test.loc['a', 'one'] = 'NaN'
df_test.loc['c', 'two'] = -99
df_test.loc['c', 'three'] = -99
df_test.loc['a', 'two'] = -100
df_test['four'] = 'test'
df_test = df_test.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

# 删除 df_change 中存在缺失值的所有行

