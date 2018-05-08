import random

print("----------------------------------")
print("     GUESS THAT NUMBER GAME")
print("----------------------------------")

that_number = random.randint(0, 100)
game = 1

while game == 1:
    your_guess = input("Guess a number between 1 and 100: ")
    your_guess = int(your_guess)
    if your_guess > that_number:
        print("The number is smaller than {}".format(your_guess))
    elif your_guess < that_number:
        print("The number is larger than {}".format(your_guess))
    else:
        game = 0

print("Congratulations! You guessed {}!".format(that_number))
