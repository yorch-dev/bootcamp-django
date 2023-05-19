class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return self.nombre
    
    def movimiento(self):
        return 'caminando'


class Maratonista(Persona):
    def movimiento(self):
        return 'trotando'


class Ciclista(Persona):
    def movimiento(self):
        return 'rodando'


def imprimir_movimiento(objeto):
    if hasattr(objeto, 'movimiento'):
        print(f'{objeto} está {objeto.movimiento()}')
    else:
        print(f'{objeto} no tiene el método movimiento')


persona_1 = Persona('persona')
maratonista_1 = Maratonista('maratonista')
ciclista_1 = Ciclista('ciclista')

listado = [persona_1, maratonista_1, ciclista_1]

for dato in listado:
    imprimir_movimiento(dato)


# Clase sin función imprimir_movimiento
# class Cosa:
#     def __str__(self):
#         return 'cosa'

# cosa = Cosa()
# imprimir_movimiento(cosa)