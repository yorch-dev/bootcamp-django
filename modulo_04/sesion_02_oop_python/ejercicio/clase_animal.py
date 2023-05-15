class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nRaza: {self.raza}\nPeso: {self.peso}"


datos_caballo = {
    'nombre': 'Zeus',
    'edad': '5 años',
    'raza': 'Pura sangre',
    'peso': '450 kg'
}

datos_leon = {
    'nombre': 'Boulder',
    'edad': '10 años',
    'raza': 'Atlas',
    'peso': '130 kg'
}


caballo = Animal(datos_caballo['nombre'], datos_caballo['raza'], datos_caballo['edad'], datos_caballo['peso'])
leon = Animal(datos_leon['nombre'], datos_leon['raza'], datos_leon['edad'], datos_leon['peso'])


print("Imprimiendo el caballo")
print(caballo)
print("\nImprimiendo el leon")
print(leon)