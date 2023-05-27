class RangoSalarioError(Exception):
    def __init__(self, mensaje_error):
        self.mensaje_error = mensaje_error
    def __str__(self):
        return repr(self.mensaje_error)


mensaje_error = 'Salario no está definido en el rango (1000 a 2000)'
continuar = True

edad = input('Ingresa el salario: ')

edad = int(edad)
if edad >=1000 and edad <=2000:
    pass
else:
    raise RangoSalarioError(mensaje_error)
