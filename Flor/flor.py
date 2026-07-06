import turtle
import math

PALETA_PETALOS = ["#FFD700", "#FFC300", "#FFEA00", "#FFB703", "#FFEE32", "#F4D35E"]

def configurar_lienzo():
    pantalla = turtle.Screen()
    pantalla.setup(width=2000, height=1050)
    pantalla.screensize(700, 800, bg="black")
    pantalla.bgcolor("black")
    pantalla.title("Una Flor para Ti")
    turtle.speed(6)
    turtle.hideturtle()
    return pantalla

def dibujar_petalos():
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()

    for i in range(70):
        color = PALETA_PETALOS[i % len(PALETA_PETALOS)]
        turtle.color(color, color)

        tamaño = max(20, 130 - i * 0.85)
        angulo = 90 - i * 0.32

        turtle.begin_fill()
        for _ in range(2):
            turtle.circle(tamaño, angulo)
            turtle.left(180 - angulo)
        turtle.end_fill()

        turtle.right(14 + i * 0.18)
        turtle.forward(2.6)

def dibujar_centro():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

def dibujar_tallo():
    turtle.penup()
    turtle.goto(0, -170)
    turtle.pendown()
    turtle.setheading(270)
    turtle.color("#2E8B57")
    turtle.pensize(15)
    turtle.forward(150)

    turtle.penup()
    turtle.goto(-15, -230)
    turtle.setheading(160)
    turtle.pendown()
    turtle.pensize(8)
    turtle.forward(45)

def escribir_mensaje():
    turtle.penup()
    turtle.goto(0, 350)
    turtle.color("#FFD700")
    turtle.write(" Una Flor para Ti ", align="center", font=("Arial", 26, "bold"))

    turtle.goto(0, 310)
    turtle.color("#FFF3B0")
    turtle.write("By She Codes MX ", align="center", font=("Arial", 15, "italic"))

def main():
    pantalla = configurar_lienzo()
    dibujar_petalos()
    dibujar_centro()
    dibujar_tallo()
    escribir_mensaje()
    turtle.update()
    pantalla.exitonclick()

if __name__ == "__main__":
    main()