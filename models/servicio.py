"""
servicio.py

Define la clase abstracta Servicio.
"""

from abc import ABC, abstractmethod


class Servicio(ABC):
    """
    Clase base abstracta para todos los servicios.
    """

    def __init__(self, nombre: str, precio_base: float):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, duracion):
        """
        Calcula el costo del servicio.
        """
        pass

    @abstractmethod
    def descripcion(self):
        """
        Describe el servicio.
        """
        pass

    def __eq__(self, other):
        return isinstance(other, Servicio) and self.nombre == other.nombre

    def __hash__(self):
        return hash(self.nombre)

    def __str__(self):
        return f"{self.nombre} (${self.precio_base})"
