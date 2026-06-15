# CV Dashboard — Christian Daniel Morán Titla

Dos versiones del mismo CV con identidad **Cocui Dev** (teal `#1F7A72`, rojo `#C43A2A`,
ink `#1C2833`; tipografías DM Serif Display + DM Sans + JetBrains Mono):

1. **`index.html`** — versión estática autocontenida para **GitHub Pages**.
2. **`cv_dashboard/`** — dashboard interactivo en **Dash (Plotly)** servido con **FastAPI**.

---

## 1. Versión estática (GitHub Pages)

`index.html` no requiere build: HTML + CSS + JS en un solo archivo (las fuentes se
cargan desde Google Fonts por CDN). Los logos y la foto van en la carpeta
`assets/` **junto** a `index.html` (rutas relativas `assets/...`).

### Publicar
```bash
# en un repo nuevo, p. ej. cv
git init
git add index.html assets/
git commit -m "CV dashboard"
git branch -M main
git remote add origin git@github.com:<usuario>/cv.git
git push -u origin main
```
Luego en GitHub → **Settings → Pages → Source: `main` / root**. Queda en
`https://<usuario>.github.io/cv/`.

> Para usar tu dominio (`cv.cocuidev.mx`) añade un archivo `CNAME` con el host
> y el registro DNS correspondiente en Cloudflare.

---

## 2. Versión Dash + FastAPI

```
cv_dashboard/
├── cv_data.py      # todos los datos del CV (editar aquí)
├── dashboard.py    # layout Dash + figuras Plotly (presentación)
├── server.py       # FastAPI que monta el dashboard vía WSGI
├── requirements.txt
└── assets/         # logos + foto (Dash los sirve automáticamente)
```

### Instalar y correr
```bash
cd cv_dashboard
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Producción / desarrollo con FastAPI:
uvicorn server:app --reload
# -> http://127.0.0.1:8000/  (redirige a /dashboard/)
#    http://127.0.0.1:8000/api/health
```

Para iterar solo el dashboard sin FastAPI:
```bash
python dashboard.py        # -> http://127.0.0.1:8050/
```

### Arquitectura
Dash corre sobre Flask (WSGI). FastAPI es ASGI, así que el dashboard se monta con
un adaptador WSGI→ASGI (`a2wsgi`) bajo `/dashboard`. El `requests_pathname_prefix`
de Dash coincide con el punto de montaje para que los assets resuelvan bien:

```python
dash_app = create_dash_app(requests_pathname_prefix="/dashboard/")
app.mount("/dashboard", WSGIMiddleware(dash_app.server))
```

Esto deja FastAPI libre para añadir endpoints REST, auth, webhooks de pago, etc.,
junto al dashboard.

### Desplegar
- **Docker / VM:** `uvicorn server:app --host 0.0.0.0 --port 8000` detrás de Nginx,
  o con workers: `gunicorn -k uvicorn.workers.UvicornWorker server:app`.
- **Cloud Run / Railway / Fly.io:** mismo comando; exponer el puerto vía `$PORT`.

### Actualizar el CV
Editar solo **`cv_data.py`**. La versión estática se actualiza en `index.html`.
