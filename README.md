# Python Utility Functions

## Overview

This repository contains a collection of Python utility functions and a class designed to demonstrate various programming concepts. The functionalities include arithmetic operations, string manipulation, dictionary merging, and object-oriented programming.

## Features

- **Arithmetic Operations**: Add two numbers.
- **Factorial Calculation**: Compute the factorial of a number.
- **String Manipulation**: Count vowels and reverse strings.
- **Dictionary Operations**: Merge two dictionaries with value summation.
- **List Sorting**: Sort tuples by age.
- **Object-Oriented Programming**: Define and use a `Car` class.
- **Decorators**: Apply a decorator to functions.

## Functions

### `add_numbers(num1, num2)`

Adds two numbers.

- **Parameters**:
  - `num1` (int or float): The first number.
  - `num2` (int or float): The second number.
- **Returns**: Sum of `num1` and `num2`.

### `calculate_factorial(n)`

Computes the factorial of a non-negative integer.

- **Parameters**:
  - `n` (int): The integer for which to compute the factorial.
- **Returns**: Factorial of `n`.

### `count_vowels(text)`

Counts the number of vowels in a given string.

- **Parameters**:
  - `text` (str): The string to analyze.
- **Returns**: Number of vowels in `text`.

### `merge_dicts(dict1, dict2)`

Merges two dictionaries, summing values for duplicate keys.

- **Parameters**:
  - `dict1` (dict): The first dictionary.
  - `dict2` (dict): The second dictionary.
- **Returns**: Merged dictionary with summed values.

### `is_even(number)`

Checks if a number is even.

- **Parameters**:
  - `number` (int): The number to check.
- **Returns**: `True` if the number is even, otherwise `False`.

### `reverse_string(text)`

Reverses a given string.

- **Parameters**:
  - `text` (str): The string to reverse.
- **Returns**: Reversed string.

### `sort_by_age(list_of_tuples)`

Sorts a list of tuples by the second element of each tuple.

- **Parameters**:
  - `list_of_tuples` (list of tuples): The list to sort.
- **Returns**: List of tuples sorted by the second element.

## Class

### `Car`

Represents a car with make, model, and year attributes.

- **Methods**:
  - `__init__(make, model, year)`: Initializes a `Car` instance with the given make, model, and year.
  - `display_info()`: Prints the car's make, model, and year.

## Decorators

### `decorator_func(func)`

A simple decorator that prints "Decorator Applied" before calling the decorated function.

- **Parameters**:
  - `func` (function): The function to decorate.
- **Returns**: The decorated function.

### `apply_decorator(func)`

Applies the `decorator_func` decorator to a function.

- **Parameters**:
  - `func` (function): The function to decorate.
- **Returns**: The decorated function.

## Usage

Here's an example of how to use the functions and class:

```python
# Example usage
from your_module import add_numbers, calculate_factorial, count_vowels, merge_dicts, is_even, reverse_string, sort_by_age, Car

# Using the functions
print(add_numbers(5, 7))
print(calculate_factorial(5))
print(count_vowels("Hello World"))
print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(is_even(6))
print(reverse_string("hello"))

# Using the Car class
car = Car('Toyota', 'Corolla', 2020)
car.display_info()

# Sorting tuples
print(sort_by_age([('Alice', 30), ('Bob', 25), ('Charlie', 35)]))


### `LICENSE`
MIT License
-----------

Copyright (c) [2024] Benson Mwangi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

