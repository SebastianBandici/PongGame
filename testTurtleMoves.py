from turtle import *
import turtle
color('blue', 'yellow')
turtle.speed(20)
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()