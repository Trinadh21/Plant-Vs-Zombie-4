import pygame
from config import*
from adding_background import*

class fixed:
    w=[pygame.image.load('s1.png'),pygame.image.load('s2.png')]
    def __init__(self,x,y):
        self.x=x 
        self.y=y
        self.width=128
        self.height=128
        self.wc=0
        self.hitbox=(self.x,self.y,100,58)
        
    def draw(self, window):
        
        if self.wc+ 1 >= 36:
            self.wc = 0
        window.blit(self.w[self.wc//18], (self.x,self.y))
        self.wc += 1