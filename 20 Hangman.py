import random

word_list = ["apple",'bannana','pear']

chosen_word = random.choice(word_list)

result = []
for i in chosen_word:
    result += "_"

print(result)

lives = 6
repeat = 1
while repeat == 1:
    guess = input("Guess a letter: ").lower()
    j=0
    for i in chosen_word:
        if i == guess:
            result[j] = guess
        j +=1
    
    if guess not in chosen_word:
        lives -=1
        print("You guessed a letter that's not in the word!")
        print(f"you have {lives} lives left")
        if lives == 0:
            repeat = 0
            print("You lose!")

    if "_" not in result:
        repeat = 0
print(result)
#print(f"The word is {chosen_word}")