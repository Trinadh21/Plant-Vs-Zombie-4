import pygame
from config import*
from adding_background import*
from player import*

class Enemy():
    walk=[pygame.image.load('w1.png'),pygame.image.load('w2.png'),pygame.image.load('w3.png'),pygame.image.load('w4.png')]
    
    def __init__(self,x,y,width,height,end,start):
        self.x=x
        
        self.y=y
        self.level1=1
        self.level2=1
        self.width=width
        self.height=height
        self.end=end
        self.vel1=3
        self.vel2=3
        self.vel=3
        self.start=start
        self.wc=0
        self.hitbox = (self.x + 17, self.y + 14, 29, 60)   

   
    def draw(self, window):
        self.move()
        if self.wc+ 1 >= 36:
            self.wc = 0
        window.blit(self.walk[self.wc//9], (self.x,self.y))
        self.wc += 1
                    
    def move(self):
        if self.vel > 0:
            if self.x < self.end+ self.vel:
                self.x += self.vel
            else:
                self.x = self.start
                self.wc = 0