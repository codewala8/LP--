def solve_nq_bb(col, n, board, rows, diag1, diag2):
    if col == n:
        print("Solution:", board)
        return True
    for row in range(n):
        if row not in rows and (col + row) not in diag1 and (col - row) not in diag2:
            board[col] = row
            rows.add(row)
            diag1.add(col + row)
            diag2.add(col - row)
            if solve_nq_bb(col + 1, n, board, rows, diag1, diag2):
                return True
            # Backtrack
            rows.remove(row)
            diag1.remove(col + row)
            diag2.remove(col - row)
    return False

n = 4
solve_nq_bb(0, n, [-1]*n, set(), set(), set())
