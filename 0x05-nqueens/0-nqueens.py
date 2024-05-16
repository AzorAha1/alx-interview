#!/usr/bin/python3
"""N QUEENS"""


import sys


def parsearguments():
    """parse argument"""
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
        return n
    except ValueError:
        print('N must be a number')
        sys.exit(1)


def is_safe(board, row, col):
    """is safe to check if its ok to insert queen"""
    for i in range(row):
        if board[i] == col:
            return False
        if abs(row - i) == abs(board[i] - col):
            return False
    return True


def solve_nqueen(n):
    def backtrackalgo(row, board, solutions):
        """backtracking algorithm"""
        if row == n:
            solutions.append(board[:])
        for col in range(n):
            if is_safe(board=board, row=row, col=col):
                board[row] = col
                backtrackalgo(board=board, row=row + 1, solutions=solutions)
                board[row] = -1
    solutions = []
    board = [-1] * n
    backtrackalgo(row=0, board=board, solutions=solutions)
    return solutions


def main():
    """main function"""
    n = parsearguments()
    solutions = solve_nqueen(n)
    for solution in solutions:
        tailoredsolution = [[r, c] for r, c in enumerate(solution)]
        print(tailoredsolution)


if __name__ == '__main__':
    main()
