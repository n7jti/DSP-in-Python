"""
Common DSP Utility Functions
=============================

This module contains utility functions used across multiple DSP lessons.

Author: DSP-in-Python Repository
License: MIT
"""

import numpy as np


def unit_impulse(n, n0=0):
    """
    Generate a unit impulse (delta function).
    
    Parameters:
    -----------
    n : array-like
        Time indices
    n0 : int or array-like
        Position(s) of the impulse(s) (default: 0)
    
    Returns:
    --------
    delta : ndarray
        Unit impulse signal
    
    Examples:
    ---------
    >>> n = np.arange(-5, 6)
    >>> delta = unit_impulse(n, n0=0)
    >>> delta = unit_impulse(n, n0=[0, 3])  # Multiple impulses
    """
    n = np.asarray(n)
    delta = np.zeros_like(n, dtype=float)
    
    if np.isscalar(n0):
        n0 = [n0]
    
    for pos in n0:
        delta[n == pos] = 1.0
    
    return delta


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
    
    Examples:
    ---------
    >>> n = np.arange(-5, 6)
    >>> u = unit_step(n, n0=0)
    """
    return np.where(n >= n0, 1.0, 0.0)


def rect_pulse(n, n1, n2):
    """
    Generate a rectangular pulse between n1 and n2 (inclusive).
    
    Parameters:
    -----------
    n : array-like
        Time indices
    n1 : int
        Start of pulse
    n2 : int
        End of pulse
    
    Returns:
    --------
    x : ndarray
        Rectangular pulse signal
    
    Examples:
    ---------
    >>> n = np.arange(-5, 6)
    >>> x = rect_pulse(n, -2, 2)
    """
    return np.where((n >= n1) & (n <= n2), 1.0, 0.0)


def exponential_sequence(n, a, n0=0):
    """
    Generate an exponential sequence: x[n] = a^(n-n0) for n >= n0
    
    Parameters:
    -----------
    n : array-like
        Time indices
    a : float or complex
        Base of the exponential
    n0 : int
        Starting position (default: 0)
    
    Returns:
    --------
    x : ndarray
        Exponential sequence (zero for n < n0)
    
    Examples:
    ---------
    >>> n = np.arange(0, 10)
    >>> x = exponential_sequence(n, 0.8)
    """
    n = np.asarray(n)
    x = np.zeros_like(n, dtype=complex if np.iscomplexobj(a) else float)
    mask = n >= n0
    x[mask] = a ** (n[mask] - n0)
    return x


def complex_exponential(n, omega, phi=0):
    """
    Generate a complex exponential: e^(j(omega*n + phi))
    
    Parameters:
    -----------
    n : array-like
        Time indices
    omega : float
        Frequency in radians per sample
    phi : float
        Phase offset in radians (default: 0)
    
    Returns:
    --------
    z : ndarray (complex)
        Complex exponential signal
    
    Examples:
    ---------
    >>> n = np.arange(0, 16)
    >>> z = complex_exponential(n, 2*np.pi/8)
    """
    return np.exp(1j * (omega * np.asarray(n) + phi))


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
    
    Examples:
    ---------
    >>> n = np.arange(0, 16)
    >>> x = sinusoidal_sequence(n, 1.0, 2*np.pi/8)
    """
    return A * np.cos(omega * np.asarray(n) + phi)


def shift_signal(x, k):
    """
    Shift a signal by k samples (circular shift for finite-length signals).
    
    Parameters:
    -----------
    x : array-like
        Input signal
    k : int
        Shift amount (positive = right shift, negative = left shift)
    
    Returns:
    --------
    y : ndarray
        Shifted signal
    
    Examples:
    ---------
    >>> x = np.array([1, 2, 3, 4, 5])
    >>> y = shift_signal(x, 2)  # Shift right by 2
    """
    return np.roll(x, k)


def downsample(x, M):
    """
    Downsample a signal by factor M (keep every M-th sample).
    
    Parameters:
    -----------
    x : array-like
        Input signal
    M : int
        Downsampling factor
    
    Returns:
    --------
    y : ndarray
        Downsampled signal
    
    Examples:
    ---------
    >>> x = np.arange(10)
    >>> y = downsample(x, 2)  # [0, 2, 4, 6, 8]
    """
    return np.asarray(x)[::M]


def upsample(x, L):
    """
    Upsample a signal by factor L (insert L-1 zeros between samples).
    
    Parameters:
    -----------
    x : array-like
        Input signal
    L : int
        Upsampling factor
    
    Returns:
    --------
    y : ndarray
        Upsampled signal
    
    Examples:
    ---------
    >>> x = np.array([1, 2, 3])
    >>> y = upsample(x, 2)  # [1, 0, 2, 0, 3, 0]
    """
    x = np.asarray(x)
    y = np.zeros(len(x) * L, dtype=x.dtype)
    y[::L] = x
    return y


def db(x, power=False):
    """
    Convert amplitude or power to decibels.
    
    Parameters:
    -----------
    x : array-like
        Input values
    power : bool
        If True, treats x as power (10*log10). If False, treats as amplitude (20*log10)
    
    Returns:
    --------
    y : ndarray
        Values in dB
    
    Examples:
    ---------
    >>> x = np.array([1, 0.5, 0.1])
    >>> y = db(x)  # Amplitude to dB
    >>> y = db(x, power=True)  # Power to dB
    """
    x = np.asarray(x)
    factor = 10 if power else 20
    return factor * np.log10(np.abs(x) + 1e-20)  # Add small value to avoid log(0)


def normalize(x):
    """
    Normalize a signal to have maximum absolute value of 1.
    
    Parameters:
    -----------
    x : array-like
        Input signal
    
    Returns:
    --------
    y : ndarray
        Normalized signal
    
    Examples:
    ---------
    >>> x = np.array([1, 2, 3, 4, 5])
    >>> y = normalize(x)  # Max value will be 1
    """
    x = np.asarray(x)
    max_val = np.max(np.abs(x))
    if max_val == 0:
        return x
    return x / max_val


if __name__ == "__main__":
    # Run some basic tests
    print("DSP Utility Functions - Basic Tests")
    print("=" * 50)
    
    n = np.arange(-5, 6)
    
    # Test impulse
    delta = unit_impulse(n, 0)
    print(f"Unit impulse at n=0: sum = {np.sum(delta)}")
    
    # Test step
    u = unit_step(n, 0)
    print(f"Unit step at n=0: values at n>=0 = {np.all(u[n>=0] == 1)}")
    
    # Test exponential
    x = exponential_sequence(n, 0.8, n0=0)
    print(f"Exponential 0.8^n: first 3 values = {x[n>=0][:3]}")
    
    # Test complex exponential
    z = complex_exponential(np.arange(8), 2*np.pi/8)
    print(f"Complex exponential period-8: |z| = {np.abs(z[0]):.4f}")
    
    print("\nAll basic tests passed!")
