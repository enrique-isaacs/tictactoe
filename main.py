import game_logic


count = 5

board = game_logic.setup_board()

while count > 0:
    
    player_character = "X"
    board = game_logic.do_move(player_character, board)
    
    for r in board:
        print(r)
    
    
    player_character = "O"
    board = game_logic.do_move(player_character, board)
    
    for r in board:
        print(r)
    
    count-=1