import game_logic


board = game_logic.setup_board()

player_dict = {
    "X" : 1,
    "O" : 2
}

player_character = ''

count = 9

for r in board:
    print(r)

def gameLoop(count, player_character, board):
    while count > 0:
        
        
        
        player_character = "X"
        board = game_logic.do_move(player_character, board)
        if game_logic.game_won(board):
            return player_character
        
        
        for r in board:
            print(r)
        
        
        player_character = "O"
        board = game_logic.do_move(player_character, board)
        
        for r in board:
            print(r)
            
        count -=1
        if game_logic.game_won(board):
            return player_character
    
player_character = gameLoop(count, player_character, board)
print(f" {player_dict[player_character]} won the game!!")