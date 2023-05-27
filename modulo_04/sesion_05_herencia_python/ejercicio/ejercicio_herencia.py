class A:
    def __init__(self):
        print("Pertenezco a la clase A")
    def metodo_a(self):
        print("Método heredado de A")

class B:
    def __init__(self):
        print("Clase B")
    def metodo_b(self):
        print("Método heredado de B")

class C(B, A):
    def metodo_c(self):
        print("Método de clase C")

objeto_clase_c = C()
objeto_clase_c.metodo_a()
objeto_clase_c.metodo_b()
objeto_clase_c.metodo_c()