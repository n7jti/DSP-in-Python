#!/usr/bin/env python3
"""
Lesson 1: Examples from the lecture
=====================================================
This script demonstrates that cos(4*PI/5) is a discrete-time sinusoid with period 5.
And it will also demonstrate that sinusoids in discrete-time can be non-periodic.
https://www.youtube.com/watch?v=hVOA8VtKLgk&t=1003s 

Author: DSP-in-Python Repository
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Create a time vector from -10 to 10 (21 samples)
n = np.arange(-10, 11)

# Compute the discrete-time sinusoid
x = np.cos(4 * np.pi / 5 * n)

# Plot the discrete-time sinusoid
plt.stem(n, x)
plt.title("Discrete-Time Sinusoid: cos(4π/5 n)")
plt.xlabel("Sample Index (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# Now demonstrate a non-periodic discrete-time sinusoid  
x_non_periodic = np.cos(7 * n)

# Plot the non-periodic discrete-time sinusoid
plt.stem(n, x_non_periodic)
plt.title("Non-Periodic Discrete-Time Sinusoid: cos(7 n)")
plt.xlabel("Sample Index (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# print out the numbers
print("Non-Periodic Discrete-Time Sinusoid cos(7 n):")
print(x_non_periodic)