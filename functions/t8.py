from turtle import *

speed('fastest')
bgcolor('black')
pencolor('yellow')
penup()
setpos(100,-100)
pendown()

for i in range(50,0,-2):
    forward(i)
    left(90)

penup()
setpos(100,100)
pendown()

for i in range(50,0,-2):
    forward(i)
    left(90)

penup()
setpos(-100,-100)
pendown()

for i in range(50,0,-2):
    forward(i)
    left(90)

penup()
setpos(-100,100)
pendown()

for i in range(50,0,-2):
    forward(i)
    left(90)

mainloop()