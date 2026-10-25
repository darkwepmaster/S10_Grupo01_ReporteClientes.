import logging_config  # noqa: F401  (configura logging al importarse)
from flask import Flask
from controllers.reportes_controller import reportes_bp

app = Flask(__name__)
app.register_blueprint(reportes_bp)


@app.get("/")
def inicio():
    return '<a href="/reportes/clientes">Descargar reporte de clientes (.xlsx)</a>'


if __name__ == "__main__":
    app.run(debug=False)
