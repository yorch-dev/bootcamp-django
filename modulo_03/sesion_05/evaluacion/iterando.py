
# Eliminar vocales

palabra = "paralelepípedo"

lista_eliminar = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]

palabra_filtrada = ''.join(filter(lambda x: not x.lower() in lista_eliminar, palabra))

print(palabra_filtrada)
