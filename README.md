# Micro Projects

A collection of small, self-contained scripts and snippets I'm using to learn Git and GitHub — commits, branches, PRs, and general workflow. Not production code, just practice and experiments.

## Structure

Each project lives in its own folder or file, small enough to understand in one sitting.

```
micro-projects/
├── neuron-numpy/
│   └── neuron.py
├── ...
```

## Projects

### `neuron-numpy`
A minimal single-neuron forward pass using NumPy (`np.dot(x, w) + b`). Written while learning basic neural net math and debugging NumPy's `randint` argument handling (a fun gotcha with positional `size` vs `high`).

```python
import numpy as np

def neuron(x, w, b):
    return np.dot(x, w) + b

x = np.random.randint(0, 3, size=(3,))
w = np.random.randint(0, 3, size=(3,))
result = neuron(x, w, 1)
print(result)
```

### `linear regresstion from scratch in deep learning`
A minimal demonstration of liear regression performed using NumPy (`y_pred = a*x + b`). in this code we initally create an array "x" (`x = np.arrange(0, 10, 0.5)`). then we create an array "y" of dependent variables and add noise in it (`y = 3*x + 2 + np.random.normal(0, 1, len(x)`). then we predict the values of y and calculate MSE.

```python
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
```

## Purpose

This repo exists mainly to build a Git habit — regular commits, clear messages, and eventually branches/PRs — while picking up small coding concepts along the way. Expect messy, incremental, and occasionally broken code.

