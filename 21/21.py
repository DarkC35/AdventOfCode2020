from timeit import default_timer as timer


def next_board(board):
    new_board = [row[:] for row in board]
    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            if board[row][col] == "L" and count_adjacent_seats(board, row, col) == 0:
                new_board[row][col] = "#"
            elif board[row][col] == "#" and count_adjacent_seats(board, row, col) >= 4:
                new_board[row][col] = "L"
    return new_board


def count_adjacent_seats(board, row, col):
    count = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not (x == 0 and y == 0) and check_if_occupied(board, row+x, col+y):
                count += 1
    return count


def check_if_occupied(board, row, col):
    if row not in range(0, len(board)):
        return False
    elif col not in range(0, len(board[0])):
        return False
    else:
        return board[row][col] == "#"


def print_board(board):
    for row in board:
        for col in row:
            print(col, end='')
        print()
    print()


def count_occupied_seats(board):
    count = 0
    for row in board:
        for col in row:
            if col == "#":
                count += 1
    return count


def check_if_same(board, prev_board):
    for row in range(0, len(board)):
        if board[row] != prev_board[row]:
            return False
    return True


start = timer()
board = []
with open("input.txt") as file:
    for x in file:
        board.append(list(x.strip()))
prev_board = None
while not prev_board or not check_if_same(board, prev_board):
    prev_board = [row[:] for row in board]
    board = next_board(board)
result = count_occupied_seats(board)
end = timer()
print("Result: ", result)
print("Time (in sec): ", end-start)
