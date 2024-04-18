#!/usr/bin/python3
def canUnlockAll(boxes):
    """function to search for keys to unlock boxes"""
    keysinboxes = {0}
    processedkeys = set()
    while True:
        newkey = False
        for setkey in keysinboxes - processedkeys:
            for key in boxes[setkey]:
                if key >= 0 and key < len(boxes):
                    newkey = True
                    keysinboxes.add(key)
            processedkeys.add(setkey)
        if not newkey:
            break
    return len(keysinboxes) == len(boxes)
