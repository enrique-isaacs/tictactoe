import pygame
import os
import game_logic as gl

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

board_image = pygame.transform.scale(pygame.image.load("images/grid3x3.png"), (300,300))
o_image = pygame.transform.scale(pygame.image.load("images/letter_o.png"), (50,50))
# x_image = pygame.transform.scale(pygame.image.load("images/letter_x.png"), (50,50))

# screen.blit(board_image, (150,200))
screen.blit(board_image, (150,200))
screen.blit(o_image, (160, 210))
# screen.blit(x_image, (270, 210))
os.system("clear")

def add_move(click_position: tuple, board):
    ## updates screen with new move
    ## also updates the game's board
    
    ...
    
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
            "x" : range(150, 246),
            "y" : range(413, 500)
        }
        
    }

def main():
    
    clock = pygame.time.Clock()
    board = gl.setup_board()

    while True:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                print("Mouse clicked at:", mouse_position)

        # Draw things on the screen
        # ...

        # Update the screen
        pygame.display.update()
        
        
if __name__ == '__main__':
    main()