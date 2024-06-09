#!/usr/bin/python3
"""this is a function"""


def makeChange(coins, total):
    """make changes"""
    # implentation using dynamic programming
    # if total <= 0:
    #     return 0
    # listformin = [float('inf')] * (total + 1)
    # listformin[0] = 0
    # for i in range(1, total + 1):
    #     for coi in coins:
    #         if coi <= i:
    #             if listformin[i - coi] != float('inf'):
    #              listformin[i] = min(listformin[i], 1 + listformin[i - coi])
    # return -1 if listformin[total] == float('inf') else listformin[total]
    # solution using greedy method
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        count = total // coin
        total -= (count * coin)
        coin_count = coin_count + count
    if total > 0:
        return -1
    return coin_count
