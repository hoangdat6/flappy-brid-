from turtle import Turtle ,Screen
import time

t = Turtle()
sc = Screen()
t.pencolor("blue")
t.speed(0)
sc.bgcolor("black")
count = 0
while count <= 200:
    t.right(count)
    t.forward(count * 2)
    count+=1

time.sleep(4)
