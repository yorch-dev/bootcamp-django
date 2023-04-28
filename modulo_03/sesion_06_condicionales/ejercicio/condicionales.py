# se busca indicar si un número es positivo, cero o negativo y, si es par o impar

import numbers

def par_impar(num):
    return 'par' if num % 2 == 0 else 'impar'

def neg_cero_pos(num):
    if num > 0:
        return 'positivo'
    elif num < 0:
        return 'negativo'
    else:
        return 'cero'
    

def pos_cero_neg_par_impar(num):
    if isinstance(num, numbers.Integral):
        if neg_cero_pos(num) == 'cero':
            return 'El número es cero'
        else:
            return f'{num} es {neg_cero_pos(num)} y es {par_impar(num)}'
    else:
        return f'Ingresar sólo números enteros. Valor ingresado: {type(num)} : {num}'

print(pos_cero_neg_par_impar('a'))
print(pos_cero_neg_par_impar('0'))
print(pos_cero_neg_par_impar(0))
print(pos_cero_neg_par_impar('-1'))
print(pos_cero_neg_par_impar(-1))
print(pos_cero_neg_par_impar(1))
print(pos_cero_neg_par_impar(-4))
print(pos_cero_neg_par_impar(4))
print(pos_cero_neg_par_impar(-7))
print(pos_cero_neg_par_impar(7))
