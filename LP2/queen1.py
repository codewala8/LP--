def is_safe(board, row, col, n):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_n_queens(board, col, n):
    if col == n:
        print("Solution:", board)
        return True
    for row in range(n):
        if is_safe(board, row, col, n):
            board[col] = row
            if solve_n_queens(board, col + 1, n):
                return True
    return False

n = 4
board = [-1] * n
solve_n_queens(board, 0, n)
