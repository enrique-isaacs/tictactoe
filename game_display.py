import pygame
import os
import game_logic as gl
# import time

pygame.init()

HEIGHT, WIDTH = 600,600
FPS = 60
BG_COLORS = {
    "White" : (255,255,255),
    "Black" : (0,0,0),
    "WhiteSmoke" : (245,245,245),
    "Silver" : (192,192,192)
}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLORS["Black"])

pygame.display.set_caption("Tic-tac-toe")

BG_IMAGE = pygame.transform.scale(pygame.image.load("images/bg_pic.jpg"), (WIDTH-50, HEIGHT-50))
board_image = pygame.transform.scale(pygame.image.load("images/3x3-grid.png"), (300,300))
o_image = pygame.transform.scale(pygame.image.load("images/letter_o.png"), (50,50))
x_image = pygame.transform.scale(pygame.image.load("images/letter_x.png"), (50,50))


os.system("clear")

def add_move(board, character):
    ## updates screen with new move
    ## also updates the game's board
    
    cell_name = get_block_position()
    position = img_positions().get(cell_name)
    updated = board
    print("In add move:")
    for r in updated:
        print(r)

    if position is not None:
        add_image_to_screen(character, position)
        updated = gl.do_move(character, board, cell_name)
        if board != []:
            return updated
        return board
    
    return board
    

def img_positions():
    
    return {
        "A" : (175, 230),
        "B" : (275, 230),
        "C" : (375, 230),
        "D" : (175, 325),
        "E" : (275, 325),
        "F" : (375, 325),
        "G" : (175, 425), 
        "H" : (275, 425),
        "I" : (375, 425)
    }
    

def get_block_position():
    
    mouse_position = {
        "x": pygame.mouse.get_pos()[0],
        "y": pygame.mouse.get_pos()[1]
    }
    
    for cells, coordinates in block_ranges().items():
       
        if mouse_position.get("x") in coordinates["x"] and mouse_position.get("y") in coordinates["y"]:
            return cells
 
    
def add_image_to_screen(character, cell):
    
    image = ''
    
    if character == "X":
        image = x_image
    elif character == "O":
        image = o_image
    
    screen.blit(image, cell)
  
  
def block_ranges():
    
    return {
        "A" : {
            "x" : range(150, 246),
            "y" : range(200, 296)
        }
        ,
        "B" : {
            "x" : range(264, 340),
            "y" : range(200, 296)
        }
        ,
        "C" : {
            "x" : range(360, 446),
            "y" : range(200, 296)
        }
        ,
        "D" : {
            "x" : range(150, 246),
            "y" : range(317, 390)
        }
        ,
        "E" : {
            "x" : range(264, 340),
            "y" : range(317, 390)
        }
        ,
        "F" : {
            "x" : range(360, 446),
            "y" : range(317, 390)
        }
        ,
        "G" : {
            "x" : range(150, 246),
            "y" : range(413, 500)
        }
        ,
        "H" : {
            "x" : range(264, 340),
            "y" : range(413, 500)
        }
        ,
        "I" : {
            "x" : range(364, 440),
            "y" : range(413, 500)
        }
        
    }
    


def get_character(characters, character_counter):
    if character_counter%2==0:
            character = characters[0]
    elif character_counter%2!=0:
        character = characters[1]
    
    return character

def main():
    
    clock = pygame.time.Clock()
    board = gl.setup_board()
    for r in board:
        print(r)
    screen.blit(board_image, (150,200))
    character_counter = 0
    characters = ["X", "O"]
    
    character = ''

    while True:
        clock.tick(FPS)
        character = get_character(characters, character_counter)
        print(f"Char count: {character_counter}")
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                character_counter+=1
                board = add_move(board, character)
                print(f"Char count @after: {character_counter}")
                
                pygame.display.update()
                
        
                
        if gl.game_won(board):
            print(f"Player: {character} won!!")
            pygame.quit()
            quit()
        # Update the screen
        pygame.display.update()


        
if __name__ == '__main__':
    main()