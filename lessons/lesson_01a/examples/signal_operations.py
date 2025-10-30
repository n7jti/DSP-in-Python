#!/usr/bin/env python3
"""
Lesson 1: Discrete-time Signals - Signal Operations
====================================================

This script demonstrates basic operations on discrete-time signals:
1. Time shifting
2. Time reversal
3. Amplitude scaling
4. Signal addition

Author: DSP-in-Python Repository
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def time_shift(x, n, k):
    """
    Shift signal x[n] by k samples.
    
    Parameters:
    -----------
    x : array-like
        Input signal
    n : array-like
        Time indices for input
    k : int
        Shift amount (positive = right shift, negative = left shift)
    
    Returns:
    --------
    x_shifted : ndarray
        Shifted signal (same length as input)
    n_shifted : ndarray
        New time indices
    """
    n_shifted = n + k
    return x, n_shifted


def time_reverse(x, n):
    """
    Reverse the signal in time: x[n] -> x[-n]
    
    Parameters:
    -----------
    x : array-like
        Input signal
    n : array-like
        Time indices
    
    Returns:
    --------
    x_reversed : ndarray
        Time-reversed signal
    n_reversed : ndarray
        Reversed time indices
    """
    return x[::-1], -n[::-1]


def main():
    """Demonstrate signal operations."""
    
    # Set up output directory
    output_dir = Path(__file__).parent.parent / 'data'
    output_dir.mkdir(exist_ok=True)
    
    # Create an example signal: rectangular pulse
    n = np.arange(-10, 11)
    x = np.where((n >= -3) & (n <= 3), 1.0, 0.0)
    
    # Perform operations
    x_shifted, n_shifted = time_shift(x, n, k=5)
    x_reversed, n_reversed = time_reverse(x, n)
    x_scaled = 2.0 * x
    
    # Create composite signal
    x2 = np.where((n >= 0) & (n <= 5), 0.5, 0.0)
    x_sum = x + x2
    
    # Create figure with subplots
    fig, axes = plt.subplots(3, 2, figsize=(12, 14))
    fig.suptitle('Discrete-Time Signal Operations', fontsize=16, fontweight='bold')
    
    # Original signal
    axes[0, 0].stem(n, x, basefmt=' ')
    axes[0, 0].set_title('Original Signal: x[n]')
    axes[0, 0].set_xlabel('n')
    axes[0, 0].set_ylabel('x[n]')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 0].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 0].set_ylim(-0.2, 2.5)
    
    # Time-shifted signal
    axes[0, 1].stem(n_shifted, x_shifted, basefmt=' ')
    axes[0, 1].set_title('Time Shifted: x[n-5]')
    axes[0, 1].set_xlabel('n')
    axes[0, 1].set_ylabel('x[n-5]')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 1].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 1].set_ylim(-0.2, 2.5)
    
    # Time-reversed signal
    axes[1, 0].stem(n_reversed, x_reversed, basefmt=' ')
    axes[1, 0].set_title('Time Reversed: x[-n]')
    axes[1, 0].set_xlabel('n')
    axes[1, 0].set_ylabel('x[-n]')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 0].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 0].set_ylim(-0.2, 2.5)
    
    # Amplitude-scaled signal
    axes[1, 1].stem(n, x_scaled, basefmt=' ')
    axes[1, 1].set_title('Amplitude Scaled: 2·x[n]')
    axes[1, 1].set_xlabel('n')
    axes[1, 1].set_ylabel('2·x[n]')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 1].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 1].set_ylim(-0.2, 2.5)
    
    # Second signal for addition
    axes[2, 0].stem(n, x2, basefmt=' ', linefmt='C1-', markerfmt='C1o')
    axes[2, 0].set_title('Second Signal: x₂[n]')
    axes[2, 0].set_xlabel('n')
    axes[2, 0].set_ylabel('x₂[n]')
    axes[2, 0].grid(True, alpha=0.3)
    axes[2, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[2, 0].axvline(x=0, color='k', linewidth=0.5)
    axes[2, 0].set_ylim(-0.2, 2.5)
    
    # Signal addition
    axes[2, 1].stem(n, x_sum, basefmt=' ', linefmt='C2-', markerfmt='C2o')
    axes[2, 1].set_title('Signal Addition: x[n] + x₂[n]')
    axes[2, 1].set_xlabel('n')
    axes[2, 1].set_ylabel('x[n] + x₂[n]')
    axes[2, 1].grid(True, alpha=0.3)
    axes[2, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[2, 1].axvline(x=0, color='k', linewidth=0.5)
    axes[2, 1].set_ylim(-0.2, 2.5)
    
    plt.tight_layout()
    output_path = output_dir / 'signal_operations.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Figure saved as '{output_path}'")
    plt.show()
    
    # Print information
    print("\n" + "="*50)
    print("Signal Operations Summary")
    print("="*50)
    print(f"Original signal: rectangular pulse from n=-3 to n=3")
    print(f"Time shift: shifted right by 5 samples (x[n-5])")
    print(f"Time reversal: signal flipped around n=0 (x[-n])")
    print(f"Amplitude scaling: multiplied by 2 (2·x[n])")
    print(f"Signal addition: sum of two signals")


if __name__ == "__main__":
    main()
