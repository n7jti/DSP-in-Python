# DSP Course Lessons Index

This document provides a comprehensive index of all 28 lessons in the DSP course with links to the corresponding YouTube lectures and lesson directories.

## How to Use This Index

Each lesson includes:
- **YouTube Link**: Direct link to Professor Radke's video lecture
- **Lesson Directory**: Path to the lesson folder in this repository
- **Topics Covered**: Key concepts and techniques
- **Python Libraries**: Main Python tools used in the examples

## Lessons Overview

### Part I: Fundamentals

#### [Lesson 1: Discrete-time Signals](./lessons/lesson_01/)
- **Video**: [DSP Lecture 1](https://www.youtube.com/watch?v=hVOA8VtKLgk&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=1)
- **Topics**: Signal types, continuous vs discrete, unit step, unit impulse, exponentials
- **Libraries**: NumPy, Matplotlib

#### [Lesson 2: Python for DSP](./lessons/lesson_02/)
- **Video**: [DSP Lecture 2](https://www.youtube.com/watch?v=FmFlQFFM-xM&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=2)
- **Topics**: Python basics, NumPy arrays, SciPy signal processing, Matplotlib plotting
- **Libraries**: NumPy, SciPy, Matplotlib, Jupyter

#### [Lesson 3: Linear, Time-Invariant Systems](./lessons/lesson_03/)
- **Video**: [DSP Lecture 3](https://www.youtube.com/watch?v=1GBOHQzjQAc&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=3)
- **Topics**: LTI systems, impulse response, system properties (linearity, time-invariance)
- **Libraries**: NumPy, SciPy.signal

#### [Lesson 4: Convolution and its Properties](./lessons/lesson_04/)
- **Video**: [DSP Lecture 4](https://www.youtube.com/watch?v=acAw5WGtzuk&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=4)
- **Topics**: Discrete convolution, convolution properties, implementation techniques
- **Libraries**: NumPy, SciPy.signal

#### [Lesson 5: The Fourier Series](./lessons/lesson_05/)
- **Video**: [DSP Lecture 5](https://www.youtube.com/watch?v=U0pKexplog8&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=5)
- **Topics**: Periodic signals, Fourier series representation, synthesis and analysis
- **Libraries**: NumPy, Matplotlib

#### [Lesson 6: The Fourier Transform](./lessons/lesson_06/)
- **Video**: [DSP Lecture 6](https://www.youtube.com/watch?v=YYFejAG47Z0&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=6)
- **Topics**: Continuous Fourier transform, transform pairs, properties
- **Libraries**: NumPy, SciPy.fft

#### [Lesson 7: Frequency Response](./lessons/lesson_07/)
- **Video**: [DSP Lecture 7](https://www.youtube.com/watch?v=hMTww2KaOeE&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=7)
- **Topics**: Frequency response of LTI systems, magnitude and phase response
- **Libraries**: SciPy.signal, Matplotlib

#### [Lesson 8: The Discrete-Time Fourier Transform](./lessons/lesson_08/)
- **Video**: [DSP Lecture 8](https://www.youtube.com/watch?v=RNBJGUa4L1Q&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=8)
- **Topics**: DTFT definition, properties, relationship to z-transform
- **Libraries**: NumPy, SciPy.fft

#### [Lesson 9: The z-Transform](./lessons/lesson_09/)
- **Video**: [DSP Lecture 9](https://www.youtube.com/watch?v=57LvJM_cg94&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=9)
- **Topics**: z-transform definition, region of convergence, common transforms
- **Libraries**: NumPy, SciPy.signal

#### [Lesson 10: The Inverse z-Transform; Poles and Zeros](./lessons/lesson_10/)
- **Video**: [DSP Lecture 10](https://www.youtube.com/watch?v=u6rJF3KtZPw&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=10)
- **Topics**: Inverse z-transform, pole-zero analysis, stability
- **Libraries**: NumPy, SciPy.signal, Matplotlib

#### [Lesson 11: The Discrete Fourier Transform](./lessons/lesson_11/)
- **Video**: [DSP Lecture 11](https://www.youtube.com/watch?v=kd5RAIW3wFs&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=11)
- **Topics**: DFT definition, circular convolution, DFT properties
- **Libraries**: NumPy.fft, SciPy.fft

### Part II: Fast Algorithms and Sampling

#### [Lesson 12: Radix-2 Fast Fourier Transforms](./lessons/lesson_12/)
- **Video**: [DSP Lecture 12](https://www.youtube.com/watch?v=M0Sa8fLOajA&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=12)
- **Topics**: FFT algorithm, computational complexity, decimation-in-time
- **Libraries**: NumPy.fft

#### [Lesson 13: The Cooley-Tukey and Good-Thomas FFTs](./lessons/lesson_13/)
- **Video**: [DSP Lecture 13](https://www.youtube.com/watch?v=k8NZ-wMMWzk&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=13)
- **Topics**: Advanced FFT algorithms, mixed-radix FFT
- **Libraries**: NumPy.fft, SciPy.fft

#### [Lesson 14: The Sampling Theorem](./lessons/lesson_14/)
- **Video**: [DSP Lecture 14](https://www.youtube.com/watch?v=FcXZ28BX-xE&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=14)
- **Topics**: Nyquist rate, aliasing, reconstruction
- **Libraries**: NumPy, SciPy.signal, Matplotlib

#### [Lesson 15: Continuous-Time Filtering with Digital Systems](./lessons/lesson_15/)
- **Video**: [DSP Lecture 15](https://www.youtube.com/watch?v=t6ACbO4kbKQ&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=15)
- **Topics**: Upsampling, downsampling, interpolation, decimation
- **Libraries**: SciPy.signal.resample

#### [Lesson 16: Multirate Signal Processing and Polyphase](./lessons/lesson_16/)
- **Video**: [DSP Lecture 16](https://www.youtube.com/watch?v=9YFmTdVYkdI&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=16)
- **Topics**: Polyphase decomposition, efficient multirate systems
- **Libraries**: SciPy.signal

### Part III: Filter Design

#### [Lesson 17: FIR Filter Design (Least-Squares)](./lessons/lesson_17/)
- **Video**: [DSP Lecture 17](https://www.youtube.com/watch?v=3AajZbHDPmQ&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=17)
- **Topics**: FIR filter design, windowing methods, least-squares approximation
- **Libraries**: SciPy.signal.firwin

#### [Lesson 18: FIR Filter Design (Chebyshev)](./lessons/lesson_18/)
- **Video**: [DSP Lecture 18](https://www.youtube.com/watch?v=Fx7DkM8CbSo&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=18)
- **Topics**: Chebyshev approximation, Parks-McClellan algorithm
- **Libraries**: SciPy.signal.remez

#### [Lesson 19: IIR Filter Design](./lessons/lesson_19/)
- **Video**: [DSP Lecture 19](https://www.youtube.com/watch?v=jRHVf5d1KTU&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=19)
- **Topics**: Butterworth, Chebyshev, elliptic filters, bilinear transform
- **Libraries**: SciPy.signal (butter, cheby1, cheby2, ellip)

### Part IV: Adaptive Filters

#### [Lesson 20: The Wiener Filter](./lessons/lesson_20/)
- **Video**: [DSP Lecture 20](https://www.youtube.com/watch?v=DH5Jw5gIPuM&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=20)
- **Topics**: Optimal filtering, Wiener-Hopf equations, noise reduction
- **Libraries**: NumPy, SciPy.signal

#### [Lesson 21: Gradient Descent and LMS](./lessons/lesson_21/)
- **Video**: [DSP Lecture 21](https://www.youtube.com/watch?v=RnD-Gj9t_CE&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=21)
- **Topics**: Adaptive filtering, LMS algorithm, convergence
- **Libraries**: NumPy

#### [Lesson 22: Least Squares and Recursive Least Squares](./lessons/lesson_22/)
- **Video**: [DSP Lecture 22](https://www.youtube.com/watch?v=hU7JJVFIq6k&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=22)
- **Topics**: RLS algorithm, exponential weighting, tracking
- **Libraries**: NumPy

### Part V: Quantization and Advanced Topics

#### [Lesson 23: Introduction to Quantization](./lessons/lesson_23/)
- **Video**: [DSP Lecture 23](https://www.youtube.com/watch?v=fEz4PxG5A1c&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=23)
- **Topics**: Quantization noise, SNR, uniform quantization
- **Libraries**: NumPy

#### [Lesson 24: Differential Quantization and Vocoding](./lessons/lesson_24/)
- **Video**: [DSP Lecture 24](https://www.youtube.com/watch?v=DH95K_4r_Aw&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=24)
- **Topics**: DPCM, delta modulation, vocoders
- **Libraries**: NumPy, SciPy

#### [Lesson 25: Perfect Reconstruction Filter Banks](./lessons/lesson_25/)
- **Video**: [DSP Lecture 25](https://www.youtube.com/watch?v=vVlQQTm8bEY&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=25)
- **Topics**: Filter banks, subband coding, introduction to wavelets
- **Libraries**: PyWavelets

#### [Lesson 26: Wavelets (Part 1)](./lessons/lesson_26/)
- **Video**: [DSP Lecture 26](https://www.youtube.com/watch?v=v4d1FHOhE4M&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=26)
- **Topics**: Wavelet theory, continuous wavelet transform
- **Libraries**: PyWavelets

#### [Lesson 27: Wavelets (Part 2)](./lessons/lesson_27/)
- **Video**: [DSP Lecture 27](https://www.youtube.com/watch?v=Y_5bx4sBN10&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=27)
- **Topics**: Discrete wavelet transform, applications
- **Libraries**: PyWavelets

#### [Lesson 28: Advanced DSP Topics](./lessons/lesson_28/)
- **Video**: [DSP Lecture 28](https://www.youtube.com/watch?v=Dy1bv8E9F48&list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et&index=28)
- **Topics**: Modern signal processing, course review
- **Libraries**: Various

## Navigation Tips

- Each lesson directory contains:
  - `README.md`: Detailed lesson information and learning objectives
  - `examples/`: Runnable Python scripts demonstrating concepts
  - `exercises/`: Practice problems with solutions
  - `data/`: Sample data files for demonstrations

- Start with Lesson 1 and progress sequentially for best results
- Most examples can be run independently
- Refer to the main `requirements.txt` for all dependencies

## Additional Resources

- [Complete YouTube Playlist](https://www.youtube.com/playlist?list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et)
- [Professor Radke's Course Page](https://sites.ecse.rpi.edu/~rjradke/dspcourse.html)
- [SciPy Signal Processing Tutorial](https://docs.scipy.org/doc/scipy/tutorial/signal.html)
