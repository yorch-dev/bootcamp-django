from clase_vehiculo import Vehiculo
from clase_automovil import Automovil
from clase_auto_carga import AutoCarga
from clase_auto_particular import AutoParticular
from clase_bicicleta import Bicicleta
from clase_motocicleta import Motocicleta
from errores import EnteroPositivoError
from leer_vehiculos import recuperar
import numbers


mensaje_error = 'Ingresar sólo números enteros mayores a cero'
continuar = True

while continuar:
    vehiculos = input('¿Cuántos vehículos desea insertar?: ')
    try:
        vehiculos = int(vehiculos)
        if isinstance(vehiculos, numbers.Integral) and vehiculos >= 0:
            continuar = False
        else:
            raise EnteroPositivoError(mensaje_error)
    except EnteroPositivoError as error:
        print(error)
    except ValueError:
        print(EnteroPositivoError(mensaje_error))


lista_vehiculos = []
for i in range(vehiculos):
    marca = input('\nInserte la marca del automóvil: ')
    modelo = input('Inserte el modelo: ')
    n_ruedas = input('Inserte el número de ruedas: ')
    velocidad = input('Inserte la velocidad en km/h: ')
    cilindrada = input('Inserte el cilindraje en cc: ')
    auto = Automovil(marca, modelo, n_ruedas, velocidad, cilindrada)
    lista_vehiculos.append(auto)


particular = AutoParticular("Ford", "Fiesta", 4, "180", "500", 5)
carga = AutoCarga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "DobleViga", 21)

lista_vehiculos += [particular, carga, bicicleta, motocicleta]

print('\nImprimiendo por pantalla los vehículos: \n')
for idx, vehiculo in enumerate(lista_vehiculos):
    print(f'Datos del vehículo {idx + 1}', end=': ')
    print(vehiculo)


a_relacionar = [Vehiculo, Automovil, AutoParticular, AutoCarga, Bicicleta, Motocicleta]
print()
for vehiculo in a_relacionar:
    print(f'Motocicleta es instancia en relación con {vehiculo.__name__}: {isinstance(motocicleta, vehiculo)}')


for vehiculo in lista_vehiculos:
    vehiculo.guardar('vehiculos.csv')


vehiculos_guardados = recuperar('vehiculos.csv')

lista_particulares = []
lista_cargas = []
lista_bicicletas = []
lista_motocicletas = []

for vehiculo in vehiculos_guardados:
    clase = vehiculo[0].split('.')[1][:-2]
    if clase == 'AutoParticular':
        lista_particulares.append(vehiculo)
    if clase == 'AutoCarga':
        lista_cargas.append(vehiculo)
    if clase == 'Bicicleta':
        lista_bicicletas.append(vehiculo)
    if clase == 'Motocicleta':
        lista_motocicletas.append(vehiculo)


print('\nLista de Vehículos Particular:')
for vehiculo in lista_particulares:
    print(vehiculo)
print('\nLista de Vehículos Carga:')
for vehiculo in lista_cargas:
    print(vehiculo)
print('\nLista de Vehículos Bicicleta:')
for vehiculo in lista_bicicletas:
    print(vehiculo)
print('\nLista de Vehículos Motocicleta:')
for vehiculo in lista_motocicletas:
    print(vehiculo)