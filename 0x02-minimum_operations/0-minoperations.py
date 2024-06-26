#!/usr/bin/python3
"""this is a function"""


def minOperations(n):
    """function to get min operations"""
    if n <= 1:
        return 0

    primefactorsofn = []
    for i in range(2, n + 1):
        while n % i == 0:
            n //= i
            primefactorsofn.append(i)
        if n == 1:
            break
    operations = sum(primefactorsofn)
    return operations
