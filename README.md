# Python - Type Annotations

## Overview
This project introduces **type annotations in Python 3** and explains how they improve code readability, maintainability, and reliability. It covers how to annotate variables and function signatures, the concept of duck typing, and how to validate code using **mypy**.

## Learning Objectives
By completing this project, I learned how to:
- Use type annotations in Python 3
- Specify function signatures and variable types
- Understand the concept of duck typing
- Validate code using mypy
- Write clear and well-documented Python modules, classes, and functions

## Requirements
- Ubuntu 20.04 LTS  
- Python 3.9  
- All files must end with a new line  
- The first line of all Python files must be:
#!/usr/bin/env python3
- Code must follow pycodestyle (version 2.5.)  
- All files must be executable  
- File length will be tested using wc  

## Documentation Requirements
All modules, classes, and functions must include proper documentation. A valid documentation is a complete sentence that clearly explains the purpose of the module, class, or function and is not just a single word.

Examples to verify documentation:
python3 -c 'print(__import__("my_module").__doc__)'  
python3 -c 'print(__import__("my_module").MyClass.__doc__)'  
python3 -c 'print(__import__("my_module").my_function.__doc__)'  

## Example: Type Annotation
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

## Validating with MyPy
mypy my_file.py

## Key Concepts
Type Annotations: Used to indicate expected types of variables, parameters, and return values.  
Duck Typing: Python focuses on behavior rather than strict type definitions; if it behaves like a duck, it is a duck.
