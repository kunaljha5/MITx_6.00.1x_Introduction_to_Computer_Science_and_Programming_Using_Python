# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random



WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for each in secretWord:
        if each not in lettersGuessed:
            return False
    return True

       




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    empty_word =  secretWord
    # FILL IN YOUR CODE HERE...
    for each in secretWord:
        if each not in lettersGuessed:
           empty_word = empty_word.replace(each,'_')
        else:
            empty_word  = empty_word
    return empty_word 



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    availbale_string = "abcdefghijklmnopqrstuvwxyz"
    for each in lettersGuessed:
        availbale_string  = availbale_string.replace(each, "")
    return availbale_string  
    

def hangman(secretWord):

    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    len_word = len(secretWord)
    print("I am thinking of a word that is "+ str(len_word) + " letters long")
  
    guess_left = 8
    lettersGuessed = []
    while (guess_left >0 ):
        print("-----------")
        print("You have " + str(guess_left) + " guesses left")
        availbale_string  =  getAvailableLetters(lettersGuessed)
        print("Available Letters: " + str(availbale_string))
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        if guess in lettersGuessed: 
            empty_word = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! You've already guessed that letter: " + str(empty_word ))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            empty_word = getGuessedWord(secretWord, lettersGuessed)
            print("Good guess: " +  str(empty_word))
            Fact_Bool = isWordGuessed(secretWord, lettersGuessed)
            if Fact_Bool == True:
                print("------------")
                print("Congratulations, you won!")
                break
        elif guess not in secretWord:
            lettersGuessed.append(guess)
            empty_word = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! That letter is not in my word: " + str(empty_word ))
            guess_left -= 1
            if guess_left == 0:
                print("-----------")
                print("Sorry, you ran out of guesses. The word was "+ str(secretWord) + "." )
        else: 
            print("Unknow Operation")
             

            
             






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
