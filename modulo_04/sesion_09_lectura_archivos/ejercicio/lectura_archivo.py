nuevo_texto = [
    'Este en una nueva línea en el archivo',
    'agregando la segunda línea del archivo',
    'finalizando la línea agregada'
]

with open('informacion.dat', 'a+', encoding='utf-8') as texto:
    for linea in nuevo_texto:
        texto.write(f'{linea}\n')


archivo = open('informacion.dat', 'r', encoding='utf-8')
contenido = archivo.read()
archivo.close()

print(contenido)
