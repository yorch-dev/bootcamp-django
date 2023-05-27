class EnteroPositivoError(Exception):
    def __init__(self, mensaje_error):
        self.mensaje_error = mensaje_error
    def __str__(self):
        return repr(self.mensaje_error)

class TipoNoValidoError(Exception):
    def __init__(self, mensaje_error):
        self.mensaje_error = mensaje_error
    def __str__(self):
        return repr(self.mensaje_error)