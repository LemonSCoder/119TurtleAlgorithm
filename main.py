import turtle as trtl
import random
import sys

screen = trtl.Screen()
screen.setup(width=600, height=600)

previous_turtles = []
turtle_shapes = ["circle", "circle", "circle", "circle", "circle", "circle", "circle", "circle"]
turtle_colors = [["#555d8e", "#566f94", "#56819b", "#5494a1", "#62a4a7", "#7db2ac", "#97c0b0", "#b1ceb5"], ["#ffadad", "#ffd6a5", "#fdffb6", "#caffbf", "#9bf6ff", "#a0c4ff", "#bdb2ff", "#ffc6ff"], ["#715660", "#846470", "#566071", "#727f96", "#c39f72", "#d5bf95", "#667762", "#879e82"], ["#c7522a", "#d68a58", "#e5c185", "#fbf2c4", "#b8cdab", "#74a892", "#3a978c", "#008585"], ["#003f5c", "#58508d", "#8a508f", "#bc5090", "#de5a79", "#ff6361", "#ff8531", "#ffa600"]]

original_turtles = previous_turtles.copy()

def create_turtle_shape(degree_input, index_number):

    heading = 0

    forward_distance = 0

    degree_turn = 0

    index_addition = 0

    for turtle_shape in turtle_shapes:
        pen = trtl.Turtle(shape = turtle_shape)
        pen.speed(20)
        previous_turtles.append(pen)
        new_color = turtle_colors[index_number][index_addition]
        pen.color(new_color)
        pen.left(degree_turn)
        index_addition += 1
        degree_turn += 45

    for step in range(50):
        for turtle in previous_turtles:
            turtle.forward(100)
            if forward_distance >= 8000 and forward_distance <= 8700:
                turtle.left(180)
            forward_distance += 100
            turtle.left(degree_input)

user_input_statement = True

while user_input_statement == True:
    user_input = input("Enter a number between 1 and 360: > ")
    if user_input.isnumeric():
        if float(user_input) in range(360):
          color_palette_input = input("What base color palette do you want for the shape? \n [A] Cool \n [B] Light Rainbow \n [C] Pale \n [D] Tropical \n [E] Sunset \n")
          if "A" in color_palette_input.upper():
            create_turtle_shape(float(user_input), 0)
          elif "B" in color_palette_input.upper():
            create_turtle_shape(float(user_input), 1)
          elif "C" in color_palette_input.upper():
            create_turtle_shape(float(user_input), 2)
          elif "D" in color_palette_input.upper():
            create_turtle_shape(float(user_input), 3)
          elif "E" in color_palette_input.upper():
            create_turtle_shape(float(user_input), 4)
          else:
            print("That's not a valid option.")
          create_new_shape = input("Do you want to create another shape? \n [Y] YES \n [N] NO \n")
          if "Y" in create_new_shape.upper():
              screen.clear()
          elif "N" in create_new_shape.upper():
              user_input_statement = False
              print("Goodbye.")
              sys.exit()
          else:
            screen.clear()
            print("That's not a valid option!")
            continue
        else:
            print ("That's not a number between 1 and 360!")
    else:
            print ("Only type a number...")


wn = trtl.Screen()
wn.mainloop()
