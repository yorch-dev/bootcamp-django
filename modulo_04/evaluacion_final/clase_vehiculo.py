import csv

class Vehiculo:

    def __init__(self, marca, modelo, n_ruedas = 4):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas
    
    def __str__(self) -> str:
        return f'Datos del {self.__class__.__name__}: Marca {self.marca}, Modelo {self.modelo}, Número de ruedas {self.n_ruedas}'
    
    def get_marca(self):
        return self.marca
    def get_modelo(self):
        return self.modelo
    def get_n_ruedas(self):
        return self.n_ruedas
    
    def set_marca(self, marca):
        self.marca = marca
    def set_modelo(self, modelo):
        self.modelo = modelo
    def set_n_ruedas(self, n_ruedas):
        self.n_ruedas = n_ruedas
    
    def guardar(self, nombre_archivo):
        archivo = open(nombre_archivo, "a")
        datos = (self.__class__, self.__dict__)
        archivo_csv = csv.writer(archivo, lineterminator='\n')
        archivo_csv.writerow(datos)
        archivo.close()
