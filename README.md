# laberinto
es un simple juego que consiste en llegar a una meta establecida, está implementado en python 3.5.

¿Cómo se obtiene el juego?

el juego se obtiene de una forma sencilla, consiste en clonar el repositorio "https://github.com/Rach2520st/laberinto" en un computador que posea python de preferencia la versión 3.5 y activado el entorno virtual y dentro de la carpeta contenedora del archivo "laberinto_pollo" ejecutar "python laberinto_pollo.py"

¿Cuáles son sus prerequisitos?

tener Python 3.5 de preferencia la versión 3.5.6

¿En qué consiste el juego?

este juego consiste en llegar a una meta establecida mediante diversos caminos y que algunos dificultan al jugador en su camino hacia la meta, aumentando la complejidad del juego, cuando el jugador llega a la meta preestablecida se considera ganador.

¿Cuáles son sus controles?

los principales controles de este juego son la flechas del teclado y cuando el jugador gana los controles pasan a ser 1 y 2 junto con enter

Sobre el código:

se podría decir que es un código bastante simple, contiene tres funciones, una que se encarga de la introducción al juego denominada "intro_al_juego", otra que se podría asignar como la función principal debido al hecho de que es contenedera de diferente funciones que permiten la impresión del laberinto, el movimiento del jugador, la colisión ocurrente entre el jugador y el muro del laberinto, y demás funciones que permiten el desarrollo del juego; esta función se llama "juego", otra de las funciones de este juego es la que permite la generación de un menú que le permite al usuario decidir si quiere o no seguir jugando, esta función se llama "menu".

contiene tres librerías os, time e input_flechas.

el laberinto está dibujado mediante emojis, la impresión ocurre debido a una gran cadena de caracteres en donde se va estableciendo que X es un muro, " " es un camino transitable por el jugador y F es el final o meta del laberinto; para dibujar el jugador se trabaja con coordenadas estableciendo que el jugador comienza en la coordenada (2,0)
para el movimiento del jugador se emplea una librería que permite el uso de las flechas del teclado, cuando se presiona la tecla con la flecha hacia arriba la coordenada y disminuye en uno (si no existe un muro), cuando es presionada la tecla con la flecha hacia abajo la coordenada y aumenta en uno (si no existe un muro), cuando es presionada la tecla con la flecha hacia la izquierda la coordenada X disminuye(si no existe un muro) y cuando se presiona la tecla con la flecha en dirección hacia la derecha la coordenada x aumenta en uno si no existe un muro.

para revisar si el jugador se topa con un muro es ingresada una función llamada "cuadradito", esta separa el "nivel" y lo convierte en muchos arreglos (la cantidad de filas) para que cuando se este moviendo está función entregue el valor de la posición a la que va a avanzar y según una condicional presente en la función "dibujar" permita que si el caracter contenido allí es diferente a X el jugador se mueva y si es igual a X el jugador se mantenga tal y como estaba.

el menú es una función que permite mediante un while la elección de dos opciones(salir del juego o volvera jugar), para volver a jugar se debe llamar a la función "reiniciar", esta hace que el jugador vuelva a la posición inicial; y luego se vuelve a llamar a la función "juego", para volver a jugar; para salir simplemente se utiliza la función exit que viene incorparada mediante la librería estándar de Python. 
