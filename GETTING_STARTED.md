# Getting Started with DSP-in-Python

This guide will help you get started with the DSP-in-Python repository.

## Quick Start

### 1. Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

### 2. Clone the Repository

```bash
git clone https://github.com/n7jti/DSP-in-Python.git
cd DSP-in-Python
```

### 3. Set Up Python Environment

#### Option A: Using venv (Recommended)

```bash
# Create virtual environment
python -m venv dsp_env

# Activate it
# On Linux/Mac:
source dsp_env/bin/activate
# On Windows:
dsp_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Option B: Using conda

```bash
conda create -n dsp python=3.10
conda activate dsp
pip install -r requirements.txt
```

#### Option C: System-wide installation (Not Recommended)

```bash
pip install -r requirements.txt
```

### 4. Test Your Installation

```bash
# Test that imports work
python -c "import numpy; import scipy; import matplotlib; print('All imports successful!')"

# Run a simple example
cd lessons/lesson_01/examples
python signal_types.py
```

If you see plots and no errors, you're all set!

## Learning Path

### Recommended Order

1. **Start with Lesson 1**: Discrete-time Signals
   - Understand basic signal types
   - Learn Python syntax for DSP
   - Get comfortable with NumPy and Matplotlib

2. **Progress through Lesson 2**: Python for DSP
   - Master the essential libraries
   - Learn MATLAB to Python conversions
   - Set up your workflow

3. **Follow the sequence**: Lessons 3-28
   - Each lesson builds on previous concepts
   - Watch the video lecture first
   - Run the example code
   - Try the exercises

### Alternative Paths

**For those new to Python:**
- Start with Lesson 2 (Python for DSP)
- Review Python basics tutorials
- Then proceed to Lesson 1

**For experienced DSP practitioners:**
- Skip directly to topics of interest
- Use the LESSONS.md index to navigate
- Each lesson is relatively self-contained

**For specific topics:**
- Filtering: Lessons 17-19
- FFT: Lessons 12-13
- Adaptive filters: Lessons 20-22
- Wavelets: Lessons 25-27

## Working with Examples

### Running Python Scripts

```bash
# Navigate to lesson examples
cd lessons/lesson_01/examples

# Run a script
python signal_types.py

# The script will:
# 1. Generate plots
# 2. Save figures to ../data/
# 3. Print information to console
```

### Interactive Exploration

For interactive work, use IPython or Jupyter:

```bash
# Install Jupyter (if not already installed)
pip install jupyter

# Start Jupyter
cd lessons
jupyter notebook

# Or use IPython
ipython
```

Then you can run code interactively:

```python
import numpy as np
import matplotlib.pyplot as plt

# Create and plot a signal
n = np.arange(0, 20)
x = np.cos(2 * np.pi * n / 8)
plt.stem(n, x)
plt.show()
```

## Common Issues and Solutions

### Issue: ImportError for numpy, scipy, or matplotlib

**Solution**: Install the required packages
```bash
pip install numpy scipy matplotlib
```

### Issue: Plots don't show up

**Solution**: 
- Make sure you have a display available
- For headless systems, save plots instead of showing them
- Use `plt.savefig()` before `plt.show()`

### Issue: Python version too old

**Solution**: Upgrade Python
```bash
# Check your version
python --version

# Use Python 3.8 or higher
# Install from python.org or use conda
```

### Issue: Module not found (even after install)

**Solution**: Check you're using the right Python
```bash
# See which python is being used
which python  # Linux/Mac
where python  # Windows

# Make sure it's the one in your virtual environment
```

## Project Structure Overview

```
DSP-in-Python/
├── README.md              # Main project overview
├── LESSONS.md             # Detailed lesson index
├── GETTING_STARTED.md     # This file
├── CONTRIBUTING.md        # Contribution guidelines
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT License
│
├── lessons/               # All course lessons
│   ├── lesson_01/
│   │   ├── README.md      # Lesson overview
│   │   ├── examples/      # Python examples
│   │   ├── exercises/     # Practice problems
│   │   └── data/          # Generated data/figures
│   ├── lesson_02/
│   └── ...
│
└── utils/                 # Shared utility functions
    └── common_functions.py
```

## Tips for Success

1. **Watch the Videos**: Professor Radke's lectures are excellent
2. **Run the Code**: Don't just read, execute and experiment
3. **Modify Examples**: Change parameters and see what happens
4. **Do the Exercises**: Practice reinforces learning
5. **Use the Community**: Open issues for questions
6. **Compare with MATLAB**: If you know MATLAB, use the conversion tables
7. **Keep a Notebook**: Document your learning journey
8. **Build Projects**: Apply concepts to real signals

## Resources

### Course Materials
- [YouTube Playlist](https://www.youtube.com/playlist?list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et)
- [Course Website](https://sites.ecse.rpi.edu/~rjradke/dspcourse.html)

### Python Documentation
- [NumPy Docs](https://numpy.org/doc/)
- [SciPy Signal Docs](https://docs.scipy.org/doc/scipy/reference/signal.html)
- [Matplotlib Docs](https://matplotlib.org/stable/contents.html)

### Learning Python
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [NumPy Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [Real Python Tutorials](https://realpython.com/)

### DSP Resources
- [DSP on Wikipedia](https://en.wikipedia.org/wiki/Digital_signal_processing)
- [Think DSP (Free Book)](https://greenteapress.com/thinkdsp/html/index.html)
- [DSP Stack Exchange](https://dsp.stackexchange.com/)

## Next Steps

After completing the setup:

1. ✅ Review the main [README.md](README.md)
2. ✅ Browse [LESSONS.md](LESSONS.md) for the full lesson list
3. ✅ Start with [Lesson 1](lessons/lesson_01/README.md)
4. ✅ Join the learning community

Happy learning! 🎓🔊📊
