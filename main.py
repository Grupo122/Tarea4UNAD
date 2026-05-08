"""
main.py
Sistema Integral de Gestión de Clientes, Servicios y Reservas
Empresa: Software FJ  |  Curso: Programación UNAD (213023)

Simula 10 operaciones completas que demuestran:
  - Registros válidos e inválidos de clientes
  - Creación correcta e incorrecta de servicios
  - Reservas exitosas y fallidas
  - try/except, try/except/else, try/except/finally
  - Encadenamiento de excepciones (raise ... from ...)
  - Registro de todos los eventos en logs/app.log
"""

# ── Modelos ────────────────────────────────────────────────────────────────
from models.cliente import Cliente, ClienteError
from models.servicios_derivados import ReservaSala, AlquilerEquipo, Asesoria
from models.reserva import Reserva

# ── Excepciones ────────────────────────────────────────────────────────────
from exceptions.servicio_error import (
    ServicioError,
    ServicioNoDisponibleError,
    ParametroInvalidoError,
    CostoInvalidoError,
)
from exceptions.reserva_error import (
    ReservaError,
    ReservaInvalidaError,
    ReservaCanceladaError,
    DuracionInvalidaError,
)

# ── Logger ─────────────────────────────────────────────────────────────────
from utils.logger import log_info, log_warning, log_error, log_exception


# ══════════════════════════════════════════════════════════════════════════════
# UTILIDAD: separador visual para la consola
# ══════════════════════════════════════════════════════════════════════════════
def separador(numero, titulo):
    print("\n" + "=" * 62)
    print(f"  OPERACION {numero}: {titulo}")
    print("=" * 62)


# ══════════════════════════════════════════════════════════════════════════════
# OPERACION 1 - Registro de cliente VALIDO
# Demuestra: try / except / else / finally
# ══════════════════════════════════════════════════════════════════════════════
def operacion_1():
    separador(1, "Registro de cliente valido")
    cliente = None
    try:
        cliente = Cliente("Ana Torres", "ana.torres@softwarefj.com", "1001234567")
        log_info(f"Cliente registrado: {cliente}")
    except ClienteError as e:
        log_error(f"Error inesperado al registrar cliente valido: {e}")
        print(f"[ERROR] {e}")
    else:
        # Solo se ejecuta si NO hubo excepcion
        print(f"[OK] Cliente registrado exitosamente:")
        print(f"     {cliente}")
    finally:
        print("-> Operacion 1 finalizada.")
    return cliente


# ══════════════════════════════════════════════════════════════════════════════
# OPERACION 2 - Registro de cliente con EMAIL INVALIDO
# Demuestra: try / except / finally + excepcion personalizada
# ══════════════════════════════════════════════════════════════════════════════
def operacion_2():
    separador(2, "Registro de cliente con email invalido")
    try:
        cliente_malo = Cliente("Pedro Gomez", "correo_sin_arroba.com", "9876543210")
        log_info(f"Cliente registrado: {cliente_malo}")
    except ClienteError as e:
        log_error(f"Error al registrar cliente con email invalido: {e}")
        print(f"[ERROR] Error capturado correctamente: {e}")
    finally:
        print("-> El sistema sigue funcionando despues del error.")
        print("-> Operacion 2 finalizada.")


# ══════════════════════════════════════════════════════════════════════════════
# OPERACION 3 - Registro de cliente con IDENTIFICACION INVALIDA
# Demuestra: try / except / finally + encadenamiento de excepciones
# ══════════════════════════════════════════════════════════════════════════════
def operacion_3():
    separador(3, "Registro de cliente con identificacion invalida")
    try:
        cliente_malo = Cliente("Laura Rios", "laura@softwarefj.com", "ID-INVALIDA")
        log_info(f"Cliente registrado: {cliente_malo}")
    except ClienteError as e:
        log_error(f"Error al registrar cliente con ID invalida: {e}")
        print(f"[ERROR] Error capturado: {e}")
        # Encadenamiento: el error de cliente genera un error de reserva
        try:
            raise ReservaError(
                "No se puede crear reserva: el cliente no es valido"
            ) from e
        except ReservaError as re:
            log_error(f"Excepcion encadenada: {re} | Causa: {re.__cause__}")
            print(f"[ERROR] Excepcion encadenada: {re}")
            print(f"        Causa original: {re.__cause__}")
    finally:
        print("-> Operacion 3 finalizada.")


