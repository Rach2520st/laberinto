from input import input as input_flechas
import os
import time

def intro_al_juego():
    print("UN POLLITO HA PERDIDO A SU MADRE")
    print("🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣")
    print("¿Quieres ayudarlo a encontrar a su madre gallina?")
    
    
        

nivel = """
xxxxxxxxxxxxxxxxxxxxxx
x  xxxxxxxxxxxxxxxxxxx
xx xxx x           xxx
xx     x xxxxxxx xxxxx
xx x xxx xxxxxxx xxxxx
xx x      xxxxxx xxxxx
xxxx xxxx x      xx xx
xxxx xxxx x x xx    xx
xxxx xxxx x x xxxxxxxx
xx   xxx  x x x xxxxxx
xxxxxxxxx x x   xxxxxx
xxxx        xxxxxxxxxx
xxxxxx xx xx       xxx
xxx    xx    x x xxxxx
xxx xx xxxxx xxx xxxxx
xxxxxx xxxxx x    xxxx
xxxxxx       x x   xxx
xxxxxx xxxxx   x x xxx
xxxxxx xxxxxxxxx x xxx
xxxxxx xxxxxxxxx x   F
xxxxxxxxxxxxxxxxxxxxxx
"""

pos_jugador_x = 1  # columna en la que se encuentra el jugador al inicio
pos_jugador_y = 2  # columna en la que se encuentra el jugador al inicio
meta_x = 21  #columna en la que se encuentra la gallina(finalización del juego)
meta_y = 20  # fila en la que se encuentra la gallina (finalizaciòn del juego)
contador = 0  #es el contador de movimientos totales del jugador en el juego


def cuadradito(x, y):
    lineas = nivel.split('\n')
    return lineas[y][x]


def dibujar():
    x = 0
    y = 0

    for character in nivel:
        if pos_jugador_x == x and pos_jugador_y == y:
            print("🐥", end="")
            x = x + 1
        elif character == "x":
            print("⬛", end="")
            x = x + 1
        elif character == "F":
            print("🐔", end="")
            x = x + 1
        elif character == " ":
            print("⬜", end="")
            x = x + 1
        elif character == "\n":
            print(" ")
            x = 0
            y = y + 1


def juego():
    global pos_jugador_x
    global pos_jugador_y
    global contador

    while True:
        dibujar()
        #print('el pollito esta en', pos_jugador_x, pos_jugador_y)
        #print('en este lugar hay un', cuadradito(pos_jugador_x, pos_jugador_y))
        tecla = input_flechas()
        if tecla.name == "arrow up":
            # si el cuadradito de arriba NO es una pared
            if cuadradito(pos_jugador_x, pos_jugador_y - 1) != "x":
                # mover al jugador
                pos_jugador_y = pos_jugador_y - 1

                # agregar uno a los movimientos totales
                contador = contador + 1

        elif tecla.name == "arrow down":
            # si el cuadradito de abajo NO es una pared
            if cuadradito(pos_jugador_x, pos_jugador_y + 1) != "x":
                pos_jugador_y = pos_jugador_y + 1  # mover
                contador = contador + 1

        elif tecla.name == "arrow right":
            # si el cuadradito a la derecha NO es una pared
            if cuadradito(pos_jugador_x + 1, pos_jugador_y) != "x":
                pos_jugador_x = pos_jugador_x + 1
                contador = contador + 1

        elif tecla.name == "arrow left":
            # si el cuadradito a la izquierda NO es una pared
            if cuadradito(pos_jugador_x - 1, pos_jugador_y) != "x":
                pos_jugador_x = pos_jugador_x - 1
                contador = contador + 1

        if pos_jugador_x == meta_x and pos_jugador_y == meta_y:
            os.system("clear")
            print("¡El pollito está con su mamá!")
            print("El número de movimientos realizados es:", contador)
            break


def reiniciar():
    global pos_jugador_x
    global pos_jugador_y
    global contador

    pos_jugador_x = 1
    pos_jugador_y = 2
    contador = 0


def menu():
    valido = True
    while valido:
        print("""\n Seleccione la opción que desee realizar:
        1.- volver a jugar :D
        2.- salir :c""")
        opcion = input()

        if opcion == "1":
            reiniciar()
            juego()

        elif opcion == "2":
            exit()

        else:
            print("esa opción no es válida, intentelo de nuevo")
            valido = False

    #el siguiente bloque hace que si la opcion que es ingresada no está en el menú, este
    #se vuelva a mostrar
    if valido is False:
        menu()

intro_al_juego()
time.sleep(3)
juego()
menu()