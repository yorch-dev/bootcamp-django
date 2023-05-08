# Suma
def suma(num_1, num_2):
    resultado = num_1 + num_2
    return resultado


# Resta
def resta(num_1, num_2):
    resultado = num_1 - num_2
    return resultado


# Multiplicación
def multiplica(num_1, num_2):
    resultado = num_1 * num_2
    return resultado


# División
def divide(num_1, num_2):
    resultado = num_1 / num_2
    return resultado


# Operaciones básicas
def operaciones_aritmeticas(num_1, num_2):
    r_suma = suma(num_1, num_2)
    r_resta = resta(num_1, num_2)
    r_multiplica = multiplica(num_1, num_2)
    r_divide = divide(num_1, num_2)
    return (r_suma, r_resta, r_multiplica, r_divide)


# Resultados
num_1 = 4
num_2 = 8
res_suma, res_resta, res_multiplica, res_divide = operaciones_aritmeticas(num_1, num_2)

resultados = {
    'Suma' : res_suma,
    'Resta' : res_resta,
    'Multiplicación' : res_multiplica,
    'División' : res_divide
}

print(f"Cálculo con los números {num_1} y {num_2}:\n{resultados}")
