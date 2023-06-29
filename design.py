import turtle
color = ['pink','green','red','white','blue','yellow','orange','cyan']
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(17)

for i in range(100):
    t.color(color[i%8])
    t.fd(i*2)
    t.left(33)
    t.width(33)