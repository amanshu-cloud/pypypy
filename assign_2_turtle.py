import turtle
turtle.pensize(5)
turtle.setx(10)
turtle.sety(10)
turtle.bgcolor('black')
tut = turtle.Turtle()

tut.pencolor('#ffffff')

w = 200
for i in range(3):
    tut.forward(200)
    tut.right(90)
while(w!=0):
    w-=20
    for i in range(2):
        tut.forward(w)
        tut.right(90)

turtle.end_fill()