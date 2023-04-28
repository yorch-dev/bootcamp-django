
# Eliminar vocales

palabra = "paralelepípedo"
lista_eliminar = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]

# Usando filter
palabra_filtrada = ''.join(filter(lambda x: not x.lower() in lista_eliminar, palabra))
print(palabra_filtrada, '/- usando filter')


# Usando for
palabra_sin_vocales = ""
for letra in palabra:
    if letra.lower() not in lista_eliminar:
        palabra_sin_vocales += letra
print(palabra_sin_vocales, '/- usando for')