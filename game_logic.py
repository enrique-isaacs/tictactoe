## This module hosts the entirety of the games logic, from checking win conditions
## processing user moves and handling cpu moves

def setup_board():
    """ Initializes a 2D array which represents the game board.
    
    Params: None
    Returns: None
    
    """
    board = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    
    return board
    
    
def updated_board(move, board, player_character):
    """_Updates the board with new player moves_

    Args:
        board (list): A list of lists containing 0's or O's and X's
        
        move (String): A String equalling to 1 - 9
        
        player_character (String): A string representing the player eg X or O
        
    Returns:
        List of lists containing Strings of X's or O's
    """
    
    index_map = {
        "1": (0, 0),
        "2": (0, 1),
        "3": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "7": (2, 0),
        "8": (2, 1),
        "9": (2, 2),
    }


    if is_valid_move(move, board):
        
        index = index_map[move]
        board[index[0]][index[1]] = player_character

    return board



def is_valid_move(move, current_board_state):
    """ Checks if a player can make a move

    Args:
        move (str): String literal in the form 1 through 9
        current_board_state (list): Current board state
        
    Returns:
        bool: True if player move can be made, else False
    """

    board_dict = board_index_map(current_board_state)

    if move in board_dict.keys(): 
        if board_dict.get(move) != "X" or  board_dict.get(move) != "O":
            return True
    return False



# this function will be used when checking if a move is valid, for eg
## if player chooses square 1, validation will check what the value of the board is
## at map index 1

def board_index_map(original_board):
    """
    Given an n x n board represented as a 2D list of values,
    returns a dictionary that maps each possible move index
    (starting from 1) to the corresponding board value.

    Args:
        original_board: A 2D list of n lists, each containing n values,
            representing the original board.

    Returns:
        A dictionary that maps each move index (1 to n^2) to the
        corresponding value on the board.

    Example:
        >>> original_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> board_index_map(original_board)
        {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    """
    
    board_size = len(original_board)
    move_map = {}
    for i in range(board_size):
        for j in range(board_size):
            move_value = str(i * board_size + j + 1)
            move_map[move_value] = original_board[i][j]
            
    
    return move_map


def do_move(player_character, current_board)->list:
    
    move = input("-> ")
    board = updated_board(move, current_board, player_character)
    return board


def game_won(current_board)-> bool:
    
    
    
    for set_list in graph_variables(current_board):
        
        if len(set(set_list)) == 1:
            return True
        
    return False

def convert_board_to_graph(board):
    
    rows = {
        
            1 : board[0],
            2 : board[1],
            3 : board[2]
    }
    
    cols = {
        1: [board[0][0], board[1][0], board[2][0]],
        2: [board[0][1], board[1][1], board[2][1]],
        3: [board[0][2], board[1][2], board[2][2]]
    }
    
    diagonals = {
        1 : [board[0][0], board[1][1], board[2][2]],
        2: [board[2][0], board[1][1], board[0][2]]
    }
    
    board_graph = {
        "rows" : rows,
        "cols" : cols,
        "diagonals" : diagonals
    }
    
    return board_graph


def graph_variables(current_board):
    
    
    row_1 = convert_board_to_graph(current_board)["rows"][1]
    row_2 = convert_board_to_graph(current_board)["rows"][2]
    row_3 = convert_board_to_graph(current_board)["rows"][3]
    
    col_1 = convert_board_to_graph(current_board)["cols"][1]
    col_2 = convert_board_to_graph(current_board)["cols"][2]
    col_3 = convert_board_to_graph(current_board)["cols"][3]
    
    diagonal_top = convert_board_to_graph(current_board)["diagonals"][1]
    diagonal_bottom = convert_board_to_graph(current_board)["cols"][2]
    
    
    return [row_1,row_2, row_3, col_1, col_2, col_3, diagonal_top, diagonal_bottom]
    
