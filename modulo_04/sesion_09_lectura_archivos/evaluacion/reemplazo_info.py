def reemplazar_texto(texto, reemplazo):
    with open('informacion.dat', 'r+', encoding='utf-8') as archivo:
        contenido = ''
        reemplazos = 0
        for linea in archivo:
            reemplazos += linea.count(texto)
            contenido += linea.replace(texto, reemplazo)
    with open('informacion.dat', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)
    print(f'Se realizaron {reemplazos} reemplazos')


reemplazar_texto('información', 'procesamiento')