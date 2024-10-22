import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Define locations for drawing
locations = [
    (-200, 200), (0, 200),   # Locations for the squares
    (-200, 100), (0, 100),   # Locations for the triangles
    (-200, 0), (0, 0)        # Locations for the rectangles
]

# Draw squares at two different locations
pen.penup()
pen.goto(locations[0])  # Move to the first location for square
pen.pendown()
figures.draw_square(100, pen)

pen.penup()
pen.goto(locations[1])  # Move to the second location for square
pen.pendown()
figures.draw_square(100, pen)

# Draw triangles at two different locations
pen.penup()
pen.goto(locations[2])  # Move to the first location for triangle
pen.pendown()
figures.draw_triangle(100, pen)

pen.penup()
pen.goto(locations[3])  # Move to the second location for triangle
pen.pendown()
figures.draw_triangle(100, pen)

# Draw rectangles at two different locations
pen.penup()
pen.goto(locations[4])  # Move to the first location for rectangle
pen.pendown()
figures.draw_rectangle(150, 80, pen)

pen.penup()
pen.goto(locations[5])  # Move to the second location for rectangle
pen.pendown()
figures.draw_rectangle(150, 80, pen)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()