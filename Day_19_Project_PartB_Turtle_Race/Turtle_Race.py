import random
from turtle import Turtle,Screen
screen = Screen()
width,height = 600,350
screen.setup(width = 600,height = 350)
bet = screen.textinput("make the bet","who is going to win? type color name.")

class TurtleRace:
    def __init__(self,color,x,y):
        self.turtle = Turtle()
        self.turtle.shape("turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x,y)
        self.turtle.pendown()

    def pitch(self, width, height):
        """Draws a race track with a dynamically positioned rectangle."""
        self.turtle.hideturtle()
        self.turtle.penup()

        # Define the starting position relative to the screen size
        start_x = -width // 2 + 20  # 20 pixels from the left edge
        start_y = height // 2 - 20  # 20 pixels from the top edge

        # Define track width and height
        track_width = width - 40  # Keeping a 20px margin on both sides
        track_height = height - 80  # Keeping a 40px margin (top/bottom)

        # Move to start position
        self.turtle.goto(start_x, start_y)
        self.turtle.pendown()

        # Draw the rectangular track
        for _ in range(2):
            self.turtle.forward(track_width)  # Move right
            self.turtle.right(90)  # Turn down
            self.turtle.forward(track_height)  # Move down
            self.turtle.right(90)  # Turn left

colors = ["violet","indigo","blue","green","yellow","orange","red"]
gap_between_racers = 30
y_starting_value = -90
end_point_distance = 270
index = 0

boarder = TurtleRace("black", 0, 0)
boarder.pitch(width, height)

racers = []
for color in colors:
    x_default_value = -screen.window_width() // 4 - 70
    y_value = y_starting_value + (index * gap_between_racers)
    racer = TurtleRace(color,x=x_default_value,y= y_value)
    racers.append(racer)
    index += 1

Race_is_on = True
while Race_is_on:
    for racer in racers:
        racer.turtle.penup()
        racer.turtle.forward(random.randint(1,10))
        if racer.turtle.xcor() >= end_point_distance:
            winner = racer.turtle.pencolor()
            Race_is_on = False

            if winner == bet:
                print(f"You won! {winner} is the winner")
            else:
                print(f"You lose! {winner} is the winner")
            break

screen.exitonclick()