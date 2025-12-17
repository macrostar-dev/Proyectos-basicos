print('!Hola, Mundo¡')

# Funcion LEN
lista1 = [123, 'xyz', 'zara']
print(f"Largo de lista: {len(lista1)}")

str1 = 'baloncento'
print(f"Largo de string: {len(str1)}")

tupla1 = (2, 3, 4, 5)
print(f"Largo de tupla: {len(tupla1)}")

dict1 = {'nombre': 'john', 'edad': 4, 'puntajes': 45}
print(f"Largo de diccionario: {len(dict1)}")

def suma(numeros):
    total = 0
    for n in numeros:
        total += n
    return total

# Ejemplo de uso de la función
resultado = suma([1, 2, 3, 4])
print(f"La suma es: {resultado}")
