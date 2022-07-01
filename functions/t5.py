from turtle import *

speed('slowest')
pencolor('violet')
sides=15
for i in range(16): #we can put range in n+1 or simple side
    forward(75)
    left(360/sides)
    dot(16)

mainloop()