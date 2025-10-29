#!/usr/bin/env python3
"""
Lesson 4: Convolution - Basic Examples
=======================================

This script demonstrates discrete-time convolution with visual examples.

Author: DSP-in-Python Repository
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def discrete_convolution(x, h):
    """
    Compute discrete convolution: y[n] = x[n] * h[n]
    
    Parameters:
    -----------
    x : array-like
        First signal
    h : array-like
        Second signal (often impulse response)
    
    Returns:
    --------
    y : ndarray
        Convolved signal (length = len(x) + len(h) - 1)
    """
    return np.convolve(x, h, mode='full')


def main():
    """Demonstrate basic convolution with visualization."""
    
    # Example 1: Rectangular pulses
    print("Example 1: Convolution of Two Rectangular Pulses")
    print("=" * 60)
    
    # Create two rectangular pulses
    x = np.array([1, 1, 1, 1])  # Length 4
    h = np.array([1, 1, 1])      # Length 3
    
    # Compute convolution
    y = discrete_convolution(x, h)
    
    # Time indices
    nx = np.arange(len(x))
    nh = np.arange(len(h))
    ny = np.arange(len(y))
    
    print(f"x[n] = {x} (length {len(x)})")
    print(f"h[n] = {h} (length {len(h)})")
    print(f"y[n] = x[n] * h[n] = {y} (length {len(y)})")
    print(f"Expected output length: {len(x)} + {len(h)} - 1 = {len(y)}")
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Convolution of Rectangular Pulses', fontsize=14, fontweight='bold')
    
    # Input signal x[n]
    axes[0, 0].stem(nx, x, basefmt=' ')
    axes[0, 0].set_title('Input Signal: x[n]')
    axes[0, 0].set_xlabel('n')
    axes[0, 0].set_ylabel('x[n]')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_ylim(0, 4.5)
    
    # Impulse response h[n]
    axes[0, 1].stem(nh, h, basefmt=' ', linefmt='C1-', markerfmt='C1o')
    axes[0, 1].set_title('Impulse Response: h[n]')
    axes[0, 1].set_xlabel('n')
    axes[0, 1].set_ylabel('h[n]')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_ylim(0, 4.5)
    
    # Output signal y[n]
    axes[1, 0].stem(ny, y, basefmt=' ', linefmt='C2-', markerfmt='C2o')
    axes[1, 0].set_title('Output: y[n] = x[n] * h[n]')
    axes[1, 0].set_xlabel('n')
    axes[1, 0].set_ylabel('y[n]')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_ylim(0, 4.5)
    
    # Interpretation
    axes[1, 1].axis('off')
    interpretation = (
        "Convolution Interpretation:\n\n"
        "• The output is a 'sliding sum'\n"
        "• Peak value = 3 (full overlap)\n"
        "• Output length = 4 + 3 - 1 = 6\n"
        "• Ramp up as signals overlap\n"
        "• Ramp down as they separate\n\n"
        "This is equivalent to:\n"
        "• Moving average filter\n"
        "• Smoothing operation\n"
        "• Integration effect"
    )
    axes[1, 1].text(0.1, 0.5, interpretation, fontsize=11, 
                     verticalalignment='center', family='monospace')
    
    plt.tight_layout()
    plt.savefig('../data/convolution_rectangles.png', dpi=150, bbox_inches='tight')
    print("\nFigure saved as 'convolution_rectangles.png'\n")
    
    # Example 2: Exponential sequence
    print("\nExample 2: Convolution with Exponential Decay")
    print("=" * 60)
    
    # Input impulse
    x2 = np.array([1, 0, 0, 0, 0])
    
    # Exponential decay impulse response (causal)
    alpha = 0.7
    h2 = alpha ** np.arange(8)
    
    # Convolution
    y2 = discrete_convolution(x2, h2)
    
    print(f"x[n] = impulse at n=0")
    print(f"h[n] = exponential decay: {alpha}^n")
    print(f"y[n] = x[n] * h[n] = impulse response h[n]")
    print(f"\nNote: Convolving with impulse returns the impulse response!")
    
    # Create second visualization
    fig2, axes2 = plt.subplots(1, 3, figsize=(14, 4))
    fig2.suptitle('Convolution with Exponential Impulse Response', 
                  fontsize=14, fontweight='bold')
    
    nx2 = np.arange(len(x2))
    nh2 = np.arange(len(h2))
    ny2 = np.arange(len(y2))
    
    axes2[0].stem(nx2, x2, basefmt=' ')
    axes2[0].set_title('Input: x[n] = δ[n]')
    axes2[0].set_xlabel('n')
    axes2[0].set_ylabel('x[n]')
    axes2[0].grid(True, alpha=0.3)
    
    axes2[1].stem(nh2, h2, basefmt=' ', linefmt='C1-', markerfmt='C1o')
    axes2[1].set_title(f'Impulse Response: h[n] = {alpha}^n·u[n]')
    axes2[1].set_xlabel('n')
    axes2[1].set_ylabel('h[n]')
    axes2[1].grid(True, alpha=0.3)
    
    axes2[2].stem(ny2, y2, basefmt=' ', linefmt='C2-', markerfmt='C2o')
    axes2[2].set_title('Output: y[n] = x[n] * h[n]')
    axes2[2].set_xlabel('n')
    axes2[2].set_ylabel('y[n]')
    axes2[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('../data/convolution_exponential.png', dpi=150, bbox_inches='tight')
    print("\nFigure saved as 'convolution_exponential.png'\n")
    
    # Example 3: Convolution modes
    print("\nExample 3: Convolution Modes")
    print("=" * 60)
    
    x3 = np.array([1, 2, 3, 4, 5])
    h3 = np.array([1, 1, 1])
    
    y_full = np.convolve(x3, h3, mode='full')
    y_same = np.convolve(x3, h3, mode='same')
    y_valid = np.convolve(x3, h3, mode='valid')
    
    print(f"x[n] = {x3}")
    print(f"h[n] = {h3} (moving average filter)")
    print(f"\nmode='full':  {y_full}  (length {len(y_full)})")
    print(f"mode='same':  {y_same}  (length {len(y_same)})")
    print(f"mode='valid': {y_valid}  (length {len(y_valid)})")
    
    plt.show()


if __name__ == "__main__":
    main()
