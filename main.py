"""
main.py
Sistema Integral de Gestión de Clientes, Servicios y Reservas
Empresa: Software FJ  |  Curso: Programación UNAD (213023)

Sistema interactivo que permite al usuario gestionar clientes, servicios y reservas,
demostrando manejo avanzado de excepciones y logging.
Además simula 10 operaciones completas que demuestran:
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
# FUNCIONES DE GESTIÓN
# ══════════════════════════════════════════════════════════════════════════════

def registrar_cliente():
    """Registra un nuevo cliente con validaciones."""
    try:
        nombre = input("Ingrese nombre del cliente: ").strip()
        email = input("Ingrese email del cliente: ").strip()
        identificacion = input("Ingrese identificación del cliente: ").strip()
        
        cliente = Cliente(nombre, email, identificacion)
        log_info(f"Cliente registrado: {cliente}")
        print(f"[OK] Cliente registrado exitosamente: {cliente}")
        return cliente
    except ClienteError as e:
        log_error(f"Error al registrar cliente: {e}")
        print(f"[ERROR] {e}")
        return None
    except Exception as e:
        log_exception(f"Error inesperado al registrar cliente: {e}")
        print(f"[ERROR] Error inesperado: {e}")
        return None

def crear_servicio():
    """Crea un nuevo servicio según el tipo seleccionado."""
    print("\nTipos de servicio disponibles:")
    print("1. Reserva de Sala")
    print("2. Alquiler de Equipo")
    print("3. Asesoría")
    
    try:
        tipo = input("Seleccione tipo de servicio (1-3): ").strip()
        
        if tipo == "1":
            nombre = input("Nombre de la sala: ").strip()
            precio = float(input("Precio por hora: ").strip())
            capacidad = int(input("Capacidad máxima: ").strip())
            servicio = ReservaSala(nombre, precio, capacidad)
        elif tipo == "2":
            nombre = input("Nombre del equipo: ").strip()
            precio = float(input("Precio por hora: ").strip())
            cantidad = int(input("Cantidad de equipos: ").strip())
            servicio = AlquilerEquipo(nombre, precio, cantidad)
        elif tipo == "3":
            nombre = input("Nombre del asesor: ").strip()
            precio = float(input("Precio por hora: ").strip())
            tipo_asesoria = input("Tipo de asesoría: ").strip()
            servicio = Asesoria(nombre, precio, tipo_asesoria)
        else:
            print("[ERROR] Tipo de servicio inválido.")
            return None
        
        log_info(f"Servicio creado: {servicio.describir()}")
        print(f"[OK] Servicio creado: {servicio.describir()}")
        return servicio
    except (ValueError, ParametroInvalidoError) as e:
        log_error(f"Error al crear servicio: {e}")
        print(f"[ERROR] {e}")
        return None
    except Exception as e:
        log_exception(f"Error inesperado al crear servicio: {e}")
        print(f"[ERROR] Error inesperado: {e}")
        return None

def crear_reserva(clientes, servicios):
    """Crea una nueva reserva."""
    if not clientes:
        print("[ERROR] No hay clientes registrados.")
        return None
    if not servicios:
        print("[ERROR] No hay servicios disponibles.")
        return None
    
    try:
        print("\nClientes disponibles:")
        for i, c in enumerate(clientes, 1):
            print(f"{i}. {c}")
        idx_cliente = int(input("Seleccione cliente (número): ").strip()) - 1
        
        print("\nServicios disponibles:")
        for i, s in enumerate(servicios, 1):
            print(f"{i}. {s.describir()}")
        idx_servicio = int(input("Seleccione servicio (número): ").strip()) - 1
        
        duracion = int(input("Duración en horas: ").strip())
        
        cliente = clientes[idx_cliente]
        servicio = servicios[idx_servicio]
        
        reserva = Reserva(cliente, servicio, duracion)
        log_info(f"Reserva creada: cliente={cliente.get_nombre()} | servicio={servicio.nombre} | duracion={duracion}h")
        print(f"[OK] Reserva creada: {reserva.estado}")
        return reserva
    except (IndexError, ValueError, ReservaError, DuracionInvalidaError) as e:
        log_error(f"Error al crear reserva: {e}")
        print(f"[ERROR] {e}")
        return None
    except Exception as e:
        log_exception(f"Error inesperado al crear reserva: {e}")
        print(f"[ERROR] Error inesperado: {e}")
        return None

def gestionar_reserva(reservas):
    """Gestiona una reserva existente (confirmar, cancelar, procesar)."""
    if not reservas:
        print("[ERROR] No hay reservas creadas.")
        return
    
    try:
        print("\nReservas disponibles:")
        for i, r in enumerate(reservas, 1):
            print(f"{i}. Cliente: {r.cliente.get_nombre()} | Servicio: {r.servicio.nombre} | Estado: {r.estado}")
        idx = int(input("Seleccione reserva (número): ").strip()) - 1
        reserva = reservas[idx]
        
        print("\nAcciones disponibles:")
        print("1. Confirmar reserva")
        print("2. Cancelar reserva")
        print("3. Procesar reserva")
        accion = input("Seleccione acción (1-3): ").strip()
        
        if accion == "1":
            reserva.confirmar()
            log_info(f"Reserva confirmada: {reserva.cliente.get_nombre()}")
        elif accion == "2":
            reserva.cancelar()
            log_info(f"Reserva cancelada: {reserva.cliente.get_nombre()}")
        elif accion == "3":
            reserva.procesar()
            log_info(f"Reserva procesada: {reserva.cliente.get_nombre()}")
        else:
            print("[ERROR] Acción inválida.")
    except (IndexError, ValueError, ReservaError) as e:
        log_error(f"Error al gestionar reserva: {e}")
        print(f"[ERROR] {e}")
    except Exception as e:
        log_exception(f"Error inesperado al gestionar reserva: {e}")
        print(f"[ERROR] Error inesperado: {e}")

def calcular_costo_servicio(servicios):
    """Calcula el costo de un servicio."""
    if not servicios:
        print("[ERROR] No hay servicios disponibles.")
        return
    
    try:
        print("\nServicios disponibles:")
        for i, s in enumerate(servicios, 1):
            print(f"{i}. {s.describir()}")
        idx = int(input("Seleccione servicio (número): ").strip()) - 1
        servicio = servicios[idx]
        
        if isinstance(servicio, AlquilerEquipo):
            duracion = int(input("Duración en horas: ").strip())
            cantidad = int(input("Cantidad de equipos: ").strip())
            costo = servicio.calcular_costo(duracion, cantidad)
        else:
            duracion = int(input("Duración en horas: ").strip())
            costo = servicio.calcular_costo(duracion)
        
        print(f"[OK] Costo calculado: ${costo}")
        log_info(f"Costo calculado para {servicio.nombre}: ${costo}")
    except (IndexError, ValueError, ServicioError) as e:
        log_error(f"Error al calcular costo: {e}")
        print(f"[ERROR] {e}")
    except Exception as e:
        log_exception(f"Error inesperado al calcular costo: {e}")
        print(f"[ERROR] Error inesperado: {e}")

def simulacion_automatica(clientes, servicios, reservas):
    """Ejecuta automáticamente las 10 operaciones de simulación."""
    print("\n" + "="*62)
    print("  SIMULACIÓN AUTOMÁTICA DE 10 OPERACIONES")
    print("="*62)
    
    # Reiniciar contadores para la simulación
    sim_operaciones = 0
    
    # OPERACION 1 - Registro de cliente VALIDO
    print("\n==============================================================")
    print("  OPERACION 1: Registro de cliente valido")
    print("==============================================================")
    try:
        cliente = Cliente("Ana Torres", "ana.torres@softwarefj.com", "1001234567")
        log_info(f"Cliente registrado: {cliente}")
        clientes.append(cliente)
        sim_operaciones += 1
        print(f"[OK] Cliente registrado exitosamente: {cliente}")
    except ClienteError as e:
        log_error(f"Error inesperado al registrar cliente valido: {e}")
        print(f"[ERROR] {e}")
    print("-> Operacion 1 finalizada.")
    
    # OPERACION 2 - Registro de cliente con EMAIL INVALIDO
    print("\n==============================================================")
    print("  OPERACION 2: Registro de cliente con email invalido")
    print("==============================================================")
    try:
        Cliente("Pedro Gomez", "correo_sin_arroba.com", "9876543210")
    except ClienteError as e:
        log_error(f"Error al registrar cliente con email invalido: {e}")
        print(f"[ERROR] Error capturado correctamente: {e}")
        sim_operaciones += 1
    print("-> El sistema sigue funcionando despues del error.")
    print("-> Operacion 2 finalizada.")
    
    # OPERACION 3 - Registro de cliente con IDENTIFICACION INVALIDA
    print("\n==============================================================")
    print("  OPERACION 3: Registro de cliente con identificacion invalida")
    print("==============================================================")
    try:
        Cliente("Laura Rios", "laura@softwarefj.com", "ID-INVALIDA")
    except ClienteError as e:
        log_error(f"Error al registrar cliente con ID invalida: {e}")
        print(f"[ERROR] Error capturado: {e}")
        # Encadenamiento: el error de cliente genera un error de reserva
        try:
            raise ReservaError("No se puede crear reserva: el cliente no es valido") from e
        except ReservaError as re:
            log_error(f"Excepcion encadenada: {re} | Causa: {re.__cause__}")
            print(f"[ERROR] Excepcion encadenada: {re}")
            print(f"        Causa original: {re.__cause__}")
        sim_operaciones += 1
    print("-> Operacion 3 finalizada.")
    
    # OPERACION 4 - Creacion CORRECTA de los tres servicios
    print("\n==============================================================")
    print("  OPERACION 4: Creacion correcta de los tres servicios")
    print("==============================================================")
    servicios_sim = []
    definiciones = [
        ("ReservaSala",    lambda: ReservaSala("Sala Innovacion", 50000, 10)),
        ("AlquilerEquipo", lambda: AlquilerEquipo("Laptop HP", 15000, 5)),
        ("Asesoria",       lambda: Asesoria("Dr. Martinez", 80000, "legal")),
    ]
    for nombre_clase, crear in definiciones:
        try:
            servicio = crear()
            log_info(f"Servicio creado: {servicio.describir()}")
            servicios_sim.append(servicio)
            servicios.append(servicio)
            sim_operaciones += 1
            print(f"[OK] {servicio.describir()}")
        except ServicioError as e:
            log_error(f"Error al crear {nombre_clase}: {e}")
            print(f"[ERROR] {e}")
        print(f"     Intento de creacion de {nombre_clase} terminado.")
    print("-> Operacion 4 finalizada.")
    
    # OPERACION 5 - Creacion INCORRECTA de servicio (precio negativo)
    print("\n==============================================================")
    print("  OPERACION 5: Creacion de servicio con precio invalido")
    print("==============================================================")
    try:
        ReservaSala("Sala Error", -5000, 8)
    except ParametroInvalidoError as e:
        log_error(f"Error al crear servicio con precio negativo: {e}")
        print(f"[ERROR] Error capturado correctamente: {e}")
        sim_operaciones += 1
    print("-> El sistema continua estable tras el error.")
    print("-> Operacion 5 finalizada.")
    
    # OPERACION 6 - Reserva EXITOSA con confirmacion y procesamiento
    print("\n==============================================================")
    print("  OPERACION 6: Reserva exitosa: confirmacion y procesamiento")
    print("==============================================================")
    if cliente and servicios_sim:
        try:
            sala = servicios_sim[0]
            reserva = Reserva(cliente, sala, 3)
            log_info(f"Reserva creada: cliente={cliente.get_nombre()} | servicio={sala.nombre} | duracion=3h")
            reservas.append(reserva)
            sim_operaciones += 1
        except ReservaError as e:
            log_error(f"Error al crear reserva exitosa: {e}")
            print(f"[ERROR] {e}")
        else:
            print(f"[OK] Reserva creada | Estado: {reserva.estado}")
            reserva.confirmar()
            print(f"[OK] Reserva confirmada | Estado: {reserva.estado}")
            reserva.procesar()
            log_info("Reserva procesada exitosamente en operacion 6")
            sim_operaciones += 1
    else:
        print("[AVISO] No hay cliente o servicios disponibles.")
    print("-> Operacion 6 finalizada.")
    
    # OPERACION 7 - Reserva FALLIDA por duracion invalida (cero)
    print("\n==============================================================")
    print("  OPERACION 7: Reserva fallida: duracion invalida (cero)")
    print("==============================================================")
    if cliente and servicios_sim:
        try:
            equipo = servicios_sim[1]
            Reserva(cliente, equipo, 0)
        except (DuracionInvalidaError, ReservaError) as e:
            log_error(f"Error al crear reserva con duracion invalida: {e}")
            print(f"[ERROR] Error capturado correctamente: {e}")
            sim_operaciones += 1
    else:
        print("[AVISO] No hay cliente o servicios disponibles.")
    print("-> Operacion 7 finalizada.")
    
    # OPERACION 8 - Intento de confirmar reserva YA CANCELADA
    print("\n==============================================================")
    print("  OPERACION 8: Operacion sobre reserva ya cancelada")
    print("==============================================================")
    if cliente and servicios_sim:
        try:
            asesoria = servicios_sim[2]
            reserva = Reserva(cliente, asesoria, 2)
            reservas.append(reserva)
            sim_operaciones += 1
            reserva.cancelar()
            print(f"[OK] Reserva cancelada | Estado: {reserva.estado}")
            # Intento de confirmar una reserva ya cancelada -> error
            reserva.confirmar()
        except ReservaCanceladaError as e:
            log_error(f"Intento de confirmar reserva cancelada: {e}")
            print(f"[ERROR] Error capturado correctamente: {e}")
            sim_operaciones += 1
        except ReservaError as e:
            log_error(f"ReservaError en operacion 8: {e}")
            print(f"[ERROR] {e}")
    else:
        print("[AVISO] No hay cliente o servicios disponibles.")
    print("-> Operacion 8 finalizada.")
    
    # OPERACION 9 - Calculo de costos con VARIANTES SOBRECARGADAS
    print("\n==============================================================")
    print("  OPERACION 9: Calculo de costos de los servicios")
    print("==============================================================")
    if servicios_sim:
        try:
            sala     = servicios_sim[0]
            equipo   = servicios_sim[1]
            asesoria = servicios_sim[2]

            # Costo de reserva de sala por 2 horas
            costo_sala = sala.calcular_costo(2)
            print(f"[OK] [{sala.nombre}] Costo por 2 horas: ${costo_sala}")

            # Costo de alquiler de equipo por 3 horas y 5 equipos
            costo_equipo = equipo.calcular_costo(3, 5)
            print(f"[OK] [{equipo.nombre}] Costo por 3 horas y 5 equipos: ${costo_equipo}")

            # Costo de asesoria por 1 hora
            costo_asesoria = asesoria.calcular_costo(1)
            print(f"[OK] [{asesoria.nombre}] Costo por 1 hora: ${costo_asesoria}")

            log_info("Operacion 9: calculo de costos completado")
            sim_operaciones += 1

        except (ServicioError, ParametroInvalidoError, CostoInvalidoError) as e:
            log_error(f"Error en calculo de costos: {e}")
            print(f"[ERROR] {e}")
    else:
        print("[AVISO] No hay servicios disponibles.")
    print("-> Operacion 9 finalizada.")
    
    # OPERACION 10 - Servicio NO DISPONIBLE + encadenamiento de excepciones
    print("\n==============================================================")
    print("  OPERACION 10: Servicio no disponible + encadenamiento de excepciones")
    print("==============================================================")
    if cliente:
        try:
            # Intentamos crear una sala con capacidad inválida
            ReservaSala("Sala Ocupada", 60000, -1)
        except ParametroInvalidoError as e:
            log_error(f"Error en operacion 10: {e}")
            print(f"[ERROR] Capturado: {e}")
            # Encadenamiento: el error del servicio causa un error de reserva
            try:
                raise ReservaInvalidaError("No se puede crear la reserva porque el servicio no es válido") from e
            except ReservaInvalidaError as re:
                log_exception(f"Excepcion encadenada en operacion 10: {re}")
                print(f"[ERROR] Excepcion encadenada: {re}")
                print(f"        Causa original: {re.__cause__}")
            sim_operaciones += 1
    else:
        print("[AVISO] No hay cliente disponible.")
    print("-> Sistema estable. Todas las excepciones fueron manejadas.")
    print("-> Operacion 10 finalizada.")
    
    print("\n" + "="*62)
    print(f"  Simulación completada. Operaciones realizadas: {sim_operaciones}")
    print("  Revisa logs/app.log para el detalle completo de eventos.")
    print("="*62)
    
    return sim_operaciones


def mostrar_logs():
    """Muestra el contenido del archivo de logs."""
    try:
        with open("logs/app.log", "r", encoding="utf-8", errors="replace") as f:
            contenido = f.read()
            print("\n" + "="*50)
            print("CONTENIDO DE LOGS:")
            print("="*50)
            print(contenido if contenido else "El archivo de logs está vacío.")
            print("="*50)
    except FileNotFoundError:
        print("[ERROR] Archivo de logs no encontrado.")
    except Exception as e:
        print(f"[ERROR] Error al leer logs: {e}")


# ══════════════════════════════════════════════════════════════════════════════
# MENÚ PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════

def menu_principal():
    """Muestra el menú principal del sistema."""
    print("\n" + "="*60)
    print("  SISTEMA DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS")
    print("  Software FJ - UNAD (213023)")
    print("="*60)
    print("1. Registrar cliente")
    print("2. Crear servicio")
    print("3. Crear reserva")
    print("4. Gestionar reserva (confirmar/cancelar/procesar)")
    print("5. Calcular costo de servicio")
    print("6. Mostrar logs")
    print("7. Simulación automática de 10 operaciones")
    print("8. Salir")
    print("="*60)


# ══════════════════════════════════════════════════════════════════════════════
# PUNTO DE ENTRADA PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n" + "*" * 62)
    print("  Software FJ - Sistema de Gestion de Clientes y Reservas")
    print("  Curso: Programacion UNAD (213023)")
    print("*" * 62)

    log_info("=" * 50)
    log_info("INICIO DE SESIÓN INTERACTIVA - Software FJ")
    log_info("=" * 50)

    clientes = []
    servicios = []
    reservas = []
    operaciones = 0

    while True:
        menu_principal()
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        if opcion == "1":
            cliente = registrar_cliente()
            if cliente:
                clientes.append(cliente)
                operaciones += 1
        elif opcion == "2":
            servicio = crear_servicio()
            if servicio:
                servicios.append(servicio)
                operaciones += 1
        elif opcion == "3":
            reserva = crear_reserva(clientes, servicios)
            if reserva:
                reservas.append(reserva)
                operaciones += 1
        elif opcion == "4":
            gestionar_reserva(reservas)
            operaciones += 1
        elif opcion == "5":
            calcular_costo_servicio(servicios)
            operaciones += 1
        elif opcion == "6":
            mostrar_logs()
        elif opcion == "7":
            sim_op = simulacion_automatica(clientes, servicios, reservas)
            operaciones += sim_op
        elif opcion == "8":
            break
        else:
            print("[ERROR] Opción inválida. Intente nuevamente.")
            continue
        
        print(f"\nOperaciones realizadas: {operaciones}")
        if operaciones >= 10:
            print("[INFO] Ha completado al menos 10 operaciones. Puede continuar o salir.")
    
    print("\n" + "*" * 62)
    print(f"  Sesión finalizada. Total operaciones: {operaciones}")
    print("  Revisa logs/app.log para el detalle completo de eventos.")
    print("*" * 62)
    

    log_info(f"FIN DE SESIÓN - Total operaciones: {operaciones}")
