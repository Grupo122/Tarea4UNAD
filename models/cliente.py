"""
cliente.py

Define la clase Cliente con validaciones, encapsulación
y manejo de excepciones.
"""

import re
import logging


class ClienteError(Exception):
    pass


class Cliente:
    def __init__(self, nombre: str, email: str, identificacion: str):
        self._nombre = None
        self._email = None
        self._identificacion = None

        self.set_nombre(nombre)
        self.set_email(email)
        self.set_identificacion(identificacion)

    # =========================
    # VALIDACIONES
    # =========================

    def _validar_nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ClienteError("Nombre debe ser string")

        if not nombre.strip():
            raise ClienteError("Nombre vacío")

        if any(char.isdigit() for char in nombre):
            raise ClienteError("Nombre no puede tener números")

        if len(nombre.strip()) < 3:
            raise ClienteError("Nombre muy corto")

    def _validar_email(self, email):
        if not isinstance(email, str):
            raise ClienteError("Email debe ser string")

        patron = r"^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

        if not re.match(patron, email.strip()):
            raise ClienteError("Email inválido")

    def _validar_identificacion(self, identificacion):
        if not isinstance(identificacion, str):
            raise ClienteError("Identificación debe ser string")

        if not identificacion.isdigit():
            raise ClienteError("Identificación inválida")

    # =========================
    # SETTERS
    # =========================

    def set_nombre(self, nombre):
        try:
            self._validar_nombre(nombre)
            self._nombre = nombre.strip().title()
        except ClienteError as e:
            logging.error(e)
            raise

    def set_email(self, email):
        try:
            self._validar_email(email)
            self._email = email.strip().lower()
        except ClienteError as e:
            logging.error(e)
            raise

    def set_identificacion(self, identificacion):
        try:
            self._validar_identificacion(identificacion)
            self._identificacion = identificacion
        except ClienteError as e:
            logging.error(e)
            raise

    # =========================
    # GETTERS
    # =========================

    def get_nombre(self):
        return self._nombre

    def get_email(self):
        return self._email

    def get_identificacion(self):
        return self._identificacion

    # =========================
    # UTILIDADES
    # =========================

    def to_dict(self):
        return {
            "nombre": self._nombre,
            "email": self._email,
            "id": self._identificacion
        }

    # =========================
    # MÉTODOS ESPECIALES
    # =========================

    def __str__(self):
        return f"Cliente({self._nombre}, {self._email}, {self._identificacion})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Cliente) and self._identificacion == other._identificacion

    def __hash__(self):
        return hash(self._identificacion)
