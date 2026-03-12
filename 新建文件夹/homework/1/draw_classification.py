import turtle

t = turtle.Turtle()
# t.screen.tracer(0)
t.speed(0)

def triangle(size):
    for i in range(3):
        t.forward(size)
        t.left(120)

def sierpinski(size, depth):

    if depth == 0:
        triangle(size)
        return

    sierpinski(size/2, depth-1)

    t.forward(size/2)
    sierpinski(size/2, depth-1)

    t.backward(size/2)
    t.left(60)
    t.forward(size/2)
    t.right(60)

    sierpinski(size/2, depth-1)

    t.left(60)
    t.backward(size/2)
    t.right(60)

sierpinski(400,3)

# turtle.update()
turtle.done()
