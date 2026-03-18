import logging
import os
from datetime import datetime
 
LOG_FILE = "bitácora.log"
 
def configurar_bitacora():
    logger = logging.getLogger("laboratorio")
    logger.setLevel(logging.DEBUG)
 
    if logger.handlers:
        logger.handlers.clear()
 
    file_handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
 
    logger.addHandler(file_handler)
    return logger
 
 
def obtener_logger():
    return logging.getLogger("laboratorio")
 
 
def log_inicio_simulacion(capacidad: int):
    logger = obtener_logger()
    logger.info("=" * 55)
    logger.info("     INICIO DE SIMULACIÓN DEL LABORATORIO")
    logger.info(f"     Fecha/Hora : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"     Capacidad  : {capacidad} computadora(s)")
    logger.info("=" * 55)
 
 
def log_estudiante_esperando(id_est, nombre):
    logger = obtener_logger()
    logger.info(f"[ID {id_est:02d}] {nombre:<15} → ESPERANDO   | Intentando adquirir semáforo...")
 
 
def log_semaforo_adquirido(id_est, nombre, num_pc, tarea, tiempo, disponibles, capacidad):
    logger = obtener_logger()
    logger.info(
        f"[ID {id_est:02d}] {nombre:<15} → ACCESO OK   | "
        f"PC {num_pc} | Tarea: '{tarea}' | Tiempo: {tiempo}s | "
        f"Disponibles: {disponibles}/{capacidad}"
    )
 
 
def log_mutex_adquirido(id_est, nombre, accion: str):
    logger = obtener_logger()
    logger.debug(f"[ID {id_est:02d}] {nombre:<15} → MUTEX ON    | {accion}")
 
 
def log_mutex_liberado(id_est, nombre, accion: str):
    logger = obtener_logger()
    logger.debug(f"[ID {id_est:02d}] {nombre:<15} → MUTEX OFF   | {accion}")
 
 
def log_estudiante_termino(id_est, nombre, tarea, num_pc, disponibles, capacidad):
    logger = obtener_logger()
    logger.info(
        f"[ID {id_est:02d}] {nombre:<15} → TERMINÓ     | "
        f"Tarea: '{tarea}' en PC {num_pc} | "
        f"Disponibles: {disponibles}/{capacidad}"
    )
 
 
def log_semaforo_liberado(id_est, nombre):
    logger = obtener_logger()
    logger.info(f"[ID {id_est:02d}] {nombre:<15} → SEMÁFORO ↑  | Recurso liberado.")
 
 
def log_fin_simulacion(capacidad, disponibles):
    logger = obtener_logger()
    logger.info("=" * 55)
    logger.info("     FIN DE SIMULACIÓN")
    logger.info(f"     Computadoras totales : {capacidad}")
    logger.info(f"     Computadoras libres  : {disponibles}")
    logger.info("=" * 55)
    logger.info(f"Bitácora guardada en: {os.path.abspath(LOG_FILE)}")