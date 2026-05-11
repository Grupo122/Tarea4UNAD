# Módulo que define los tres servicios especializados del sistema
# Cada uno hereda de la clase abstracta Servicio

from models.servicio import Servicio
from exceptions.servicio_error import ParametroInvalidoError


class ReservaSala(Servicio):
    """Servicio de reserva de salas para reuniones o eventos."""

    def __init__(self, nombre, precio_por_hora, capacidad):
        """Constructor de ReservaSala. Recibe el nombre, precio y capacidad máxima."""
        # llama al constructor de Servicio para guardar nombre y precio
        super().__init__(nombre, precio_por_hora)
        # valida la capacidad
        if capacidad <= 0:
            raise ParametroInvalidoError("La capacidad debe ser mayor a cero", servicio=nombre)
        # guarda la capacidad máxima de personas
        self.capacidad = capacidad

    def calcular_costo(self, duracion):
        """Calcula el costo multiplicando el precio por la duración."""
        try:
            # valida que la duración sea mayor a cero
            self.validar_duracion(duracion)
            return self.precio_por_hora * duracion
        except Exception as e:
            print(f"Error al calcular costo: {e}")
        finally:
            print("Cálculo de costo terminado")

    def describir(self):
        """Describe el servicio de reserva de sala."""
        return f"Reserva de sala: {self.nombre} | Capacidad: {self.capacidad} personas | Precio: ${self.precio_por_hora}/hora"

    def validar_parametros(self):
        """Valida que la capacidad sea mayor a cero."""
        try:
            # verifica que la capacidad sea mayor a cero
            if self.capacidad <= 0:
                raise ParametroInvalidoError("La capacidad debe ser mayor a cero", servicio=self.nombre)
        except ParametroInvalidoError as e:
            print(f"Error: {e}")
        finally:
            print("Validación de parámetros terminada")


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos tecnológicos."""

    def __init__(self, nombre, precio_por_hora, cantidad_equipos):
        """Constructor de AlquilerEquipo. Recibe el nombre, precio y cantidad de equipos."""
        # llama al constructor de Servicio para guardar nombre y precio
        super().__init__(nombre, precio_por_hora)
        # valida la cantidad
        if cantidad_equipos <= 0:
            raise ParametroInvalidoError("La cantidad debe ser mayor a cero", servicio=nombre)
        # guarda la cantidad de equipos a alquilar
        self.cantidad_equipos = cantidad_equipos

    def calcular_costo(self, duracion, cantidad_equipos):
        """Calcula el costo multiplicando el precio por la duración y cantidad de equipos."""
        try:
            # valida que la duración sea mayor a cero
            self.validar_duracion(duracion)
            return self.precio_por_hora * duracion * cantidad_equipos
        except Exception as e:
            print(f"Error al calcular costo: {e}")
        finally:
            print("Cálculo de costo terminado")

    def describir(self):
        """Describe el servicio de alquiler de equipos."""
        return f"Alquiler de equipo: {self.nombre} | Cantidad de equipos: {self.cantidad_equipos} equipos | Precio: ${self.precio_por_hora}/hora"

    def validar_parametros(self):
        """Valida que la cantidad de equipos sea mayor a cero."""
        try:
            # verifica que la cantidad de equipos sea mayor a cero
            if self.cantidad_equipos <= 0:
                raise ParametroInvalidoError("La cantidad debe ser mayor a cero", servicio=self.nombre)
        except ParametroInvalidoError as e:
            print(f"Error: {e}")
        finally:
            print("Validación de parámetros terminada")


class Asesoria(Servicio):
    """Servicio de asesorías especializadas."""

    def __init__(self, nombre, precio_por_hora, tipo_asesoria):
        """Constructor de Asesoria. Recibe el nombre, precio y tipo de asesoría."""
        # llama al constructor de Servicio para guardar nombre y precio
        super().__init__(nombre, precio_por_hora)
        # valida el tipo
        if not tipo_asesoria or not tipo_asesoria.strip():
            raise ParametroInvalidoError("El tipo de asesoría no puede estar vacío", servicio=nombre)
        # guarda el tipo de asesoría
        self.tipo_asesoria = tipo_asesoria

    def calcular_costo(self, duracion):
        """Calcula el costo multiplicando el precio por la duración."""
        try:
            # valida que la duración sea mayor a cero
            self.validar_duracion(duracion)
            return self.precio_por_hora * duracion
        except Exception as e:
            print(f"Error al calcular costo: {e}")
        finally:
            print("Cálculo de costo terminado")

    def describir(self):
        """Describe el servicio de asesoría."""
        return f"Tipo de asesoría: {self.tipo_asesoria} | Precio: ${self.precio_por_hora}/hora"

    def validar_parametros(self):
        """Valida que el tipo de asesoría no esté vacío."""
        try:
            # verifica que el tipo de asesoría no esté vacío
            if not self.tipo_asesoria or not self.tipo_asesoria.strip():
                raise ParametroInvalidoError("El tipo de asesoría no puede estar vacío", servicio=self.nombre)
        except ParametroInvalidoError as e:
            print(f"Error: {e}")
        finally:
            print("Validación de parámetros terminada")