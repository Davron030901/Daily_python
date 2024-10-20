# import colorgram
# rgb_colors=[]
# colors=colorgram.extract('images.jpeg',30)
# for color in colors:
#     r=color.rgb.r
#     g = color.rgb.g
#     b= color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim=turtle_module.Turtle()
color_list=[(248, 247, 246), (234, 241, 247), (247, 240, 245), (244, 249, 246), (141, 163, 182), (14, 119, 185), (206, 138, 168), (199, 175, 9), (240, 213, 62), (220, 156, 97), (150, 17, 34), (122, 72, 100), (13, 143, 53), (74, 29, 35), (59, 34, 31), (204, 67, 26), (226, 170, 199), (242, 80, 27), (16, 172, 189), (34, 176, 93), (2, 114, 63), (247, 214, 2), (114, 188, 142), (181, 95, 111), (188, 182, 211), (40, 39, 46), (157, 207, 217), (229, 173, 162), (162, 208, 181), (118, 117, 163)]
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
numbers_of_dots=100

for dot_count in range(1,numbers_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen=turtle_module.Screen()
screen.exitonclick()
