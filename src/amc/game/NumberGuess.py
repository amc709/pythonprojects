'''
Created on Mar 28, 2017

@author: acastillon
'''

from random import random
import re


count = 0
maxTries = 8
gameLevel = 1
limitNum = 100


def generateGuessNumber():
    """
    Randomly generates a number between 1-100 to be guessed by user.
    """
    
    global numberToGuess
    
    ran = random()
    ran *= limitNum
    numberToGuess = int(ran)
    return numberToGuess
    
    
def processGuess(guess): 
    global count
    isFound = False  
    if guess > numberToGuess:
        print("... LOWER")        
    elif guess < numberToGuess:
        print("... HIGHER")        
    else:
        count += 1
        print("Congratulations!!! You found it in " + str(count) + " tries.")
        isFound = True
    return isFound    


def showGameLevels():
    print("Game Levels:")
    print("   (1) Normal")
    print("   (2) Hard")
    print("   (3) Are you crazy???")
    
    global gameLevel
    global maxTries
    global limitNum
    
    while True:
        try:
            gameLevel = int(input("What level do you want to play (1,2,or 3)?  "))
            if gameLevel != 1 and gameLevel != 2 and gameLevel != 3:
                continue
            break
        except Exception:
            print("    ===>  WRONG ENTRY!!!  Please reenter.")
            continue
    
    if gameLevel == 2:
        maxTries = 12
        limitNum = 1000
    elif gameLevel == 3:
        maxTries = 15
        limitNum = 10000
    else:
        maxTries = 8
        limitNum = 100

def play():
    """
    Starts the number guessing game.
    """
    showGameLevels()
    
    print("\nI'm thinking of a number between 1 and {0}.  Can you guess what it is?".format(limitNum)) 

    global count
    
    numberToGuess = generateGuessNumber();
    
    print("You have " + str(maxTries) + " tries to guess the mystery number ...")
    for i in range(maxTries):
        while True:
            try:
                guess = int(input("Attempt " + str(i + 1) +" - Guess a number:  "))
                break
            except Exception:
                print("    ===>  WRONG ENTRY!!!  Please reenter.")
                continue
            
        isFound = processGuess(guess)
        if isFound:
            break
        else:
            count +=1    
            if count == maxTries:
                print("Sorry, you were not able to make the correct guess.  The mystery number is '" + str(numberToGuess) + "'.")      
        
    postPlay()
        

def postPlay():
    """
    After the game, the user is asked if he wants to play another game. If so, the game restarts.
    """
    global count
    global numberToGuess
    
    playAgain = input("Play again (Y/N)?  ")
    if re.match("^y.*", playAgain):
        print("===================================================")
        
        count = 0
        numberToGuess = 0
        play()
    else:
        print()
        print("Thanks for playing! :)")        
# -------------------------------------



if __name__ == '__main__':
    play()
