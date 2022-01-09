# Hangman
A word guessing game
This game has been coded in Python 2.7 and includes the following modules:
* *Random Module* : to generate a random number that retrieves the corresponding word from a text file

 ## How the code works
 First a random word is generated, this word is tracked to the line number of the file storing the words. The corresponding word is stored in a variable. The user is asked to enter a word at a time, the letter pressed by the user is tracked by a loop. The letter if found in the word, is revealed else it gets stored in the wrong word list and the stick figure accordingly updates. If the user loses the game, the credit of the corect word is displayed on the screen.
