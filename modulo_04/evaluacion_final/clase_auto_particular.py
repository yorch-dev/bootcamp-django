from clase_automovil import Automovil

class AutoParticular(Automovil):

    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, n_puestos):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.n_puestos = n_puestos
    
    def __str__(self) -> str:
        return super().__str__() + f', Número de puestos {self.n_puestos}'
    
    def get_n_puestos(self):
        return self.n_puestos
    
    def set_n_puestos(self, n_puestos):
        self.n_puestos = n_puestos