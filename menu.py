import pygame
from config import*
from menu2 import*
clock = pygame.time.Clock()


def menuPage():
    intro = True
    while intro:
        # pressed=pygame.key.get_pressed()
        # print(pressed[pygame.K_LEFT])
        # if pressed[pygame.K_LEFT]:
        #     intro = False
        displayInstructions()
        clock.tick(27)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                intro = False
            press = pygame.key.get_pressed()
            print(press[pygame.K_LEFT])
            if press[pygame.K_LEFT]:
                intro = True
            elif press[pygame.K_RETURN]:
                intro = False
        # window.fill((255,0,0))
        # font = pygame.font.SysFont("comicsans", 60, True)
        # text1 = font.render("WELcomE To gaMe oF ZomBiEs",1, (255,255,255))
        # window.blit(text1, (200, 200))
        # pygame.display.update()
