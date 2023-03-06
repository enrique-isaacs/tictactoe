import pygame
import os

pygame.init()

HEIGHT, WIDTH = 600,600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Tic-tac-toe")

image = pygame.transform.scale(pygame.image.load("images/grid3x3.png"), (250,250))

screen.blit(image, (180,200))
os.system("clear")

while True:
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