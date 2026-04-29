"""
sistema.py

Módulo principal que gestiona clientes y reservas.

Responsabilidades:
- Registrar clientes
- Crear reservas
- Evitar duplicados
- Coordinar la lógica del sistema
"""

from models.cliente import Cliente
from models.reserva import Reserva

from exceptions.reserva_error import ReservaError
from exceptions.cliente_error import ClienteError


class Sistema:
    """
    Clase principal del sistema.

    Gestiona:
    - Clientes
    - Reservas

    Evita duplicados y mantiene consistencia de datos.
    """

    # =========================
    # CONSTRUCTOR
    # =========================

    def __init__(self):
        self._clientes = []
        self._reservas = set()  # 👈 evita duplicados automáticamente

    # =========================
    # CLIENTES
    # =========================

    def agregar_cliente(self, cliente: Cliente):
        """
        Agrega un cliente al sistema.

        :raises ClienteError: si ya existe
        """
        if not isinstance(cliente, Cliente):
            raise ClienteError("El objeto debe ser de tipo Cliente")

        if cliente in self._clientes:
            raise ClienteError("El cliente ya está registrado")

        self._clientes.append(cliente)

    def obtener_clientes(self):
        """Retorna la lista de clientes."""
        return list(self._clientes)

    # =========================
    # RESERVAS
    # =========================

    def crear_reserva(self, cliente: Cliente, servicio, duracion):
        """
        Crea una reserva validando duplicados.

        :return: Reserva
        :raises ReservaError:
        """
        nueva_reserva = Reserva(cliente, servicio, duracion)

        # 🔥 evitar duplicados activos
        for r in self._reservas:
            if (
                r == nueva_reserva and
                r.get_estado() != "cancelada"
            ):
                raise ReservaError("Ya existe una reserva activa igual")

        self._reservas.add(nueva_reserva)
        return nueva_reserva

    def obtener_reservas(self):
        """Retorna todas las reservas."""
        return list(self._reservas)

    def reservas_por_cliente(self, cliente: Cliente):
        """
        Obtiene todas las reservas de un cliente.
        """
        return [r for r in self._reservas if r.get_cliente() == cliente]

    # =========================
    # OPERACIONES SOBRE RESERVAS
    # =========================

    def confirmar_reserva(self, reserva: Reserva):
        """
        Confirma una reserva.
        """
        if reserva not in self._reservas:
            raise ReservaError("La reserva no existe en el sistema")

        reserva.confirmar()

    def cancelar_reserva(self, reserva: Reserva):
        """
        Cancela una reserva.
        """
        if reserva not in self._reservas:
            raise ReservaError("La reserva no existe en el sistema")

        reserva.cancelar()

    def procesar_reserva(self, reserva: Reserva):
        """
        Procesa una reserva y retorna su costo.
        """
        if reserva not in self._reservas:
            raise ReservaError("La reserva no existe en el sistema")

        return reserva.procesar()

    # =========================
    # MÉTODOS AUXILIARES
    # =========================

    def existe_reserva(self, reserva: Reserva) -> bool:
        """
        Verifica si una reserva existe en el sistema.
        """
        return reserva in self._reservas

    def eliminar_reserva(self, reserva: Reserva):
        """
        Elimina una reserva del sistema.
        """
        if reserva not in self._reservas:
            raise ReservaError("La reserva no existe")

        self._reservas.remove(reserva)

    # =========================
    # REPRESENTACIÓN
    # =========================

    def __str__(self):
        return f"Sistema(Clientes={len(self._clientes)}, Reservas={len(self._reservas)})"
