import pygame
from player import*
from enemy import*
from fixed import*
from coins import*



window = pygame.display.set_mode((1200,657))
win = pygame.display.set_mode((1200,657))
winWidth=1200
winHeight=657
man=Player(600,590,364,64)
spike=[fixed(500,285),fixed(1050,285),fixed(250,165),fixed(750,165),fixed(0,45),fixed(0,405),fixed(145,525)]
vil=[Enemy(0,515,77,64,1200,0),Enemy(400,515,77,64,1200,0),Enemy(0,45,77,64,1200,0),Enemy(400,45,77,64,1200,0),Enemy(220,160,77,64,1200,0),Enemy(660,160,77,64,1200,0),Enemy(0,280,77,64,1200,0),Enemy(950,280,77,64,1200,0),Enemy(500,400,77,64,1200,0)] 
coins=[Coin(100,130),Coin(400,130),Coin(800,130),Coin(1100,130),Coin(40,350),Coin(300,350),Coin(700,350),Coin(950,350),Coin(790,480),Coin(350,480),Coin(600,240)]


