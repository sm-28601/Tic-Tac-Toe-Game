import random
from helper import *
spots = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}

# Main game loop
def play_game():
    # Print welcome message once
    print_welcome_message()

    # Get player names
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")

    # Randomly decide who goes first
    current_player = player1 if random.choice([True, False]) else player2
    print(f"\n{current_player} will go first!\n")

    # Initialize the game state
    playing, complete = True, False
    turn = 0
    spots = {i: ' ' for i in range(1, 10)}  # Create a dictionary for the 3x3 grid

    while playing:
        clear_output()
        print_welcome_message()
        draw_board(spots)

        print(f"{current_player}'s turn ({check_turn(turn)}): Pick a spot (1-9) or press 'q' to quit")

        # Get input and check its validity
        choice = input()
        if choice == 'q':
            playing = False
            break
        elif choice.isdigit() and int(choice) in spots:
            if spots[int(choice)] not in {"X", "O"}:
                spots[int(choice)] = check_turn(turn)
                turn += 1

                # Check for a win after a move
                if check_for_win(spots):
                    playing, complete = False, True
                    clear_output()
                    print_welcome_message()
                    draw_board(spots)
                    print(f"Congratulations! {current_player} wins!")
                    break

                # Switch players
                current_player = player1 if current_player == player2 else player2
            else:
                print("Spot already taken. Try again.")
        else:
            print("Invalid input. Choose a number between 1 and 9.")

        # Check for a draw
        if turn >= 9:
            playing = False

    if not complete:
        clear_output()
        print_welcome_message()
        draw_board(spots)
        print("It's a draw!")

    print("Thanks for playing!")
play_game()


