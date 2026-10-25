import logging
from flask import Blueprint, send_file
from dao.clientes_dao import listar_clientes
from services.reporte_service import construir_dataframe, exportar_clientes

reportes_bp = Blueprint("reportes", __name__)
logger = logging.getLogger(__name__)


@reportes_bp.get("/reportes/clientes")
def descargar_clientes():
    logger.info("Solicitud de reporte de clientes")
    try:
        registros = listar_clientes()
        df = construir_dataframe(registros)

        if df.empty:
            logger.warning("Reporte solicitado sin datos disponibles")
            return "No existen datos para exportar", 404

        ruta = exportar_clientes(df)
        return send_file(ruta.resolve(), as_attachment=True)
    except Exception:
        logger.exception("No fue posible generar el reporte")
        return "Error interno al generar el reporte", 500
