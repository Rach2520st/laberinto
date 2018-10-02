"""laberinto"""

import turtle
import os
pantalla = turtle.Screen()
pantalla.bgcolor("white")
pantalla.title("El Grandioso laberinto")
pantalla.setup(700, 700)
"""el bucle anterior esta diciendole que color de pantalla quiere cual es su título y de que tamaño quiere que sea la pantalla"""

cont = 0

class Dibujar():
    def _iniciar_(self):
        turtle._iniciar_(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

"""el próximo bloque tiene la función de definir e integrar el jugador al juego como un objeto"""
class Jugador():
    def __iniciar__(self):
        turtle.turtle._iniciar_(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

    cont = 0
    """las proximos cuatro bucles son para brindar movimiento al jugador"""

    def posicionar(self, x, y):
        turtle.goto(x, y)

    def ir_arriba(self):
        mover_x = jugador.xcor()
        mover_y = jugador.ycor() + 24
        """funcion que permite detener al jugador si hay un muro"""
        if(mover_x, mover_y) not in muros:
            turtle.goto(mover_x, mover_y)
            """self.goto(self.xcor(),self.ycor() - 24)"""
            self.cont = self.cont + 1

    def ir_abajo(self):
        mover_x = jugador.xcor()
        mover_y = jugador.ycor() - 24
        if(mover_x, mover_y) not in muros:
            self.goto(mover_x, mover_y)
            """self.goto(self.xcor(),self.ycor() + 24)"""
            self.cont = self.cont + 1

    def ir_a_la_izqu(self):
        mover_x = jugador.xcor() - 24
        mover_y = jugador.ycor()
        if(mover_x, mover_y) not in muros:
            self.goto(mover_x, mover_y)
            """self.goto(self.xcor() - 20, self.ycor())"""
            self.cont = self.cont + 1

    def ir_a_la_der(self):
        mover_x = jugador.xcor() + 24
        mover_y = jugador.ycor()
        if(mover_x, mover_y) not in muros:
            self.goto(mover_x, mover_y)
            self.cont = self.cont + 1
            """self.goto(self.xcor() + 20, self.ycor())"""


"""crear niveles"""
niveles = []

"""crear nivel 1"""
nivel_1 = """
xxP xxxxxxxxxxxxxxxxxxxx
xxx xxx x           xxxx
xxx     x xxxxxxx xxxxxx
xxx x xxx xxxxxxx xxxxxx
xxx x      xxxxxx xxxxxx
xxxxx xxxx x      xx xxx
xxxxx xxxx x x xx    xxx
xxxxx xxxx x x xxxxxxxxx
xxx   xxx  x x x xxxxxxx
xxxxxxxxxx x x   xxxxxxx
xxxxx        xxxxxxxxxxx
xxxxxxx xx xx       xxxx
xxxx    xx    x x xxxxxx
xxxx xx xxxxx xxx xxxxxx
xxxxxxx xxxxx x    xxxxxx
xxxxxxx       x x   xxxx
xxxxxxx xxxxx   x x xxxx
xxxxxxx xxxxxxxxx x xxxx
xxxxxxx xxxxxxxxx x   F
xxxxxxxxxxxxxxxxxxxxxxxx
"""
"""el agregar una "P" al laberinto indica en que posición inicia el jugador"""
"""agrega el nivel_1 a la lista de niveles"""
niveles.append(nivel_1)
Cont = 0


def configuracion_lab(niveles):
    final = (0, 0)
    for x in range(len(niveles)):
        for y in range(len(niveles[x])):
            """x & y se denominan coordenadas dentro del laberinto"""
            character = niveles[x][y]
            pantalla_x = -288 + (x * 24)
            pantalla_y = 288 - (y * 24)
            """establece que x es un muro del laberinto"""
            if character == "x":
                turtle.goto(pantalla_x, pantalla_y)
                turtle.stamp()
                muros.append((pantalla_x, pantalla_y))
                """agrega las coordenadas de los muros"""
            if character == "P":
                jugador.posicionar(pantalla_x, pantalla_y)
            if character == "F":
                """ultima coordenada""" 
                final = (pantalla_x, pantalla_y)


            os.system("clear")
            print("""~FELICIDADES AVENTURERO~
                          ¡HAZ GANADO!""")
            print("tu número de movimientos realizados es:")
            print(Cont)


dibujar = Dibujar()
jugador = Jugador()

muros = []
"""llamar a la función para que configure el nivel_1"""
configuracion_lab(niveles[0])

"""este es el enlace de teclado, permite que
el jugador se mueva presionando el teclado del computador llamando
a la librería tortuga"""
pantalla.listen()
pantalla.onkey(jugador.ir_a_la_izqu, "Left")
pantalla.onkey(jugador.ir_a_la_der, "Right")
pantalla.onkey(jugador.ir_abajo, "Down")
pantalla.onkey(jugador.ir_arriba, "Up")
pantalla.exitonclick()
