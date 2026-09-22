import numpy as np
import matplotlib.pyplot as plt
import random

w = 7
b = 2
np.random.seed(42)
x = np.arange(0, 10, 0.5)
y = x*7 + 2+ np.random.normal(0, 1, len(x))

y_pred = w*x + b
error = y - y_pred
mse = np.mean(error **2)
print(mse)
plt.plot(x, y, color = "blue")
plt.plot(x, y_pred, color = "red")
plt.show()
