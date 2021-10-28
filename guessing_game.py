import random

def play():
    print("################################")
    print("Welcome to the guessing game")
    print("################################\n")

    secret_number = random.randrange(1,101)
    points = 100

    while(True):
        print("(1) Easy (2) Medium (3) Hard\n")
        try:  
            level = int(input("Select your difficulty level: "))
            if(level < 1 or level > 3):
                print("Option out of range.\n")
                continue
            break
        except ValueError:
            print("Inserted value is not an integer.\n")
            continue

    if(level == 1):
        total_rounds = 20
        lost_points = 3
    elif(level == 2):
        total_rounds = 10
        lost_points = 5
    else:
        total_rounds = 5
        lost_points = 15

    for round in range(1, total_rounds + 1):
        print(f"Round {round} of {total_rounds}\n")

        for flag in range(1,4):
            try:  
                guess = input("Type an integer number between 1 and 100: ")
                guess = int(guess)
                if(guess < 0 or guess > 100):
                    print(f"Error {flag} of 3")
                    print("Number out of valid range.\n")
                    continue
                break
            except ValueError:
                try:
                    float(guess)
                    print(f"Error {flag} of 3")
                    print("This is not an integer. Please enter a valid number.\n")
                except ValueError:
                    print(f"Error {flag} of 3")
                    print("This is not a number. Please enter a valid number.\n")
                    round = round - 1

        if(guess == secret_number):
            print("Correct! You won\n")
            print(f"Points: {points}\n")
            break
        else:    
            if(guess > secret_number):
                print("Wrong! The secret number is smaller than ", guess)
            else:
                print("Wrong! The secret number is bigger than ", guess)
            points -= lost_points
            print(f"You lost {lost_points} points :(\n")

    print(f"The number was: {secret_number}")
    print("Game over")

if(__name__ == "__main__"):
    play()