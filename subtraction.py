#!/usr/bin/env python3

"""
SciFi Calculator - Subtraction Module
-------------------------------------
This script takes two integers as input arguments and returns their difference.
Developed as part of a DevOps collaboration demo between two users.
"""

import sys

def subtract(a, b):
    """
    Subtract two integers and return the result.
    """
    return a - b

def main():
    """
    Entry point for the subtraction calculator.
    Validates inputs and performs subtraction.
    """
    print("Welcome to SciFi Calculator - Subtraction Module")

    if len(sys.argv) != 3:
        print("Usage: python subtraction.py <int1> <int2>")
        return

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("Error: Both inputs must be integers.")
        return

    result = subtract(num1, num2)
    print(f"The result of subtracting {num2} from {num1} is: {result}")

if __name__ == "__main__":
    main()
