
### connectfour_network

import connectfour
import common_ui
import I32CFSP

CONNECTFOUR_HOST = 'sgagomas-office.calit2.uci.edu'
CONNECTFOUR_PORT = 4444

def network_game(connection: I32CFSP.ConnectfourConnection, game_state: connectfour.ConnectFourGameState) -> None:
    '''
    Sends the input to the server that is listening to a specific port; receives
    and analyzes the output received from the server.
    '''
    while True:
        player_turn = 1
        if player_turn == 1:
            move = common_ui.ask_move()
            if move == 'D':
                col_num = common_ui.valid_move(game_state)  #checks if the user's name is valid and returns column number
                game_state = common_ui.check_error_drop(game_state, col_num)  # returns the new game state after user's move and prints out the new table
                if I32CFSP.user_move(connection, 'DROP ', col_num):   # sends the user's move to the server and returns True if the server sends 'OKAY'
                    game_state = I32CFSP.server_move(connection, game_state)   # creates a new game state after the server's move
                    r3 = I32CFSP.read_line(connection)   # receives response from server
                    if 'WINNER' in r3:   # if there is WINNER in respons, end the game and print winner's name
                        common_ui.print_winner(game_state)
                        I32CFSP.close(connection)
                        break
                        
                    elif r3 == 'READY':
                        player_turn = 1   # if the response is 'READY', continue the game
                    else:
                        player_turn = 0

            elif move == 'P':
                col_num = common_ui.valid_move(game_state)
                game_state = common_ui.check_error_pop(game_state, col_num)
                if I32CFSP.user_move(connection, 'POP ', col_num):
                    game_state = I32CFSP.server_move(connection, game_state)
                    r3 = I32CFSP.read_line(connection)
                    if 'WINNER' in r3:
                        common_ui.print_winner(game_state)
                        I32CFSP.close(connection)
                        break
                    elif r3 == 'READY':
                        player_turn = 1
                    else:
                        player_turn = 0

            else:
                print('Invalid move, please try again ')


def user_interface() -> None:
    #Global function that establishes the connection by asking the user to enter a host
    #and a port to which they want to connect. Begins the ConnectFour game, when the server
    #has responded.
    host = I32CFSP.ask_host()#Asks for the host to which to connect to
    port = I32CFSP.ask_port()#Asks for the port to which to connect to
    connection = I32CFSP.connect(host, port)
    username = common_ui.ask_username()#Asks for the username
    I32CFSP.greeting(connection, username)
    
    game_state = connectfour.new_game_state()#Reeturns the game state after each turn
    common_ui.board_print(common_ui.create_board(game_state.board))#Prints the booard after each turn
    common_ui.show_player_turn(game_state) #Shows whose current turn it is

    network_game(connection, game_state)

if __name__ == '__main__':
    user_interface()
