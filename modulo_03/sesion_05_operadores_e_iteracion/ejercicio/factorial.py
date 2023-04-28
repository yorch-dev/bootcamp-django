import numbers

def factorial(x):
    mensaje_error = 'Ingresar sólo enteros >= 1'
    if isinstance(x, numbers.Integral):
        if x > 1:
            return x * factorial(x-1)
        elif x == 1:
            return 1
        else:
            return mensaje_error
    else:
        return mensaje_error


n_buscado = 4
print(f'El factorial de {n_buscado} es {factorial(n_buscado)}')

# Pruebas

# print(f'Factorial de "a" = {factorial("a")}')
# print(f'Factorial de -2 = {factorial(-2)}')
# print(f'Factorial de 0 = {factorial(0)}')
# print(f'Factorial de 1 = {factorial(1)}')
# print(f'Factorial de 2 = {factorial(2)}')
# print(f'Factorial de 3 = {factorial(3)}')
# print(f'Factorial de 4 = {factorial(4)}')
# print(f'Factorial de 5 = {factorial(5)}')
# print(f'Factorial de 6 = {factorial(6)}')