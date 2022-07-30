from math import ceil
def paint_can(wall_h, wall_w, coverage):
    area = wall_h * wall_w
    cans = ceil(area / coverage)

    print(f"You'll need {cans} cans of paint.")

test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))

paint_can(wall_h = test_h, wall_w = test_w, coverage = 5 )
