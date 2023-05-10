
#создаём библиатеки 
import pygame
from pygame.locals import*
import random
#создаём класс

class Ptiza:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 708))
        self.bird = Rect(65, 50, 50, 50)
        self.background = pygame.image.load('assets/fon flappy.jpg').convert()
        self.birdSprites = [pygame.image.load("assets/doggy.png").convert_alpha(),
                            pygame.image,load("assets/deed.png")]
        self

