secret = 38
print("=== Welcome to guess the number! ===")
print("Guess a number between 1 & 50")
guess_count = 1
win = False
while guess_count <= 5:
    guess = int(input(""))
    if guess > 50 or guess < 1:
        print("invalid guess, try again")
        guess = int(input(""))
    elif guess >= 49:
        print("warm")
        guess_count += 1
    elif guess <= 29 and guess >= 20:
        print("cold")
        guess_count += 1
    elif guess >= 30 and guess <= 35:
        print("hot")
        guess_count += 1
    elif guess == 36 or 37 or 39 or 40:
        print("Very Close!")
    elif guess >= 41 and guess <= 49:
            print("hot")
            guess_count += 1
    elif guess == 50:
        print("cold")
        guess_count += 1
    elif guess == 38:
        print("Well done you did it")
        guess_count += 10
        win = True
    else:
        print("ice cold")
if win == True:
    print("You win! Well done!")
else:
    print("Better luck next time!")
