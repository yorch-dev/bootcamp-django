from clase_vehiculo import Vehiculo

class Automovil(Vehiculo):

    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, n_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self) -> str:
        return super().__str__() + f', Velocidad {self.velocidad} Km/h, Cilindrada {self.cilindrada} cc'
    
    def get_velocidad(self):
        return self.velocidad
    def get_cilindrada(self):
        return self.cilindrada
    
    def set_velocidad(self, velocidad):
        self.velocidad = velocidad
    def set_cilindrada(self, cilindrada):
        self.cilindrada = cilindrada