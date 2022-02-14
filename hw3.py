from cProfile import run
from curses import KEY_UP
import pygame

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

carimg = pygame.image.load("car.jpeg")
clock = pygame.time.Clock()

pygame.display.set_caption("Race Car")

def car(x, y):
    screen.blit(carimg, (x, y))

def game_loop():
    run = False
    x_change = 0
    x = 400
    y = 470

    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

        x += x_change


        car(x,y)
        


        screen.fill((123, 123, 123))
        screen.blit(carimg, (400, 470))
        clock.tick(100)
        pygame.display.update()

game_loop()
pygame.quit()
quit()