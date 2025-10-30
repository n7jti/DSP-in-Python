#!/usr/bin/env python3
"""
Lesson 1: Discrete-time Signals - Basic Signal Types
=====================================================

This script demonstrates basic discrete-time signals:
1. Unit Impulse (Delta function)
2. Unit Step function
3. Exponential sequences
4. Sinusoidal sequences

Author: DSP-in-Python Repository
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def unit_impulse(n, n0=0):
    """
    Generate a unit impulse (delta function).
    
    Parameters:
    -----------
    n : array-like
        Time indices
    n0 : int
        Position of the impulse (default: 0)
    
    Returns:
    --------
    delta : ndarray
        Unit impulse signal
    """
    return np.where(n == n0, 1.0, 0.0)


def unit_step(n, n0=0):
    """
    Generate a unit step function.
    
    Parameters:
    -----------
    n : array-like
        Time indices
    n0 : int
        Starting position of the step (default: 0)
    
    Returns:
    --------
    u : ndarray
        Unit step signal
    """
    return np.where(n >= n0, 1.0, 0.0)


def exponential_sequence(n, a):
    """
    Generate an exponential sequence: x[n] = a^n
    
    Parameters:
    -----------
    n : array-like
        Time indices
    a : float or complex
        Base of the exponential
    
    Returns:
    --------
    x : ndarray
        Exponential sequence
    """
    return a ** n


def sinusoidal_sequence(n, A, omega, phi=0):
    """
    Generate a sinusoidal sequence: x[n] = A*cos(omega*n + phi)
    
    Parameters:
    -----------
    n : array-like
        Time indices
    A : float
        Amplitude
    omega : float
        Frequency in radians per sample
    phi : float
        Phase in radians (default: 0)
    
    Returns:
    --------
    x : ndarray
        Sinusoidal sequence
    """
    return A * np.cos(omega * n + phi)


def main():
    """Demonstrate basic discrete-time signals."""
    
    # Set up output directory
    output_dir = Path(__file__).parent.parent / 'data'
    output_dir.mkdir(exist_ok=True)
    
    # Time index
    n = np.arange(-10, 21)
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Basic Discrete-Time Signals', fontsize=16, fontweight='bold')
    
    # 1. Unit Impulse
    delta = unit_impulse(n, n0=0)
    axes[0, 0].stem(n, delta, basefmt=' ')
    axes[0, 0].set_title('Unit Impulse: δ[n]')
    axes[0, 0].set_xlabel('n')
    axes[0, 0].set_ylabel('δ[n]')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 0].axvline(x=0, color='k', linewidth=0.5)
    
    # 2. Unit Step
    u = unit_step(n, n0=0)
    axes[0, 1].stem(n, u, basefmt=' ')
    axes[0, 1].set_title('Unit Step: u[n]')
    axes[0, 1].set_xlabel('n')
    axes[0, 1].set_ylabel('u[n]')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 1].axvline(x=0, color='k', linewidth=0.5)
    
    # 3. Exponential Sequence (decay)
    a = 0.8
    x_exp = exponential_sequence(n, a)
    axes[1, 0].stem(n, x_exp, basefmt=' ')
    axes[1, 0].set_title(f'Exponential Sequence: x[n] = {a}^n')
    axes[1, 0].set_xlabel('n')
    axes[1, 0].set_ylabel('x[n]')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 0].axvline(x=0, color='k', linewidth=0.5)
    
    # 4. Sinusoidal Sequence
    A = 1.0
    omega = 2 * np.pi / 8  # Period of 8 samples
    x_sin = sinusoidal_sequence(n, A, omega)
    axes[1, 1].stem(n, x_sin, basefmt=' ')
    axes[1, 1].set_title(f'Sinusoidal: x[n] = cos(2πn/8)')
    axes[1, 1].set_xlabel('n')
    axes[1, 1].set_ylabel('x[n]')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 1].axvline(x=0, color='k', linewidth=0.5)
    
    plt.tight_layout()
    output_path = output_dir / 'basic_signals.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Figure saved as '{output_path}'")
    plt.show()
    
    # Print some signal properties
    print("\n" + "="*50)
    print("Signal Properties")
    print("="*50)
    print(f"Unit Impulse at n=0: δ[0] = {delta[n==0][0]}")
    print(f"Unit Step at n=0: u[0] = {u[n==0][0]}")
    print(f"Unit Step at n=-1: u[-1] = {u[n==-1][0]}")
    print(f"Exponential at n=0: {a}^0 = {x_exp[n==0][0]}")
    print(f"Exponential at n=5: {a}^5 = {x_exp[n==5][0]:.4f}")
    print(f"Sinusoidal at n=0: cos(0) = {x_sin[n==0][0]:.4f}")
    print(f"Sinusoidal period: 8 samples")


if __name__ == "__main__":
    main()
