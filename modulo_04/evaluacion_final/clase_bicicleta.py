from clase_vehiculo import Vehiculo
from errores import TipoNoValidoError

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, tipo):
        super().__init__(marca, modelo, n_ruedas)
        if tipo in ('Urbana', 'Deportiva', 'Carrera'):
            self.tipo = tipo
        else:
            mensaje_error_tipo = 'Sólo tipo "Urbana", "Deportiva" o "Carrera"'
            raise TipoNoValidoError(mensaje_error_tipo)
    
    def __str__(self) -> str:
        return super().__str__() + f', Tipo {self.tipo}'
    
    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self, tipo):
        self.tipo = tipo
