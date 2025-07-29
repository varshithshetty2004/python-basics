def print_board(board):
    for row in board:
        print(''.join(row))
    print()  # Adds a blank line between solutions

def safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True

def solve(board, row, n):
    if row == n:
        print_board(board)
        return
    for col in range(n):
        if safe(board, row, col, n):
            board[row][col] = "Q"
            solve(board, row + 1, n)
            board[row][col] = "."  # backtrack

# Driver code
n = int(input("Enter the number of queens (n): "))
board = [["." for _ in range(n)] for _ in range(n)]
solve(board, 0, n)
