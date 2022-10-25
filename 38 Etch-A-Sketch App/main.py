from turtle import Turtle, Screen

timy = Turtle()
timy_screen = Screen()


def forward():
    timy.forward(10)


def backward():
    timy.backward(10)


def clockwise():
    timy.setheading(timy.heading() + 10)


def anti_clockwise():
    timy.setheading(timy.heading() - 10)


def clear_screen():
    timy.clear()
    timy.penup()
    timy.home()
    timy.pendown()

timy_screen.listen()
timy_screen.onkey(fun= forward, key= "w")
timy_screen.onkey(fun= backward, key= "s")
timy_screen.onkey(fun= anti_clockwise, key= "a")
timy_screen.onkey(fun= clockwise, key= "d")
timy_screen.onkey(fun= clear_screen, key= "c")

timy_screen.exitonclick()