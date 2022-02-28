from cgitb import grey
import pygame, random
from car import Car
pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

speed = 1 
colorList = (RED, GREEN, PURPLE, YELLOW,CYAN, BLUE)


SCRENWIDTH = 800
SCREENHEIGHT = 600
#might need to reorder??
size = (SCREENHEIGHT, SCRENWIDTH)
screen = pygame.display.set_caption("Race Game")

all_sprites = pygame.sprite.Group()


playerCar = Car(RED, 60, 80, 70)
playerCar.rect.x = 160
playerCar.rect.y = SCREENHEIGHT - 100

car1 = Car(PURPLE, 60, 80, random.randint(50,100))
car1.rect.x = 60
car1.rect.y = -100

car2 = Car(YELLOW, 60, 80, random.randint(50, 100))
car2.rect.x = 160
car2.rect.y = -600

car3 = Car(CYAN, 60, 80, random.randint(50, 100))
car3.rect.x = 260
car3.rect.y = -300

car4 = Car(BLUE, 60, 80, random.randint(50, 100))
car4.rect.x = 360
car4.rect.y = -900

#add to list of objects
all_sprites.add(playerCar)
all_sprites.add(car1)
all_sprites.add(car2)
all_sprites.add(car3)
all_sprites.add(car4)

all_coming_objects = pygame.sprite.Group()
all_coming_objects.add(car1)
all_coming_objects.add(car2)
all_coming_objects.add(car3)
all_coming_objects.add(car4)


carryon = True
clock = pygame.time.Clock()

while carryon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryon = False
        elif event.type == pygame.KEYDOWN:
            if event.type==pygame.K_x:
                playerCar.moveRight(10)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight
    if keys[pygame.K_UP]:
        speed += .05
    if keys[pygame.K_DOWN]:
        speed -= .05

    for car in all_coming_objects:
        Car.moveFoward(speed)
        if car.rect.y > SCREENHEIGHT:
            car.changeSPEED(random.randint(50, 100))
            car.repaint(random.choice(colorList))
            car.rect.y = -200

    car_collide = pygame.sprite.spritecollide(playerCar,all_coming_objects, False)
    for car in car_collide:
        print("Car Crash! You Lose!")
        #Game Over
        carryon = False

    all_sprites.update()


    screen.fill(GREEN)
    #Draw Road
    pygame.draw.rect(screen, GREY, [40,0, 400,SCREENHEIGHT])
    
    pygame.draw.line(screen, WHITE, [140,0],[140,SCREENHEIGHT],5)
    
    pygame.draw.line(screen, WHITE, [240,0],[240,SCREENHEIGHT],5)
    
    pygame.draw.line(screen, WHITE, [340,0],[340,SCREENHEIGHT],5)
 
 
    #draw all the sprites
    all_sprites.draw(screen)
 
    #Refresh Screen
    pygame.display.flip()
 
    
    clock.tick(60)
 
pygame.quit()
