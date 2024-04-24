#!/usr/bin/python3
"""this is a function"""


def minOperations(n):
    """_summary_

    Args:
        n (_type_): _description_
    """
    operations = 0
    for i in range(2, n+1):
        while(n % i == 0):
            operations += i
            n = n // i
    return operations
