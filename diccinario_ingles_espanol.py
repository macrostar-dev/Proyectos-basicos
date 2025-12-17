import random#inporto una funcion de numeros alazar
import time#funcion de tiempo(no se usa)


eng_words = ['Hi','Bye','Task', 'Programm']#Palabras en ingles
sp_words = ['Hola','Adiós','Tarea', 'Programa']#Palabras en espñol
score = 0

mode = input("Elige un modo: 0 - añadir nuevas palabras, 1 - entrenamiento: \n")#Seleccion de un numero para alguna de las dos funciones
while ((mode != '0') and (mode != '1')):#Identifica si el paso solisitado existe, si no eta generara un bucle
    mode = input("Símbolo no válido. Elija 0 o 1. (0 añade nuevas palabras, mientras que 1 permite el entrenamiento) \n")#Esta es la opcion generara por el bucle solo desapacera haasata que una de laas dos opciones sean seleccionaadas 

if mode == "1":# se ejecutara si el numero es 1
    print("¡Traduce tantas palabras como puedas! ¡Tienes 10 intentos!")# Mostra un mensaje en la consola de la cantidad de la cantidaaaad de intentos
    for i in range(10):# es el rango de ejecucion
        number = random.randint(0, len(eng_words)-1)#
        print("Cómo deberíamos traducirlo " + eng_words[number])#mostrara la palabraa seleccionada alazar
        if input() == sp_words[number]:#Edentifica si laa palaaabra fue dijitada correctaamente
            print("¡¡¡Genial!!!")# Mensaje de caaalificacion
            score += 1#puntos obtenidos
        else:#Se ejecuta si fallas
            print("No, no del todo... La palabra correcta es - " + eng_words[number])#mensaje para mencionar que esta mal traducido
else:#
    word = input("Escribe una palabra en español: ")#palabra en espaañol
    translate = input("Escriba la traducción de esta palabra: ")#palabra traducidaa al ingles
    if len(word) > 0 and len(translate) > 0:#que cantidad dde letras sea mayor a 0
        sp_words.append(word)# lo sube al diccionario dde español
        eng_words.append(translate)#lo sube al diccoionario ingles
        print("La palabra se ha añadido correctamente")# mensaje para confirmar que se logro todo correctamente
    #falta el else 