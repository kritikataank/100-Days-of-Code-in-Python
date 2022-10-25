import turtle
from turtle import Turtle, Screen
import random

timy = Turtle()
timy_screen = Screen()
timy_screen.colormode(255)

# Draw a square

#timy.shape("turtle")
#for _ in range(4):
    #timy.forward(100)
    #timy.right(90)

# Draw a Dashed Line

# for _ in range(15):
#     timy.forward(10)
#     timy.penup()
#     timy.forward(10)
#     timy.pendown()

# Draw Different Shapes

# for i in range (3,11):
#     ang = 360/i
#     colour = ["Navy", "PaleGreen", "DarkSlateGray", "Yellow", "DarkOliveGreen", "Maroon", "DarkOrange"]
#     timy.color(random.choice(colour))
#     for _ in range (i):
#         timy.forward(100)
#         timy.right(ang)

# Generate a Random Walk

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

# timy.shape("circle")
# timy.pensize(15)
# timy.speed("fastest")
# for _ in range(200):
#     #colour = ["Navy", "PaleGreen", "DarkSlateGray", "Yellow", "DarkOliveGreen", "Maroon", "DarkOrange"]
#     #timy.color(random.choice(colour))
#     timy.pencolor(random_color())
#     direction = [0, 90, 180, 270]
#     timy.forward(30)
#     timy.setheading(random.choice(direction))

# Draw a Spirograph

# timy.speed("fastest")
# def draw_spirograph(size_of_gap):
#      for _ in range(int(360/size_of_gap)):
#          timy.pencolor(random_color())
#          timy.circle(100)
#          timy.setheading(timy.heading() + size_of_gap)
# draw_spirograph(5)

timy_screen.exitonclick()