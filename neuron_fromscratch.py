import numpy as np
import random

def neuron(x, w, b):
  return np.dot(x, w) + b  # initially the neurons have a linear activation function

x = np.random.randint(0, 3,size = (3,1))
w = np.random.randint(0, 3, size = (1,3))
result = neuron(x , w, 1)
print(result)
