# Ejercicio 1 
numeros = 10, 20, 30, 40
print(f'Segundo: {numeros[1]}\nMin: {min(numeros)}\nMax: {max(numeros)}')

# Ejercicio 2 
nombre = input('Digite su nombre: ')
veces = int(input('Digite un numero: '))
print((nombre + '\n') * veces)

# Ejercicio 3
x = input('Digite el nombre: ')
print(f'{x.lower()}\n{x.upper()}\n{x.title()}')

# Ejercicio 4
num_list = [1, 2, 3, 4]
def sum_custom(n, t):
    for s in n: t += s
    return t

def mul_custom(n, t): 
    for s in n: t *= s
    return t

print(f"Suma: {sum_custom(num_list, 0)}")
print(f"Multiplicación: {mul_custom(num_list, 1)}")

# Ejercicio 5
n = input('Digite su nombre: ')
gen_op = input('Generos:\n1.Hombre\n2.Mujer\nDigite el numero: ')
u_reg = input('Cree su usuario: ')
c_reg = input('Cree su contraseña: ')

if input('Usuario: ') == u_reg and input('Contraseña: ') == c_reg:
    print('Logueo con exito')
    if (gen_op == '1' and n < 'n') or (gen_op == '2' and n < 'm'):
        print('Grupo A')
    else: 
        print('Grupo B')
else:
    print('Usuario no encontrado')