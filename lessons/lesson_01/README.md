# Lesson 1: Discrete-time Signals

📺 [Watch Lecture 1 on YouTube](https://www.youtube.com/watch?v=hVOA8VtKLgk&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=1)

## Python Implementation

### Required Libraries

```python
import numpy as np
import matplotlib.pyplot as plt
```

### Example Code

See the `examples/` directory for python versions of the examples in the course that are done in matlab. 

## Running the Examples

```bash
cd examples
python even_and_odd-Parts.py
python discrete_time_sinusoids.py
```

## MATLAB to Python Conversion Notes

| MATLAB | Python (NumPy) |
|--------|----------------|
| `n = 0:10` | `n = np.arange(0, 11)` |
| `zeros(1, N)` | `np.zeros(N)` |
| `ones(1, N)` | `np.ones(N)` |
| `stem(n, x)` | `plt.stem(n, x)` |
| `length(x)` | `len(x)` |

## Additional Resources

- [NumPy Array Creation](https://numpy.org/doc/stable/user/basics.creation.html)
- [Matplotlib Stem Plots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html)
- [SciPy Signal Processing](https://docs.scipy.org/doc/scipy/reference/signal.html)

## Next Lesson

[Lesson 2: Python for DSP](../lesson_01a/) - Learn the essential Python tools for digital signal processing.
