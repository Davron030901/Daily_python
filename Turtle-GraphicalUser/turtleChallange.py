import turtle as t
import random

tim =t.Turtle()
tim.shape("turtle")
tim.color("green","red")
colours=["dark green","cyan","goldenrod","deep pink","lime","blue","yellow","indigo"]
def draw_shape(count):
    grade=360
    temp = grade / count
    for _ in range(count):
        # tim.forward(100)
        # tim.left(temp)
        tim.right(temp)
        tim.forward(100)
count=3
while count!=10:
    tim.color(random.choice(colours))
    draw_shape(count)
    count+=1

#
# screen=Screen()
# screen.exitonclick()