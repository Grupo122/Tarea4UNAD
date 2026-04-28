l"""
cliente.py

Módulo que define la clase Cliente con validaciones robustas,
encapsulación y manejo de excepciones personalizadas.

Este módulo está diseñado para ser reutilizable dentro de sistemas
orientados a objetos que requieran gestión de clientes.
"""

import re


class ClienteError(Exception):
    """
    Excepción personalizada para errores relacionados con la clase Cliente.

    Se lanza cuando ocurre un error en la validación o manipulación
    de los datos del cliente.

    Ejemplo:
        >>> raise ClienteError("Email inválido")
    """
    pass


class Cliente:
    """
    Representa un cliente dentro del sistema.

    Esta clase implementa encapsulación, validaciones estrictas
    y manejo de errores mediante excepciones personalizadas.

    :param nombre: Nombre completo del cliente
    :type nombre: str
    :param email: Correo electrónico del cliente
    :type email: str
    :param identificacion: Identificación única del cliente
    :type identificacion: str

    :raises ClienteError: Si alguno de los datos es inválido

    Ejemplo:
        >>> cliente = Cliente("Juan Perez", "juan@mail.com", "12345")
        >>> print(cliente)
        Cliente: Juan Perez | Email: juan@mail.com | ID: 12345
    """

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
        Valida que el nombre sea correcto.

        :param nombre: Nombre a validar
        :type nombre: str
        :raises ClienteError: Si el nombre es inválido

        Ejemplo:
            >>> cliente._validar_nombre("Juan Perez")
            # No lanza error

            >>> cliente._validar_nombre("")
            ClienteError: El nombre no puede estar vacío
        """
        if not nombre or not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío")

        if any(char.isdigit() for char in nombre):
            raise ClienteError("El nombre no debe contener números")

    def _validar_email(self, email: str):
        """
        Valida el formato del correo electrónico.

        :param email: Email a validar
        :type email: str
        :raises ClienteError: Si el email no tiene formato válido

        Ejemplo:
            >>> cliente._validar_email("correo@mail.com")
            # No lanza error

            >>> cliente._validar_email("correo_mal")
            ClienteError: Formato de email inválido
        """
        if not isinstance(email, str):
            raise ClienteError("El email debe ser un string")

        email = email.strip()

        patron = r"^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

        if not re.match(patron, email):
            raise ClienteError(
                "Formato de email inválido. Ejemplo válido: usuario@dominio.com"
            )

    def _validar_identificacion(self, identificacion: str):
        """
        Valida la identificación del cliente.

        :param identificacion: Identificación a validar
        :type identificacion: str
        :raises ClienteError: Si la identificación es inválida

        Ejemplo:
            >>> cliente._validar_identificacion("12345")
            # No lanza error

            >>> cliente._validar_identificacion("abc")
            ClienteError: La identificación debe contener solo números
        """
        if not identificacion:
            raise ClienteError("La identificación no puede estar vacía")

        if not identificacion.isdigit():
            raise ClienteError("La identificación debe contener solo números")

    # =========================
    # SETTERS
    # =========================

    def set_nombre(self, nombre: str):
        """
        Establece el nombre del cliente con validación.

        :param nombre: Nuevo nombre
        :type nombre: str
        :raises ClienteError: Si el nombre es inválido

        Ejemplo:
            >>> cliente.set_nombre("Carlos Ruiz")
        """
        try:
            self._validar_nombre(nombre)
            self._nombre = nombre.strip()
        except ClienteError as e:
            raise ClienteError(f"Error en nombre: {e}") from e

    def set_email(self, email: str):
        """
        Establece el email del cliente con validación.

        :param email: Nuevo email
        :type email: str
        :raises ClienteError: Si el email es inválido

        Ejemplo:
            >>> cliente.set_email("nuevo@mail.com")
        """
        try:
            self._validar_email(email)
            self._email = email.strip().lower()
        except ClienteError as e:
            raise ClienteError(f"Error en email: {e}") from e

    def set_identificacion(self, identificacion: str):
        """
        Establece la identificación del cliente con validación.

        :param identificacion: Nueva identificación
        :type identificacion: str
        :raises ClienteError: Si la identificación es inválida

        Ejemplo:
            >>> cliente.set_identificacion("98765")
        """
        try:
            self._validar_identificacion(identificacion)
            self._identificacion = identificacion
        except ClienteError as e:
            raise ClienteError(f"Error en identificación: {e}") from e

    # =========================
    # GETTERS
    # =========================

    def get_nombre(self) -> str:
        """
        Obtiene el nombre del cliente.

        :return: Nombre del cliente
        :rtype: str

        Ejemplo:
            >>> cliente.get_nombre()
            'Juan Perez'
        """
        return self._nombre

    def get_email(self) -> str:
        """
        Obtiene el email del cliente.

        :return: Email del cliente
        :rtype: str

        Ejemplo:
            >>> cliente.get_email()
            'juan@mail.com'
        """
        return self._email

    def get_identificacion(self) -> str:
        """
        Obtiene la identificación del cliente.

        :return: Identificación del cliente
        :rtype: str

        Ejemplo:
            >>> cliente.get_identificacion()
            '12345'
        """
        return self._identificacion

    # =========================
    # REPRESENTACIÓN
    # =========================

    def __str__(self):
        """
        Representación legible del cliente.

        Ejemplo:
            >>> print(cliente)
            Cliente: Juan Perez | Email: juan@mail.com | ID: 12345
        """
        return f"Cliente: {self._nombre} | Email: {self._email} | ID: {self._identificacion}"

    def __repr__(self):
        """
        Representación técnica del objeto.

        Ejemplo:
            >>> repr(cliente)
            'Cliente(nombre=Juan Perez, email=juan@mail.com, id=12345)'
        """
        return f"Cliente(nombre={self._nombre}, email={self._email}, id={self._identificacion})"

    # =========================
    # MÉTODOS ADICIONALES
    # =========================

    def actualizar_datos(self, nombre=None, email=None):
        """
        Actualiza los datos del cliente de forma controlada.

        :param nombre: Nuevo nombre (opcional)
        :type nombre: str
        :param email: Nuevo email (opcional)
        :type email: str
        :raises ClienteError: Si algún dato es inválido

        Ejemplo:
            >>> cliente.actualizar_datos(nombre="Nuevo Nombre")
            >>> cliente.actualizar_datos(email="nuevo@mail.com")
        """
        try:
            if nombre is not None:
                self.set_nombre(nombre)

            if email is not None:
                self.set_email(email)

        except ClienteError as e:
            raise ClienteError("Error al actualizar datos del cliente") from e