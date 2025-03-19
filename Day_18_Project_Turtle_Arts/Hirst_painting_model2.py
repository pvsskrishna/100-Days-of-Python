import turtle
import random
from turtle import Turtle,Screen
# """This below code is used to extract the all the colours or desired number of colors that exist in image
# Extracting the RGB values from image"""
#
# import colorgram
#
# image = r"C:\Users\varun\PycharmProjects\PythonProject\Programes\Days\Day_18_Project_Turtle_Arts\image.jpeg"
#
# def extract_colors(image_path,num_of_colors):
#     """Extract RGB colors in tuples from image in a list """
#     colors = colorgram.extract(image_path,num_of_colors)
#     colors_list = []
#     for color in colors:
#         colors_list.append((color.rgb.r,color.rgb.g,color.rgb.b))
#     return colors_list
#
# print(extract_colors(image,100))

"""These are the extracted colors from that image taken from the output that generated from the above code from terminal"""

color_list = [(229, 227, 224), (227, 223, 225), (217, 226, 220), (195, 172, 122), (221, 226, 232), (159, 100, 58),
              (186, 161, 51), (126, 37, 25), (8, 54, 78), (52, 34, 29), (109, 70, 85), (118, 162, 175), (26, 119, 167),
              (74, 35, 43), (86, 139, 65), (9, 64, 44), (69, 153, 133), (121, 35, 40), (182, 98, 82), (209, 202, 146),
              (146, 177, 160), (176, 148, 154), (176, 203, 188), (218, 179, 172), (30, 79, 61), (23, 77, 92),
              (93, 143, 149), (159, 108, 112), (218, 179, 183), (168, 202, 208), (111, 130, 145)]

turtle.colormode(255)

tim = Turtle()
screen = Screen()
screen.screensize()
screen.setup(width = 1.0, height = 1.0)

tim.speed("fastest")
tim.penup()
tim.hideturtle()

number_of_dots = 100
dot_size = 20
distance = 50
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for count in range(1,number_of_dots+1):
    color = random.choice(color_list)
    tim.dot(dot_size,color)
    tim.forward(distance)

    if count % 10 == 0:
        tim.setheading(90)
        tim.forward(distance)
        tim.setheading(180)
        tim.forward(distance*10)
        tim.setheading(0)

screen.exitonclick()