"""
sistema.py

Coordina clientes y reservas.
"""

from models.cliente import Cliente, ClienteError
from models.reserva import Reserva

from exceptions.reserva_error import ReservaError


class Sistema:

    def __init__(self):
        self._clientes = []
        self._reservas = set()

    # =========================
    # CLIENTES
    # =========================

    def agregar_cliente(self, cliente: Cliente):
        if not isinstance(cliente, Cliente):
            raise ClienteError("Objeto inválido")

        if cliente in self._clientes:
            raise ClienteError("Cliente duplicado")

        self._clientes.append(cliente)

    def obtener_clientes(self):
        return list(self._clientes)

    # =========================
    # RESERVAS
    # =========================

    def crear_reserva(self, cliente, servicio, duracion):
        nueva = Reserva(cliente, servicio, duracion)

        for r in self._reservas:
            if r == nueva and r.get_estado() != "cancelada":
                raise ReservaError("Reserva duplicada")

        self._reservas.add(nueva)
        return nueva

    def confirmar_reserva(self, reserva):
        if reserva not in self._reservas:
            raise ReservaError("Reserva no existe")

        reserva.confirmar()

    def cancelar_reserva(self, reserva):
        if reserva not in self._reservas:
            raise ReservaError("Reserva no existe")

        reserva.cancelar()

    def procesar_reserva(self, reserva):
        if reserva not in self._reservas:
            raise ReservaError("Reserva no existe")

        return reserva.procesar()

    def obtener_reservas(self):
        return list(self._reservas)

    # =========================
    # UTILIDADES
    # =========================

    def reservas_por_cliente(self, cliente):
        return [r for r in self._reservas if r.get_cliente() == cliente]

    def __str__(self):
        return f"Sistema(Clientes={len(self._clientes)}, Reservas={len(self._reservas)})"
