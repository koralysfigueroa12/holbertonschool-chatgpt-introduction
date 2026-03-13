#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function: Calculates the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): The non-negative integer for which the factorial is calculated.

    Returns:
    int: The factorial of the given number n. If n is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input number from command line arguments, convert to int
f = factorial(int(sys.argv[1]))
# Print the result
print(f)
