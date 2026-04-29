"""
cliente.py

Módulo que define la clase Cliente con validaciones robustas,
encapsulación, manejo de excepciones personalizadas y utilidades
para integración dentro del sistema.

Diseñado para ser reutilizable y extensible.
"""

import re
import logging


class ClienteError(Exception):
    """
    Excepción personalizada para errores relacionados con Cliente.

    Ejemplo:
        >>> raise ClienteError("Email inválido")
    """
    pass


class Cliente:
    """
    Representa un cliente del sistema.

    Garantiza la integridad de los datos mediante validaciones estrictas,
    normalización de entrada y manejo de errores.

    :param nombre: Nombre completo del cliente
    :param email: Correo electrónico
    :param identificacion: Identificación única (solo números)
    :raises ClienteError: Si los datos son inválidos

    Ejemplo:
        >>> c = Cliente("Juan Perez", "JUAN@mail.com", "123")
        >>> print(c)
        Cliente: Juan Perez | Email: juan@mail.com | ID: 123
    """

    # =========================
    # CONSTRUCTOR
    # =========================

    def __init__(self, nombre: str, email: str, identificacion: str):
        self._nombre = None
        self._email = None
        self._identificacion = None

        self.set_nombre(nombre)
        self.set_email(email)
        self.set_identificacion(identificacion)

    # =========================
    # VALIDACIONES INTERNAS
    # =========================

    def _validar_nombre(self, nombre: str):
        """
        Valida el nombre del cliente.

        Reglas:
        - No vacío
        - Solo texto
        - Longitud mínima

        :raises ClienteError:
        """
        if not isinstance(nombre, str):
            raise ClienteError("El nombre debe ser un string")

        if not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío")

        if any(char.isdigit() for char in nombre):
            raise ClienteError("El nombre no debe contener números")

        if len(nombre.strip()) < 3:
            raise ClienteError("El nombre es demasiado corto")

    def _validar_email(self, email: str):
        """
        Valida el formato del email.

        :raises ClienteError:
        """
        if not isinstance(email, str):
            raise ClienteError("El email debe ser un string")

        email = email.strip()

        patron = r"^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

        if not re.match(patron, email):
            raise ClienteError(
                "Formato de email inválido. Ejemplo: usuario@dominio.com"
            )

    def _validar_identificacion(self, identificacion: str):
        """
        Valida la identificación.

        :raises ClienteError:
        """
        if not isinstance(identificacion, str):
            raise ClienteError("La identificación debe ser string")

        if not identificacion:
            raise ClienteError("La identificación no puede estar vacía")

        if not identificacion.isdigit():
            raise ClienteError("La identificación debe contener solo números")

    # =========================
    # SETTERS (encapsulación)
    # =========================

    def set_nombre(self, nombre: str):
        """
        Establece el nombre del cliente con validación y normalización.
        """
        try:
            self._validar_nombre(nombre)
            self._nombre = nombre.strip().title()
        except ClienteError as e:
            logging.error(f"Error en set_nombre: {e}")
            raise ClienteError(f"Error en nombre: {e}") from e

    def set_email(self, email: str):
        """
        Establece el email con validación y normalización.
        """
        try:
            self._validar_email(email)
            self._email = email.strip().lower()
        except ClienteError as e:
            logging.error(f"Error en set_email: {e}")
            raise ClienteError(f"Error en email: {e}") from e

    def set_identificacion(self, identificacion: str):
        """
        Establece la identificación del cliente.
        """
        try:
            self._validar_identificacion(identificacion)
            self._identificacion = identificacion
        except ClienteError as e:
            logging.error(f"Error en set_identificacion: {e}")
            raise ClienteError(f"Error en identificación: {e}") from e

    # =========================
    # GETTERS
    # =========================

    def get_nombre(self) -> str:
        """Retorna el nombre del cliente."""
        return self._nombre

    def get_email(self) -> str:
        """Retorna el email del cliente."""
        return self._email

    def get_identificacion(self) -> str:
        """Retorna la identificación del cliente."""
        return self._identificacion

    # =========================
    # MÉTODOS DE NEGOCIO
    # =========================

    def actualizar_datos(self, nombre=None, email=None):
        """
        Actualiza datos del cliente de forma controlada.

        :param nombre: Nuevo nombre (opcional)
        :param email: Nuevo email (opcional)
        """
        try:
            if nombre is not None:
                self.set_nombre(nombre)

            if email is not None:
                self.set_email(email)

        except ClienteError as e:
            logging.error(f"Error al actualizar datos: {e}")
            raise ClienteError("Error al actualizar datos del cliente") from e

    def to_dict(self) -> dict:
        """
        Convierte el cliente a diccionario.

        Ejemplo:
            >>> c.to_dict()
            {'nombre': 'Juan', 'email': 'juan@mail.com', 'id': '123'}
        """
        return {
            "nombre": self._nombre,
            "email": self._email,
            "id": self._identificacion
        }

    def es_valido(self) -> bool:
        """
        Indica si el cliente es válido.

        :return: True siempre que el objeto exista sin errores
        """
        return True

    # =========================
    # MÉTODOS ESPECIALES
    # =========================

    def __str__(self):
        return f"Cliente: {self._nombre} | Email: {self._email} | ID: {self._identificacion}"

    def __repr__(self):
        return f"Cliente(nombre={self._nombre}, email={self._email}, id={self._identificacion})"

    def __eq__(self, other):
        """
        Compara clientes por identificación.
        """
        if not isinstance(other, Cliente):
            return False
        return self._identificacion == other._identificacion

    def __hash__(self):
        """
        Permite usar Cliente en sets y diccionarios.
        """
        return hash(self._identificacion)