from clase_bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    
    def __init__(self, marca, modelo, n_ruedas, tipo, motor, cuadro, nro_radio):
        super().__init__(marca, modelo, n_ruedas, tipo)
        self.nro_radio = nro_radio
        self.cuadro = cuadro
        self.motor = motor
    
    def __str__(self) -> str:
        return super().__str__() + f', Nro Radio {self.nro_radio}, Cuadro {self.cuadro}, Motor {self.motor}'

    def get_nro_radio(self):
        return self.nro_radio
    def get_cuadro(self):
        return self.cuadro
    def get_motor(self):
        return self.motor
    
    def set_nro_radio(self, nro_radio):
        self.nro_radio = nro_radio
    def set_cuadro(self, cuadro):
        self.cuadro = cuadro
    def set_motor(self, motor):
        self.motor = motor