# Verificación de edad
if int(input('Digite la edad: ')) in range(17):
    print('Es menor de edad')
else:
    print('Es mayor de edad')

# Pares e impares con entrada de usuario
limite = int(input('Digite la cantidad de numeros: '))
for numero in range(limite + 1):
    if numero % 2 == 0:
        print(f'El numero {numero} es par')       
    else:
        print(f'El numero {numero} es impar')
        
# Pares e impares con lista definida
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in n:
    tipo = "par" if numero % 2 == 0 else "impar"
    print(f'El numero {numero} es {tipo}')