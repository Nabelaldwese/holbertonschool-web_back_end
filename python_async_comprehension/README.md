# Python - Asynchronous Comprehensions and Generators

## Overview
This project explores asynchronous generators and asynchronous comprehensions in Python. It focuses on how to write async generators, how to use async comprehensions, and how to type-annotate generators. These concepts are important when working with asynchronous data streams and concurrent operations.

## Learning Objectives
By completing this project, I learned how to:
- Write an asynchronous generator
- Use async comprehensions
- Type-annotate generators
- Write clear documentation for modules and functions
- Apply asynchronous programming concepts in real scenarios

## Requirements
- Ubuntu 20.04 LTS  
- Python 3.9  
- All files must end with a new line  
- The first line of all Python files must be:
#!/usr/bin/env python3
- Code must follow pycodestyle (version 2.5.x)  
- File length will be tested using wc  
- All functions and coroutines must be type-annotated  

## Documentation Requirements
All modules and functions must include proper documentation. A valid documentation is a complete sentence explaining the purpose of the module or function and is not just a single word.

Examples to verify documentation:
python3 -c 'print(__import__("my_module").__doc__)'  
python3 -c 'print(__import__("my_module").my_function.__doc__)'  

## Example: Asynchronous Generator
from typing import Generator
import asyncio

async def async_generator() -> Generator[float, None, None]:
    """Yield random numbers asynchronously."""
    import random
    for _ in range(5):
        await asyncio.sleep(1)
        yield random.random()

## Example: Async Comprehension
async def async_comprehension():
    """Collect values from an async generator using comprehension."""
    return [i async for i in async_generator()]

## Key Concepts
Asynchronous Generator: A generator defined with async def that uses yield and await.  
Async Comprehension: A comprehension that iterates over an async generator.  
Type Annotation for Generators: Using typing.Generator or typing.AsyncGenerator to define types.
