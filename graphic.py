import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
NAVYBLUE = ( 60,  60, 120)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
font = pygame.font.SysFont('Arial', 25, False, True)
font2 = pygame.font.SysFont('Arial', 25, False, False)
DISPLAYSURF= pygame.display.set_mode((700,600))
pygame.display.set_caption('Hangman!')
DISPLAYSURF.fill(WHITE)
text = font.render("Welcome! Let's play Hangman!",True,BLACK)
DISPLAYSURF.blit(text, [100, 125])
pygame.display.update()
fpsClock.tick(FPS)


def start(hang_list,remove_list):
    DISPLAYSURF= pygame.display.set_mode((700, 600))
    pygame.display.set_caption('Hangman!')
    DISPLAYSURF.fill(NAVYBLUE)
    pygame.draw.line(DISPLAYSURF, WHITE, [50,400], [100, 400], 10)
    update_text(hang_list,remove_list)
    pygame.display.update()
    fpsClock.tick(FPS)

def update_text(hang_list, remove_list):
    display_string=str('  '.join(hang_list))
    text = font.render(display_string,True,WHITE)
    DISPLAYSURF.blit(text, [100, 450])
    text = font2.render("Wrong Guesses: ",True,WHITE)
    DISPLAYSURF.blit(text, [10, 500])
    display_string=str(',  '.join(remove_list))
    text = font.render(display_string,True,WHITE)
    DISPLAYSURF.blit(text, [200, 500])

def won():
    DISPLAYSURF= pygame.display.set_mode((700, 600))
    pygame.display.set_caption('Hangman!')
    DISPLAYSURF.fill(WHITE)
    text = font.render("Congrats! You Won!",True,BLACK)
    DISPLAYSURF.blit(text, [150, 125])   
    pygame.display.update()
    fpsClock.tick(10)

def lost():
    DISPLAYSURF= pygame.display.set_mode((700, 600))
    pygame.display.set_caption('Hangman!')
    DISPLAYSURF.fill(WHITE)
    text = font.render("Oh No! You Lost!",True,BLACK)
    DISPLAYSURF.blit(text, [150, 125])   
    pygame.display.update()
    fpsClock.tick(10)


def hang_man(attempt,hang_list,remove_list):
    
    DISPLAYSURF= pygame.display.set_mode((700, 600))
    pygame.display.set_caption('Hangman!')
        
    while True:
    # main game loop
        DISPLAYSURF.fill(NAVYBLUE)
        pygame.draw.line(DISPLAYSURF, WHITE, [50,400], [100, 400], 10)
        if attempt==1:
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (75, 400),5)
                update_text(hang_list,remove_list)

        elif attempt==2:
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (75, 400),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (200, 100),5)
                update_text(hang_list,remove_list)
        
        elif attempt==3:
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (75, 400),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (200, 100),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 100), (200, 150),5)
                update_text(hang_list,remove_list)

        elif attempt==4:
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (75, 400),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (200, 100),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 100), (200, 150),5)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [175,150,50,50], 5)
                pygame.draw.arc(DISPLAYSURF, WHITE, [180,160,40,25],3.14+3.14/3,2*3.14-3.14/3,1)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [205,165,5,5], 2)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [190,165,5,5], 2)
                update_text(hang_list,remove_list)

        elif attempt==5:
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (75, 400),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (200, 100),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 100), (200, 150),5)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [175,150,50,50], 5)
                pygame.draw.arc(DISPLAYSURF, WHITE, [180,160,40,25],3.14+3.14/3,2*3.14-3.14/3,1)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [205,165,5,5], 2)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [190,165,5,5], 2)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 200), (200, 300),5)
                update_text(hang_list,remove_list)

        elif attempt==6:
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (75, 400),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (200, 100),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 100), (200, 150),5)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [175,150,50,50], 5)
                pygame.draw.arc(DISPLAYSURF, WHITE, [180,160,40,25],3.14+3.14/3,2*3.14-3.14/3,1)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [205,165,5,5], 2)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [190,165,5,5], 2)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 200), (200, 300),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 300), (150, 350),5)
                update_text(hang_list,remove_list)

        elif attempt==7:
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (75, 400),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (200, 100),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 100), (200, 150),5)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [175,150,50,50], 5)
                pygame.draw.arc(DISPLAYSURF, WHITE, [180,160,40,25],3.14+3.14/3,2*3.14-3.14/3,1)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [205,165,5,5], 2)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [190,165,5,5], 2)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 200), (200, 300),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 300), (150, 350),5)        
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 300), (250, 350),5)
                update_text(hang_list,remove_list)

        elif attempt==8:
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (75, 400),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (200, 100),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 100), (200, 150),5)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [175,150,50,50], 5)
                pygame.draw.arc(DISPLAYSURF, WHITE, [180,160,40,25],3.14+3.14/3,2*3.14-3.14/3,1)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [205,165,5,5], 2)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [190,165,5,5], 2)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 200), (200, 300),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 300), (150, 350),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 300), (250, 350),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 225), (250, 275),5)
                update_text(hang_list,remove_list)

        elif attempt==9:
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (75, 400),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (200, 100),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 100), (200, 150),5)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [175,150,50,50], 5)
                pygame.draw.arc(DISPLAYSURF, WHITE, [180,160,40,25],3.14+3.14/3,2*3.14-3.14/3,1)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [205,165,5,5], 2)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [190,165,5,5], 2)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 200), (200, 300),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 300), (150, 350),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 300), (250, 350),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 225), (250, 275),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 225), (150, 275),5)
                update_text(hang_list,remove_list)

        elif attempt==10:
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (75, 400),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (75, 100), (200, 100),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 100), (200, 150),5)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [175,150,50,50], 5)
                pygame.draw.arc(DISPLAYSURF, WHITE, [180,180,40,25],3.14/3,3.14-3.14/3,1)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [205,165,5,5], 2)
                pygame.draw.ellipse(DISPLAYSURF, WHITE, [190,165,5,5], 2)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 200), (200, 300),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 300), (150, 350),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 300), (250, 350),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 225), (250, 275),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (200, 225), (150, 275),5)
                pygame.draw.line(DISPLAYSURF, WHITE, (150, 200), (250, 200),5)
                update_text(hang_list,remove_list)

        else:
               update_text(hang_list,remove_list)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
          
        pygame.display.update()
        fpsClock.tick(FPS)
        return  