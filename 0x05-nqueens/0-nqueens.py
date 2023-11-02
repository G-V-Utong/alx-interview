#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at a given position on the board.

    Args:
    board (list): The current state of the chessboard.
    row (int): The row where the queen is to be placed.
    col (int): The column where the queen is to be placed.
    n (int): The size of the board.

    Returns:
    bool: True if it's safe to place the queen, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(n):
    """
    Solve the N-Queens problem and print all possible solutions.

    Args:
    n (int): The size of the chessboard and the number of queens to be placed.
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    def solve(board, col):
        if col == n:
            for row in range(n):
                print("".join(["Q" if board[row][i] == 1 else "." for i in range(n)]))
            print()
            return
        
        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(board, col + 1)
                board[row][col] = 0
    
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
