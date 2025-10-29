# Lesson 1: Discrete-time Signals

## Overview

This lesson introduces the fundamental concepts of discrete-time signals, which are the foundation of digital signal processing.

## Learning Objectives

After completing this lesson, you should be able to:
- Understand the difference between continuous-time and discrete-time signals
- Define and generate basic discrete-time signals
- Work with unit impulse, unit step, and exponential sequences
- Visualize discrete-time signals using Python

## Video Lecture

📺 [Watch Lecture 1 on YouTube](https://www.youtube.com/watch?v=hVOA8VtKLgk&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=1)

## Key Concepts

### Discrete-time Signals

A discrete-time signal is a sequence of numbers, typically denoted as x[n], where n is an integer index.

### Basic Signals

1. **Unit Impulse (Delta Function)**
   - δ[n] = 1 when n = 0
   - δ[n] = 0 when n ≠ 0

2. **Unit Step Function**
   - u[n] = 1 when n ≥ 0
   - u[n] = 0 when n < 0

3. **Exponential Sequences**
   - x[n] = aⁿ for all n
   - Real exponentials (a real)
   - Complex exponentials (a = e^(jω))

4. **Sinusoidal Sequences**
   - x[n] = A·cos(ωn + φ)
   - A: amplitude
   - ω: frequency (radians per sample)
   - φ: phase

## Python Implementation

### Required Libraries

```python
import numpy as np
import matplotlib.pyplot as plt
```

### Example Code

See the `examples/` directory for complete implementations:
- `signal_types.py`: Demonstrates basic signal types
- `signal_operations.py`: Shows signal operations (shifting, scaling, reversal)
- `complex_exponentials.py`: Complex exponential signals and Euler's formula

## Running the Examples

```bash
cd examples
python signal_types.py
```

## Exercises

Practice problems are available in the `exercises/` directory:
1. Create a discrete-time signal with custom properties
2. Implement signal shifting and scaling
3. Generate sinusoidal sequences with different frequencies

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

[Lesson 2: Python for DSP](../lesson_02/) - Learn the essential Python tools for digital signal processing.
