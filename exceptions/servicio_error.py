class ServicioError (Exception):
    def __init__ (self, mensaje, servicio=None):
        super().__init__(mensaje)
        self.servicio = servicio
    def __str__(self):
        if self.servicio is not None:
            return f"[ServicioError] {self.args[0]} -> Servicio: {self.servicio}"
        return f"[ServicioError] {self.args[0]}"
class ServicioNoDisponibleError (ServicioError):
    def __str__(self):
        if self.servicio is not None:
            return f"[ServicioNoDisponibleError] {self.args[0]} -> Servicio: {self.servicio}"
        return f"[ServicioNoDisponibleError] {self.args[0]}"
class ParametroInvalidoError (ServicioError):
    def __str__(self):
        if self.servicio is not None:
            return f"[ParametroInvalidoError] {self.args[0]} -> Servicio: {self.servicio}"
        return f"[ParametroInvalidoError] {self.args[0]}"
class CostoInvalidoError (ServicioError):
    def __str__(self):
        if self.servicio is not None:
            return f"[CostoInvalidoError] {self.args[0]} -> Servicio: {self.servicio}"
        return f"[CostoInvalidoError] {self.args[0]}"