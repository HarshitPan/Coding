import turtle
turtle.speed(4)
#turtle.bgcolor("black")
turtle.pensize(5)
def curve():
    for i in range(20):
        #turtle.speed(5)
        turtle.right(1)
        turtle.forward(1)
       # turtle.speed(1)]
def curve_back():
    for i in range(20):
        #turtle.speed(5)
        turtle.left(1)
        turtle.backward(1)
turtle.color("yellow", "black")
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.backward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.backward(120)
turtle.left(75)
turtle.backward(50)
turtle.left(15)
turtle.forward(50)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(50)
turtle.left(10)
turtle.backward(50)
turtle.right(55)

turtle.forward(50)
curve()
curve_back()
turtle.backward(25)
turtle.right(85)
turtle.forward(30)
turtle.left(36)
turtle.forward(35)
turtle.left(90)
turtle.forward(100)
turtle.backward(60)
turtle.right(60)
turtle.forward(55)
turtle.backward(55)
turtle.right(60)
turtle.forward(55)
turtle.right(60)
turtle.forward(150)
turtle.left(45)
turtle.forward(30)
turtle.backward(30)
turtle.right(45+90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90+45)
turtle.forward(30)
turtle.hideturtle()
turtle.done()