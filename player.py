import pygame
from adding_background import*
from config import*
class Player():
    def __init__(self,x ,y ,width ,height ):
        self.x=x
        self.y=y
        self.level=1
        self.width=width
        self.height=height
        self.vel=5
        self.left=False
        self.right=False
        self.hitbox = (self.x + 17, self.y + 11, 29, 70)  
        self.check=1 

       
