import random
from time import sleep

def play():
    print_game_header()

    attempts, errors = level_select()
    secret_word = select_secret_word()
    word_blanks = ["_" for letter in secret_word]
    tried_letters = []
    lost = False

    print_gallows(errors, word_blanks)

    while(not lost):
        print_round_header(attempts, errors, tried_letters)

        guess = guess_input()
        word_blanks, errors = check_guess(guess, tried_letters, secret_word, word_blanks, errors)
        tried_letters.append(guess)
        print_gallows(errors, word_blanks)

        if("_" not in word_blanks):
            break
        lost = errors == attempts

    if(lost == True):
        print_lose_message(secret_word)
    else:
        print_win_message()

    print("\nGAME OVER\n")


def print_game_header():
    print("################################")
    print("Welcome to the hangman game")
    print("################################\n")

def level_select():
    while(True):
        print("(1) Easy (2) Medium (3) Hard\n")
        try:  
            level = int(input("Select your difficulty level: "))
            if(level < 1 or level > 3):
                print("Option out of range.\n")
                sleep(2)
                continue
            break
        except ValueError:
            print("Inserted value is not an integer.\n")
            sleep(2)
            continue

    if(level == 1):
        errors = 0
    elif(level == 2):
        errors = 1
    else:
        errors = 2
    
    attempts = 6

    return attempts, errors

def select_secret_word(filepath = "words.txt"):
    words = []
    with open(filepath) as file:
        for row in file:
            words.append(row.strip().upper())

    rand_idx = random.randrange(0, len(words))
    secret_word = words[rand_idx]
    return secret_word

def print_round_header(attempts, errors, tried_letters):
    remaining_attempts = attempts - errors
    print(f"\n{remaining_attempts} attempts remaining\n")
    print(f"Tried letters: {tried_letters}\n")
    sleep(1)

def guess_input():
    while(True):
        guess = input("Type a letter: ").strip().upper()
        if(len(guess) > 1):
            print("You must insert only one letter.\n")
            sleep(2)
        elif(guess.isnumeric()):
            print("You must insert a letter.\n")
            sleep(2)
        else:
            break
    return guess

def check_guess(guess, tried_letters, secret_word, word_blanks, errors):
    if(guess in tried_letters):
        print("\nYou already tried this one!\n")
        sleep(1)
    elif(guess in secret_word):
        index = 0
        for letter in secret_word:
            if(guess == letter):
                word_blanks[index] = guess

            index+=1
        print(f"\nNice!\n")
        sleep(1)
    
    else:
        errors += 1
        print(f"\nWrong!\n")
        sleep(1)
    
    return word_blanks, errors

def print_lose_message(secret_word):
    print("\nOh, no! You lose!\n")
    print(f"\nThe secret word was {secret_word}\n")
    print("     ________________         ")
    print("   /                  \       ")
    print(" /                      \  ")
    print(" |     X  X     X  X     |   ")
    print(" |      XX       XX      |     ")
    print(" |     X  X     X  X     |      ")
    print("  \                     /      ")
    print("   \__      X X      __/     ")
    print("   |\       X X      /|       ")
    print("   | |              | |        ")
    print("   |   I I I I I I    |        ")
    print("   |    I I I I I     |        ")
    print("    \_              _/       ")
    print("     \_____________/           ")

def print_win_message():
    print("\nCongratulations, you win!\n")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_gallows(errors, word_blanks):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif(errors == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    elif(errors == 3):
        print(" |      (_)   ")
        print(" |      /|    ")
        print(" |            ")
        print(" |            ")

    elif(errors == 4):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |            ")
        print(" |            ")

    elif(errors == 5):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |      /     ")

    elif (errors == 6):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |      / \   ")

    print("_|___         ")
    print(word_blanks)


if(__name__ == "__main__"):
    play()