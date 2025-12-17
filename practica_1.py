# Validación de contraseña
x = input('Digite la nueva contraseña: ')
x1 = input('Digite la contraseña: ')
if x.lower() == x1.lower(): 
    print('Contraseña correcta')
else: 
    print('Contraseña incorrecta')

# Rango de números pares/impares
inicio = int(input('Digite el primer numero del rango: '))
fin = int(input('Digite el ultimo numero del rango: '))
for numero in range(inicio, fin + 1): 
    if numero % 2 == 0: 
        print(f'El numero {numero} es par')       
    else: 
        print(f'El numero {numero} es impar')

# Mayoría de edad
if int(input('Digite la edad: ')) in range(17): 
    print('Es menor de edad')
else: 
    print('Es mayor de edad')

# Costo de ingreso por edad
edad = int(input('Digite la edad para calcular costo: '))
if edad in range(7, 17): 
    print('El costo del ingreso sera de 5 dolares')
elif edad < 7: 
    print('El costo del ingreso sera de 0 dolares')
else: 
    print('El costo del ingreso sera de 10 dolares')

# Menú de Pizza
menu = ['1.Pimienta', '2.Hongos', '3.Peperoni', '4.Jamon', '5.Salmon', '6.Tocineta', '7.Res']
print('Menu de productos de Menstofar')
for item in menu: 
    print(item)

y = int(input('Digite el numero del ingrediente que desea en su pizza: ')) - 1
if menu[y] in menu[2:6]: 
    print(f'Su pizza no es vegetariana y lleva los productos: Mozzarella, Tomate y {menu[y][2:]}')
else: 
    print(f'Su pizza es vegetariana y lleva los productos: Mozzarella, Tomate y {menu[y][2:]}')

# Clasificación de grupos
gen = input('Genero:\n1.Hombre\n2.Mujer\nDigite el numero: ')
nom = input('Digite su nombre: ')
if (gen == '1' and nom[0].lower() < 'n') or (gen == '2' and nom[0].lower() < 'm'): 
    print('Eres del grupo A')
else: 
    print('Eres del grupo B')