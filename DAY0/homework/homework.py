from turtle import *
#printing a square

color("green")
width(7)
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
left(90)
end_fill()
#printing a dor
color("blue")
begin_fill()
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()

right(150)

#pringing a ruff
color("red")
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()
exitonclick()
print("the end")