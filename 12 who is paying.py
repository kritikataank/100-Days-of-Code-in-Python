import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

Enter_name = input("Enter everybody's name seperated by comma: ")
names = Enter_name.split(", ")
# person = random.choice(names)
n = len(names)

person = random.randint(0, n-1)

print(f"{names[person]} is going to buy the meal today!")