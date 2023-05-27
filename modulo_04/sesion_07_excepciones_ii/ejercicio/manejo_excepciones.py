import numbers

class EsNumeroError(Exception):
    def __init__(self, mensaje_error):
        self.mensaje_error = mensaje_error
    def __str__(self):
        return repr(self.mensaje_error)


mensaje_error = 'Sólo números enteros mayores a cero'
continuar = True

while continuar:
    edad = input('Ingresa tu edad: ')
    try:
        edad = int(edad)
        if isinstance(edad, numbers.Integral) and edad >= 18:
            print('Es adulto')
            continuar = False
        elif isinstance(edad, numbers.Integral) and edad > 0:
            print('No es un adulto')
            continuar = False
        else:
            raise EsNumeroError(mensaje_error)
    except EsNumeroError as error:
        print(error)
    except ValueError:
        print(EsNumeroError(mensaje_error))
    
