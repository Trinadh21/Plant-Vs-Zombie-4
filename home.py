import pygame
from adding_background import* 
from config import*
from player import*
from enemy import*
from bg import*
import math
from menu import*
from menu2 import*


clock=pygame.time.Clock()
pygame.init()

pygame.display.set_caption("river crossing game")

run = True
score=0
cs=0
time = pygame.time.get_ticks()
var=0
flag=0
count=0
pre=0
menuPage()
while run:
    
    clock.tick(27)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT :
            run = False
    press=pygame.key.get_pressed()
    if press[pygame.K_LEFT] and man.x-man.vel>=-10:
        man.x -= man.vel
        man.hitbox = (man.x + 17, man.y + 11, 29, 52)  
       
    elif press[pygame.K_RIGHT] and man.x+man.vel<=1150:
        man.x += man.vel
        man.hitbox = (man.x + 17, man.y + 11, 29, 52) 
    elif press[pygame.K_UP] and man.y-man.vel>=0:
        man.y-=man.vel
        man.hitbox = (man.x + 17, man.y + 11, 29, 52) 
    elif press[pygame.K_DOWN] and man.y+man.vel+man.height<=657:
        man.y+=man.vel
        man.hitbox = (man.x + 17, man.y + 11, 29, 52)
    if man.check==1:
        for i in range(10,-1,-1):
            if 59*(i+1) >= man.y+65:
                if score<((9-i)/2)*10+((9-i)//2)*5+5:
                    score=((9-i)/2)*10+((9-i)//2)*5+5
               
    else:
        for i in range(0,10):
            if 59*(i+1) <= man.y+11:
                if score<(i/2)*10+(i//2)*5+5:
                    score=((i/2)*10)+(i//2)*5+5
    if man.check==1:
        if man.y<=30:
            for i in vil:
                i.level1+=1
                i.vel=3*(i.level1)
            man.check=-1
            man.x=300
            man.y=-13
            man.hitbox = (man.x + 17, man.y + 11, 29, 52)
            ct=pygame.time.get_ticks()
            var=ct-time
            time=ct
            flag=1
            print("score")
            print(10)
            print(score)
            if man.check==1:
                score=score*(vil[0].level2-1)
                pl=1
            else:
                pl=2
                score=score*(vil[0].level1-1)
            print("score")
            print(10+pl)
            print(score)
            
            draw(2,score-2*var//1000+count*10,pre,1)
            for i in coins:
                i.x=i.px 
                i.y=i.py 
                i.hitbox=(i.x,i.y,50,50)
                  
    else:
        if man.y>=590:
            for i in vil:
                i.level2+=1
                i.vel=3*(i.level2)

            man.check=1
            man.x=600
            man.y=590
            man.hitbox = (man.x + 17, man.y + 11, 29, 52)
            ct=pygame.time.get_ticks()
            var=ct-time
            time=ct
            flag=1
            print("score")
            print(10)
            print(score) 
            if man.check==1:
                score=score*(vil[0].level2-1)
                pl=1
            else:
                pl=2
                score=score*(vil[0].level1-1)
            print("score")
            print(10+pl)
            print(score)
            draw(1,score-2*var//1000+count*10,pre,1)
            for i in coins:
                i.x=i.px 
                i.y=i.py
                i.hitbox=(i.x,i.y,50,50)
                

    for i in vil:
        if ((man.hitbox[0]+man.hitbox[2] >= i.hitbox[0] and man.hitbox[0]+man.hitbox[2] <= i.hitbox[0]+i.hitbox[2]) or (man.hitbox[0]>=i.hitbox[0] and man.hitbox[0]<=i.hitbox[0]+i.hitbox[2])):
            if ((man.hitbox[1]+man.hitbox[3]>=i.hitbox[1] and man.hitbox[1]+man.hitbox[3]<=i.hitbox[1]+i.hitbox[3]) or (man.hitbox[1]>= i.hitbox[1] and man.hitbox[1]<=i.hitbox[1]+i.hitbox[3])):
                if man.check==1:
                    man.check=-1
                else:
                    man.check=1
                
                if man.check == 1:
                    man.x=600
                    man.y=590
                    for i in vil:
                        i.vel=3*(i.level1)
                    
                else:
                    man.x=300
                    man.y=-13
                    for i1 in vil:
                        i1.vel=3*(i1.level2)
                man.hitbox = (man.x + 17, man.y + 11, 29, 52)
                for i1 in coins:
                    i1.x=i1.px 
                    i1.y=i1.py
                    i1.hitbox=(i1.x,i1.y,50,50)
                ct=pygame.time.get_ticks()
                var=ct-time
                if man.check==1:
                    score=score*(vil[0].level2)
                    pl=1
                else:
                    pl=2
                    score=score*(vil[0].level1)
                print("score")
                print(pl)
                print(score)
                    
                draw(pl,score-(2*var//1000)+count*10,pre,0)
                ct=pygame.time.get_ticks()
                time=ct
                flag=1
                
    for i in spike:
        if ((man.hitbox[0]+man.hitbox[2] >= i.hitbox[0] and man.hitbox[0]+man.hitbox[2] <= i.hitbox[0]+i.hitbox[2]) or (man.hitbox[0]>=i.hitbox[0] and man.hitbox[0]<=i.hitbox[0]+i.hitbox[2]))and (i.wc)%2==0:
            if ((man.hitbox[1]+man.hitbox[3]>=i.hitbox[1] and man.hitbox[1]+man.hitbox[3]<=i.hitbox[1]+i.hitbox[3]) or (man.hitbox[1]>= i.hitbox[1] and man.hitbox[1]<=i.hitbox[1]+i.hitbox[3])):
                if man.check==1:
                    man.check=-1
                else:
                    man.check=1
             
                if man.check==1:
                    man.x=600
                    man.y=590
                    for i1 in vil:
                        i1.vel=3*(i1.level1)
                else:
                    man.x=300
                    man.y=-13
                    for i1 in vil:
                        i1.vel=3*(i1.level2)
                for i1 in coins:
                    i1.x=i1.px 
                    i1.y=i1.py
                    i1.hitbox=(i1.x,i1.y,50,50)
                man.hitbox = (man.x + 17, man.y + 11, 29, 52)
                ct=pygame.time.get_ticks()
                var=ct-time
                
                if man.check==1:
                    pl=1
                    score=score*(vil[0].level2)
                else:
                    pl=2
                    score=score*(vil[0].level1)
                print("score")
                print(pl)
                print(score)
                draw(pl,score-(2*var//1000)+count*10,pre,0)
                ct=pygame.time.get_ticks()
                time=ct
                flag=1
    
    for i in coins:
        if ((man.hitbox[0]+man.hitbox[2] >= i.hitbox[0] and man.hitbox[0]+man.hitbox[2] <= i.hitbox[0]+i.hitbox[2]) or (man.hitbox[0]>=i.hitbox[0] and man.hitbox[0]<=i.hitbox[0]+i.hitbox[2]))and (i.wc)%2==0:
            if ((man.hitbox[1]+man.hitbox[3]>=i.hitbox[1] and man.hitbox[1]+man.hitbox[3]<=i.hitbox[1]+i.hitbox[3]) or (man.hitbox[1]>= i.hitbox[1] and man.hitbox[1]<=i.hitbox[1]+i.hitbox[3])):
                i.x=-2367
                count += 1 
                i.hitbox=(i.x,i.y,50,50)
    if man.check==1:
        for i in vil:
            i.vel=3*(i.level1)
    else:
        for i in vil:
            i.vel=3*(i.level2)
    ct=pygame.time.get_ticks()
    if man.check==1:
        #score=score*vil[0].level1
        p=1
        
    else:
        #score=score*vil[0].level2
        p=2
    if flag==1:
        redrawTheWindow(score,var,count,p,pre)
    else:
        var=pygame.time.get_ticks()-time
        if p==1:
            redrawTheWindow(score*vil[0].level1,var,count,p,pre)
        else:
            redrawTheWindow(score*vil[0].level2,var,count,p,pre)
            
    # print("pre")
    # print(p)
    # print(pre)
        
    if flag==1:
        pre=score+((count)*10)-(2*var//1000)
        print(score)
        print(count*10)
        print(var)
        print(time)
        print(pre)
        time=pygame.time.get_ticks()
        score=0
        flag=0
        count=0
pygame.quit()




