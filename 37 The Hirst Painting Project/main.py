from turtle import Turtle, Screen
import random
# import colorgram
#
# colors = colorgram.extract('image.jpg',70)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color.append((r, g, b))
#
# print(rgb_color)

color_list = [(249, 242, 246), (126, 165, 189), (215, 158, 80), (175, 10, 27), (134, 186, 161), (54, 101, 148), (217, 127, 160), (234, 204, 109), (23, 18, 56), (208, 75, 121), (47, 128, 80), (232, 71, 48), (141, 68, 106), (36, 24, 17), (180, 163, 39), (48, 45, 116), (57, 22, 46), (143, 80, 32), (153, 21, 14), (73, 163, 98), (120, 117, 162), (224, 167, 188), (236, 176, 158), (35, 56, 34), (23, 91, 52), (32, 166, 192), (170, 203, 188), (177, 198, 202), (185, 187, 207), (81, 69, 41), (238, 201, 2), (242, 14, 27)]

timy = Turtle()
timy_screen = Screen()
timy_screen.colormode(255)

timy.setheading(215)
timy.penup()
timy.forward(270)
timy.setheading(270)
timy.forward(60)
timy.setheading(0)

timy.pensize(20)

num_of_dots = 180

for i in range(10):
    for j in range(10):
        timy.pendown()
        timy.dot(20, random.choice(color_list))
        timy.penup()
        timy.forward(50)
    timy.penup()
    timy.setheading(90)
    timy.forward(50)
    timy.setheading(180)
    timy.forward(500)
    timy.setheading(0)

timy_screen.exitonclick()