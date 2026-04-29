# Módulo utilitario para el registro de eventos y errores del sistema
# Guarda todos los logs en el archivo logs/app.log

import logging
import os

# Crea la carpeta logs si no existe
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configura el sistema de logs
logging.basicConfig(
    filename="logs/app.log",   # archivo donde se guardan los registros
    level=logging.INFO,         # registra INFO, WARNING y ERROR
    format="%(asctime)s - %(levelname)s - %(message)s"
    # asctime = fecha y hora, levelname = tipo, message = mensaje
)

def log_info(mensaje):
    """Registra un evento informativo exitoso."""
    logging.info(mensaje)

def log_warning(mensaje):
    """Registra una advertencia cuando algo es sospechoso."""
    logging.warning(mensaje)

def log_error(mensaje):
    """Registra un error cuando algo falla."""
    logging.error(mensaje)

def log_exception(mensaje):
    """Registra un error con el detalle completo de dónde ocurrió."""
    logging.exception(mensaje)