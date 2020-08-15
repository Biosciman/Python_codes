import numpy as np
import csv

# 利用 numpy 读取 csv 文件数据，命名为 iris，并以 ndarry 形式展示出来

with open('iris.csv', 'r', encoding='UTF-8') as f:
    # np.loadtxt数据读取时默认为float，可改为str；跳过首行：skiprow = 1；读取特定列：usecols参数
    data = np.loadtxt(f, delimiter=',')

# 找出原数据中最小值和最大值出现的位置
dataMaxIndex = np.argmax(data)
dataMinIndex = np.argmin(data)

# 利用 numpy 找出花萼最小值与最大值
dataMax = data[np.argmax(data)]
dataMin = data[np.argmin(data)]

# 将 iris 原数据进行从小到大排序，并以 ndarray 形式展示出来
dataSort = sorted(data)
dataSort = np.array(dataSort)

# 去除该组数据中的重复值
# a, s, p = np.unique(A, return_index=True, return_inverse=True)
# 对于一维数组或者列表，unique函数去除其中重复的元素，并按元素由大到小返回一个新的无元素重复的元组或者列表
# return_index=True表示返回新列表元素在旧列表中的位置，并以列表形式储存在s中
# return_inverse=True 表示返回旧列表元素在新列表中的位置，并以列表形式储存在p中
dataUnique = np.unique(data)

# 请利用 numpy 计算出该组花萼的平均长度
dataMean = np.mean(data, axis=0)

# 用numpy计算出该组数据的标准差和方差
# var方差
# std标准差
dataVar = np.var(data, axis=0)
dataStd = np.std(data, axis=0)

# 求出所有花瓣累积总和
dataSum = np.sum(data, axis=0)

# 对已排序的 iris 数据进行累积求和运算
dataCumsum = np.cumsum(dataSort, axis=0)

# 统计花萼长度比平均值 5.84 高的有多少
Number = (data > 5.84).sum()
