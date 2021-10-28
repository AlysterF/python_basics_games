import guessing_game as guessing
import hangman_game as hangman

print("####################")
print("Best Games in Python")
print("####################\n")


while(True):
    print("(1) Guessing (2) Hangman (3) Quit Program\n")
    try:  
        game = int(input("Select your game: "))
        if(game < 1 or game > 3):
            print("Option out of range.\n")
            continue
        break
    except ValueError:
        print("Inserted value is not an integer.\n")
        continue

if(game==1):
    guessing.play()
elif(game==2):
    hangman.play()
else:
    quit()