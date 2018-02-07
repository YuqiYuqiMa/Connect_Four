
### common_ui

import connectfour

turn_dictionary = {connectfour.RED: 'RED', connectfour.YELLOW: 'YELLOW'}

def ask_username() -> str:
    #Asks the user for username and returns the username if it is valid;
    #ask for re-try if the username is invalid
    while True:
        username = input('What is your name? ').strip()

        if len(username) > 0:
            return username
        else:
            print('Error, please try again ')


def ask_move() -> str:
    #Ask the player(s) for move: enter either [D]rop or [P]op.
    #If move is invalid, asks for re-try. If valid, returns the move
    while True:
        move = input('Please enter move:([D]rop or [P]op):').upper()
        if move == 'D' or 'P':
            return move
        else:
            print('Invalid command, please try again ')


def ask_col_number() -> int:
    #Asks for a column number
    while True:
        try:
            col = eval(input('Please enter column number: ').strip())
            return col
        except:
            print('Invalid move, please try again')
    


def create_board(original_board: '2D list') -> '2D list':
    #Returns a 2D list by appending either '.', 'Y', or 'R' to every item(col)
    #in row to denote an empty space in the board, YELLOW, or RED player's
    #discs, respectively
    Board = []
    for row in original_board:
        sub_list = []
        for col in row:
            if col == 0:
                sub_list.append(".")
            elif col == 1:
                sub_list.append('R')
            elif col == 2:
                sub_list.append('Y')
        Board.append(sub_list)
    return Board

def board_print(T: '2D list') -> None:
    #Prinrs the board (2D list) 
    s = ""
    for num in range(1, (len(T) + 1)):
        s += str(num) + "  "
    print(s)
       
    for row in range(len(T[0])):
        for col in range(len(T)):
            print("{:2s}".format(T[col][row]), sep = "      ", end = " ")
        print()

def show_player_turn(game_state: connectfour.ConnectFourGameState) -> None:
    #Prints out the color-coded for the player whose turn it is
    #by using the dictionary value
    print("Turn: Player {}".format(turn_dictionary[game_state.turn]))


def print_board_drop(game_state: connectfour.ConnectFourGameState, col: int) -> connectfour.ConnectFourGameState:
    #Returns the current state of the game (by printing out the board) after each
    #the player has made a move(drop)
    game_state = connectfour.drop_piece(game_state, col)
    board_print(create_board(game_state.board))
    return game_state
    
    
def print_board_pop(game_state: connectfour.ConnectFourGameState, col: int) -> connectfour.ConnectFourGameState:
    #Returns the current state of the game (by printing out the board) after each
    #the player has made a move(pop)
    game_state = connectfour.pop_piece(game_state, col)
    board_print(create_board(game_state.board))
    return game_state
        
def valid_move(game_state: connectfour.ConnectFourGameState) -> int:
    #Returns the column number if the entered col_num is correct (according
    #to the game protocol); Raises an exception and asks for a reentry
    #if the number is invalid
    try:
        col_num = ask_col_number() - 1
        return col_num

    except:
        print('Invalid move, please try again:  ')                           
        

def check_error_drop(game_state: connectfour.ConnectFourGameState, col: int) -> connectfour.ConnectFourGameState:
    #Returns the current state of the game (by printing out the board) after
    #the player has made a valid move(drop); Raises an exception, prompting the
    #user for a reentry if the move in invalid. Catches invalid column number
    #and any other bugs that may make the program crash 
    try:
        game_state = print_board_drop(game_state, col)
    except ValueError:
        print("Invalid number, please try again: ")                            
    except:
        print('ERROR')
    return game_state


def check_error_pop(game_state: connectfour.ConnectFourGameState, col: int) -> connectfour.ConnectFourGameState:
    #Returns the current state of the game (by printing out the board) after
    #the player has made a valid move(pop); Raises an exception, prompting the
    #user for a reentry if the move in invalid. Catches invalid column number
    #and any other bugs that may make the program crash 
    try:
        game_state = print_board_pop(game_state, col)
    except ValueError:
        print('Invalid number, please try again: ')
    except:
        print('ERROR')
    return game_state

def print_winner(game_state: connectfour.ConnectFourGameState) -> None:
    #Prints out the name(either RED or YELLOW) of the winner
    winner = connectfour.winning_player(game_state)
    print("Game Over! Winner is player {} !".format(turn_dictionary[winner]))
