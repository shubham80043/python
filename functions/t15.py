from turtle import *
import random

speed('fastest')
color=['red','blue']
for i in range(50):
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    penup()
    goto(x,y)
    pendown()
    pensize(random.randint(2,3))
    pencolor(color[random.randint(0,1)])
    radius=random.randint(8,30)
    fillcolor('yellow')
    begin_fill()
    for i in range(6):
        circle(radius)
        left(60)
    end_fill()
mainloop()