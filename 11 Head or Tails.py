import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

coin_side = random.randint(0, 1)

if coin_side == 1:
    print("Heads")
else:
    print("Tails")