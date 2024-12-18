import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador

def main(): 
    nombre_jugador = input("Bienvenido al juego de Iván, por favor introducí tu nombre: ")
    jugador = Jugador(nombre_jugador) 

    enemigos = [Enemigo("Alien", 50, 5), Enemigo("Robot", 50, 5), Enemigo("Marley", 60, 4)] 

    print("Comienza el juego")

    while True:
        enemigo_actual = random.choice(enemigos) 
        print(f"Te has encontrado con {enemigo_actual.nombre}")

        while enemigo_actual.salud > 0:
            accion = input("¿Qué deseas hacer? atacar/huir: ").lower() 
            
            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(f"Has atacado a {enemigo_actual.nombre} y le has causado {dano_jugador} puntos de daño") 
                enemigo_actual.recibir_dano(dano_jugador) 

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(f"{enemigo_actual.nombre} te ha atacado y te causó {dano_enemigo} puntos de daño")
                    jugador.recibir_dano(dano_enemigo)
            elif accion == "huir":
                print("¡Eres un cobarde!")
                break

        if jugador.salud <= 0:
            print("Has perdido la partida") 
            break 
        jugador.ganar_experiencia(20) 

        continuar = input("¿Quieres seguir explorando? (s/n): ").lower()
        if continuar != "s":
            print("Gracias por jugar el juego de Iván")
            break 

if __name__ == "__main__":
    main()
