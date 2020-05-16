import random


# Function that can print out a board.
def display_board(board):
    print(f"     |     |\n"
          f"  {board[0]}  |  {board[1]}  |  {board[2]}\n"
          f"_____|_____|_____\n"
          f"     |     |\n"
          f"  {board[3]}  |  {board[4]}  |  {board[5]}\n"
          f"_____|_____|_____\n"
          f"     |     |\n"
          f"  {board[6]}  |  {board[7]}  |  {board[8]}\n"
          f"     |     |\n")


# Function that can take in a player name and assign their marker as 'X' or 'O'
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1: Do you want to be 'X' or 'O'?").upper()
    if marker == 'X':
        print(f"Then {player2_name} will get 'O'")
        return 'X', 'O'
    else:
        print(f"Then {player2_name} will get 'X'")
        return 'O', 'X'


# Function that takes following argument in and assigns them to the board.
#           1. the board list object
#           2. a marker ('X' or 'O') and
#           3. a desired position (number 1-9).
def place_marker(board, marker, pos):
    board[pos - 1] = marker


# Function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    return board[0] == board[1] == board[2] == mark or board[3] == board[4] == board[4] == mark or \
           board[6] == board[7] == board[8] == mark or board[0] == board[3] == board[6] == mark or \
           board[1] == board[4] == board[7] == mark or board[2] == board[5] == board[8] == mark or \
           board[0] == board[4] == board[8] == mark or board[2] == board[4] == board[6] == mark


# Function that uses the random module to randomly decide which player goes first.
# You may want to lookup random.randint() Return a string of which player went first.

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# Function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, pos):
    if board[pos - 1] == ' ':
        return True
    else:
        print("SORRY! THE PLACE IS ALREADY OCCUPIED")


# Function that checks if the board is full and returns a boolean value.
def full_board_check(board):
    for i in range(9):
        if board[i] == ' ':
            return False
    return True


# Function that asks for a player's next position and
# then uses the function from function space_check to check if it's a free position.
def player_choice(board):
    pos = 0
    while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, pos):
        pos = int(input("Enter the position from 1 to 9 : "))

    return pos


# Function that asks the player if they want to play again and returns a boolean True if yes.
def replay():
    return input('Do you want to play again? y or n?') == 'y'


print('WELCOME TO TIC TAC TOE')
while True:
    print("Here is the board on which you are going to play.")
    the_board = [' ']*9
    display_board(the_board)

    # Set the game up here
    player1_name = input("Enter player 1 name : ")
    player2_name = input("Enter player 2 name : ")
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(f"{turn} will go first")

    play_game = input("Ready to play? y or n? ")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker
            place_marker(the_board, player1_marker, position)
            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("PLAYER 1 HAS WON !")
                game_on = False
            else:
                # If tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker
            place_marker(the_board, player2_marker, position)
            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("PLAYER 2 HAS WON !")
                game_on = False
            else:
                # If tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = "Player 1"

    if not replay():
        break
