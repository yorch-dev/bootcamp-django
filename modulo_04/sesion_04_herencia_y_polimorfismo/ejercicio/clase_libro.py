# Creo clase Libro sin mayor definición
class Libro:
    pass


# Creo 2 instancias de libro
libro_1 = Libro()
libro_2 = Libro()


# Asigno atributos de instancia con notación de punto
libro_1.autor = 'Dan Brown'
libro_1.titulo = 'Inferno'

libro_2.autor = 'Dan Brown'
libro_2.titulo = 'El Código Da Vinci'
libro_2.ann_de_publicacion = 2003


# Imprimo __dict__
print(libro_1.__dict__)
print(libro_2.__dict__)