import pygame
from config import*
from adding_background import*

class Coin:
    w=[pygame.image.load('g1.png'),pygame.image.load('g2.png'),pygame.image.load('g3.png'),pygame.image.load('g4.png'),pygame.image.load('g5.png'),pygame.image.load('g6.png'),pygame.image.load('g7.png')]
    def __init__(self,x,y):
        self.x=x 
        self.y=y
        self.px=x
        self.py=y
        self.width=50
        self.height=50
        self.wc=0
        self.hitbox=(self.x,self.y,50,50)
        
    def draw(self, window):
        
        if self.wc+ 1 >= 21:
            self.wc = 0
        window.blit(self.w[self.wc//3], (self.x,self.y))
        self.wc += 1