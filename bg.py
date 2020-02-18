import pygame
from config import*


def draw(pl, score, pre, update):
    if update == 1:
        score += (10 * (score)) // 65
    window.fill(blackBackground)
    font = pygame.font.SysFont(fontType, fontSize2, True)
    if pl == 2:
        text1 = font.render(appreciationPlayer1, 1, whiteBackground)
        text2 = font.render(scorePlayer1 + str(score), 1, whiteBackground)
        window.blit(text1, (winWidth / 6, (2 * winHeight) / 7))
        window.blit(text2, (winWidth / 4, (9 * winHeight) / 10))
        if update == 1:
            text5 = font.render(eligiblityConvey, 1, whiteBackground)
            window.blit(text5, (0, (400 * winHeight) / 660))

    else:
        if pre > score:
            text1 = font.render(appreciationPlayer2, 1, whiteBackground)
            text2 = font.render(stats, 1, whiteBackground)
            text3 = font.render(player1 + str(pre), 1, whiteBackground)
            text4 = font.render(player2 + str(score), 1, whiteBackground)
        elif pre == score:
            text1 = font.render(tiePlayer2, 1, whiteBackground)
            text2 = font.render(stats, 1, whiteBackground)
            text3 = font.render(player1 + str(pre), 1, whiteBackground)
            text4 = font.render(player2 + str(score), 1, whiteBackground)
        else:
            text1 = font.render(appreciationWinner, 1, whiteBackground)
            text2 = font.render(stats, 1, whiteBackground)
            text3 = font.render(player1 + str(pre), 1, whiteBackground)
            text4 = font.render(player2 + str(score), 1, whiteBackground)
        window.blit(text1, ((175 * winWidth) / 1200, (200 * winHeight) / 660))
        window.blit(text2, ((175 * winWidth) / 1200, (350 * winHeight) / 660))
        window.blit(text3, ((200 * winWidth) / 1200, (400 * winHeight) / 660))
        window.blit(text4, ((200 * winWidth) / 1200, (450 * winHeight) / 660))
        if update == 1:
            text5 = font.render(eligiblityConvey, 1, whiteBackground)
            window.blit(text5, (0, (500 * winHeight) / 660))

    pygame.display.update()
    pygame.time.wait(3500)
