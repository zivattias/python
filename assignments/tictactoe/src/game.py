from game_logic import check_win
from game_board import *
from game_turns import *
from os import system
from random import randint


def print_greeting() -> None:
    greeting_msg = """
 _______       ___      .__   __.  __   _______  __              ___      .__   __.  _______      ________   __  ____    ____  __     _______.
|       \\     /   \\     |  \\ |  | |  | |   ____||  |            /   \\     |  \\ |  | |       \\    |       /  |  | \\   \\  /   / (_ )   /       |
|  .--.  |   /  ^  \\    |   \\|  | |  | |  |__   |  |           /  ^  \\    |   \\|  | |  .--.  |   `---/  /   |  |  \\   \\/   /   |/   |   (----`
|  |  |  |  /  /_\\  \\   |  . `  | |  | |   __|  |  |          /  /_\\  \\   |  . `  | |  |  |  |      /  /    |  |   \\      /          \\   \\    
|  '--'  | /  _____  \\  |  |\\   | |  | |  |____ |  `----.    /  _____  \\  |  |\\   | |  '--'  |     /  /----.|  |    \\    /       .----)   |   
|_______/ /__/     \\__\\ |__| \\__| |__| |_______||_______|   /__/     \\__\\ |__| \\__| |_______/     /________||__|     \\__/        |_______/    
                     .___________. __    ______ .___________.    ___       ______ .___________.  ______    _______                            
                     |           ||  |  /      ||           |   /   \\     /      ||           | /  __  \\  |   ____|                           
                     `---|  |----`|  | |  ,----'`---|  |----`  /  ^  \\   |  ,----'`---|  |----`|  |  |  | |  |__                              
                         |  |     |  | |  |         |  |      /  /_\\  \\  |  |         |  |     |  |  |  | |   __|                             
                         |  |     |  | |  `----.    |  |     /  _____  \\ |  `----.    |  |     |  `--'  | |  |____                            
                         |__|     |__|  \\______|    |__|    /__/     \\__\\ \\______|    |__|      \\______/  |_______|                           
                                          .___  ___.      ___      .__   __.  __       ___                                                    
                                          |   \\/   |     /   \\     |  \\ |  | |  |     /   \\                                                   
                                          |  \\  /  |    /  ^  \\    |   \\|  | |  |    /  ^  \\                                                  
                                          |  |\\/|  |   /  /_\\  \\   |  . `  | |  |   /  /_\\  \\                                                 
                                          |  |  |  |  /  _____  \\  |  |\\   | |  |  /  _____  \\                                                
                                          |__|  |__| /__/     \\__\\ |__| \\__| |__| /__/     \\__\\"""

    print(greeting_msg)
    print()
    return


def random_start_player():
    rand_num = randint(1, 2)
    player = Turn.player1.value if rand_num == 1 else Turn.player2.value
    return player


def random_start_shape():
    rand_num = randint(1, 2)
    shape = Shape.x.value if rand_num == 1 else Shape.o.value
    return shape


def start_game() -> bool:
    game_over: bool = False
    num_turns: int = 0

    size = get_board_size()
    board = initialize_board(size)
    system("clear")
    display_current_board(board)
    turn = random_start_player()
    shape = random_start_shape()

    while not game_over:
        display_turn_prompt(turn)
        row, col = get_user_turn(size)
        update_board_with_turn(board, row, col, shape)
        system("clear")
        display_current_board(board)

        # TODO: Doesn't work when player actually wins, but performs the check after 1 turn
        if num_turns >= 2 * size - 1:
            if check_win(board, size):
                game_over = True

        turn = toggle_turn(turn)
        shape = toggle_shape(shape)
        num_turns += 1

    return False