# ══════════════════════════════════════════════════════════════════════════════
# OPERACION 4 - Creacion CORRECTA de los tres servicios
# Demuestra: try / except / else / finally + polimorfismo (describir())
# ══════════════════════════════════════════════════════════════════════════════
def operacion_4():
    separador(4, "Creacion correcta de los tres servicios")
    servicios = []
    definiciones = [
        ("ReservaSala",    lambda: ReservaSala("Sala Innovacion", 50000, 10)),
        ("AlquilerEquipo", lambda: AlquilerEquipo("Laptop HP", 15000, 5)),
        ("Asesoria",       lambda: Asesoria("Dr. Martinez", 80000, "legal")),
    ]
    for nombre_clase, crear in definiciones:
        try:
            servicio = crear()
            log_info(f"Servicio creado: {servicio.describir()}")
        except ServicioError as e:
            log_error(f"Error al crear {nombre_clase}: {e}")
            print(f"[ERROR] {e}")
        else:
            print(f"[OK] {servicio.describir()}")
            servicios.append(servicio)
        finally:
            print(f"     Intento de creacion de {nombre_clase} terminado.")
    print("-> Operacion 4 finalizada.")
    return servicios


# ══════════════════════════════════════════════════════════════════════════════
# OPERACION 5 - Creacion INCORRECTA de servicio (precio negativo)
# Demuestra: try / except / finally + ParametroInvalidoError
# ══════════════════════════════════════════════════════════════════════════════
def operacion_5():
    separador(5, "Creacion de servicio con precio invalido")
    try:
        sala_mala = ReservaSala("Sala Error", -5000, 8)
        log_info(f"Servicio creado: {sala_mala}")
    except ParametroInvalidoError as e:
        log_error(f"Error al crear servicio con precio negativo: {e}")
        print(f"[ERROR] Error capturado correctamente: {e}")
    except ServicioError as e:
        log_error(f"ServicioError inesperado: {e}")
        print(f"[ERROR] {e}")
    finally:
        print("-> El sistema continua estable tras el error.")
        print("-> Operacion 5 finalizada.")


# ══════════════════════════════════════════════════════════════════════════════
# OPERACION 6 - Reserva EXITOSA con confirmacion y procesamiento
# Demuestra: try / except / else / finally + flujo completo de Reserva
# ══════════════════════════════════════════════════════════════════════════════
def operacion_6(cliente, servicios):
    separador(6, "Reserva exitosa: confirmacion y procesamiento")
    if not cliente or not servicios:
        print("[AVISO] No hay cliente o servicios disponibles.")
        return
    try:
        sala = servicios[0]
        reserva = Reserva(cliente, sala, 3)
        log_info(
            f"Reserva creada: cliente={cliente.get_nombre()} | "
            f"servicio={sala.nombre} | duracion=3h"
        )
    except ReservaError as e:
        log_error(f"Error al crear reserva exitosa: {e}")
        print(f"[ERROR] {e}")
    else:
        print(f"[OK] Reserva creada | Estado: {reserva.estado}")
        reserva.confirmar()
        print(f"[OK] Reserva confirmada | Estado: {reserva.estado}")
        reserva.procesar()
        log_info("Reserva procesada exitosamente en operacion 6")
    finally:
        print("-> Operacion 6 finalizada.")


# ══════════════════════════════════════════════════════════════════════════════
# OPERACION 7 - Reserva FALLIDA por duracion invalida (cero)
# Demuestra: try / except / finally + DuracionInvalidaError
# ══════════════════════════════════════════════════════════════════════════════
def operacion_7(cliente, servicios):
    separador(7, "Reserva fallida: duracion invalida (cero)")
    if not cliente or not servicios:
        print("[AVISO] No hay cliente o servicios disponibles.")
        return
    try:
        equipo = servicios[1]
        reserva_mala = Reserva(cliente, equipo, 0)
        log_info("Reserva con duracion cero creada (no deberia llegar aqui)")
    except (DuracionInvalidaError, ReservaError) as e:
        log_error(f"Error al crear reserva con duracion invalida: {e}")
        print(f"[ERROR] Error capturado correctamente: {e}")
    finally:
        print("-> Operacion 7 finalizada.")


# ══════════════════════════════════════════════════════════════════════════════
# OPERACION 8 - Intento de confirmar reserva YA CANCELADA
# Demuestra: try / except / finally + ReservaCanceladaError
# ══════════════════════════════════════════════════════════════════════════════
def operacion_8(cliente, servicios):
    separador(8, "Operacion sobre reserva ya cancelada")
    if not cliente or not servicios:
        print("[AVISO] No hay cliente o servicios disponibles.")
        return
    try:
        asesoria = servicios[2]
        reserva = Reserva(cliente, asesoria, 2)
        reserva.cancelar()
        print(f"[OK] Reserva cancelada | Estado: {reserva.estado}")
        # Intento de confirmar una reserva ya cancelada -> error
        reserva.confirmar()
        log_info("Confirmacion tras cancelacion (no deberia llegar aqui)")
    except ReservaCanceladaError as e:
        log_error(f"Intento de confirmar reserva cancelada: {e}")
        print(f"[ERROR] Error capturado correctamente: {e}")
    except ReservaError as e:
        log_error(f"ReservaError en operacion 8: {e}")
        print(f"[ERROR] {e}")
    finally:
        print("-> Operacion 8 finalizada.")


