import random

def ordenar_lista(lista):
    """
        Ordena una lista de mayor a menor.
        Disminuye el ciclo for a los valores hasta el último index cambiado
    """
    lista_ordenada = lista.copy()
    index_ultimo_cambio = len(lista_ordenada) - 1
    hay_cambio = True
    while hay_cambio:
        hay_cambio = False
        for index in range(index_ultimo_cambio):
            if lista_ordenada[index] < lista_ordenada[index + 1]:
                lista_ordenada[index], lista_ordenada[index + 1] = (lista_ordenada[index + 1], lista_ordenada[index])
                index_ultimo_cambio = index
                hay_cambio = True
    return lista_ordenada

largo_lista_a_ordenar = 3

lista_a_ordenar = [random.randint(1, 1000) for _ in range(largo_lista_a_ordenar)]
lista_ordenada = ordenar_lista(lista_a_ordenar)

print(f'Lista a ordenar:\n{lista_a_ordenar}\n')
print(f'Lista ordenada:\n{lista_ordenada}\n')
