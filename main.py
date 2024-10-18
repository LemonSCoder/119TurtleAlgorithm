import turtle as trtl
import random
import sys

screen = trtl.Screen()
screen.setup(width=600, height=600)

previous_turtles = []
turtle_shapes = ["circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "brown", "pink"]

original_turtles = previous_turtles.copy()

def create_turtle_shape(degree_input):

    step = 0

    heading = 0

    forward_distance = 0

    speed = 0

    degree_turn = 0

    for turtle_shape in turtle_shapes:
        pen = trtl.Turtle(shape = turtle_shape)
        pen.speed(20)
        previous_turtles.append(pen)
        new_color = turtle_colors.pop()
        pen.color(new_color)
        pen.left(degree_turn)
        degree_turn += 45

    for step in range(50):
        for turtle in previous_turtles:
            turtle.forward(100)
            if forward_distance >= 8000 and forward_distance <= 8700:
                turtle.left(180)
            forward_distance += 100
            turtle.left(float(user_input))
        
    step += 1

user_input_statement = True

while user_input_statement == True:
    user_input = input("Enter a number between 1 and 360: > ")
    if user_input.isnumeric():
        if float(user_input) in range(360):
            create_turtle_shape(float(user_input))
        else:
            print ("That's not a number between 1 and 360!")
    else:
            print ("Only type a number...")
    create_new_shape = input("Do you want to create another shape? \n [Y] YES \n [N] NO \n")
    if "Y" in create_new_shape.upper():
        screen.clear()
    else:
        user_input_statement = False
        print("Goodbye.")
        sys.exit()


wn = trtl.Screen()
wn.mainloop()
