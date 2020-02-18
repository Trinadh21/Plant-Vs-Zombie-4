import pygame
from adding_background import*
from config import*
from player import*
from enemy import*
from bg import*
import math
from menu import*
from menu2 import*


clock = pygame.time.Clock()
pygame.init()

pygame.display.set_caption("river crossing game")

run = True
score = 0
cs = 0
time = pygame.time.get_ticks()
var = 0
flag = 0
count = 0
pre = 0
music = pygame.mixer.music.load('ZombieMusic.mp3')
pygame.mixer.music.play(-1)
menuPage()
while run:

    clock.tick(mainFunctionFrameRate)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        print(event)
    press = pygame.key.get_pressed()
    if press[pygame.K_LEFT] and man.x - man.vel >= -(10 * winWidth) / 1200:
        man.x -= man.vel
        man.hb = (man.x + 17, man.y + 11, 29, 52)
        man.left = True
        man.right = False

    elif press[pygame.K_RIGHT] and man.x + man.vel <= (1150 * winWidth) / 1200:
        man.x += man.vel
        man.hb = (man.x + 17, man.y + 11, 29, 52)
        man.left = False
        man.right = True
    elif press[pygame.K_UP] and man.y - man.vel >= 0:
        man.y -= man.vel
        man.hb = (man.x + 17, man.y + 11, 29, 52)
        man.left = False
        man.right = False
    elif press[pygame.K_DOWN]:
        if man.y + man.vel + man.height <= (657 * winHeight) / 657:
            man.y += man.vel
            man.hb = (man.x + 17, man.y + 11, 29, 52)
            man.left = False
            man.right = False
    else:
        man.left = False
        man.right = False
        man.walkCount = 0
    if man.check == 1:
        for i in range(0, 10):
            print('first')
            print(59 * (10 - i))
            print('second')
            print(man.hb[1])
            if 59 * (9 - i + 1) >= man.hb[1] + 46:
                print(i)
                if score < (math.ceil(i / 2)) * 10 + ((i) // 2) * 5 + 5:
                    score = (math.ceil(i / 2)) * 10 + ((i) // 2) * 5 + 5

    else:
        for i in range(0, 10):
            if 59 * (i + 1) <= man.hb[1]:
                if score < math.ceil(i / 2) * 10 + (i // 2) * 5 + 5:
                    score = (math.ceil(i / 2) * 10) + (i // 2) * 5 + 5
    if man.check == 1:
        if man.y <= 30:
            for i in vil:
                i.level1 += 1
                i.vel = i.velInitial * (i.level1)
            man.check = -1
            man.x = 300
            man.y = -13
            man.hb = (man.x + 17, man.y + 11, 29, 52)
            ct = pygame.time.get_ticks()
            var = ct - time
            time = ct
            flag = 1
            print("score")
            print(10)
            print(score)
            if man.check == 1:
                score = score * (vil[0].level2 - 1)
                pl = 1
            else:
                pl = 2
                score = score * (vil[0].level1 - 1)
            print("score")
            print(10 + pl)
            print(score)

            draw(2, score - 2 * var // 1000 + count * 10, pre, 1)
            for i in coins:
                i.x = i.px
                i.y = i.py
                i.hb = (i.x, i.y, 50, 50)

    else:
        if man.y >= 590:
            for i in vil:
                i.level2 += 1
                i.vel = i.velInitial * (i.level2)

            man.check = 1
            man.x = 600
            man.y = 590
            man.hb = (man.x + 17, man.y + 11, 29, 52)
            ct = pygame.time.get_ticks()
            var = ct - time
            time = ct
            flag = 1
            print("score")
            print(10)
            print(score)
            if man.check == 1:
                score = score * (vil[0].level2 - 1)
                pl = 1
            else:
                pl = 2
                score = score * (vil[0].level1 - 1)
            print("score")
            print(10 + pl)
            print(score)
            draw(1, score - 2 * var // 1000 + count * 10, pre, 1)
            for i in coins:
                i.x = i.px
                i.y = i.py
                i.hb = (i.x, i.y, 50, 50)

    for i in vil:
        if ((man.hb[0] +
             man.hb[2] >= i.hb[0] and man.hb[0] +
             man.hb[2] <= i.hb[0] +
             i.hb[2]) or (man.hb[0] >= i.hb[0] and man.hb[0] <= i.hb[0] +
                          i.hb[2])):
            if ((man.hb[1] +
                 man.hb[3] >= i.hb[1] and man.hb[1] +
                 man.hb[3] <= i.hb[1] +
                 i.hb[3]) or (man.hb[1] >= i.hb[1] and man.hb[1] <= i.hb[1] +
                              i.hb[3])):
                if man.check == 1:
                    man.check = -1
                else:
                    man.check = 1

                if man.check == 1:
                    man.x = 600
                    man.y = 590
                    for i1 in vil:
                        i1.vel = i1.velInitial * (i1.level1)

                else:
                    man.x = 300
                    man.y = -13
                    for i1 in vil:
                        i1.vel = i1.velInitial * (i1.level2)
                man.hb = (man.x + 17, man.y + 11, 29, 52)
                for i1 in coins:
                    i1.x = i1.px
                    i1.y = i1.py
                    i1.hb = (i1.x, i1.y, 50, 50)
                ct = pygame.time.get_ticks()
                var = ct - time
                if man.check == 1:
                    score = score * (vil[0].level2)
                    pl = 1
                else:
                    pl = 2
                    score = score * (vil[0].level1)
                print("score")
                print(pl)
                print(score)

                draw(pl, score - (2 * var // 1000) + count * 10, pre, 0)
                ct = pygame.time.get_ticks()
                time = ct
                flag = 1

    for i in spike:
        if ((man.hb[0] + man.hb[2] >= i.hb[0] and man.hb[0] +
             man.hb[2] <= i.hb[0] +
             i.hb[2]) or (man.hb[0] >= i.hb[0] and man.hb[0] <= i.hb[0] +
                          i.hb[2])):
            if ((man.hb[1] +
                 man.hb[3] >= i.hb[1] and man.hb[1] +
                 man.hb[3] <= i.hb[1] +
                 i.hb[3]) or (man.hb[1] >= i.hb[1] and man.hb[1] <= i.hb[1] +
                              i.hb[3])):
                if man.check == 1:
                    man.check = -1
                else:
                    man.check = 1

                if man.check == 1:
                    man.x = 600
                    man.y = 590
                    for i1 in vil:
                        i1.vel = i1.velInitial * (i1.level1)
                else:
                    man.x = 300
                    man.y = -13
                    for i1 in vil:
                        i1.vel = i1.velInitial * (i1.level2)
                for i1 in coins:
                    i1.x = i1.px
                    i1.y = i1.py
                    i1.hb = (i1.x, i1.y, 50, 50)
                man.hb = (man.x + 17, man.y + 11, 29, 52)
                ct = pygame.time.get_ticks()
                var = ct - time

                if man.check == 1:
                    pl = 1
                    score = score * (vil[0].level2)
                else:
                    pl = 2
                    score = score * (vil[0].level1)
                print("score")
                print(pl)
                print(score)
                draw(pl, score - (2 * var // 1000) + count * 10, pre, 0)
                ct = pygame.time.get_ticks()
                time = ct
                flag = 1

    for i in coins:
        if ((man.hb[0] +
             man.hb[2] >= i.hb[0] and man.hb[0] + man.hb[2] <= i.hb[0] +
             i.hb[2]) or (man.hb[0] >= i.hb[0] and man.hb[0] <= i.hb[0] +
                          i.hb[2])):
            if ((man.hb[1] +
                 man.hb[3] >= i.hb[1] and man.hb[1] +
                 man.hb[3] <= i.hb[1] +
                 i.hb[3]) or (man.hb[1] >= i.hb[1] and man.hb[1] <= i.hb[1] +
                              i.hb[3])):
                i.x = -2367
                count += 1
                i.hb = (i.x, i.y, 50, 50)
    if man.check == 1:
        for i in vil:
            i.vel = i.velInitial * (i.level1)
    else:
        for i in vil:
            i.vel = i.velInitial * (i.level2)
    ct = pygame.time.get_ticks()
    if man.check == 1:
        # score=score*vil[0].level1
        p = 1

    else:
        # score=score*vil[0].level2
        p = 2
    if flag == 1:
        if p == 1:
            redrawTheWindow(score, var, count, p, pre, vil[0].level1)
        else:
            redrawTheWindow(score, var, count, p, pre, vil[0].level2)

    else:
        var = pygame.time.get_ticks() - time
        if p == 1:
            redrawTheWindow(
                score *
                vil[0].level1,
                var,
                count,
                p,
                pre,
                vil[0].level1)
        else:
            redrawTheWindow(
                score *
                vil[0].level2,
                var,
                count,
                p,
                pre,
                vil[0].level2)

    # print("pre")
    # print(p)
    # print(pre)

    if flag == 1:
        pre = score + ((count) * 10) - (2 * var // 1000)
        print(score)
        print(count * 10)
        print(var)
        print(time)
        print(pre)
        time = pygame.time.get_ticks()
        score = 0
        flag = 0
        count = 0
pygame.quit()
