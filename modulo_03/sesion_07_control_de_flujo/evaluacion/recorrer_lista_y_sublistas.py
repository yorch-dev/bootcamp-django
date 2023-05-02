
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