#!/usr/bin/python3
"""this is a function"""


def validUTF8(data):
    """validate utf-8

    Args:
        data (list): _description_

    Returns:
        boolean: _description_
    """
    numberofbytes = 0
    for bytes in data:
        if numberofbytes == 0:
            if bytes >> 5 == 0b110:
                numberofbytes = 1
            elif bytes >> 4 == 0b1110:
                numberofbytes = 2
            elif bytes >> 3 == 0b11110:
                numberofbytes = 3
            elif bytes >> 7:
                return False
        else:
            if bytes >> 6 != 0b10:
                return False
            numberofbytes = numberofbytes - 1
    return numberofbytes == 0
