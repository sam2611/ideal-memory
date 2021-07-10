import turtle
sc = turtle.Screen()
alex=turtle.Turtle()
sc.bgcolor("black")
alex.color("white")
alex.speed(5)
t=10
alex.right(45)
col=["yellow","red","green","blue","yellow",
     "red","green","blue","yellow","red",
     "green","blue","yellow","red","green","blue",
     "yellow","red","green","blue",]
for i in range(20):
    alex.forward(t)
    alex.right(120)
    alex.forward(t)
    alex.right(120)
    alex.forward(t)
    alex.right(120)
    alex.forward(t)
    alex.right(120)
    alex.forward(t)
    t=t+10
    alex.color(col[i])
    if t==150:
        break
alex.penup()
alex.forward(230)
alex.pendown()
alex.speed(1)
alex.write("Congratulation", "left", font=("Verdana",30, "normal"))

