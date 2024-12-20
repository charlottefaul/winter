import turtle


screen = turtle.Screen()
screen.screensize(800, 800)
screen.bgcolor('OrangeRed4')


t_ground = turtle.Turtle()
t_ground.speed(0)
t_ground.penup()
t_ground.goto(-1000, -100)
t_ground.pendown()
t_ground.fillcolor('salmon4')
t_ground.pencolor('salmon4')
t_ground.begin_fill()
t_ground.goto(1000, -100)
t_ground.goto(1000, -1000)
t_ground.goto(-1000, -1000)
t_ground.goto(-1000, -100)
t_ground.end_fill()


t.pencolor('DarkRed')
t.pensize(8)
t.penup()
t.goto(-250,250)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.penup()
t.goto(-200,200)
t.pendown()
t.right(90)
t.forward(100)
t.penup()
t.goto(-250,200)
t.pendown()
t.left(90)
t.forward(100)


t.penup()
t.goto(-1000, -100)
t.pendown()
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(1000)
t.right(90)
t.forward(50)
t.right(90)
t.forward(1000)
t.right(90)
t.end_fill()


t.penup()
t.goto(-175,-200)
t.pendown()
t.goto(-175,-300)

t.pencolor('green')
t.fillcolor('green')
t.pensize(1)
t.begin_fill()
t.penup()
t.goto(-250,-250)
t.pendown()
t.goto(-100,-250)
t.goto(-175,50)
t.goto(-250,-250)
t.end_fill()

import turtle

fireplace = turtle.Turtle()
fireplace.speed(5)

fireplace.penup()
fireplace.goto(-100, -100)
fireplace.pendown()
fireplace.begin_fill()
fireplace.color("brown")
fireplace.forward(200)
fireplace.left(90)
fireplace.forward(150)
fireplace.left(90)
fireplace.end_fill()
fireplace.penup()
fireplace.goto(-80, -80)
fireplace.pendown()
fireplace.begin_fill()
fireplace.color("black")
fireplace.forward(160)
fireplace.left(90)
fireplace.forward(120)
fireplace.left(90)
fireplace.end_fill()

fireplace.penup()
fireplace.goto(-60, -150)
fireplace.pendown()
fireplace.begin_fill()
fireplace.color("saddlebrown")
fireplace.forward(60)
fireplace.left(90)
fireplace.forward(20)
fireplace.left(90)
fireplace.end_fill()

fireplace.penup()
fireplace.goto(0, -150)
fireplace.pendown()
fireplace.begin_fill()
fireplace.color("saddlebrown")
fireplace.forward(60)
fireplace.left(90)
fireplace.forward(20)
fireplace.left(90)
fireplace.end_fill()

fireplace.penup()
fireplace.goto(-30, 50)
fireplace.pendown()
fireplace.begin_fill()
fireplace.color("darkgrey")
fireplace.forward(60)
fireplace.left(90)
fireplace.forward(100)
fireplace.left(90)
fireplace.end_fill()

fireplace.hideturtle()


turtle.done()




turtle.done()