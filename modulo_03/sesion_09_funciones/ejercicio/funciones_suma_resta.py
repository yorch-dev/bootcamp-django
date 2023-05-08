from functools import reduce

def suma_resta(*lista):
    suma = reduce(lambda x, y: x + y, lista)
    resta = reduce(lambda x, y: x - y, lista)
    return (suma, resta)

# Intercambio formas para llamar a la función
# Desde lista
lista = [7, 4, 3]
resultado_suma, resultado_resta = suma_resta(*lista)
print("Llamado desde lista")
print("Resultado suma: ", resultado_suma)
print("Resultado resta: ", resultado_resta)

# De forma directa
resultado_suma, resultado_resta = suma_resta(8, 5, 6)
print("\nLlamado directo")
print("Resultado suma: ", resultado_suma)
print("Resultado resta: ", resultado_resta)