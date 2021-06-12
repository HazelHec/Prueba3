import random


def palindromo (palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def main ():
    print ("Probando el uso de git para ser un mejor programador a futuro")
    palabra = input("Por favor escribe una palabra  ")
    for i in range (10):
        print(palabra)
    
    #bash moding
    print ("\n\nAdemas descubriremos si tu palabra es un palindromo o no")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Tu plabra es un palindromo")
    else:
        print("No es un palindromo\n\n")


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