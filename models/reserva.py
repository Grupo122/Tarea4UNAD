# Módulo que define la clase Reserva
# Conecta un cliente con un servicio y gestiona su estado

from exceptions.reserva_error import ReservaError, ReservaCanceladaError, ReservaInvalidaError, DuracionInvalidaError

class Reserva:
    """Representa una reserva que conecta un cliente con un servicio."""

    def __init__(self, cliente, servicio, duracion):
        """Constructor de Reserva. Valida los datos antes de crearla."""
        try:
            # verifica que el cliente no sea vacío
            if cliente is None:
                raise ReservaInvalidaError("El cliente no puede estar vacío")
            # verifica que el servicio no sea vacío
            if servicio is None:
                raise ReservaInvalidaError("El servicio no puede estar vacío")
            # verifica que la duración sea mayor a cero
            if duracion <= 0:
                raise DuracionInvalidaError("La duración debe ser mayor a cero", Reserva=duracion)
            
            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "pendiente"  # estado inicial siempre es pendiente

        except ReservaInvalidaError as e:
            print(f"Error al crear reserva: {e}")
        finally:
            print("Proceso de creación de reserva terminado")

    def confirmar(self):
        """Cambia el estado de la reserva a confirmada."""
        try:
            # no se puede confirmar si ya está cancelada
            if self.estado == "cancelada":
                raise ReservaCanceladaError("No se puede confirmar una reserva cancelada", Reserva=self.estado)
            self.estado = "confirmada"
            print(f"Reserva confirmada exitosamente")
        except ReservaCanceladaError as e:
            print(f"Error: {e}")
        except ReservaInvalidaError as e:
            print(f"Error: {e}")
        finally:
            print("Proceso de confirmación terminado")

    def cancelar(self):
        """Cambia el estado de la reserva a cancelada."""
        try:
            # no se puede cancelar si ya está cancelada
            if self.estado == "cancelada":
                raise ReservaCanceladaError("La reserva ya ha sido cancelada previamente", Reserva=self.estado)
            self.estado = "cancelada"
            print(f"Reserva cancelada con éxito")
        except ReservaCanceladaError as e:
            print(f"Error: {e}")
        finally:
            print("Proceso de cancelación terminado")

    def procesar(self):
        """Procesa la reserva y calcula el costo total."""
        try:
            # solo se puede procesar si está confirmada
            if self.estado != "confirmada":
                raise ReservaInvalidaError("La reserva debe estar confirmada para procesarse", Reserva=self.estado)
            # calcula el costo según el servicio y la duración
            costo_total = self.servicio.calcular_costo(self.duracion)
            # verifica que el costo sea válido
            if costo_total <= 0:
                raise ReservaError("El costo calculado no es válido", Reserva=self.estado)
            print(f"Reserva procesada exitosamente")
            print(f"Cliente: {self.cliente}")
            print(f"Servicio: {self.servicio}")
            print(f"Duración: {self.duracion} horas")
            print(f"Costo total: ${costo_total}")
        except ReservaInvalidaError as e:
            print(f"Error: {e}")
        except ReservaError as e:
            print(f"Error: {e}")
        finally:
            print("Proceso de procesamiento terminado")
                