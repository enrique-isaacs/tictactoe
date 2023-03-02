import unittest
import game_logic


class GameLogicTests(unittest.TestCase):
    
    def test_board_init(self):
        
        board = game_logic.setup_board()
        self.assertEqual(board, [[0,0,0],
                                 [0,0,0],
                                 [0,0,0]])
    
    
    def test_update_board(self):
        ## this test can only be implemented once players can make moves to update the board
        ...
        
        
    def test_move_be_made(self):
        
        board = [[0,'X',0],
                 [0,'X',0],
                 [0,0,0]]
        
        