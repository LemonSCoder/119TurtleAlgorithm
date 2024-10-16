# 119TurtleAlgorithm

### Algorithm Purpose in Real Life
+ Our group's code is very good for creating illusions or entertaining people as it is both satisfying and interesting. Not only this, the code is capable of creating complex shapes that are equal.
### Explain your Code
+ Our app has 8 shapes that move from the center of the screen to the edge of the screen, then back to the center. But before this happens, we ask the user to pick a number from 1-360. This will determine the shape that is being drawn. Overall, this means there are over 360 different shapes to draw! If met with a non-numeric answer or an answer outside of this requested range, the program will start over again. If the user picks a valid number, the user will be prompted to choose what type of "base color palette" they want this drawing to utilize, meaning that each of these eight shapes will be assigned a different color to draw with given the base color palette the user chooses out of five options (Cool, Light Rainbow, Pale, Tropical, and Sunset) represented by the letters A, B, C, D, and E. If the user types an answer that isn't A, B, C, D, or E (or at least doesn't contain them), the program will skip to its end, asking the user whether or not they want to have the program continue making drawings for them (If the user enters an answer that contains more than one of these letters, the program will run the program as if only the earliest letter checked for in the conditional and contained in the user's answer was entered by the user). After the user chooses their base color palette for the drawing, the program will start creating this drawing via the function create_turtle_shape(), which takes the number the user inputs as well as the index of the list within the list turtle_colors that contains the base color palette desired by the user (turtle_colors is a two-dimensional list). Each shape will appear on the screen and be set to be at different angles from each other so that they all draw in different areas of the canvas. Each shape is also assigned a color (via the variable index_addition, which adds one to itself for every turtle_shape in turtle_shapes) from the base color palette selected by the user. After this, the program iterates for step in range(50) and for turtle in previous_turtles within that iteration, allowing for each of the eight shapes to move 100 units in their designated direction based on the angle they were turned by one at a time for as long as for step in range(50) iterates. Once these eight shapes have traveled a total distance of 8000 units or more while not exceeding a total distance of 8700 units (calculated by forward_distance, which increases by 100 each time a shape moves since each shape, when it's their turn to move, goes forward 100 units), all eight of these shapes will turn left 180 degrees (allowing for them to go inwards again). Before these shapes move outwards again, they will turn left a certain number of degrees, and that number of degrees depends on the number the user chose from 1 to 360 at the beginning of the program, allowing for the program to create a unique drawing based on this number in the process. After the drawing is finished, the user is asked whether or not they want to have the program make another drawing for them. If the user responds with an (uppercased) answer that includes "Y" in it or with an invalid response, then the drawing will be erased from the turtle output screen using screen.clear() and the program will start all over again. However, if the user responds with an (uppercased) answer that includes "N" in it, the program will bid the user farewell and terminate.
### Variables Involved
+ Our code will include booleans (ex. user_input_statement), strings (ex. user_input and create_new_shape), integers (ex. index_addition and degree_turn), floats (ex. the eventual conversion of the variable user_input into a float variable), if statements, lists (ex. previous_turtles, turtle_shapes, and turtle_colors), and nested loops

### Link to Perf Task Doc
https://docs.google.com/document/d/11iKygGJbnxXfKnLON7xIGFWmN6H7MNS9LlgvDm_wU54/edit?usp=sharing 


### Sketch of Project
+ ![IMG_5339](https://github.com/user-attachments/assets/a0bef3de-4851-4638-b645-9a6b3f13d2b5)
+ ![IMG_5340](https://github.com/user-attachments/assets/09fcdd68-333b-473f-aee8-e574d3e85ce0)

### Video Matthew Liu

https://github.com/user-attachments/assets/b20b8024-c652-4d63-8f94-e053e087039c



