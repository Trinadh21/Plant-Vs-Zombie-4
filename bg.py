import pygame
from config import*

def draw(pl,score,pre,update):
    window.fill((0,0,0))
    font = pygame.font.SysFont("comicsans", 60, True)
    if pl==2:
        text1 = font.render("WELL DONE,Player"+str(1),1, (255,255,255))
        text2= font.render("Your total score is: "+str(score),1, (255,255,255))
        window.blit(text1, (200, 200))  
        window.blit(text2, (300, 350))
        if update==1:
            text5 = font.render("You are eligible for level update",1, (255,255,255))
            window.blit(text5, (0,400))
            
    else:
        if pre>score:
            text1 = font.render("WELL tried,You lost(Player2)",1, (255,255,255))
            text2 = font.render("FINAL STATS",1, (255,255,255))
            text3 = font.render("Player1: "+str(pre),1, (255,255,255))
            text4 = font.render("Player2: "+str(score),1, (255,255,255))        
        elif pre==score:
            text1 = font.render("Congratulations,match drawn(Player2)",1, (255,255,255))
            text2 = font.render("FINAL STATS",1, (255,255,255))
            text3 = font.render("Player1: "+str(pre),1, (255,255,255))
            text4 = font.render("Player2: "+str(score),1, (255,255,255))
        else :
            text1 = font.render("Fantastic performance,You Won(player2)",1, (255,255,255))
            text2 = font.render("FINAL STATS",1, (255,255,255))
            text3 = font.render("Player1: "+str(pre),1, (255,255,255))
            text4 = font.render("Player2: "+str(score),1, (255,255,255))              
        window.blit(text1, (175, 200))  
        window.blit(text2, (175, 350))
        window.blit(text3, (200, 400))  
        window.blit(text4, (200, 450))
        if update==1:
            text5 = font.render("You are eligible for level update",1, (255,255,255))
            window.blit(text5, (0,500))
  
    pygame.display.update()
    pygame.time.wait(3500)
    
