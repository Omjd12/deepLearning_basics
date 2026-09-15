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

## Purpose

This repo exists mainly to build a Git habit — regular commits, clear messages, and eventually branches/PRs — while picking up small coding concepts along the way. Expect messy, incremental, and occasionally broken code.

