import pygame
import os
import game_logic as gl

pygame.init()

HEIGHT, WIDTH = 600,600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Tic-tac-toe")

board_image = pygame.transform.scale(pygame.image.load("images/grid3x3.png"), (300,300))

screen.blit(board_image, (150,200))
os.system("clear")

def add_move(click_position: tuple, board):
    
    ...

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