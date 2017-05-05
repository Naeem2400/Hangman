import random
import graphic

#INPUT A CHARACTER FROM USER AND CHECK IF IT IS PRESENT IN THE STRING
#RETURNS 1 IF FOUND
#RETURNS 0 IF NOT FOUND
#VARIABLES DEFINED GLOBALLY

hang_list=list()

def match_found(user_input,total_len,word):
   flag=False;
   for index in range(0,total_len):
       if user_input == word[index]:
          flag=True
          hang_list[index]=user_input
   return flag


def print_list (a_list):
   for i in range(0,len(a_list)):
      print a_list[i],
   print '\n'

def check_underscr(a_list):
  flag=False
  for index in range(0,len(a_list)):
      if hang_list[index]=="_":
          flag=True
          break;
  return flag

def FindWord ():
    #FINDING A RANDOM WORD
    path='words.txt'
    num=random.randint(1,4)
    line_number = 0
    word=" "
    with open(path,'r') as a_file:
      for a_line in a_file:
         line_number += 1
         if line_number == num:
           #print(a_line.rstrip())
           a_list = a_line.split(' ') 
           #print(a_list)
           word=a_list[1]
           #print word
           break
    #print(num)
    a_file.close()
    return word


def main ():   
    word=FindWord()
    total_len=len(word)-1
    
    remove_list=list()
    
    for index in range (0,total_len):
       hang_list.append("_")

    enter=raw_input("Enter any char to continue: ")
    graphic.start(hang_list,remove_list)

    print ' '.join(hang_list)

    while len(remove_list) is not 10:
       userInput=raw_input("Enter character: ")
       check=match_found(userInput,total_len,word)
       if check:
          graphic.hang_man(len(remove_list),hang_list,remove_list)
       elif not check:
          remove_list.append(userInput)
          print "Incorrect Characters: ",
          print_list(remove_list)
          graphic.hang_man(len(remove_list),hang_list,remove_list)
       print_list(hang_list)
       print '\n'
       letters_left=check_underscr(hang_list)
       if not letters_left:
          enter=raw_input("Enter any char to continue: ")
          graphic.won()
          enter=raw_input("Enter any char to continue: ")
          break

    if len(remove_list)==10:
      enter=raw_input("Enter any char to continue: ")
      graphic.lost()
      enter=raw_input("Enter any char to continue: ")


if __name__ == "__main__":
    main()


