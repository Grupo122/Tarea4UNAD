from services.sistema import Sistema
from models.cliente import Cliente
from models.servicios_derivados import ServicioSala, ServicioEquipo

from utils.logger import log_info, log_error


def main():
    sistema = Sistema()

    # =========================
    # CASOS VÁLIDOS
    # =========================

    try:
        c1 = Cliente("Juan Perez", "juan@mail.com", "123")
        sistema.agregar_cliente(c1)
        log_info("Cliente creado correctamente")

        servicio = ServicioSala("Sala A", 50)

        r1 = sistema.crear_reserva(c1, servicio, 2)
        sistema.confirmar_reserva(r1)

        costo = sistema.procesar_reserva(r1)

        print(f"Costo de reserva: {costo}")
        log_info("Reserva procesada correctamente")

    except Exception as e:
        log_error(f"Error en caso válido: {e}")

    # =========================
    # CASOS INVÁLIDOS
    # =========================

    # 1. Cliente inválido
    try:
        Cliente("", "correo_mal", "abc")
    except Exception as e:
        log_error(f"Cliente inválido: {e}")

    # 2. Reserva duplicada
    try:
        r2 = sistema.crear_reserva(c1, servicio, 2)
    except Exception as e:
        log_error(f"Reserva duplicada: {e}")

    # 3. Duración inválida
    try:
        sistema.crear_reserva(c1, servicio, -1)
    except Exception as e:
        log_error(f"Duración inválida: {e}")

    # 4. Confirmar cancelada
    try:
        r3 = sistema.crear_reserva(c1, servicio, 1)
        sistema.cancelar_reserva(r3)
        sistema.confirmar_reserva(r3)
    except Exception as e:
        log_error(f"Confirmar cancelada: {e}")

    # 5. Procesar sin confirmar
    try:
        r4 = sistema.crear_reserva(c1, servicio, 1)
        sistema.procesar_reserva(r4)
    except Exception as e:
        log_error(f"Procesar sin confirmar: {e}")

    print("Simulación terminada")


if __name__ == "__main__":
    main()
