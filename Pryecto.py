import random


def main ():
    print ("Probando el uso de git para ser un mejor programador a futuro")
    palabra = input("Por favor escribe una palabra  ")
    for i in range (10):
        print(palabra)

    print("Muy bien ahora vamos a hacer una cosa más")
    contador = 0
    intentos = 0
    numero_random = random.randint(1,100)
    print("Bienvenidos, Bienvenidos, hoy haremos un juego que consiste en que tu usuario adivine un número del 1 al 100")
    numero = int(input ("¿Cuál es el número? "))
    while contador == 0:
        if numero < numero_random:
            print("Aún falta para lograrlo \n")
            intentos += 1
        elif numero > numero_random:
            print("Te exediste \n")
            intentos += 1
        else:
            intentos += 1
            print("Eres muy bueno \nLo lograste en: " + str(intentos))
            contador +=1
        numero = int(input("Intentalo de nuevo: "))



if __name__ == '__main__':
    main()