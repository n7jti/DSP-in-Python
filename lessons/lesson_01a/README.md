# Lesson 1a: Python for DSP

📺 [Watch Lecture 1a on YouTube](https://www.youtube.com/watch?v=FmFlQFFM-xM&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=2)

## Python Implementation

### Required Libraries

```python
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
```

### Example Topics

## MATLAB to Python Quick Reference

### Array Creation

| Operation | MATLAB | Python (NumPy) |
|-----------|--------|----------------|
| Range | `0:10` | `np.arange(0, 11)` |
| Linspace | `linspace(0, 1, 100)` | `np.linspace(0, 1, 100)` |
| Zeros | `zeros(1, N)` | `np.zeros(N)` |
| Ones | `ones(1, N)` | `np.ones(N)` |
| Identity | `eye(N)` | `np.eye(N)` |
| Random | `rand(N)` | `np.random.rand(N)` |

### Array Operations

| Operation | MATLAB | Python (NumPy) |
|-----------|--------|----------------|
| Element-wise multiply | `x .* y` | `x * y` |
| Matrix multiply | `x * y` | `x @ y` or `np.dot(x, y)` |
| Transpose | `x'` | `x.T` |
| Length | `length(x)` | `len(x)` |
| Size | `size(x)` | `x.shape` |
| Max | `max(x)` | `np.max(x)` |
| Sum | `sum(x)` | `np.sum(x)` |

### Signal Processing

| Operation | MATLAB | Python (SciPy) |
|-----------|--------|----------------|
| Convolution | `conv(x, h)` | `np.convolve(x, h)` or `signal.convolve(x, h)` |
| FFT | `fft(x)` | `np.fft.fft(x)` |
| Filter | `filter(b, a, x)` | `signal.lfilter(b, a, x)` |
| Spectrogram | `spectrogram(x)` | `signal.spectrogram(x)` |
| Window | `hann(N)` | `signal.hann(N)` |

### Plotting

| Operation | MATLAB | Python (Matplotlib) |
|-----------|--------|---------------------|
| Line plot | `plot(x, y)` | `plt.plot(x, y)` |
| Stem plot | `stem(n, x)` | `plt.stem(n, x)` |
| Subplot | `subplot(2, 2, 1)` | `plt.subplot(2, 2, 1)` |
| Title | `title('Title')` | `plt.title('Title')` |
| Labels | `xlabel('x')` | `plt.xlabel('x')` |
| Grid | `grid on` | `plt.grid(True)` |
| Show | Not needed | `plt.show()` |
| Save | `saveas(gcf, 'file.png')` | `plt.savefig('file.png')` |

## Key Differences from MATLAB

1. **Indexing**: Python uses 0-based indexing, MATLAB uses 1-based
   - MATLAB: `x(1)` is first element
   - Python: `x[0]` is first element

2. **Ranges**: Python ranges are [start, stop) (exclusive end)
   - MATLAB: `1:5` gives [1, 2, 3, 4, 5]
   - Python: `range(1, 6)` gives [1, 2, 3, 4, 5]

3. **Arrays vs Lists**: NumPy arrays behave differently from Python lists
   - Use NumPy arrays for numerical work
   - Element-wise operations work on arrays, not lists

4. **Plotting**: Need to explicitly call `plt.show()` in scripts

5. **Matrix Operations**: Use `@` for matrix multiplication, `*` is element-wise

## Installation Tips

### Using pip
```bash
pip install numpy scipy matplotlib jupyter
```

### Using conda
```bash
conda install numpy scipy matplotlib jupyter
```

### Virtual Environment (Recommended)
```bash
python -m venv dsp_env
source dsp_env/bin/activate  # Windows: dsp_env\Scripts\activate
pip install -r requirements.txt
```

## Running the Examples

```bash
cd examples
python numpy_basics.py
python scipy_signal_demo.py
python plotting_dsp_signals.py
```

For Jupyter notebook:
```bash
jupyter notebook jupyter_intro.ipynb
```

## Additional Resources

- [NumPy Documentation](https://numpy.org/doc/)
- [NumPy for MATLAB Users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)
- [SciPy Signal Processing Tutorial](https://docs.scipy.org/doc/scipy/tutorial/signal.html)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Jupyter Documentation](https://jupyter.org/documentation)

## Next Lesson


