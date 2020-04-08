#Práctica Threading por Daryl Mendoza
import random
import datetime 
import threading
from time import sleep #Se mantienen las 3 bibliotecas del juego ejemplo, añadiendo el método sleep de la clase time para pausar la funcion timenow

def timenow(): #Funcion que se ejecutará en un thread, imprime un string con la fecha y hora del servidor, se pausa por 60 segundos y repite.
    while True:
        x = str(datetime.datetime.now())
        print("La fecha y hora del servidor es: " + x)
        sleep(60)

def game(): #El juego se convierte en una función para ejecutarse en otro thread.
    intentosRealizados = 0
    print('Hola! Como te llamas? ')
    miNombre = input()  
    numero = random.randint(1, 20)
    print('Bueno, ' + miNombre + ', estoy pensando en un numero entre 1 y 20.')
    while intentosRealizados < 6:
        print('Intenta adivinar.')
        estimacion = input()
        estimacion = int(estimacion)

        intentosRealizados = intentosRealizados + 1
        
        if estimacion < numero:
            print('Tu estimacion es muy baja.')

        if estimacion > numero:
            print('Tu estimacion es muy alta.')

        if estimacion == numero:
            break

    if estimacion == numero:
        intentosRealizados = str(intentosRealizados)
        print('Buen trabajo, ' + miNombre + '! Has adivinado mi numero en ' + intentosRealizados + ' intentos!')

    if estimacion != numero:
        numero = str(numero)
        print('Pues no. El numero que estaba pensando era ' + numero)

t = threading.Thread(target=timenow)
g = threading.Thread(target=game) #Se instancia dos veces la clase threading creando dos objetos de tipo Thread.

t.start()
g.start() #Se inicializan los dos threads a fin de ejecutarse en threading.

#Se inicializa el programa, se imprime la fecha y ahora esperaremos un par de minutos para observar que efectivamente se trabaja en threading
#Mientras se ejecuta la función timenow es posible continuar con la función game.