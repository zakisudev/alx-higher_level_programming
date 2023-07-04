#!/usr/bin/python3
""" N-queens """

import sys


def init_board(n):
    """ Initialize an n by n sized chessboard containing 0 """
    c_board = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(' ')
        c_board.append(row)
    return c_board


def board_copy(board):
    """ Return a deepcopy of a board """
    return [row.copy() for row in board]


def get_solved(c_board):
    """ Return the list of lists representation of a solved board """
    solved = []
    for row in range(len(c_board)):
        for col in range(len(c_board)):
            if c_board[row][col] == "Q":
                solved.append([row, col])
    return solved


def xout(c_board, row, col):
    """ X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed. """
    n = len(c_board)
    # X out all spots horizontally
    for c in range(n):
        if c != col:
            c_board[row][c] = "x"
    # X out all spots vertically
    for r in range(n):
        if r != row:
            c_board[r][col] = "x"
    # X out all spots diagonally
    for i in range(n):
        for j in range(n):
            if (i + j == row + col) or (i - j == row - col):
                if (i != row) and (j != col):
                    c_board[i][j] = "x"


def rec_solve(board, row, queens, solved):
    """ Recursively solve an N-queens puzzle """
    n = len(board)
    if queens == n:
        solved.append(get_solved(board))
        return solved

    for col in range(n):
        if board[row][col] == " ":
            tmp = board_copy(board)
            tmp[row][col] = "Q"
            xout(tmp, row, col)
            solved = rec_solve(tmp, row + 1, queens + 1, solved)

    return solved


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    c_board = init_board(int(sys.argv[1]))
    solved = rec_solve(c_board, 0, 0, [])
    for sol in solved:
        print(sol)

