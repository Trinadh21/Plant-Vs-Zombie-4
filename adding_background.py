import pygame
from config import*
from player import*
from enemy import*




def redrawTheWindow(currentScore,currentTime,c,pl,pre):
    window.fill(yellowBackground)
   
    for i in range (6):
        pygame.draw.rect(window,greenBackground,(0,2*i*(winHeight//11),winWidth,winHeight//11))
    for i in vil:
        i.hitbox=(i.x + 17, i.y + 19, 29, 60)   
        pygame.draw.rect(window, redBackground,i.hitbox,2)
        i.draw(window)
   
    for i in spike:
        i.hitbox=(i.x+20, i.y +70, 100, 58)   
        pygame.draw.rect(window, redBackground,i.hitbox,2)
        i.draw(window)
    for i in coins:
        pygame.draw.rect(window, redBackground,i.hitbox,2)
        i.draw(window)
    man.draw(window)
    pygame.draw.rect(window, redBackground,man.hitbox,2)
    font = pygame.font.SysFont("comicsans", fontSize1, True)
    font1 = pygame.font.SysFont("comicsans", fontSize2, True)
    text2 = font.render("Time: "+ str(currentTime//1000),1, (0,0,0))
    text1 = font.render("Layerscore: "+ str(currentScore),1, (0,0,0))
    text5 = font.render("coins: "+ str(c),1, (0,0,0))
    text6 = font.render("player: "+ str(pl),1, (0,0,0))
    text7 = font1.render("FINAL SCORE: "+ str(currentScore+c*10-2*(currentTime//1000)),1, (0,0,0))
    if pl==1:
        text8 = font.render("player2 score: "+ "NA",1, (0,0,0))
    else:
        text8 = font.render("player1 score: "+ str(pre),1, (0,0,0))
    window.blit(text8, (0, winHeight/66))
    window.blit(text1, ((10*winWidth)/12, winHeight/66))
    window.blit(text5, ((87*winWidth)/120, winHeight/66))
    window.blit(text2, ((75*winWidth)/120, winHeight/66))
    window.blit(text6, (winWidth/2, winHeight/66))
    window.blit(text7, ((2*winWidth)/3, (61*winHeight)/66))

    text3 = font1.render("Start",1, blackBackground)
    text4 = font1.render("End",1, blackBackground)
    if man.check==1:
        window.blit(text3,((45*winWidth)/12,(59*winHeight)/66))
        window.blit(text4,((45*winWidth)/12,(10*winHeight)/660))
    else:
        window.blit(text4,((45*winWidth)/12,(59*winHeight)/66))
        window.blit(text3,((45*winWidth)/12,(10*winHeight)/660))
        
        
        

    
    pygame.display.update()
    
    
    
