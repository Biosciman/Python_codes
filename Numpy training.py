import numpy as np
import matplotlib.pyplot as plt

# 用 numpy 创建一个 2 * 2 的二维数组 ndarray，指定元素类型为 float，命名为 arr1
arr1 = np.array([[2]*2]*2, dtype=float)


# 生成元素全为 0 的 6 * 6 矩阵 arr2；元素全为 1 的 6 * 6 矩阵 arr3；以及 6 * 6 的单位矩阵 arr4
arr2 = np.zeros((6, 6))
arr3 = np.ones((6, 6))
arr4 = np.empty((6, 6))

# 运用 arange 函数生成生成 [0, 10) 区间内，步长为 2 的整数序列 arr5
arr5 = np.arange(0, 10, 2)

# 生成 0~10 间的等差数列 arr6，元素个数为 6
arr6 = np.linspace(0, 11, 6)

# 创建一个长度为 10 的随机数组（每个元素都是整数）并将最大值替换为 0
arr7 = np.random.randint(1, 100, [1, 10])
n = np.argmax(arr7)
arr7[0][n] = 0

# 计算数组 x = np.array([1,2,3,2,3,4,3,4,5,6]) 和数组 y = np.array([7,2,10,2,7,4,9,4,9,8]) 之间的欧式距离
x = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
y = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
dist1 = np.sqrt(np.sum(np.square(x-y)))
dist2 = np.linalg.norm(x-y)

# 利用 seed 生成一组固定的随机数 np.random.seed(1) ，并用此组成模拟的资金价值曲线 values = np.random.randn(1000).cumsum()
# 请利用 matplotlib 作出该资金价值曲线图
np.random.seed(1)
values = np.random.randn(1000).cumsum()
x = np.linspace(1, 1000, 1000)
plt.plot(x, values)
# plt.show()

# 计算上述任务中资金价值的最大回撤
# 最大回撤是指投资组合在选定的周期内，任一时间点往后推，可能出现资产净值下降的最大幅度。
# 最大回撤计算公式为 max_drawdown = np.max(np.maximum.accumulate(values) - values)
np.random.seed(1)
# cumsum()沿着指定轴的元素累加和所组成的数组，其形状与输入数组一致
values = np.random.randn(1000).cumsum()

def MaxDrawdown(list):
    """
    最大回撤率
    :param list:输入数组
    :return:返回最大回撤率
    """
    # numpy.maximum:比较两个数组并返回一个包含元素最大值的新数组
    # numpy.ufunc.accumulate: 累计将运算符应用于所有元素的结果
    i = np.argmax((np.maximum.accumulate(list)-list)/np.maximum.accumulate(list))
    if i == 0:
        return 0
    else:
        j = np.argmax(list[:i])
    return (list[j] - list[i]) / list[j]

print(MaxDrawdown(values))
maxDrawdown = ((np.maximum.accumulate(values)-values)/np.maximum.accumulate(values)).max()
print(maxDrawdown)

