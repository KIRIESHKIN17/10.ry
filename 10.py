import turtle
turtle.shapesize(2)
turtle.color("green","yellow")
turtle.speed(5)

for step in range(1):
    turtle.begin_fill()
    for i in range(1):
        turtle.forward(50)
        turtle.left(50)
    turtle.end_fill()
    turtle.forward(50)
    turtle.right(50)
turtle.hideturtle()
x = input()