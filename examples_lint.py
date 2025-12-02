"""Examples file to demonstrate various linting violations."""
# This file intentionally contains code violations for linting purposes


# E: pycodestyle errors
def example_e_errors():
    """Demonstrate pycodestyle errors."""
    x=1  # E225: missing whitespace around operator
    y = 2;  # E702: multiple statements on one line
    if x==y:  # E225: missing whitespace around operator
        pass
    long_line = "This is a very long line that exceeds the line length limit of 88 characters and should trigger a line too long error"  # noqa: E501


# W: pycodestyle warnings
def example_w_warnings():
    """Demonstrate pycodestyle warnings."""
    x = 1
    y = 2
    z = 3  # noqa: F841
    return x, y


# F: Pyflakes - undefined names and unused variables
def example_f_errors():
    """Demonstrate Pyflakes errors."""
    unused_variable = 42  # F841: local variable assigned but never used
    print(undefined_variable)  # F821: undefined name


# I: isort - import order
import os
import sys
from typing import Dict
import json  # should be grouped with imports
from collections import defaultdict


# UP: pyupgrade - modern Python syntax
def example_up_errors():
    """Demonstrate pyupgrade violations."""
    # Old-style type hints
    x = []  # type: list
    y = {}  # type: dict
    # Should use modern syntax instead


# B: flake8-bugbear - potential bugs
def example_b_errors():
    """Demonstrate bugbear errors."""
    mutable_default = []

    def function_with_mutable_default(items=mutable_default):  # B006: mutable default
        items.append(1)
        return items

    # Likely bug - comparison to True
    if 1 == True:  # B015: redundant comparison
        pass
 

# SIM: flake8-simplify - code simplification
def example_sim_errors():
    """Demonstrate simplify violations."""
    # Can be simplified
    if True:
        x = 1
    else:
        x = 2
    
    # Unnecessary ternary
    y = 1 if True else 0
    
    # Can use walrus operator
    data = [1, 2, 3, 4, 5]
    if len(data) > 0:
        print(data)


# A: flake8-builtins - shadowing builtins
def example_a_errors():
    """Demonstrate builtin shadowing."""
    # Shadowing built-in names
    list = [1, 2, 3]  # A001: variable name shadows a Python builtin
    dict = {"key": "value"}  # A001: variable name shadows a Python builtin
    id = "some_id"  # A001: variable name shadows a Python builtin


# C4: flake8-comprehensions - comprehension improvements
def example_c4_errors():
    """Demonstrate comprehension errors."""
    # Unnecessary list comprehension
    x = [i for i in range(5)]  # C418: unnecessary list comprehension
    
    # Can be simplified to set
    y = set([i for i in range(5)])
    
    # Nested comprehension that could be flattened
    matrix = [[1, 2], [3, 4]]
    flattened = [item for row in matrix for item in row]


# ANN: flake8-annotations - type hints
def example_missing_annotations(x, y):  # ANN001, ANN002: missing type annotation
    """Demonstrate missing annotations."""
    return x + y


def example_return_annotation(x: int, y: int):  # ANN201: missing return type annotation
    """Function without return type annotation."""
    return x + y


class ExampleClass:
    """Class with annotation issues."""

    def method_without_annotations(self, arg):  # ANN001, ANN201: missing annotations
        """Method without type annotations."""
        return arg * 2


# RUF: Ruff-specific rules
def example_ruf_errors():
    """Demonstrate Ruff-specific errors."""
    # Unused noqa directive
    x = 1  # noqa: F841
    
    # Collection literal instead of list/dict calls
    empty_dict = dict()  # RUF010: unnecessary dict call
    empty_list = list()  # RUF010: unnecessary list call


# Additional examples
def poor_naming_and_formatting():
    """More examples with multiple issues."""
    a=1  # Multiple issues: no spaces, poor naming
    b =2  # inconsistent spacing
    c= 3
    
    # Overly complex condition
    if a == 1 and b == 2 and c == 3:
        if a > 0:
            if b > 0:
                if c > 0:
                    print("All positive")


def function_with_many_parameters(a, b, c, d, e, f, g, h):  # ANN001, ANN002: missing annotations
    """Too many parameters."""
    unused = a  # F841: unused variable
    return b + c


# Using single quotes when double quotes configured
def string_examples():
    """String formatting issues."""
    single_quote = 'This should use double quotes'  # Quote style violation
    another = 'Also wrong'
    correct = "This is correct"
