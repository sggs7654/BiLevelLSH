import numpy as np
from sys import maxsize


class RPTree:
    max_level = 4  # RP树生长层数, 4层RP树将把数据分割成16部分
    mat = None  # np矩阵, 一行一个向量
    nrow = None
    ncolum = None
    hp = None  # 保存超平面信息的二维数组[level,offset], 数组元素为元组(theta, random_vec)
    indices = None  # 保存分割后各簇的索引集

    def __init__(self, mat):  # 加载数据集
        self.mat = mat
        self.nrow, self.ncolum = mat.shape
        self.hp = np.empty((self.max_level, 2 ** self.max_level))
        self.indices = np.empty(2 ** self.max_level)

    # 对数据集执行rp树分割, 返回分割后的子簇及超平面树
    def fit(self, indices=None, logic_index=(1, 1)):  # 两个参数分别是索引集, 超平面在数组中的逻辑下标
        if indices is None:  # 第一次调用fit时, indices为总索引集
            indices = range(self.nrow)
        level, offset = logic_index
        if level <= self.max_level:
            p1, p2, hp = self.divide(indices)
            self.hp[level - 1, offset - 1] = hp  # 逻辑下标→自然下标
            self.fit(p1, (level + 1, 2 * offset))  # 右孩子
            self.fit(p2, (level + 1, 2 * offset - 1))  # 左孩子
        else:
            self.indices[offset] = indices
            return

    # 把输入索引划分到两个子集中, 其输入为一个数据索引集, 输出为两个数据索引集及超平面参数
    def divide(self, indices):
        random_vec = np.random.random(size=self.ncolum)  # 产生n维随机向量, n为矩阵的列数
        random_vec /= np.linalg.norm(random_vec)  # 转化为单位向量
        n = len(indices)
        a = np.empty(n)  # 用来保存中间变量的数组, a = v点乘x
        for i in range(len(indices)):  # 遍历索引集对应向量
            a[i] = random_vec.dot(self.mat[indices[i]])
        a.sort()
        c_min = maxsize  # 保存c的最小值, 初始化为系统最大整数maxsize
        c_min_index = None  # 保存c取到最小值时的索引i
        for i in range(1, n - 1):
            u1 = np.sum(a[0:i]) / (i + 1)
            u2 = np.sum(a[i:n]) / (n - i + 1)
            c1 = np.sum(np.square(a[0:i] - u1))
            c2 = np.sum(np.square(a[i:n] - u2))
            c = c1 + c2
            if c < c_min:
                c_min = c
                c_min_index = i
        theta = (a[c_min_index] + a[c_min_index + 1]) / 2
        part_1 = [i for i in indices if self.mat[i].dot(random_vec) <= theta]
        part_2 = [i for i in indices if i not in part_1]
        return part_1, part_2, (theta, random_vec)
