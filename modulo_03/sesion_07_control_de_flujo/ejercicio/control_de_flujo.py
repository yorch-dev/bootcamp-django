
"""
    Crear lista con 10 enteros, recorrerla con for, imprimir valor e indicar si es par, impar o cero
"""

import random

lista = random.sample(range(0, 20), 10)
lista.sort()

def par_cero_impar(num):
    if num == 0:
        return "cero"
    if num % 2 == 0:
        return "par"
    return "impar"

print(lista)
for num in lista:
    print(f"{num} es {par_cero_impar(num)}")
