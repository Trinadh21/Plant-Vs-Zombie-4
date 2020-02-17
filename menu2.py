import pygame
from config import*
clock=pygame.time.Clock()
def displayInstructions():
    window.fill((255,0,0))
    font = pygame.font.SysFont("comicsans", 60, True)
    text1 = font.render("WELcomE To gaMe oF ZomBiEs",1, (255,255,255))
    window.blit(text1, (200, 200))
    text1 = font.render("PRess ENTer ----->",1, (255,255,255))
    window.blit(text1, (200, 500))
    pygame.display.update()
