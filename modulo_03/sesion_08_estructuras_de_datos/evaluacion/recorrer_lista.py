lista = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]


for i in lista:
    if isinstance(i, list):
        for index, j in enumerate(i):
            if index == 0 and j == 0:
                print()
                break
            if j == 0:
                if index == len(i) - 1:
                    print()
                else: continue
            elif index == len(i) - 1:
                print(j)
            else: print(j, end=" ")

print()

# Creando diccionario con las sublistas
mi_dict = {}
grupos = ['A', 'B', 'C', 'D']

for index, item in enumerate(lista):
    mi_dict[grupos[index]] = item

for clave, valor in mi_dict.items():
    print(f"{clave}: {valor}")