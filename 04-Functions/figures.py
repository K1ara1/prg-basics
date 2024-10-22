import turtle

def draw_square(length, pen):
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(length, pen):
    for i in range(3):
        pen.forward(length)
        pen.left(120)  

def draw_rectangle(length_a, length_b, pen):
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)