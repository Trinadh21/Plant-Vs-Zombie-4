import pygame
from config import*
from player import*
from enemy import*


manImage=pygame.image.load('standing.png')

def redrawTheWindow(currentScore,currentTime,c,pl,pre):
    window.fill((255,255,0))
   
    for i in range (6):
        pygame.draw.rect(window,(0,255,0),(0,2*i*(657//11),1200,657//11))
    window.blit(manImage,(man.x,man.y))
    for i in vil:
        i.hitbox=(i.x + 17, i.y + 14, 29, 60)   
        pygame.draw.rect(window, (255,0,0),i.hitbox,2)
        i.draw(window)
   
    for i in spike:
        i.hitbox=(i.x+20, i.y +70, 100, 58)   
        pygame.draw.rect(window, (255,0,0),i.hitbox,2)
        i.draw(window)
    for i in coins:
        pygame.draw.rect(window, (255,0,0),i.hitbox,2)
        i.draw(window)
    pygame.draw.rect(window, (255,0,0),man.hitbox,2)
    font = pygame.font.SysFont("comicsans", 30, True)
    font1 = pygame.font.SysFont("comicsans", 50, True)
    text2 = font.render("Time: "+ str(currentTime//1000),1, (0,0,0))
    text1 = font.render("Layerscore: "+ str(currentScore),1, (0,0,0))
    text5 = font.render("coins: "+ str(c),1, (0,0,0))
    text6 = font.render("player: "+ str(pl),1, (0,0,0))
    text7 = font1.render("FINAL SCORE: "+ str(currentScore+c*10-2*(currentTime//1000)),1, (0,0,0))
    if pl==1:
        text8 = font.render("player2 score: "+ "NA",1, (0,0,0))
    else:
        text8 = font.render("player1 score: "+ str(pre),1, (0,0,0))
    window.blit(text8, (0, 10))
    window.blit(text1, (1000, 10))
    window.blit(text5, (870, 10))
    window.blit(text2, (750, 10))
    window.blit(text6, (600, 10))
    window.blit(text7, (800, 610))

    text3 = font1.render("Start",1, (0,0,0))
    text4 = font1.render("End",1, (0,0,0))
    if man.check==1:
        window.blit(text3,(450,590))
        window.blit(text4,(450,10))
    else:
        window.blit(text4,(450,590))
        window.blit(text3,(450,10))
        
        
        

    
    pygame.display.update()
    
    
    
