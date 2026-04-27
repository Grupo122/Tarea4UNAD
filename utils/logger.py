import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(mensaje):
    logging.info(mensaje)

def log_error(mensaje):
    logging.error(mensaje)