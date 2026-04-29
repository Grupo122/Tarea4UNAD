"""
servicios_derivados.py

Implementaciones concretas de servicios.
"""

from models.servicio import Servicio


class ServicioSala(Servicio):

    def calcular_costo(self, horas):
        return self.precio_base * horas

    def descripcion(self):
        return "Reserva de sala"


class ServicioEquipo(Servicio):

    def calcular_costo(self, dias):
        return self.precio_base * dias

    def descripcion(self):
        return "Alquiler de equipo"


class ServicioAsesoria(Servicio):

    def calcular_costo(self, horas):
        return self.precio_base * horas * 1.2

    def descripcion(self):
        return "Asesoría especializada"
