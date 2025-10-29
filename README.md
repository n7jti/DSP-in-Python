# DSP-in-Python

This repository contains Python examples that follow the Digital Signal Processing (DSP) course by Professor Rich Radke from Rensselaer Polytechnic Institute. The goal is to convert the MATLAB examples used in the course to free, accessible Python examples using NumPy, SciPy, and Matplotlib.

## Course Information

- **Course**: ECSE-4530 Digital Signal Processing
- **Instructor**: Professor Rich Radke, Rensselaer Polytechnic Institute
- **YouTube Playlist**: [Digital Signal Processing](https://www.youtube.com/playlist?list=PLuh62Q4Sv7BUSzx5Jr8Wrxxn-U10qG1et)
- **Course Website**: [DSP Video Lectures](https://sites.ecse.rpi.edu/~rjradke/dspcourse.html)
- **Textbook**: Digital Signal Processing by Proakis and Manolakis (4th Edition)

## Course Lessons

The course consists of 28 comprehensive lessons covering fundamental and advanced DSP topics:

### Part I: Fundamentals (Lessons 1-11)
1. **Discrete-time Signals** - Introduction to signal types and discrete-time signal basics
2. **Python for DSP** - Python tools and libraries for DSP (NumPy, SciPy, Matplotlib)
3. **Linear, Time-Invariant Systems** - Impulse response and system properties
4. **Convolution and its Properties** - Understanding and implementing convolution
5. **The Fourier Series** - Periodic signal representation
6. **The Fourier Transform** - Transition from time to frequency domain
7. **Frequency Response** - System analysis in the frequency domain
8. **The Discrete-Time Fourier Transform** - DTFT theory and applications
9. **The z-Transform** - Transform methods for discrete systems
10. **The Inverse z-Transform; Poles and Zeros** - System analysis using poles and zeros
11. **The Discrete Fourier Transform** - DFT and its properties

### Part II: Fast Algorithms and Sampling (Lessons 12-16)
12. **Radix-2 Fast Fourier Transforms** - Efficient FFT algorithms
13. **The Cooley-Tukey and Good-Thomas FFTs** - Advanced FFT algorithms
14. **The Sampling Theorem** - Nyquist sampling and aliasing
15. **Continuous-Time Filtering with Digital Systems; Upsampling and Downsampling** - Rate conversion
16. **Multirate Signal Processing and Polyphase Representations** - Efficient multirate systems

### Part III: Filter Design (Lessons 17-19)
17. **FIR Filter Design (Least-Squares)** - FIR filter design using least-squares method
18. **FIR Filter Design (Chebyshev)** - Chebyshev approximation for FIR filters
19. **IIR Filter Design** - Infinite impulse response filter design

### Part IV: Adaptive Filters (Lessons 20-22)
20. **The Wiener Filter** - Optimal filtering for noise reduction
21. **Gradient Descent and LMS** - Adaptive filter algorithms
22. **Least Squares and Recursive Least Squares** - RLS algorithms for parameter estimation

### Part V: Quantization and Advanced Topics (Lessons 23-28)
23. **Introduction to Quantization** - Analog-to-digital conversion
24. **Differential Quantization and Vocoding** - Advanced quantization methods
25. **Perfect Reconstruction Filter Banks and Introduction to Wavelets** - Subband coding
26. **Wavelets (Part 1)** - Wavelet theory and transforms
27. **Wavelets (Part 2)** - Advanced wavelet applications
28. **Advanced DSP Topics** - Modern signal processing techniques

## Repository Structure

Each lesson has its own directory containing:
- **README.md**: Lesson overview, objectives, and references to the video lecture
- **examples/**: Python scripts demonstrating key concepts
- **exercises/**: Practice problems (where applicable)
- **data/**: Sample data files for demonstrations

```
DSP-in-Python/
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── lessons/
│   ├── lesson_01_discrete_time_signals/
│   ├── lesson_02_python_for_dsp/
│   ├── lesson_03_lti_systems/
│   ├── ...
│   └── lesson_28_advanced_topics/
└── utils/
    └── common_functions.py
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/n7jti/DSP-in-Python.git
   cd DSP-in-Python
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running Examples

Navigate to any lesson directory and run the Python scripts:

```bash
cd lessons/lesson_01_discrete_time_signals/examples
python signal_types.py
```

## Python Libraries Used

This repository uses free and open-source Python libraries:

- **NumPy**: Numerical computing and array operations
- **SciPy**: Scientific computing, including signal processing functions
- **Matplotlib**: Plotting and visualization
- **IPython/Jupyter**: Interactive computing (optional)

## Contributing

Contributions are welcome! If you'd like to add examples, fix bugs, or improve documentation:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-example`)
3. Commit your changes (`git commit -m 'Add new example for Lesson X'`)
4. Push to the branch (`git push origin feature/new-example`)
5. Open a Pull Request

Please ensure your code follows Python best practices (PEP 8) and includes appropriate comments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Professor Rich Radke for creating and sharing the excellent DSP course
- Rensselaer Polytechnic Institute for making the course materials publicly available
- The open-source Python community for the amazing scientific computing tools

## Additional Resources

- [Rich Radke's YouTube Channel](https://www.youtube.com/@RichRadke)
- [SciPy Signal Processing Documentation](https://docs.scipy.org/doc/scipy/reference/signal.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

## Contact

For questions or suggestions, please open an issue on GitHub.
