def pascal_triangle(n):
    if n <= 0:
        return []
    else:
        # the first item in the list added
        thelist = [[1]]
        # range of n - 1 because first item already added in the list
        for i in range(n - 1):
            #adding zeroes at the start and end of the list to help with the calculation of the inner items
            templist = [0] + thelist[-1] + [0]
            row = []
            # the range is the length of the last item + 1 because the length of the list increments by one
            for j in range(len(thelist[-1]) + 1):
                row.append(templist[j] + templist[j + 1])
            thelist.append(row)
        return thelist