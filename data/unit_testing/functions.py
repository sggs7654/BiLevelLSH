import matplotlib.pyplot as plt
import numpy as np


def load_data_test(mnist):
    mnist.load_data()
    index = (0, 17, 9999)
    for i in index:
        title_text = "Index:" + str(i) + "/" + str(mnist.num - 1)
        plt.title(title_text)
        temp = mnist.mat[i]
        im = np.reshape(temp, (28, 28))  # 把一维向量重整为28*28矩阵
        plt.imshow(im, cmap='gray')  # 把矩阵解析为灰度图像
        plt.show()