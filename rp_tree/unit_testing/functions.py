import numpy as np
import matplotlib.pyplot as plt


def divide_test(rp_tree):
    # indices = np.random.choice(range(rp_tree.nrow), 5500, replace=False)
    indices = range(rp_tree.nrow)
    p1, p2= rp_tree.divide(indices)
    print(len(p1) + len(p2) == len(indices), len(p1), len(p2))

