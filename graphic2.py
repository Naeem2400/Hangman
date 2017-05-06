import pygame, sys, time, random
import key_pressed
from pygame.locals import *
pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

#COLOURS: (R    G     B)
BLACK =   (  0,   0,   0)
WHITE =   (255, 255, 255)
NAVYBLUE =( 0,  128, 128)

#FONTS USED IN THE GAME    ('TYPE',SIZE,BOLD,ITALICS)
font = pygame.font.SysFont('Arial', 25, False, True)
font2 = pygame.font.SysFont('Arial', 25, False, False)

#FIRST SCREEN TO APPEAR WHEN THE GAME STARTS
DISPLAYSURF= pygame.display.set_mode((700,800))
pygame.display.set_caption('Hangman!')
DISPLAYSURF.fill(WHITE)
text = font.render("Welcome! Let's play Hangman!",True,BLACK)
DISPLAYSURF.blit(text, [100, 125])
pygame.display.update()
fpsClock.tick(10)
time.sleep(2)

#FindWord() RETURNS A RANDOM WORD FROM A TEXT FILE. THIS WORD IS TO BE GUESSED IN THE GAME 
def FindWord ():
    path='words.txt'
    num=random.randint(1,45)
    line_number = 0
    word=" "
    with open(path,'r') as word_file:
      for line in word_file:
         line_number += 1
         if line_number == num:
           word=line
           break
    word_file.close()
    return word

#match_found(str,int,str) RETURNS TRUE IF THE LETTER ENTERED BY THE USER COMES IN THE WORD
#ELSE IT RETURNS FALSE. IT TAKES IN THE KEY PRESSED,LENGTH OF THE WORD AND THE WORD ITSELF
def match_found(user_input,total_len,word,hang_list):
   flag=False;
   user_input=user_input.lower()
   for index in range(0,total_len):
       if user_input == word[index]:
          flag=True
          hang_list[index]=user_input
   return flag

#search(str,list) CHECKS IF THE LETTER ENTERED BY USER HAS BEEN ENTERED BEFORE, IF YES IT RETURNS TRUE
#ELSE IT RETURNS FALSE. IT TAKES IN THE KEY PRESSED AND THE LIST WHICH STORES THE WRONG GUESSES 
def search(user_input,remove_list):
   flag=False;
   user_input=user_input.lower()
   for index in range(0,len(remove_list)):
       if user_input == remove_list[index]:
          flag=True
          break
   return flag

#check_underscr(list) CHECKS THE STATE OF THE GUESSED WORD FOR A BLANK. IF A BLANK EXISTS IT RETURNS TRUE
#ELSE IT RETURNS FALSE
def check_underscr(hang_list):
  flag=False
  for index in range(0,len(hang_list)):
      if hang_list[index]=="_":
          flag=True
          break;
  return flag

#start(list,list) DISPLAYS THE SCREEN WITH THE FIRST STATE OF THE GUESSED WORD
def start(hang_list,remove_list):
    DISPLAYSURF= pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Hangman!')
    DISPLAYSURF.fill(NAVYBLUE)
    pygame.draw.line(DISPLAYSURF, WHITE, [50,400], [100, 400], 10)
    update_text(hang_list,remove_list)
    pygame.display.update()
    fpsClock.tick(FPS)
    return

#update_text(ist,list) DISLPAYS THE STATE OF THE WORD TO BE GUESSED AND WRONG GUESSES ON THE SCREEN
def update_text(hang_list, remove_list):
    display_string=str('  '.join(hang_list))
    text = font.render(display_string,True,WHITE)
    DISPLAYSURF.blit(text, [100, 450])
    text = font2.render("Wrong Guesses: ",True,WHITE)
    DISPLAYSURF.blit(text, [10, 500])
    display_string=str(',  '.join(remove_list))
    text = font.render(display_string,True,WHITE)
    DISPLAYSURF.blit(text, [200, 500])

#won() DISPLAYS THE WINNING SCREEN AFTER THE USER HAS GUESSED THE RIGHT WORD
def won():
    DISPLAYSURF= pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Hangman!')
    DISPLAYSURF.fill(WHITE)
    text = font.render("Congrats! You Won!",True,BLACK)
    DISPLAYSURF.blit(text, [150, 125])   
    pygame.display.update()
    fpsClock.tick(10)
    time.sleep(2)

#lost(str) DISPLAYS THE SCREEN INFORMING THE USER THAT THEY HAVE LOST AND IT ALSO DISPLAYS THE CORRECT WORD
def lost(word):
    DISPLAYSURF= pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Hangman!')
    DISPLAYSURF.fill(WHITE)
    text = font.render("Oh No! You Lost!",True,BLACK)
    DISPLAYSURF.blit(text, [150, 125])   
    text = font.render("Correct Word: "+word.strip(),True,BLACK)
    DISPLAYSURF.blit(text, [150, 200]) 
    pygame.display.update()
    fpsClock.tick(10)
    time.sleep(2)

#hang_man(int,list,list) IT DISPLAYS THE STATE OF THE STICK MAN, DEPENDING UPON NO. OF ATTEMPTS
#AND ALSO CALLS update_text(list,list) TO UPDATE STATE OF GUESSED WORRD ON THE SCREEN
def hang_man(attempt,hang_list,remove_list):
    
    DISPLAYSURF= pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Hangman!')
        
    while True:
    # main game loop
        DISPLAYSURF.fill(NAVYBLUE)
        pygame.draw.line(DISPLAYSURF, WHITE, [50,400], [100, 400], 10)
        if attempt==0:
                start(hang_list,remove_list)

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
        
        pygame.display.update()
        fpsClock.tick(FPS)
        #time.sleep(3)
        return

#THE MAIN FUNCTION WHICH COORDINATES THE WORKING OF THE ABOVE FUNCTIONS AND ALSO CONTAINS THE MAIN GAME LOOP
def main():
   word=FindWord()
   total_len=len(word)-1
   remove_list=list()
   hang_list=list() 
   for index in range (0,total_len):
      hang_list.append("_")

   DISPLAYSURF= pygame.display.set_mode((700,800))
   pygame.display.set_caption('Hangman!')
   DISPLAYSURF.fill(WHITE)
   start(hang_list,remove_list)
   KeepGoing=True
   while KeepGoing:
        text = font2.render("Enter Character: ",True,WHITE)
        DISPLAYSURF.blit(text, [10,600])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               sys.exit()
            elif event.type == pygame.KEYUP:
               KeyName = pygame.key.name(event.key)
               text = font2.render(KeyName,True,WHITE)
               DISPLAYSURF.blit(text, [200, 600])
               pygame.display.update()
               time.sleep(1)
               check=match_found(KeyName,total_len,word,hang_list)
               if check:
                  hang_man(len(remove_list),hang_list,remove_list)
               elif not check:
                  if not search(KeyName,remove_list):
                      remove_list.append(KeyName)
                  hang_man(len(remove_list),hang_list,remove_list)
                  letters_left=check_underscr(hang_list)
                  if not letters_left:
                     won()
                     KeepGoing=False
                  if len(remove_list)==10:
                     lost(word)
                     KeepGoing=False 
            
            fpsClock.tick(FPS)
               
if __name__ == "__main__":
    main()