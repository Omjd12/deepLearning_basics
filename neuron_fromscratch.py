import numpy as np
import random

def sigmoid(z):
  return 1/(1+np.exp(-z))

def relu(z):
  return np.maximum(0, z)

def tanh(z):
  return np.tanh(z)

def neurons(x, w, b, Activation = None):
  z = np.dot(x, w) + b
  if Activation is None:
    return z
  return Activation(z)

x = np.random.randint(0, 3,size = (1, 3))
w = np.random.randint(0, 3, size = (3, 1))
result = neurons(x,w, 4)
print(result)
result = neurons(x , w, 1, Activation= tanh)
print(result)
result = neurons(x, w, 2, Activation= relu)
print(result)
result = neurons(x, w, 1, Activation= sigmoid)
print(result)
