from turtle import Turtle,Screen

timy=Turtle()
screen=Screen()
timy.shape("turtle")
timy.color("green","red")

def move_forwards():
    timy.forward(10)

def move_backwards():
    timy.backward(10)

def turn_left():
    new_heading=timy.heading()+10
    timy.setheading(new_heading)

def turn_right():
    new_heading=timy.heading()-10
    timy.setheading(new_heading)

def clear():
    timy.clear()
    timy.penup()
    timy.home()
    timy.pendown()
screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")


# screen.onkey(key="space", fun=move_forward())
screen.exitonclick()
