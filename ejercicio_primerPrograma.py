#esto es un juego de adivinar numeros 
import random
answer = "si"
while(answer == "si"):
    print("hola. cual es tu nombre?")
    name = input()
    secretNumber = random.randint(1, 20)
    print ("Bueno, " + name + ", estoy pensando en un numero entre 1 y 20")

    for guessesTaken in range(1, 7):
        print("prueba adivinar")
        guess = int(input())

        if guess < secretNumber:
            print("el numero es mas grande.")
        elif guess > secretNumber:
            print("el numero es mas chico .")
        else:
            break #correct guess condition

    if guess == secretNumber:
        print("bien hecho, " + name + " adivinaste mi numero en " + str(guessesTaken) + " intentos")
    else:
        print("no. el numero en el que estaba pensando era " + str(secretNumber))
    print("quieres jugar de vuelta? (si/no)")
    answer = input()
    if answer == "no":
        break
        
