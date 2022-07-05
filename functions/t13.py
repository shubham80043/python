from turtle import *

pencolor('blue')
pensize(3)
fillcolor('yellow')
speed('fastest')
for i in range(12,0,-1):
    begin_fill()
    circle(i*10)
    lt(25)
    end_fill()

mainloop()