#!/usr/bin/env python3
import sys

def parsearguments():
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    print(n)
    
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(row - i) == abs(board[i] - col):
            return False
    return True


def main():
    parsearguments()

if __name__ == '__main__':
    main()