import pygame
White = (255,255,255)

class Car(pygame.sprite.Sprite):

    def __init__(self, color, width, height, speed):
        super().__init__()

        #color for car
        #background color
        self.image = pygame.Surface([width, height])
        self.image.fill(White)
        self.image.set_colorkey(White)

        #initialise car attributes
        self.width=width
        self.height=height
        self.color = color
        self.speed = speed

        #load car
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        #fetch car
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])