# Módulo de excepciones personalizadas para las Reservas
# Se usa para manejar errores cuando hay problemas con las reservas del sistema

class ReservaError(Exception):
    """Error general de las reservas del sistema."""

    def __init__(self, mensaje, Reserva=None):
        # Guarda el mensaje en la clase madre Exception
        super().__init__(mensaje)
        # Guarda el ID o nombre de la reserva que causó el error
        self.Reserva = Reserva

    def __str__(self):
        # Si hay una reserva, la muestra junto al mensaje
        if self.Reserva is not None:
            return f"[ReservaError] {self.args[0]} -> Reserva: {self.Reserva}"
        # Si no hay reserva, solo muestra el mensaje
        return f"[ReservaError] {self.args[0]}"


class ReservaInvalidaError(ReservaError):
    """Error cuando los datos de la reserva no son válidos."""

    def __str__(self):
        # Si hay una reserva, la muestra junto al mensaje
        if self.Reserva is not None:
            return f"[ReservaInvalidaError] {self.args[0]} -> Reserva: {self.Reserva}"
        # Si no hay reserva, solo muestra el mensaje
        return f"[ReservaInvalidaError] {self.args[0]}"


class ReservaCanceladaError(ReservaError):
    """Error cuando se intenta operar sobre una reserva que ya fue cancelada."""

    def __str__(self):
        # Si hay una reserva, la muestra junto al mensaje
        if self.Reserva is not None:
            return f"[ReservaCanceladaError] {self.args[0]} -> Reserva: {self.Reserva}"
        # Si no hay reserva, solo muestra el mensaje
        return f"[ReservaCanceladaError] {self.args[0]}"


class DuracionInvalidaError(ReservaError):
    """Error cuando la duración de la reserva es negativa, cero o excesiva."""

    def __str__(self):
        # Si hay una reserva, la muestra junto al mensaje
        if self.Reserva is not None:
            return f"[DuracionInvalidaError] {self.args[0]} -> Reserva: {self.Reserva}"
        # Si no hay reserva, solo muestra el mensaje
        return f"[DuracionInvalidaError] {self.args[0]}"