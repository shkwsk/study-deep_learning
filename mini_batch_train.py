import sys, os
sys.path.append('../deep-learning-from-scratch')
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape) # (60000, 784)
print(t_test.shape)  # (10000, 10)

