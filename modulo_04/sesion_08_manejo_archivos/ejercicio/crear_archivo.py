from io import open

def crear_archivo(nombre_archivo, texto = None, modo="x+"):
    try:
        archivo = open(nombre_archivo, modo, encoding='utf-8')
        if texto:
            archivo.write(texto)
        archivo.close()
    except FileExistsError:
        print(f'El archivo "{nombre_archivo}" ya existe')

nombre_archivo = 'informacion.dat'
contenido = ''

for i in range(5):
    contenido += f'Datos de información en la línea {i + 1}\n'


crear_archivo(nombre_archivo, contenido)