# ══════════════════════════════════════════════════════════════════════════════
# OPERACION 9 - Calculo de costos con VARIANTES SOBRECARGADAS
# Demuestra: polimorfismo + metodos sobrecargados (impuesto, descuento, informe)
# ══════════════════════════════════════════════════════════════════════════════
def operacion_9(servicios):
    separador(9, "Calculo de costos con variantes sobrecargadas")
    if not servicios:
        print("[AVISO] No hay servicios disponibles.")
        return
    try:
        sala     = servicios[0]
        equipo   = servicios[1]
        asesoria = servicios[2]

        # ReservaSala: costo base y con IVA
        costo_base_sala = sala.calcular_costo(2, personas=5)
        costo_iva_sala  = sala.calcular_costo_con_impuesto(2)
        print(f"[OK] [{sala.nombre}] Costo base (2h, 5 personas): ${costo_base_sala}")
        print(f"[OK] [{sala.nombre}] Costo con IVA 19%:           ${costo_iva_sala}")

        # AlquilerEquipo: costo con 10% de descuento
        costo_desc = equipo.calcular_costo_con_descuento(3, descuento_pct=10)
        print(f"[OK] [{equipo.nombre}] Costo con 10% descuento (3h): ${costo_desc}")

        # Asesoria: costo base y con informe escrito (+20%)
        costo_base_ases    = asesoria.calcular_costo(1)
        costo_con_informe  = asesoria.calcular_costo(1, incluir_informe=True)
        print(f"[OK] [{asesoria.nombre}] Costo base (1h):           ${costo_base_ases}")
        print(f"[OK] [{asesoria.nombre}] Con informe escrito (+20%): ${costo_con_informe}")

        log_info("Operacion 9: calculo de variantes de costo completado")

    except (ServicioError, ParametroInvalidoError, CostoInvalidoError) as e:
        log_error(f"Error en calculo de costos (operacion 9): {e}")
        print(f"[ERROR] {e}")
    finally:
        print("-> Operacion 9 finalizada.")


# ══════════════════════════════════════════════════════════════════════════════
# OPERACION 10 - Servicio NO DISPONIBLE + encadenamiento de excepciones
# Demuestra: ServicioNoDisponibleError + raise ... from ... + log_exception
# ══════════════════════════════════════════════════════════════════════════════
def operacion_10(cliente):
    separador(10, "Servicio no disponible + encadenamiento de excepciones")
    if not cliente:
        print("[AVISO] No hay cliente disponible.")
        return
    try:
        # Sala marcada como NO disponible
        sala_ocupada = ReservaSala("Sala Ocupada", 60000, 8, disponible=False)
        log_info(f"Sala creada (no disponible): {sala_ocupada.nombre}")

        # Intentar calcular el costo debe lanzar ServicioNoDisponibleError
        costo = sala_ocupada.calcular_costo(2)
        log_info(f"Costo calculado (no deberia llegar aqui): ${costo}")

    except ServicioNoDisponibleError as e:
        log_error(f"Servicio no disponible en operacion 10: {e}")
        print(f"[ERROR] Capturado: {e}")
        # Encadenamiento: el error del servicio causa un error de reserva
        try:
            raise ReservaInvalidaError(
                "No se puede crear la reserva porque el servicio no esta disponible"
            ) from e
        except ReservaInvalidaError as re:
            log_exception(f"Excepcion encadenada en operacion 10: {re}")
            print(f"[ERROR] Excepcion encadenada: {re}")
            print(f"        Causa original: {re.__cause__}")

    except ServicioError as e:
        log_error(f"ServicioError en operacion 10: {e}")
        print(f"[ERROR] {e}")

    finally:
        print("-> Sistema estable. Todas las excepciones fueron manejadas.")
        print("-> Operacion 10 finalizada.")


# ══════════════════════════════════════════════════════════════════════════════
# PUNTO DE ENTRADA PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n" + "*" * 62)
    print("  Software FJ - Sistema de Gestion de Clientes y Reservas")
    print("  Curso: Programacion UNAD (213023)")
    print("*" * 62)

    log_info("=" * 50)
    log_info("INICIO DE SIMULACION - Software FJ")
    log_info("=" * 50)

    # Ejecuta las 10 operaciones en secuencia.
    # El sistema NO se detiene ante ningún error.
    cliente   = operacion_1()
    operacion_2()
    operacion_3()
    servicios = operacion_4()
    operacion_5()
    operacion_6(cliente, servicios)
    operacion_7(cliente, servicios)
    operacion_8(cliente, servicios)
    operacion_9(servicios)
    operacion_10(cliente)

    print("\n" + "*" * 62)
    print("  Simulacion completada.")
    print("  Revisa logs/app.log para el detalle completo de eventos.")
    print("*" * 62 + "\n")

    log_info("FIN DE SIMULACION - Software FJ")
