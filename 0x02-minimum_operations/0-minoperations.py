#!/usr/bin/python3
"""this is a function"""


def minOperations(n):
    """_summary_

    Args:
        n (_type_): _description_
    """
    operations = 0
    if n <= 1:
        return 0
    primefactorsofn = []
    for i in range(2, n+1):
        while(n % i == 0):
            primefactorsofn.append(i)
            n = n // i
    for primefactor in primefactorsofn:
        if primefactor != 1:
            operations += primefactor
    return operations
