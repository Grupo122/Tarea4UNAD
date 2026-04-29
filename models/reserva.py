"""
reserva.py

Define la clase Reserva que conecta Cliente y Servicio.
"""

import logging

from exceptions.reserva_error import (
    ReservaError,
    ReservaCanceladaError,
    ReservaInvalidaError,
    DuracionInvalidaError
)


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self._validar_cliente(cliente)
        self._validar_servicio(servicio)
        self._validar_duracion(duracion)

        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "pendiente"

    # =========================
    # VALIDACIONES
    # =========================

    def _validar_cliente(self, cliente):
        if cliente is None:
            raise ReservaInvalidaError("Cliente inválido")

    def _validar_servicio(self, servicio):
        if servicio is None:
            raise ReservaInvalidaError("Servicio inválido")

    def _validar_duracion(self, duracion):
        if not isinstance(duracion, (int, float)):
            raise DuracionInvalidaError("Duración debe ser numérica")

        if duracion <= 0:
            raise DuracionInvalidaError("Duración inválida")

    # =========================
    # GETTERS
    # =========================

    def get_cliente(self):
        return self._cliente

    def get_servicio(self):
        return self._servicio

    def get_duracion(self):
        return self._duracion

    def get_estado(self):
        return self._estado

    # =========================
    # LÓGICA
    # =========================

    def confirmar(self):
        if self._estado == "cancelada":
            raise ReservaCanceladaError("No se puede confirmar una reserva cancelada")

        self._estado = "confirmada"

    def cancelar(self):
        if self._estado == "cancelada":
            raise ReservaCanceladaError("La reserva ya está cancelada")

        self._estado = "cancelada"

    def procesar(self):
        if self._estado != "confirmada":
            raise ReservaInvalidaError("Debe estar confirmada")

        try:
            costo = self._servicio.calcular_costo(self._duracion)

            if costo <= 0:
                raise ReservaError("Costo inválido")

            return costo

        except Exception as e:
            logging.error(e)
            raise ReservaError("Error procesando reserva") from e

    # =========================
    # MÉTODOS ESPECIALES
    # =========================

    def __eq__(self, other):
        return (
            isinstance(other, Reserva) and
            self._cliente == other._cliente and
            self._servicio == other._servicio and
            self._duracion == other._duracion
        )

    def __hash__(self):
        return hash((self._cliente, self._servicio, self._duracion))

    def __str__(self):
        return f"Reserva({self._cliente}, {self._servicio}, {self._duracion}, {self._estado})"
