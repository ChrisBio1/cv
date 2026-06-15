"""Servidor FastAPI que expone el dashboard del CV (Dash) en producción.

El dashboard de Dash corre sobre Flask (WSGI) y se monta dentro de FastAPI
(ASGI) con un adaptador WSGI. FastAPI queda libre para añadir endpoints REST
(p. ej. /api/health) junto al dashboard.

Ejecutar:
    uvicorn server:app --reload
Luego abrir http://127.0.0.1:8000/  (redirige a /dashboard/)
"""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from dashboard import create_dash_app

# Adaptador WSGI->ASGI. Starlette movió WSGIMiddleware a a2wsgi en versiones
# recientes; intentamos ambas rutas para máxima compatibilidad.
try:
    from a2wsgi import WSGIMiddleware
except ImportError:  # pragma: no cover
    from fastapi.middleware.wsgi import WSGIMiddleware

# El prefijo DEBE coincidir con el punto de montaje y terminar en "/".
DASH_PREFIX = "/dashboard/"

app = FastAPI(
    title="CV · Christian Daniel Morán Titla",
    description="Dashboard interactivo del CV servido con FastAPI + Dash.",
    version="1.0.0",
)

dash_app = create_dash_app(requests_pathname_prefix=DASH_PREFIX)


@app.get("/", include_in_schema=False)
def root() -> RedirectResponse:
    """Redirige la raíz al dashboard."""
    return RedirectResponse(url=DASH_PREFIX)


@app.get("/api/health")
def health() -> dict:
    """Endpoint de salud para monitoreo / load balancers."""
    return {"status": "ok", "service": "cv-dashboard"}


# Monta la app Dash (Flask/WSGI) bajo /dashboard.
app.mount("/dashboard", WSGIMiddleware(dash_app.server))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
