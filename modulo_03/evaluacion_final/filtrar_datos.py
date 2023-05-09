lista_de_nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Magos y científicos
lista_magos = ["Harry Houdini", "David Blaine", "Teller"]
lista_cientificos = ["Newton", "Hawking", "Einstein"]


# función para filtro. Retorna lista sacando los datos incluidos en lista_filtro
def filtrar(lista_a_filtrar, lista_filtro):
    return list(filter(lambda x: x not in lista_filtro, lista_a_filtrar))

# Creo lista_otros y la filtro
lista_otros = lista_de_nombres.copy()
lista_otros = filtrar(lista_otros, lista_magos)
lista_otros = filtrar(lista_otros, lista_cientificos)


# función para hacer "grandioso"
def hacer_grandioso(*args):
    return list(map(lambda x: f"El gran {x}", args))


# función imprimir nombres
def imprimir_nombres(titulo, *args):
    print(f'\n{titulo}')
    for nombre in args:
        print(f'- {nombre}')


# Salida
lista_magos = hacer_grandioso(*lista_magos)
imprimir_nombres('Nombres lista origen:', *lista_de_nombres)
imprimir_nombres('Magos 🧙‍♂️:', *lista_magos)
imprimir_nombres('Científicos 🧪:', *lista_cientificos)
imprimir_nombres('Otros 👥:', *lista_otros)
