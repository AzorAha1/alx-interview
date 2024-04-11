#!/usr/bin/python3
"""
0-main
"""


def pascal_triangle(n):
    """pascal_triangle"""
    if n <= 0:
        return []
    else:
        # the first item in the list added
        thelist = [[1]]
        # range of n - 1 because first item already added in the list
        for i in range(n - 1):
            # zeroesatthetartandendofthelist to with the cal of the inner items
            templist = [0] + thelist[-1] + [0]
            row = []
            # therangeisthelengthofthelastitem+1becausethelengthofthelistincrementsbyone
            for j in range(len(thelist[-1]) + 1):
                row.append(templist[j] + templist[j + 1])
            thelist.append(row)
        return thelist
