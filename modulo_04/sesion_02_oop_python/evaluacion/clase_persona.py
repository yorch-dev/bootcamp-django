class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Apellidos: {self.apellidos}, Sexo: {self.sexo}, Edad: {self.edad}, Estatura: {self.estatura}, Peso: {self.peso}'

    def get_nombre(self):
        return self.nombre
    def get_apellidos(self):
        return self.apellidos
    def get_sexo(self):
        return self.sexo
    def get_edad(self):
        return self.edad
    def get_estatura(self):
        return self.estatura
    def get_peso(self):
        return self.peso
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_apellidos(self, apellidos):
        self.apellidos = apellidos
    def set_sexo(self, sexo):
        self.sexo = sexo
    def set_edad(self, edad):
        self.edad = edad
    def set_estatura(self, estatura):
        self.estatura = estatura
    def set_peso(self, peso):
        self.peso = peso


persona_1 = Persona('Pedro', 'Vivas', 'Masculino', '20 años', '1.78 mts', '68 Kg')
persona_2 = Persona('Juan', 'Camargo', 'Masculino', '18', '1.8 mts', '75 Kg')

print(f"Persona 1, estado inicial:\n{persona_1}")
print(f"\nPersona 2, estado inicial:\n{persona_2}")

persona_1.set_edad('21 años')
persona_2.set_apellidos('Santiago')

print(f"\nPersona 1, después de cambio:\n{persona_1}")
print(f"\nPersona 2, después de cambio:\n{persona_2}")