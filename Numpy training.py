import numpy as np

# 用 numpy 创建一个 2 * 2 的二维数组 ndarray，指定元素类型为 float，命名为 arr1
arr1 = np.array([[2]*2]*2, dtype=float)


# 生成元素全为 0 的 6 * 6 矩阵 arr2；元素全为 1 的 6 * 6 矩阵 arr3；以及 6 * 6 的单位矩阵 arr4
arr2 = np.zeros((6, 6))
arr3 = np.ones((6, 6))
arr4 = np.empty((6, 6))
