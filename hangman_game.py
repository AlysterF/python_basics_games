import random

def play():
    print("################################")
    print("Welcome to the hangman game")
    print("################################\n")

    secret_word = 'APPLE'

    lost = False
    word_guessed = False

    while(not lost and not word_guessed):

        while(True):
            guess = input("Type a letter: ").strip().upper()
            if(len(guess) > 1):
                print("You must insert only one letter.")
            elif(guess.isnumeric()):
                print("You must insert a letter.")
            else:
                break
        
        index = 0
        for letter in secret_word:
            if(guess == letter):
                print(index)
            index+=1

    print("Game over")

if(__name__ == "__main__"):
    play()