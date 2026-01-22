#!/usr/bin/env python3

"""
SciFi calculator - Addition Module
----------------------------------
This script takes two integers as inputs and returns their sum.
Developed as part of a DevOps collaboration demo betwen two users
"""

# Global variable (used only for demonstration)
welcome_message = "Welcome to SciFi Calculator - Addition Module"

def add_numbers(a, b):
    # Local variable
    result = a + b
    return result

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Main logic
if __name__ == "__main__":
    import sys

    print(welcome_message)

    if len(sys.argv) != 3:
        print("Usage: python addition.py <int1> <int2>")
        sys.exit(1)

    arg1, arg2 = sys.argv[1], sys.argv[2]

    if not (is_integer(arg1) and is_integer(arg2)):
        print("Error: Both inputs must be integers.")
        sys.exit(1)

    num1 = int(arg1)
    num2 = int(arg2)

    total = add_numbers(num1, num2)
    print(f"Result: {num1} + {num2} = {total}")

