# Hangman
A word guessing game
This game has been coded in Python 2.7 and includes the following modules:
* *Random Module* : to generate a random number that retrieves the corresponding word from a text file
* *Pygame Module* : this module changes the stick figure depending upon your guesses
 ## How the code works
 First a random word is generated, this word is tracked to the line number of the file storing the words. The corresponding word is stored in a variable. The user is asked to enter a single character at a time, the letter pressed by the user is tracked by a function in pygame module. The letter if found in the word, is revealed else it gets stored in the wrong guess list and the stick figure accordingly updates. In case the user loses the game, the correct word is also displayes on the screen.
