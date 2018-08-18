import numpy as np


def decode(x):  # 接受一个8*n位实数向量(np数组)), 将返回其E8编码
    if len(x) % 8 != 0:
        raise RuntimeError("E8 decoder: len(x)%8 is not 0")
    x1 = decode_D8(x)  # 分别计算D8(x)和D8(x-1/2)
    x2 = decode_D8(x - 1/2) + 1/2
    r1 = np.linalg.norm(x1 - x)  # 然后计算两个向量离x的欧氏距离
    r2 = np.linalg.norm(x2 - x)
    return x1 if r1 < r2 else x2  # 保留距离最小的向量, 作为E8(x)返回


def decode_D8(x):  # x是一个8*n位实数向量(np数组)), decode_D8将返回x的D8编码
    rx = np.round(x)  # 首先: 把x按四舍五入的规则进行取整
    if np.sum(rx) % 2 == 0:  # 然后, 然后验证其和是否为偶数
        d8_x = rx  # 如果是偶数, 则保留为D8(x)
    else:  # 否则, 找到取整时跨度最大的元素, 反向取整
        max_span = 0
        target_index = -1
        for i in range(len(x)):
            span = np.abs(x[i] - rx[i])
            if span > max_span:
                max_span = span
                target_index = i
        if np.modf(x[target_index])[0] >= 0.5:
            rx[target_index] = np.floor(x[target_index])
        else:
            rx[target_index] = np.ceil(x[target_index])
        d8_x = rx
    return d8_x
