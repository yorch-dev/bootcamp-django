from clase_automovil import Automovil

class AutoCarga(Automovil):

    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga
    
    def __str__(self) -> str:
        return super().__str__() + f', Peso carga {self.peso_carga}'
    
    def get_peso_carga(self):
        return self.peso_carga
    
    def set_peso_carga(self, peso_carga):
        self.peso_carga = peso_carga