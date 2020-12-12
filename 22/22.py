from timeit import default_timer as timer
import numpy as np


def next_board(board):
    new_board = np.copy(board)
    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            if board[row][col] == "L" and count_adjacent_seats(board, row, col) == 0:
                new_board[row][col] = "#"
            elif board[row][col] == "#" and count_adjacent_seats(board, row, col) >= 5:
                new_board[row][col] = "L"
    return new_board


# some ugly magic
def count_adjacent_seats(board, row, col):
    count = 0
    full_row = board[row]
    full_col = board[:, col]
    # left
    if check_if_next_seat_is_taken(np.flip(full_row[:col])):
        count += 1
    # right
    if check_if_next_seat_is_taken(full_row[col+1:]):
        count += 1
    # top
    if check_if_next_seat_is_taken(np.flip(full_col[:row])):
        count += 1
    # bottom
    if check_if_next_seat_is_taken(full_col[row+1:]):
        count += 1
    # upper left
    if check_if_next_seat_is_taken(np.fliplr(np.flipud(board)[len(board)-row:]).diagonal(len(board[0]) - col)):
        count += 1
    # upper right
    if check_if_next_seat_is_taken(np.flipud(board)[len(board)-row:].diagonal(col + 1)):
        count += 1
    # lower left
    if check_if_next_seat_is_taken(np.fliplr(board[row+1:]).diagonal(len(board[0]) - col)):
        count += 1
    # lower right
    if check_if_next_seat_is_taken(board[row+1:].diagonal(col+1)):
        count += 1
    return count


def check_if_next_seat_is_taken(array):
    for x in array:
        if x == '#':
            return True
        elif x == 'L':
            return False
    return False


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
        if not (board[row] == prev_board[row]).all():
            return False
    return True


start = timer()
board = []
with open("input.txt") as file:
    for x in file:
        board.append(list(x.strip()))
board = np.array(board)
prev_board = np.array([])
while prev_board.size == 0 or (not check_if_same(board, prev_board)):
    prev_board = np.copy(board)
    board = next_board(board)
result = count_occupied_seats(board)
end = timer()
print("Result: ", result)
print("Time (in sec): ", end-start)
