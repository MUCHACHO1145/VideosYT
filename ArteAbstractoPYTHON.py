import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)  

def random_color():
    return random.choice(["red", "green", "blue", "yellow", "purple", "orange", "cyan", "magenta"])

def draw_circle():
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))  
    t.pendown()
    t.color(random_color())  
    t.begin_fill()
    t.circle(random.randint(20, 100))  
    t.end_fill()

def draw_lines():
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))  
    t.pendown()
    t.color(random_color())  
    for _ in range(10):
        t.forward(random.randint(50, 150))  
        t.left(random.randint(30, 180))  

def draw_shapes():
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))  
    t.pendown()
    sides = random.randint(3, 10)  
    angle = 360 / sides
    t.color(random_color()) 
    for _ in range(sides):
        t.forward(random.randint(50, 150))  
        t.left(angle)

for _ in range(10):
    draw_circle()
    draw_lines()
    draw_shapes()

# Finalizar
t.hideturtle()
turtle.done()
