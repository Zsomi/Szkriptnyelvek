import turtle
import random

def dobas():
    t.clear()
    t.pensize(5)
    t.pencolor("blue")
    # Négyzet
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    # Üres Ciklus Számláló
    for _ in range(4):
        t.forward(100)
        t.left(90)

    # Véletlenszerű
    dobas = random.randint(1, 6)
    print(dobas)

    # Pontok Rajzolása
    t.penup()
    if dobas in [1, 3, 5]:
        t.goto(0, 0)
        t.dot(15)
    if dobas in [2, 3, 4, 5, 6]:
        t.goto(-25, 25)
        t.dot(15)
        t.goto(25, -25)
        t.dot(15)
    if dobas in [4, 5, 6]:
        t.goto(-25, -25)
        t.dot(15)
        t.goto(25, 25)
        t.dot(15)
    if dobas == 6:
        t.goto(-25, 0)
        t.dot(15)
        t.goto(25, 0)
        t.dot(15)


ablak = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.onkey(dobas, "d")
turtle.onkey(turtle.bye, "Escape")
turtle.listen()
ablak.mainloop()