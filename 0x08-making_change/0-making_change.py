#!/usr/bin/python3
"""this is a function"""


def makeChange(coins, total):
    """make changes"""
    if total < 1:
        return 0
    listformin = [float('inf')] * (total + 1)
    listformin[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                listformin[i] = min(listformin[i], 1 + listformin[i - coin])
    return -1 if listformin[total] == float('inf') else listformin[total]
