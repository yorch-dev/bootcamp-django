
# Lista original
mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]


print("Ordenando Listas\n")

# Quito duplicados convirtiendo en set
mi_set = set(mi_lista)
# Asigno mi_set a una nueva lista
lista_a_ordenar = list(mi_set)
# Ordeno la lista, luego la imprimo
lista_a_ordenar.sort()
print("Casting set/list y método sort: ", lista_a_ordenar)


# Lo siguiente es hacer uso de algoritmo para ordenar, creado en sesión 6
def ordenar_lista(lista):
    """
        Ordena una lista de menor a mayor.
        Disminuye el ciclo for a los valores hasta el último index cambiado
    """
    lista_ordenada = lista.copy()
    index_ultimo_cambio = len(lista_ordenada) - 1
    hay_cambio = True
    while hay_cambio:
        hay_cambio = False
        for index in range(index_ultimo_cambio):
            if lista_ordenada[index] > lista_ordenada[index + 1]:
                lista_ordenada[index], lista_ordenada[index + 1] = (lista_ordenada[index + 1], lista_ordenada[index])
                index_ultimo_cambio = index
                hay_cambio = True
    return lista_ordenada

mi_set_2 = set(mi_lista)
lista_a_ordenar_2 = list(mi_set_2)
print("Ordenada con función: ", ordenar_lista(lista_a_ordenar_2))


print("Mi lista original", mi_lista)