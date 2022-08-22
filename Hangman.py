"This is my new Hangman game."

import random

Word_File = "words.txt"

def loadwords():
    OpenText = open(Word_File, 'r')
    ReadText = OpenText.readline()
    LineText = ReadText.split()
    return LineText

def chooseword(WordList):
    return random.choice(WordList)

def wordlength(secretword):
    length = len(secretword)
    return print("I'm thinking of a word that has", length, "letters.")

def iswordguessed(secretword, lettersguessed):
    letters = secretword.split()
    for letters in secretword:
        if not letters in lettersguessed:
            return False
    return True
    
def availableletters(lettersguessed):
    availableletters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in availableletters:
        if not i in lettersguessed:
            result += i
            availableletters = result
    return print("Availble letters:",availableletters)

def getguessedword(secretword, lettersguessed):
    hidden = list(secretword)
    for i in range(len(hidden)):
        if not hidden[i] in lettersguessed:
            hidden[i]='_ '
    return print(' '.join(hidden))

def hangman(secretword, lettersguessed):
    print ("Let's play Hangman!")
    print(" ")
    wordlength(secretword)
    GuessCount = 8
    print ("You have", GuessCount, "guesses.")
    print(" ")
    getguessedword(secretword, lettersguessed)
    print('')
    while GuessCount > 0:
        availableletters(lettersguessed)
        guess = input("Please choose a letter:")
        print("")
        print("")
        if not guess in secretword:
            if not guess in lettersguessed:
                GuessCount += -1
                print(" ")
                print ("Sorry,", guess," is not in my word.")
                print ("You have", GuessCount, "guesses left. Try again:")
                print(" ")
                getguessedword(secretword, lettersguessed)
                print(" ")
                lettersguessed.append(guess)
            else:
                print(" ")
                print("You already guessed that letter. Try again:")
                print(" ")
                getguessedword(secretword, lettersguessed)
                print(" ")
                lettersguessed.append(guess)
            if GuessCount == 0:
                print("You lost!")
                print("The word was", secretword)
                print(" ")
                replay = input("Would you like to play again?")
                print(" ")
                if replay == "yes":
                    print(" ")
                    lettersguessed = []
                    WordList = loadwords()
                    secretword = chooseword(WordList).lower()
                    hangman(secretword, lettersguessed)
                else:
                    print("Thanks for playing. Goodbye!")
                    print(" ")
                break
        else:
            if not guess in lettersguessed:
                print("")
                print("Great guess,", guess, "is in my word!")
                lettersguessed.append(guess)
                if iswordguessed(secretword,lettersguessed)== True:
                    print(secretword)
                    print ("Congratulations, you win!")
                    print(" ")
                    replay = input("Would you like to play again?")
                    print(" ")
                    if replay == "yes":
                        print(" ")
                        lettersguessed = []
                        WordList = loadwords()
                        secretword = chooseword(WordList).lower()
                        hangman(secretword, lettersguessed)
                        print(" ")
                    else:
                        print("Thanks for playing. Goodbye!")
                        print(" ")
                    break
                else:
                    print ("You still have", GuessCount, "guesses left.")
                    print(" ")
                    getguessedword(secretword, lettersguessed)
                    print(" ")
            else:
                print(" ")
                print("You already guessed that letter. Try again:")
                print(" ")
                getguessedword(secretword, lettersguessed)
                print(" ")
                lettersguessed.append(guess)
                

WordList = loadwords()
lettersguessed = []
secretword = chooseword(WordList).lower()    
hangman(secretword, lettersguessed)
