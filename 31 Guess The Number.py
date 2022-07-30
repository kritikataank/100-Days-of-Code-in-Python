import random

def guess_result(number, guessed, atmp):
    if guessed == number:
        print("You guessed right!")
        return atmp - atmp
    elif guessed > number:
        print("Too high")
        print("Guess Again.")
        return atmp - 1
    else:
        print("Too low")
        print("Guess Again.")
        return atmp - 1

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    if level == "hard":
        return 5

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    num = random.randint(1, 100)

    turns = difficulty()
    guess = 0
    while guess != num and turns != 0:
        guess = int(input("Make a guess: "))
        turns = guess_result(num, guess, turns)
        print(f"You have {turns} turns left.")
            
game()