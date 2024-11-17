import os

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_board(spots):
    # Display a formatted 3x3 board
    board = (f" {spots[1]} | {spots[2]} | {spots[3]}\n"
             f"---|---|---\n"
             f" {spots[4]} | {spots[5]} | {spots[6]}\n"
             f"---|---|---\n"
             f" {spots[7]} | {spots[8]} | {spots[9]}\n")
    print(board)

def check_turn(turn):
    return 'X' if turn % 2 != 0 else 'O'

def check_for_win(spots):
    win_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]
    for combo in win_combinations:
        if spots[combo[0]] == spots[combo[1]] == spots[combo[2]] and spots[combo[0]] != ' ':
            return True
    return False

def print_welcome_message():
    print("Welcome to Tic Tac Toe!")
    print("\nInstructions:")
    print("1. The game is played on a 3x3 grid.")
    print("2. Players take turns placing X or O in an empty cell.")
    print("3. The first to align three in a row (horizontal, vertical, or diagonal) wins.")
    print("4. Enter a number (1-9) to place your marker as shown below:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    print("\nPlayer 1: X")
    print("Player 2: O")
    print("Get ready to play!\n")
