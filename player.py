import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    direction = 0
    nullDirection = 0
    speed = 2

    def __init__(self, col, size):
        super().__init__()
        self.col = col
        self.size = size

        self.image = pygame.image.load("blueBall.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()

    def keyDown(self, keys):  # function for changing direction when an arrow key is pressed
        if keys[K_LEFT] and self.nullDirection != 1:  # checks which keys are held down
            self.direction = 1
            self.rect.x -= self.speed
        elif keys[K_UP] and self.nullDirection != 2:
            self.direction = 2
            self.rect.y -= self.speed
        elif keys[K_RIGHT] and self.nullDirection != 3:
            self.direction = 3
            self.rect.x += self.speed
        elif keys[K_DOWN] and self.nullDirection != 4:
            self.direction = 4
            self.rect.y += self.speed