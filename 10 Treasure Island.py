print("Welcome to Treasure Island!")
print("Your mission is to find the treasure. ")
cross_road = input("You're at a cross-road. Do you want to turn left(L) or right(R) ?")
if cross_road == "R":
    print("Game Over")
else:
    island = input("You came to a lake! There is an island in the middle of the lake. Do you want to wait(W) for the boat or swim(S) ?")
    if island == "S":
        print("Game Over")
    else:
        door = input("You've arrived at the island unharmed. There is a house with three doors. One is red(R), one yellow(Y) and one blue(B). which colour do you choose? ")
        if door == "Y":
            print("You win!")
        else:
            print("Game Over")