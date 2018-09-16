from rp_tree.rp_tree import RPTree
from data.data_class import MNIST
from rp_tree.unit_testing import functions

mnist = MNIST()
mnist.load_data()
rp_tree = RPTree(mnist.mat)
# functions.divide_test(rp_tree)  # 测试通过

