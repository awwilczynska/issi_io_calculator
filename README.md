# Simple Calculator

A Python-based calculator implementation with comprehensive testing and code coverage reporting. This project demonstrates best practices in software engineering including unit testing, code coverage, and proper documentation.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division
- **Error Handling**: Proper handling of division by zero
- **Object-Oriented Design**: Calculator class with encapsulated operands
- **Interactive CLI**: User-friendly command-line interface
- **Comprehensive Testing**: Full test suite with pytest
- **Code Coverage**: HTML coverage reports generated

## Project Structure

```
issi_io_calculator/
├── calculator.py          # Main calculator module
├── test_calculator.py     # Unit tests
├── README.md             # This file
├── .gitignore            # Git ignore rules
├── .coveragerc           # Coverage configuration file
├── .coverage             # Coverage data file (generated after running coverage)
├── .git/                 # Git version control directory
├── .pytest_cache/        # Pytest cache directory (generated during testing)
├── __pycache__/          # Python bytecode cache
└── htmlcov/              # Code coverage reports (HTML)
    ├── index.html        # Main coverage report
    ├── calculator_py.html # Calculator module coverage
    ├── test_calculator_py.html # Test file coverage
    ├── function_index.html # Function coverage index
    ├── class_index.html  # Class coverage index
    └── [other HTML/CSS/JS files] # Supporting coverage assets
```

## Requirements

- Python 3.6+
- pytest (for running tests)
- coverage (for generating coverage reports)

## Configuration Files

The project includes several configuration files:

- **`.coveragerc`**: Configuration for code coverage reporting, excludes `if __name__ == "__main__":` blocks from coverage analysis
- **`.gitignore`**: Comprehensive Python gitignore rules for excluding temporary files, virtual environments, and IDE files

## Generated Files & Directories

During development and testing, the following files and directories are automatically generated:

- **`.coverage`**: Coverage data file created when running coverage analysis
- **`.pytest_cache/`**: Pytest cache directory for improved test performance
- **`__pycache__/`**: Python bytecode cache for faster module loading
- **`htmlcov/`**: HTML coverage reports directory with detailed coverage visualization

## Installation

### Option 1: Using Virtual Environment (Recommended)

1. Clone or download this repository
2. Navigate to the calculator directory
3. Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

4. Install required dependencies:

```bash
pip install pytest coverage
```

### Option 2: Global Installation

1. Clone or download this repository
2. Navigate to the calculator directory
3. Install required dependencies:

```bash
pip install pytest coverage
```

## Usage

### Interactive Calculator

Run the calculator in interactive mode:

```bash
python calculator.py
```

This will start an interactive session where you can:
1. Select an operation (1-4)
2. Enter two numbers
3. View the calculation result

### Using the Calculator Class

You can also import and use the Calculator class in your own Python code:

```python
from calculator import Calculator

# Create calculator instance with two operands
calc = Calculator(10, 5)

# Perform operations
result_add = calc.sum()        # 15.0
result_sub = calc.subtract()   # 5.0
result_mul = calc.multiply()   # 50.0
result_div = calc.divide()     # 2.0
```

## Testing

### Running Tests

Execute all unit tests:

```bash
pytest test_calculator.py
```

Run tests with verbose output:

```bash
pytest test_calculator.py -v
```

### Test Coverage

The project includes comprehensive test coverage for all calculator operations:

- **Addition**: Positive numbers, negative numbers, and mixed operations
- **Subtraction**: Positive numbers, negative numbers, and mixed operations  
- **Multiplication**: Regular numbers, negative numbers, and multiplication by zero
- **Division**: Normal division and proper error handling for division by zero

### Generate Coverage Report

To generate HTML coverage reports:

```bash
coverage run -m pytest test_calculator.py
coverage html
```

Open `htmlcov/index.html` in your web browser to view the detailed coverage report.

**Note**: The project includes a `.coveragerc` configuration file that:
- Sets the source directory for coverage analysis
- Excludes `if __name__ == "__main__":` blocks from coverage calculations to focus on testable code

## API Reference

### Calculator Class

#### Constructor
```python
Calculator(op1: float, op2: float)
```
Initialize calculator with two operands.

**Parameters:**
- `op1` (float): First operand
- `op2` (float): Second operand

#### Methods

##### `sum() -> float`
Returns the sum of the two operands.

##### `subtract() -> float`
Returns the difference (op1 - op2).

##### `multiply() -> float`
Returns the product of the two operands.

##### `divide() -> float`
Returns the quotient (op1 / op2).

**Raises:**
- `ZeroDivisionError`: When attempting to divide by zero

## Development

### Development Environment Setup

It's recommended to use a virtual environment for development:

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install development dependencies
pip install pytest coverage
```

### Code Style
- Follow PEP 8 Python style guidelines
- Use type hints for function parameters and return values
- Include comprehensive docstrings for all classes and methods
- Private attributes use double underscore prefix (`__attribute`)

### Testing Guidelines
- Write tests for all new functionality
- Ensure edge cases are covered (e.g., division by zero, negative numbers)
- Test both positive and negative scenarios
- Maintain test coverage above 90%
- Use descriptive test function names

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is part of an academic assignment for AGH University of Science and Technology, course "Wybrane zagadnienia z inżynierii oprogramowania" (Selected Topics in Software Engineering).

## Project Status

This project demonstrates:
- ✅ Object-oriented programming principles
- ✅ Comprehensive unit testing with pytest
- ✅ Code coverage reporting
- ✅ Proper error handling and validation
- ✅ Documentation and code comments
- ✅ Virtual environment usage
- ✅ Git version control with appropriate .gitignore

## Author
Aleksandra Wilczyńska
Created as part of the postgraduate studies ISSI (Inżynieria Systemów Sztucznej Inteligencji) program at AGH University of Science and Technology.