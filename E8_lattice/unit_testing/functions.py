import numpy as np
from E8_lattice.E8_decode import *


def decode_test():
    print("decode_test:")
    x = np.array([1.2, 1.2, 1.2, 1.2, 1.2, 1.1, 1.8, 1.4])
    print(np.array_equal(decode(x), np.array([1, 1, 1, 1, 1, 1, 2, 2])))


def decode_D8_test():
    print("decode_D8_test:")
    x = np.array([1.2, 1.2, 1.2, 1.2, 1.2, 1.1, 1.8, 1.4])
    print(np.array_equal(decode_D8(x), np.array([1, 1, 1, 1, 1, 1, 2, 2])))
    x = np.array([0.7, 0.7, 0.7, 0.7, 0.7, 0.6, 1.3, 0.9])
    print(np.array_equal(decode_D8(x), np.array([1, 1, 1, 1, 1, 1, 1, 1])))
    x = np.array([0, 0, 1.2, 1.2, 1.2, 1.2, 1.2, 1.1, 1.8, 1.4])
    print(np.array_equal(decode_D8(x), np.array([0, 0, 1, 1, 1, 1, 1, 1, 2, 2])))