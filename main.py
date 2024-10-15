import turtle as trtl

screen = trtl.Screen()
screen.setup(width=600, height=600)

previous_turtles = []
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "brown", "pink"]

degree_turn = 0

for turtle_shape in turtle_shapes:
    pen = trtl.Turtle(shape = turtle_shape)
    previous_turtles.append(pen)
    pen.penup()
    new_color = turtle_colors.pop()
    pen.fillcolor(new_color)
    pen.left(degree_turn)
    degree_turn += 45

original_turtles = previous_turtles.copy()

step = 0

heading = 0

for step in range(50):
    for turtle in previous_turtles:
        turtle.forward(15)
        if (turtle.xcor() == -300) or (turtle.xcor() == 300) or (turtle.ycor() == -300) or (turtle.ycor() == 300) or (turtle.xcor() == -600) or (turtle.xcor() == 600) or (turtle.ycor() == -600) or (turtle.ycor() == 600):
            '''
            for turtleheading in previous_turtles:
                turtle.setheading(heading)
                heading += 45
            '''
            turtle.left(180)


    step += 1


wn = trtl.Screen()
wn.mainloop()
