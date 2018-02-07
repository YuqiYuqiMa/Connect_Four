
### connectfour_console

import connectfour
import common_ui


def play_game() -> None:
    #Global function that calls on all of the functions from two other modules.
    #Checks the validity of the move user typed. After the game is over,
    #breaks out of the loop by printing the winner's name (either RED or YELLOW) 
    game_state = connectfour.new_game_state()
    common_ui.board_print(common_ui.create_board(game_state.board))
    common_ui.show_player_turn(game_state)
    winner = connectfour.winning_player(game_state)
    
    if winner == 0:
        while True:
            if connectfour.winning_player(game_state) == 0:
                move = common_ui.ask_move()

                if move == 'D':
                    col_num = common_ui.valid_move(game_state)
                    game_state = common_ui.check_error_drop(game_state, col_num)
                       
                elif move == 'P':
                    col_num = common_ui.valid_move(game_state)
                    game_state = common_ui.check_error_pop(game_state, col_num)

                else:
                    print('Invalid move, please try again ')

            else:
                common_ui.print_winner(game_state)
                break
            common_ui.show_player_turn(game_state)
            

if __name__ == '__main__':
    play_game()
