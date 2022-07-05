from turtle import *

color=['red','yellow']
pencolor('blue')
pensize(4)
for i in range(8,0,-1):
    penup()
    setpos(0,-20*i)
    pendown()
    fillcolor(color[i%2])
    begin_fill()
    circle(20*i)
    end_fill()

mainloop()