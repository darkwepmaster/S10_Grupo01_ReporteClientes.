import pandas as pd
from services.reporte_service import construir_dataframe, exportar_clientes

REGISTROS = [{"id": 1, "nombres": "Ana", "apellidos": "Torres", "edad": 21}]


def test_construir_dataframe_con_registros():
    df = construir_dataframe(REGISTROS)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert list(df.columns) == ["ID", "Nombres", "Apellidos", "Edad"]


def test_construir_dataframe_vacio():
    assert construir_dataframe([]).empty


def test_exportar_genera_xlsx(tmp_path):
    ruta = exportar_clientes(construir_dataframe(REGISTROS), carpeta=str(tmp_path))
    assert ruta.exists() and ruta.suffix == ".xlsx"
