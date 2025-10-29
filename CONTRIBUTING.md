# Contributing to DSP-in-Python

Thank you for your interest in contributing to DSP-in-Python! This document provides guidelines for contributing to this educational repository.

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

1. **New Examples**: Python implementations of DSP concepts
2. **Bug Fixes**: Corrections to existing code
3. **Documentation**: Improvements to README files, comments, or guides
4. **Exercises**: New practice problems with solutions
5. **Data Files**: Sample data for demonstrations
6. **Visualizations**: Better plots or animations

### Getting Started

1. **Fork the Repository**
   ```bash
   git clone https://github.com/n7jti/DSP-in-Python.git
   cd DSP-in-Python
   ```

2. **Set Up Your Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Code Guidelines

### Python Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable names
- Include docstrings for functions and classes
- Add comments to explain complex logic

### Code Example Template

```python
#!/usr/bin/env python3
"""
Lesson X: Topic Name - Subtopic
================================

Brief description of what this script demonstrates.

Author: Your Name (optional)
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
# Add other imports as needed


def example_function(param1, param2):
    """
    Brief description of function.
    
    Parameters:
    -----------
    param1 : type
        Description
    param2 : type
        Description
    
    Returns:
    --------
    result : type
        Description
    
    Examples:
    ---------
    >>> result = example_function(1, 2)
    """
    # Implementation
    pass


def main():
    """Main function demonstrating the concept."""
    # Your code here
    pass


if __name__ == "__main__":
    main()
```

### Documentation Standards

Each lesson should include:

1. **README.md** with:
   - Overview of the topic
   - Learning objectives
   - Link to the video lecture
   - Key concepts
   - Code examples
   - MATLAB to Python conversion notes (where applicable)
   - Links to additional resources

2. **Example Scripts** that:
   - Are self-contained and runnable
   - Include clear comments
   - Generate informative plots
   - Print relevant output
   - Save figures to the `data/` directory

3. **Exercise Files** (optional) that:
   - Provide clear problem statements
   - Include solution code (can be in a separate file)
   - Test understanding of key concepts

## Lesson Structure

Each lesson directory should follow this structure:

```
lesson_XX/
├── README.md              # Lesson overview and guide
├── examples/              # Runnable Python scripts
│   ├── example_1.py
│   └── example_2.py
├── exercises/             # Practice problems
│   ├── exercise_1.py
│   └── solutions/         # Solutions (separate subdirectory)
│       └── exercise_1_solution.py
└── data/                  # Generated plots and data files
    ├── figure_1.png
    └── sample_data.npy
```

## Commit Guidelines

### Commit Messages

Use clear, descriptive commit messages:

```
Add convolution example for Lesson 4

- Implement discrete convolution function
- Add visualization comparing input signals and output
- Include example with rectangular pulses
```

Format:
- First line: Brief summary (50 chars or less)
- Blank line
- Detailed description (if needed)
- List specific changes with bullet points

### What to Commit

**Do commit:**
- Source code (.py files)
- Documentation (.md files)
- Example data files (small, necessary files)
- Requirements updates

**Don't commit:**
- Generated plots (unless they're reference examples)
- Large data files (> 1MB)
- Virtual environment files
- IDE-specific files
- `__pycache__` directories
- `.pyc` files

## Testing Your Changes

Before submitting:

1. **Test Your Code**
   ```bash
   cd lessons/lesson_XX/examples
   python your_script.py
   ```

2. **Verify Imports**
   - Ensure all required packages are in `requirements.txt`
   - Test in a fresh virtual environment if possible

3. **Check Output**
   - Plots should be clear and well-labeled
   - Console output should be informative
   - No error messages or warnings

4. **Review Documentation**
   - Links should work
   - Code examples should be accurate
   - Instructions should be clear

## Submitting a Pull Request

1. **Update Your Branch**
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Push Your Changes**
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create Pull Request**
   - Go to GitHub and create a new pull request
   - Provide a clear title and description
   - Reference any related issues
   - Explain what you changed and why

4. **Pull Request Template**
   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] New example
   - [ ] Bug fix
   - [ ] Documentation update
   - [ ] Exercise addition
   
   ## Lesson(s) Affected
   - Lesson X: Topic Name
   
   ## Testing
   - [ ] Code runs without errors
   - [ ] Plots are generated correctly
   - [ ] Documentation is accurate
   
   ## Screenshots (if applicable)
   [Include plots or output]
   ```

## Reporting Issues

When reporting bugs or suggesting improvements:

1. **Search Existing Issues** first
2. **Use a Clear Title** describing the problem
3. **Provide Details**:
   - What you expected to happen
   - What actually happened
   - Steps to reproduce
   - Python version and OS
   - Relevant code snippets or error messages

## Code of Conduct

- Be respectful and constructive
- Focus on education and clarity
- Help others learn
- Give credit where due
- Follow the MIT license terms

## Questions?

If you have questions about contributing:
- Open an issue with the "question" label
- Check existing documentation
- Review similar examples in the repository

## Recognition

Contributors will be recognized in the repository. Significant contributions may be highlighted in release notes.

Thank you for helping make DSP concepts more accessible through Python!
