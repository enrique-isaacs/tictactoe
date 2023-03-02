## This module hosts the entirety of the games logic, from checking win conditions
## processing user moves and handling cpu moves

def setup_board():
    """ Initializes a 2D array which represents the game board.
    
    Params: None
    Returns: None
    
    """
    
    return [[0 for _ in range(3)] for _ in range(3)]
    
    
def updated_board(board):
    """_Updates the board with new player moves_

    Args:
        board (list): A list of lists containing 0's or O's and X's
        
    Returns:
        List of lists containing Strings of X's or O's
    """
    ##TODO
    # - Add code that checks for player moves, adds those moves to board if move can be made
    
    
    return []


def can_move_be_made(move, current_board_state):
    """ Boolean function that checks if a player can make a move

    Args:
        move (String): String literal in the form of X or O
        current_board_state (List): Current board state
        
    Returns:
        Boolean True if player move can be made, else False
    """
    
    return 0


