from functools import reduce

# Gestión de helados
helados = {'Vainilla': 1000, 'Chocolate': 1200, 'Mora': 900, 'Coco': 3000}
# Nota: Este bucle es infinito hasta que se cierre el programa
# for x in list(helados): print(x)
# helado = input('Digite un helado de la lista: ') ... (Tu código original continúa aquí)

# Cálculo de múltiplos y temperaturas
x = float(input('Digita el primer numero: '))
c = float(input('Digita el segundo numero: '))
f, t = divmod(x, c)
if t == 0:
    print(f'{x} es multiplo de {c}')  
else:
    f, t = divmod(c, x)
    if t == 0:
        print(f'{c} es multiplo de {x}')  
    else:
        print('No hay ningun multiplo de los dos')

# Máximos y mínimos en lista
c = []
f = int(input('Digite la cantidad de numeros que desea introducir: '))
for _ in range(f):
    m = int(input('Digite el numero: '))
    c.append(m)
print(f'El numero minimo es {min(c)} y el maximo es {max(c)}')

# String reverso
print(input('Digite un texto para invertir:')[::-1]) 

# Reducción (Multiplicación y Suma de lista)
b = int(input('Digite la cantidad de numeros para operar: '))
numeros = []
for i in range(b):
    h = int(input(f'Digite el numero {i+1}: '))
    numeros.append(h)

print(f"Multiplicación total: {reduce(lambda x, y: x * y, numeros)}")
print(f"Suma total: {sum(numeros)}")