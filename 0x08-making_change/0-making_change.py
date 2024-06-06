#!/usr/bin/python3
"""this is a function"""


def makeChange(coins, total):
    """make changes"""
    if total < 1:
        return 0;
    thelistformin = [float('inf')] * (total + 1);
    thelistformin[0] = 0;
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                thelistformin[i] = min(thelistformin[i], 1 + thelistformin[i - coin]);
    return -1 if thelistformin[total] == float('inf') else thelistformin[total]

