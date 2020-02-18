import pygame
from player import*
from enemy import*
from fixed import*
from coins import*

# style of writing
fontType="comicsans" 

# All strings which are used
appreciationPlayer1='WELL DONE,Player 1' 
scorePlayer1='Your total score is:'
appreciationPlayer2="WELL tried,You lost(Player2)"
stats="FINAL STATS"
player1="Player1: "
player2="Player2: "
tiePlayer2="Congratulations,match drawn(Player2)"
appreciationWinner="Fantastic performance,You Won(player2)"
eligiblityConvey="You are eligible for level update"

# all background colours
blackBackground=(0,0,0)
whiteBackground=(255,255,255)
yellowBackground=(255,255,0)
greenBackground=(0,255,0)
redBackground=(255,0,0)

# screen dimensions
winWidth=1200
winHeight=660

# font sizes
fontSize1=30
fontSize2=50

# setting window resolutions stuff
window = pygame.display.set_mode((winWidth,winHeight))
win = pygame.display.set_mode((winWidth,winHeight))

# all sprites locations are said here
man=Player(600,590,364,64)
spike=[fixed(500,285),fixed(1050,285),fixed(250,165),fixed(750,165),fixed(0,45),fixed(0,405),fixed(145,525)]
vil=[Enemy(0,520,77,64,1200,0),Enemy(400,520,77,64,1200,0),Enemy(0,40,77,64,1200,0),Enemy(400,40,77,64,1200,0),Enemy(220,160,77,64,1200,0),Enemy(660,160,77,64,1200,0),Enemy(0,280,77,64,1200,0),Enemy(950,280,77,64,1200,0),Enemy(500,400,77,64,1200,0)] 
coins=[Coin(100,130),Coin(400,130),Coin(800,130),Coin(1100,130),Coin(40,350),Coin(300,350),Coin(700,350),Coin(950,350),Coin(790,480),Coin(350,480),Coin(600,240)]

# initialising velocity
man.vel=5
for i in vil:
    i.velInitial=3
    
# frame rates
mainFunctionFrameRate=27


