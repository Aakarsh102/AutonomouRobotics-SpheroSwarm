import turtle
from turtle import *
from simulation.turtlesim import InitializeEnv

ball = Turtle()
ball.shape("circle")
ball.xcor()

# turtle.setworldcoordinates(0,0,400,400)
screen = turtle.Screen()

def configure_directions(ball, list_of_cors):
    list_to_return = []
    for i in list_of_cors:
        if i[0] > ball.xcor():
            list_to_return.append("right")
        elif i[0] < ball.xcor():
            list_to_return.append("left")

        if i[1] > ball.ycor():
            list_to_return.append("up")
        elif i[1] < ball.ycor():
            list_to_return.append("down")

        if i[0] == ball.xcor() and i[1] == ball.ycor():
            list_to_return.append("nothing")


screen.screensize(400,400)
screen.bgcolor("blue")
l = InitializeEnv.InitializeEnv(10, screen, 60)
ballList = l.get_ball_list()
screen.mainloop()

# screen.
# while True:
#     turtle.mainloop()

