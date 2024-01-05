import random
import os

def print_board(board):
    os.system("clear" if os.name == "posix" else "cls")
    for row in board:
        print(" ".join(map(str, row)))
    print()

def place_random_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def slide(row):
    new_row = [0] * 4
    index = 0
    for value in row:
        if value != 0:
            new_row[index] = value
            index += 1
    return new_row

def merge(row):
    for i in range(3):
        if row[i] == row[i+1] and row[i] != 0:
            row[i] *= 2
            row[i+1] = 0
    return row

def move_left(board):
    new_board = []
    for row in board:
        new_row = slide(row)
        new_row = merge(new_row)
        new_row = slide(new_row)
        new_board.append(new_row)
    return new_board

def move_right(board):
    reversed_board = [row[::-1] for row in board]
    new_board = move_left(reversed_board)
    return [row[::-1] for row in new_board]

def move_up(board):
    transposed_board = [list(row) for row in zip(*board)]
    new_board = move_left(transposed_board)
    return [list(row) for row in zip(*new_board)]

def move_down(board):
    transposed_board = [list(row) for row in zip(*board)]
    new_board = move_right(transposed_board)
    return [list(row) for row in zip(*new_board)]

def is_game_over(board):
    for row in board:
        if 0 in row:
            return False
        for i in range(3):
            if row[i] == row[i+1]:
                return False
    for j in range(4):
        for i in range(3):
            if board[i][j] == board[i+1][j]:
                return False
    return True

def is_win(board):
    for row in board:
        if 2048 in row:
            return True
    return False

def main():
    board = [[0] * 4 for _ in range(4)]
    place_random_tile(board)
    place_random_tile(board)

    while True:
        print_board(board)

        if is_game_over(board):
            print("Game Over!")
            break

        if is_win(board):
            print("You win!")
            break

        move = input("Enter move (W/A/S/D): ").upper()

        if move == "W":
            board = move_up(board)
        elif move == "A":
            board = move_left(board)
        elif move == "S":
            board = move_down(board)
        elif move == "D":
            board = move_right(board)
        else:
            print("Invalid move! Use W/A/S/D.")

        place_random_tile(board)

if __name__ == "__main__":
    main()
