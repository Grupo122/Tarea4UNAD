# Módulo que define la clase abstracta Servicio
# Es la base de todos los servicios del sistema

from abc import ABC, abstractmethod
from exceptions.servicio_error import ServicioError, ParametroInvalidoError

class Servicio(ABC):
    """Clase abstracta base para todos los servicios del sistema"""

    def __init__(self, nombre, precio_por_hora):
        """Constructor de Servicio. Valida el nombre y el precio"""
        self.nombre = nombre
        self.precio_por_hora = precio_por_hora
        try:
            # verifica que el nombre no esté vacío
            if not nombre or not nombre.strip():
                raise ParametroInvalidoError("El nombre del servicio no puede estar vacío", servicio=nombre)
            # verifica que el precio sea mayor a cero
            if precio_por_hora <= 0:
                raise ParametroInvalidoError("El precio por hora debe ser mayor a cero", servicio=nombre)
            

        except ParametroInvalidoError as e:
            print(f"Error al crear servicio: {e}")
        finally:
            print("Proceso de creación de servicio terminado")

    @abstractmethod
    def calcular_costo(self, duracion):
        """Calcula el costo del servicio según la duración, cada hijo lo implementa a su manera"""
        pass

    @abstractmethod
    def describir(self):
        """Describe el servicio, cada hijo lo implementa a su manera"""
        pass

    @abstractmethod
    def validar_parametros(self):
        """Valida los parámetros específicos de cada servicio. Cada hijo lo implementa a su manera"""
        pass

    def __str__(self):
        """Muestra el nombre y precio del servicio"""
        return f"Servicio: {self.nombre} | Precio por hora: ${self.precio_por_hora}"

    def validar_duracion(self, duracion):
        """Valida que la duración sea mayor a cero"""
        try:
            # verifica que la duración sea mayor a cero
            if duracion <= 0:
                raise ParametroInvalidoError("La duración debe ser mayor a cero", servicio=self.nombre)
        except ParametroInvalidoError as e:
            print(f"Error: {e}")
        finally:
            print("Validación de duración terminada")
    
    



