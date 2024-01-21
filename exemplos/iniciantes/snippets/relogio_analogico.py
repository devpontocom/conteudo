import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Relógio Analógico com Turtle")

# Criar função de desenho
def desenhar_relogio(h, m, s, turtle):
    # Desenhar a hora
    turtle.penup()
    turtle.goto(0, 0)
    turtle.color("white")
    turtle.setheading(90)
    angle = (h / 12) * 360
    turtle.right(angle)
    turtle.pendown()
    turtle.forward(50)

    # Desenhar o minuto
    turtle.penup()
    turtle.goto(0, 0)
    turtle.color("blue")
    turtle.setheading(90)
    angle = (m / 60) * 360
    turtle.right(angle)
    turtle.pendown()
    turtle.forward(80)

    # Desenhar o segundo
    turtle.penup()
    turtle.goto(0, 0)
    turtle.color("red")
    turtle.setheading(90)
    angle = (s / 60) * 360
    turtle.right(angle)
    turtle.pendown()
    turtle.forward(100)

# Criar objeto Turtle
ponteiro = turtle.Turtle()
ponteiro.speed(0)

while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    desenhar_relogio(h, m, s, ponteiro)
    wn.update()
    time.sleep(1)
    ponteiro.clear()

turtle.done()