class ReservaError (Exception):
    def __init__ (self, mensaje, Reserva =None):
        super().__init__(mensaje)
        self.Reserva = Reserva
    def __str__(self):
        if self.Reserva is not None:
            return f"[ReservaError] {self.args[0]} -> Reserva: {self.Reserva}"
        return f"[ReservaError] {self.args[0]}"
class ReservaInvalidaError (ReservaError):
    def __str__(self):
        if self.Reserva is not None:
            return f"[ReservaInvalidaError] {self.args[0]} -> Reserva: {self.Reserva}"
        return f"[ReservaInvalidaError] {self.args[0]}"
class ReservaCanceladaError (ReservaError):
    def __str__(self):
        if self.Reserva is not None:
            return f"[ReservaCanceladaError] {self.args[0]} -> Reserva: {self.Reserva}"
        return f"[ReservaCanceladaError] {self.args[0]}"
class DuracionInvalidaError (ReservaError):
    def __str__(self):
        if self.Reserva is not None:
            return f"[DuracionInvalidaError] {self.args[0]} -> Reserva: {self.Reserva}"
        return f"[DuracionInvalidaError] {self.args[0]}"