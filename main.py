# -------Global variable--------

# board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
# if game is still going
game_still_going = True

# who win or lose
winner = None

# whose turn is it
current_player = "X"


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():
    # Display intial game
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    # the game has ended
    if winner == "X" or winner == "O":
        print(winner + "won")
    elif winner == None:
        print("tie")


def handle_turn(player):
    position = input("choose a position from 1 to 9: ")
    position = int(position) - 1

    board[position] = player

    display_board()


def check_if_game_over():
    check_if_tie()
    check_for_winner()


def check_for_winner():
    # set up globals var
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_colunmns()
    # check diagonals
    diagonal_winner = check_diagonals()

    # get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows(row_1=None, row_2=None, row_3=None):
    # set up globals var
    global game_still_going
    # check if rows are equal
    row_1 == board[0] == board[1] == board[2] != "-"
    row_2 == board[3] == board[4] == board[5] != "-"
    row_3 == board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_colunmns(columns_1=None, columns_2=None, columns_3=None):
    # set up globals var
    global game_still_going
    # check if columns are equal
    columns_1 == board[0] == board[3] == board[6] != "-"
    columns_2 == board[1] == board[4] == board[7] != "-"
    columns_3 == board[2] == board[5] == board[8] != "-"

    if columns_1 or columns_2 or columns_3:
        game_still_going = False
    # return the winner X or O
    elif columns_1:
        return board[0]
    elif columns_2:
        return board[1]
    elif columns_3:
        return board[2]
    return


def check_diagonals(diagonals_1=None, diagonals_2=None):
    # set up globals var
    global game_still_going
    # check if columns are equal
    diagonals_1 == board[0] == board[4] == board[8] != "-"
    diagonals_2 == board[6] == board[4] == board[2] != "-"

    if diagonals_1 or diagonals_2:
        game_still_going = False
    # return the winner X or O
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]

    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
     game_still_going = False
    return


# if current is x then the pc is o or oposite
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()
