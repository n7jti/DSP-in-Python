#!/usr/bin/env python3
"""
Lesson 1: Discrete-time Signals - Complex Exponentials
=======================================================

This script demonstrates complex exponential signals and Euler's formula:
e^(jωn) = cos(ωn) + j·sin(ωn)

Author: DSP-in-Python Repository
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def complex_exponential(n, omega):
    """
    Generate a complex exponential: e^(j*omega*n)
    
    Parameters:
    -----------
    n : array-like
        Time indices
    omega : float
        Frequency in radians per sample
    
    Returns:
    --------
    z : ndarray (complex)
        Complex exponential signal
    """
    return np.exp(1j * omega * n)


def main():
    """Demonstrate complex exponentials and Euler's formula."""
    
    # Set up output directory
    output_dir = Path(__file__).parent.parent / 'data'
    output_dir.mkdir(exist_ok=True)
    
    # Time index
    n = np.arange(0, 32)
    
    # Frequency
    omega = 2 * np.pi / 8  # Period of 8 samples
    
    # Generate complex exponential
    z = complex_exponential(n, omega)
    
    # Separate into real and imaginary parts
    real_part = np.real(z)
    imag_part = np.imag(z)
    magnitude = np.abs(z)
    phase = np.angle(z)
    
    # Create figure with subplots
    fig = plt.figure(figsize=(14, 10))
    fig.suptitle('Complex Exponential Signals: e^(j·2πn/8)', fontsize=16, fontweight='bold')
    
    # Create grid for subplots
    gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)
    
    # 1. Real part
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.stem(n, real_part, basefmt=' ')
    ax1.set_title('Real Part: cos(2πn/8)')
    ax1.set_xlabel('n')
    ax1.set_ylabel('Re{e^(jωn)}')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='k', linewidth=0.5)
    
    # 2. Imaginary part
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.stem(n, imag_part, basefmt=' ', linefmt='C1-', markerfmt='C1o')
    ax2.set_title('Imaginary Part: sin(2πn/8)')
    ax2.set_xlabel('n')
    ax2.set_ylabel('Im{e^(jωn)}')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='k', linewidth=0.5)
    
    # 3. Magnitude
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.stem(n, magnitude, basefmt=' ', linefmt='C2-', markerfmt='C2o')
    ax3.set_title('Magnitude: |e^(jωn)|')
    ax3.set_xlabel('n')
    ax3.set_ylabel('|e^(jωn)|')
    ax3.grid(True, alpha=0.3)
    ax3.axhline(y=1, color='r', linestyle='--', linewidth=1, alpha=0.5, label='|z| = 1')
    ax3.legend()
    ax3.set_ylim(0, 1.2)
    
    # 4. Phase
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.stem(n, phase, basefmt=' ', linefmt='C3-', markerfmt='C3o')
    ax4.set_title('Phase: ∠e^(jωn)')
    ax4.set_xlabel('n')
    ax4.set_ylabel('∠e^(jωn) [radians]')
    ax4.grid(True, alpha=0.3)
    ax4.axhline(y=0, color='k', linewidth=0.5)
    ax4.axhline(y=np.pi, color='r', linestyle='--', linewidth=1, alpha=0.5)
    ax4.axhline(y=-np.pi, color='r', linestyle='--', linewidth=1, alpha=0.5)
    ax4.set_ylim(-np.pi - 0.5, np.pi + 0.5)
    
    # 5. Complex plane (first 8 samples)
    ax5 = fig.add_subplot(gs[2, :])
    circle = plt.Circle((0, 0), 1, fill=False, color='gray', linestyle='--', linewidth=1)
    ax5.add_patch(circle)
    
    # Plot trajectory
    n_plot = n[:9]  # First period
    z_plot = z[:9]
    ax5.plot(np.real(z_plot), np.imag(z_plot), 'b-', linewidth=1, alpha=0.5)
    ax5.scatter(np.real(z_plot), np.imag(z_plot), c=n_plot, cmap='viridis', s=100, 
                edgecolors='black', linewidth=1, zorder=3)
    
    # Add colorbar to show time progression
    cbar = plt.colorbar(ax5.scatter(np.real(z_plot), np.imag(z_plot), c=n_plot, 
                                     cmap='viridis', s=100), ax=ax5)
    cbar.set_label('Sample index n')
    
    # Mark starting point
    ax5.plot(1, 0, 'ro', markersize=12, label='n=0')
    
    ax5.set_xlabel('Real Part')
    ax5.set_ylabel('Imaginary Part')
    ax5.set_title('Complex Plane Trajectory (First Period)')
    ax5.grid(True, alpha=0.3)
    ax5.axhline(y=0, color='k', linewidth=0.5)
    ax5.axvline(x=0, color='k', linewidth=0.5)
    ax5.set_aspect('equal')
    ax5.legend()
    ax5.set_xlim(-1.3, 1.3)
    ax5.set_ylim(-1.3, 1.3)
    
    output_path = output_dir / 'complex_exponentials.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Figure saved as '{output_path}'")
    plt.show()
    
    # Print Euler's formula verification
    print("\n" + "="*60)
    print("Euler's Formula Verification: e^(jωn) = cos(ωn) + j·sin(ωn)")
    print("="*60)
    print(f"Frequency ω = 2π/8 = {omega:.4f} rad/sample")
    print(f"\nAt n=0:")
    print(f"  e^(j·0) = {z[0]:.4f}")
    print(f"  cos(0) + j·sin(0) = {real_part[0]:.4f} + j·{imag_part[0]:.4f}")
    print(f"\nAt n=2:")
    print(f"  e^(j·π/2) = {z[2]:.4f}")
    print(f"  cos(π/2) + j·sin(π/2) = {real_part[2]:.4f} + j·{imag_part[2]:.4f}")
    print(f"\nAt n=4:")
    print(f"  e^(j·π) = {z[4]:.4f}")
    print(f"  cos(π) + j·sin(π) = {real_part[4]:.4f} + j·{imag_part[4]:.4f}")
    print(f"\nNote: All magnitudes = 1, as |e^(jωn)| = 1 for real ω")
    print(f"Period = 8 samples")


if __name__ == "__main__":
    main()
