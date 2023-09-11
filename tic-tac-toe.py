#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    position = int(position)
    board[position] = mark
    return board

# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard():
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    user_input = False
    if position in range(1, 10):
        user_input = True
        if board[position] != ' ':
            user_input = False
    elif isinstance(position, str): 
        if position.isnumeric(): # check for numeric number in string
            if int(position) in range(1, 10):
                user_input = True
                if board[int(position)] != ' ':
                    user_input = False
    return user_input

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7], 
    [2, 5, 8],
    [3, 6, 9],
    [3, 5, 7],
    [1, 5, 9]
]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    return ((board[7] == player and board[8] == player and board[9] == player) or # across the botton
    (board[4] == player and board[5] == player and board[6] == player) or # across the middle
    (board[1] == player and board[2] == player and board[3] == player) or # across the top
    (board[7] == player and board[4] == player and board[1] == player) or # down the left
    (board[8] == player and board[5] == player and board[2] == player) or # down the middle
    (board[9] == player and board[6] == player and board[3] == player) or # down the right side
    (board[7] == player and board[5] == player and board[3] == player) or # diagonal
    (board[9] == player and board[5] == player and board[1] == player)) # diagonal    



# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    board_full = False
    board_empty = 0
    for k in board.keys():
        if board[k] == ' ':
            board_empty += 1
    if board_empty == 0:
        board_full = True
    return board_full

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
def replay():
    play_again = input('Do you want to play again? Enter Y or N: ').upper().startswith('Y')
    if play_again:
        board.update({
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '}
        )
    return play_again

#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User

while True:
    gameEnded = False
    currentTurnPlayer = 'X'
    # entry point of the whole program
    print('Game started: \n\n' +
        ' 1 | 2 | 3 \n' +
        ' --------- \n' +
        ' 4 | 5 | 6 \n' +
        ' --------- \n' +
        ' 7 | 8 | 9 \n')
    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")
        while not validateMove(move):
            move = input("Invalid move. Please choose number [1-9] only OR choose another number. Input: ")
        markBoard(move, currentTurnPlayer)
        if checkWin(currentTurnPlayer):
            printBoard()
            print("Congratulations! Player {} won the game!".format(currentTurnPlayer))
            gameEnded = True
        else:
            if checkFull():
                printBoard()
                print("The game is a draw!")
                break
            else:
                printBoard()
                if currentTurnPlayer == 'X':
                    currentTurnPlayer = 'O'
                else:
                    currentTurnPlayer = 'X'
    if not replay():
        print("Thank you for playing my game. Come again!")
        break