dicc = {
    'LOL': 'una respuesta a algo gracioso',
    'CRINGE': 'algo raro o embarazoso',
    'ROFL': 'una respuesta a una broma',
    'SHEESH': 'ligera desaprobación',
    'CREEPY': 'aterrador, siniestro',
    'AGGRO': 'ponerse agresivo/enojado',
    'LMAO': 'riendo a carcajadas',
    'EPIC': 'algo grandioso o impresionante',
    'YOLO': 'solo se vive una vez',
    'SWAG': 'actitud elegante y segura',
    'HYPE': 'excitación o anticipación intensa',
    'FOMO': 'miedo a perderse algo'
}

print("Palabras en el diccionario:")
for palabra in dicc.keys():print(palabra)
palabra_seleccionada = input('\nIntroduzca la palabra que desea entender del diccionario: ').strip().upper()
if palabra_seleccionada in dicc:print(f'El significado de {palabra_seleccionada} es {dicc[palabra_seleccionada]}')
else:print(f'La palabra {palabra_seleccionada} no fue encontrada en el diccionario.')
