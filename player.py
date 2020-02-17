import pygame
from config import*
from adding_background import*
from player import*
class Player():
    walk1=[
          pygame.transform.flip(pygame.image.load('r1.png'),1,0),
          pygame.transform.flip(pygame.image.load('r2.png'),1,0),
          pygame.transform.flip(pygame.image.load('r3.png'),1,0),
          pygame.transform.flip(pygame.image.load('r4.png'),1,0),
          pygame.transform.flip(pygame.image.load('r5.png'),1,0),
          pygame.transform.flip(pygame.image.load('r6.png'),1,0),
          pygame.transform.flip(pygame.image.load('r7.png'),1,0),
          pygame.transform.flip(pygame.image.load('r8.png'),1,0)]
    walk=[
          pygame.image.load('r1.png'),
          pygame.image.load('r2.png'),
          pygame.image.load('r3.png'),
          pygame.image.load('r4.png'),
          pygame.image.load('r5.png'),
          pygame.image.load('r6.png'),
          pygame.image.load('r7.png'),
          pygame.image.load('r8.png')]
    stand=[pygame.image.load('idle__001.png')
           ]
    def __init__(self,x ,y ,width ,height ):
        self.x=x
        self.y=y
        self.level=1
        self.width=width
        self.height=height
        self.vel=5
        self.left=False
        self.right=False
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)  
        self.check=1 
        self.walkCount=0
    def draw(self, window):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0
        if self.left:
            window.blit(self.walk1[self.walkCount//3], (self.x+20,self.y+10))
            self.walkCount += 1
        elif self.right:
            window.blit(self.walk[self.walkCount//3], (self.x+20,self.y+10))
            self.walkCount +=1
        else:
            window.blit(self.stand[0], (self.x+20,self.y+10))
            
        

       
