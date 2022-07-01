from turtle import *

speed('slowest')
bgcolor('black')
pencolor('yellow')

for i in range(50):
    forward(i)
    left(90)
    dot(i)

mainloop()