import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def identity_function(x):
    return x

def main():
    x = np.arange(-5.0, 5.0, 0.1)
    # y = step_function(x)
    # y = sigmoid(x)
    y = relu(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.show()

if __name__ == '__main__':
    main()
