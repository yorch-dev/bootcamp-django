from io import open

def crear_archivo(nombre_archivo, texto = None, modo="x+"):
    try:
        archivo = open(nombre_archivo, modo, encoding='utf-8')
        if texto:
            archivo.write(texto)
        archivo.close()
    except FileExistsError:
        print(f'El archivo "{nombre_archivo}" ya existe, ha sido creado previamente')

nombre_archivo = 'informacion.dat'
contenido = ''

for i in range(5):
    contenido += f'Datos de información en la línea {i + 1}\n'

crear_archivo(nombre_archivo, contenido)

# ***************************
# El archivo se crea según ejercicio anterior y se intenta crear nuevamente para mensaje de error
crear_archivo(nombre_archivo, contenido)

# Se leerá a continuación

def lectura_archivo(ruta):
    try:
        archivo = open(ruta, 'r', encoding='utf-8')
        contenido = archivo.read()
        archivo.close()
        print(contenido)
    except FileNotFoundError:
        print('Archivo no encontrado')
    except Exception as error:
        print('Error no previsto', type(error).__name__)

ruta_archivo = 'informacion.dat'
lectura_archivo(ruta_archivo)