import logging
from db import get_connection

logger = logging.getLogger(__name__)


def listar_clientes():
    sql = """
        SELECT id, nombres, apellidos, edad
        FROM dbo.clientes
        ORDER BY apellidos, nombres
    """
    with get_connection() as cn:
        cursor = cn.cursor()
        cursor.execute(sql)
        columnas = [c[0] for c in cursor.description]
        filas = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    logger.info("Clientes consultados: %s", len(filas))
    return filas


def listar_clientes_por_edad(edad_minima: int):
    """Consulta parametrizada: el valor del usuario nunca se concatena al SQL."""
    sql = """
        SELECT id, nombres, apellidos, edad
        FROM dbo.clientes
        WHERE edad >= ?
        ORDER BY apellidos, nombres
    """
    with get_connection() as cn:
        cursor = cn.cursor()
        cursor.execute(sql, edad_minima)
        columnas = [c[0] for c in cursor.description]
        return [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
