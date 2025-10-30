#!/usr/bin/env python3
"""
Lesson 1: Examples from the lecture
=====================================================
This script demonstrates breaking a random discrete-time signal into its even and odd components.
https://www.youtube.com/watch?v=hVOA8VtKLgk&t=1003s 

Author: DSP-in-Python Repository
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Setup our preferred random number generator
# In this case a uniform distribution between 0 and 1
# You can seed if you want a reproducible pseudorandom sequence
rng = np.random.default_rng()

# Get a random signal with 9 values from uniform distribution
x = rng.random(size=9)

# get the random numbers between -.5 and .5
x = x - 0.5

# Create time indices from -4 to 4 
n = np.arange(-4, 5)  # Creates [-4, -3, -2, -1, 0, 1, 2, 3, 4]

# Plot the random signal with custom x-axis
plt.figure(figsize=(10, 6))
plt.stem(n, x)
plt.title("Figure 1: Random Signal")
plt.xlabel("Sample Index (n)")
plt.ylabel("Amplitude")
plt.grid(True)
# Show non-blocking plot, if this was empty or TRUE the script would stop here until the plot 
# window was closed.  So show the plot but continue executing the script.
plt.show(block=False) 

# Reverse the array. 
# This is a function in matlab. But in python we can do it with slicing. 
negx = x[::-1]

# Now we do the flipped plot as a separate figure   
plt.figure(figsize=(10, 6))
plt.stem(n, negx)
plt.title("Figure 2: Flipped Random Signal")
plt.xlabel("Sample Index (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show(block=False)

#Now get the even part of X
evenx = 0.5 * (x + negx)

# Now compute the odd part of X
oddx = 0.5 * (x - negx)

plt.figure(figsize=(10, 6))
plt.stem(n, evenx)
plt.title("Figure 3: Even Part of Random Signal")
plt.xlabel("Sample Index (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show(block=False)

plt.figure(figsize=(10, 6))
plt.stem(n, oddx)
plt.title("Figure 4: Odd Part of Random Signal")
plt.xlabel("Sample Index (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show(block=False)

# Now show that the sum of even and odd is the original signal
q = evenx + oddx
plt.figure(figsize=(10, 6))
plt.stem(n, q)  
plt.title("Figure 5: Sum of Even and Odd Parts")
plt.xlabel("Sample Index (n)")
plt.ylabel("Amplitude")
plt.grid(True)

# Show the final plot and block so the script doesn't end until we close it.  If we didn't block, all
# the plots would close as soon as the script ended.    
# This wouldn't be a problem if we were running this in an interactive environment like Jupyter Notebook.
plt.show(block=True)