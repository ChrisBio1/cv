"""Datos estructurados del CV de Christian Daniel Morán Titla.

Centraliza todo el contenido para que el dashboard (dashboard.py) sea
puramente de presentación. Editar aquí para actualizar el CV.
"""

# ---------------------------------------------------------------- branding
COLORS = {
    "ink": "#1C2833",
    "ink2": "#15303a",
    "teal": "#1F7A72",
    "teal_bright": "#2A9D8F",
    "red": "#C43A2A",
    "grey": "#808B96",
    "bg": "#EEF2F1",
    "surface": "#FFFFFF",
    "line": "#E1E7E6",
    "text": "#22313b",
}

PROFILE = {
    "name": "Christian Daniel Morán Titla",
    "title": "Científico de datos",
    "kicker": "Biólogo · M.C. Ecología Integrativa · Esp. Métodos Estadísticos",
    "location": "Huitzilac, Morelos, México",
    "phone": "222 109 7767",
    "email": "christianbiotitla@gmail.com",
    "linkedin": "https://www.linkedin.com/in/christian-daniel-mor%C3%A1n-titla-a99418130/",
    "github": "https://github.com/",
    "gitlab": "https://gitlab.com/",
    "site": "https://cocuidev.mx",
    "photo": "foto.png",
    "brand_logo": "cocuite-dev.png",
    "summary": (
        "Investigo poblaciones y comunidades biológicas desde la ecología, la "
        "biogeografía y la bioacústica, aplicando machine learning, inteligencia "
        "artificial, modelado matemático y estadística. Especialista en métodos "
        "estadísticos para problemas de ciencias sociales, exactas, biológicas y "
        "finanzas corporativas. Actualmente lidero proyectos de analítica avanzada, "
        "modelos de ML, desarrollo DevOps y agentes de IA."
    ),
}

KPIS = [
    ("+10", "Años en estadística e investigación"),
    ("5", "Programas académicos · Lic → Doctorado"),
    ("3", "Publicaciones científicas"),
    ("8+", "Áreas de especialización"),
]

# Botones de filtro (id interno, etiqueta visible). "todos" siempre primero.
CATEGORIES = [
    ("todos", "Todos"),
    ("investigacion", "Investigación"),
    ("analitica", "Analítica Avanzada"),
    ("mlia", "ML & IA"),
    ("bi", "BI"),
    ("devops", "DevOps"),
]

# (periodo, puesto, organización, [bullets], vigente, [(logo, oscuro)], [tags])
EXPERIENCE = [
    ("Ene. 2026 — Actual", "Consultor de investigación en bioacústica", "CONABIO · Contrato temporal", [
        "Plataforma interactiva de paisaje sonoro de distintas regiones de México (proyecto CoSMoS).",
        "Índices de paisaje sonoro como equivalencia de integridad ecosistémica.",
        "Storytelling de historias de usuario entre lo teórico y lo didáctico.",
    ], True, [("conabio.png", False)], ["investigacion", "analitica", "devops", "mlia", "bi"]),
    ("Ene. 2025 — Actual", "Científico de Datos", "Grupo Financiero Base · Banco Base", [
        "Retención y ofertas de spread (IA): red neuronal profunda que predice fuga de clientes FX sobre modelos BTYD; maximización del spread sin comprometer la relación contractual.",
        "BI de fondeo de tesorería: dashboards en Tableau y Power BI de operaciones de divisas.",
        "ETL de utilidades: vista materializada transaccional (extracción, limpieza, transformación, cruce, validación e ingesta).",
    ], True, [("banco-base.png", False)], ["analitica", "mlia", "bi", "devops"]),
    ("Ene. 2024 — Actual", "Científico de Datos MLOps", "Cocui Dev · Consultoría independiente", [
        "DevOps de flujos: implementación (API/preprocesamiento, EDA/MLOps), despliegue (CI-CD) y monitoreo (ETL/BI).",
        "App web de IA para identificación de especies de aves por canto.",
        "POS de restaurante y agente de IA para clasificación de artículos y metaanálisis automático.",
    ], True, [("cocuite-dev.png", True)], ["investigacion", "mlia", "devops", "bi"]),
    ("Mar. 2017 — Actual", "Asesor de campo y de investigación", "Facultad de Ciencias Biológicas · BUAP", [
        "Gestión de proyectos de bioacústica in situ (objetivos, hipótesis, diseño de muestreo).",
        "Toma de datos con dispositivos acústicos, preprocesamiento, análisis estadístico e interpretación.",
    ], True, [("buap.png", True)], ["investigacion", "analitica"]),
    ("Abr. 2024 — Ene. 2025", "Gerente de IA y crimen financiero", "Grupo FINDEP · Financiera Independencia", [
        "DevOps y gestión de modelos de IA: blindaje financiero con modelos de identidad, contactabilidad y fraude.",
    ], False, [("findep.png", False)], ["analitica", "mlia", "devops", "bi"]),
    ("Ago. 2022 — Abr. 2024", "Consultor de conocimiento de mercado · BI", "Grupo Salinas · Banco Azteca", [
        "Pronósticos de fondeo de remesas, análisis de KPI's, segmentación de clientes y modelos BTYD.",
    ], False, [("azteca.png", False)], ["analitica", "bi"]),
    ("2017 — 2022", "Trayectoria temprana en datos & estadística", "INEGI · DAI · Latreach / Base 10", [
        "INEGI (2022): enlace de vinculación estadística 'C' — geoestadística, ML y análisis de texto.",
        "DAI (2019): analista estadístico — docencia, investigación y consultoría.",
        "Latreach (2017): data scientist — inteligencia de negocios y data marketing.",
    ], False, [("inegi.jpeg", False), ("dai.jpg", True), ("base.jpg", True)],
        ["investigacion", "analitica", "mlia", "bi"]),
]

# (área, años, nivel 0-100, [tags])
SPECIALIZATION = [
    ("Estadística avanzada", 10, 98, ["analitica", "investigacion"]),
    ("Métodos de investigación", 10, 96, ["investigacion"]),
    ("Bioacústica · Biogeografía · Ecología", 10, 95, ["investigacion"]),
    ("Machine Learning", 8, 88, ["mlia", "analitica"]),
    ("Sistemas de información geográfica", 6, 78, ["analitica", "investigacion"]),
    ("Inteligencia artificial", 4, 68, ["mlia"]),
    ("Inteligencia de negocios", 4, 66, ["bi", "analitica"]),
    ("DevOps", 2, 52, ["devops"]),
]

# (lenguaje, nivel 0-5, [tags])
LANGUAGES_CODE = [
    ("SQL", 5.0, ["analitica", "bi", "devops"]),
    ("Python", 5.0, ["mlia", "analitica", "devops", "investigacion"]),
    ("R", 4.5, ["analitica", "investigacion", "mlia"]),
    ("JavaScript", 3.0, ["devops"]),
    ("HTML / CSS", 3.5, ["devops"]),
    ("Julia", 2.0, ["analitica", "investigacion"]),
]

# (herramienta, puntos 0-5, [tags]) — Power BI primero, luego Tableau, luego Looker
BI_TOOLS = [
    ("Power BI", 5, ["bi"]),
    ("Tableau", 4, ["bi"]),
    ("Looker Studio", 3, ["bi"]),
]
CLOUD = [
    ("Google Cloud", 4, ["devops", "mlia", "analitica"]),
    ("AWS · Cloudera", 3, ["devops", "mlia", "analitica"]),
    ("RStudio Server", 4, ["devops", "analitica", "investigacion"]),
]

LANGUAGES_HUMAN = [("Español", "Nativo", 100), ("Inglés", "B1", 55)]

# (grupo, [tags], [chips], [chips destacados])
STACK = [
    ("Técnicas ML & IA", ["mlia", "analitica"],
     ["Supervisado", "No supervisado", "Semisupervisado", "Refuerzo",
      "scikit-learn", "TensorFlow", "Keras", "PyTorch", "OpenCV", "Ollama",
      "Series de tiempo", "Reconocimiento de imágenes"],
     ["Supervisado", "No supervisado", "Semisupervisado", "Refuerzo"]),
    ("DevOps & nube", ["devops"],
     ["FastAPI", "Flask", "Shiny", "React", "Docker", "MLflow", "H2O",
      "Pipelines · CI/CD", "AWS", "Google Cloud", "Firebase", "BigQuery",
      "Netlify", "GitHub / GitLab"],
     ["AWS", "Google Cloud", "Firebase", "BigQuery"]),
    ("Software & SIG", ["investigacion", "analitica", "bi"],
     ["Raven", "Audacity", "QGIS", "ArcGIS", "IDRISI", "Jupyter", "RStudio",
      "VS Code", "Tableau", "Power BI", "Looker Studio"],
     []),
    ("Metodología & datos", ["investigacion", "analitica", "devops", "bi"],
     ["Método científico", "Scrum", "Docencia", "Investigación",
      "Big Data", "Procesos ETL", "API's", "Scraping", "Linux · Mac · Windows"],
     ["Método científico", "Scrum"]),
]

# (año, grado, institución, [(badge, tipo)], (logo, oscuro), [tags])
EDUCATION = [
    ("2026", "Doctorado en Ciencias Biológicas", "UNAM",
     [("En curso", "go"), ("Promedio 10", "grade")], ("unam.png", True),
     ["investigacion", "analitica", "mlia"]),
    ("2025", "Maestría en Ciencia de Datos", "INFOTEC",
     [("En curso", "go"), ("Promedio 9.6", "grade")], ("infotec_posgrados.png", True),
     ["mlia", "analitica", "devops", "bi"]),
    ("2023", "Especialidad en Métodos Estadísticos", "CIMAT",
     [("Promedio 10.0", "grade")], ("cimat.png", True),
     ["analitica", "investigacion"]),
    ("2023", "Maestría en Ecología Integrativa", "INIRENA · UMSNH",
     [("Promedio 9.83", "grade")], ("inirena.png", False),
     ["investigacion"]),
    ("2018", "Licenciatura en Biología", "BUAP",
     [("Promedio 7.88", "grade")], ("buap.png", True),
     ["investigacion"]),
]

# (año, título, fuente, doi/url, [tags])
PUBLICATIONS = [
    ("2025", "Niche-related processes explain phylogenetic structure of acoustic bird communities in Mexico",
     "Morán-Titla CD, García-Chávez J, López-Toledo L, González C. PeerJ 13:e18412",
     "https://doi.org/10.7717/peerj.18412", ["investigacion", "analitica"]),
    ("2022", "El mejor lugar para cantar: hipótesis de adaptación acústica en aves",
     "Morán Titla CD, González C. Elementos 126 (2022) 81–88.", "", ["investigacion"]),
    ("2019", "Description and statistical analysis of the SOD1 network and its genetic properties",
     "Russian Journal of Biological Physics and Chemistry, 1:4, 131–137.", "",
     ["investigacion", "analitica"]),
]

CERTIFICATIONS = [
    ("2025", "Diplomado en Inteligencia Artificial Aplicada"),
    ("2024", "Google: IA y productividad"),
    ("2024", "Negociación"),
    ("2022", "Scrum Fundamentals Certified"),
    ("2018", "Diplomado en sistemas dinámicos"),
]
CERTIFICATIONS_TAGS = ["mlia", "devops", "analitica"]

CONFERENCES = [
    ("2021", "Competencia por el nicho acústico y estructura filogenética de comunidades de aves — XVIII Congreso para el Estudio y Conservación de las Aves en México"),
    ("2018", "Comunidad acústica de la ornitofauna en zona semiárida (Reserva Tehuacán–Cuicatlán) — II Congreso Internacional de ANP"),
    ("2017", "Relación espacial del canto de Toxostoma curvirostre — XV Congreso para el Estudio y Conservación de las Aves en México"),
]
CONFERENCES_TAGS = ["investigacion"]

# Talleres impartidos y educación continua (con sus tags)
WORKSHOPS = [
    ("2019", "Análisis bioestadístico con R (enfoque biomédico), 60 h — Facultad de Medicina, BUAP"),
    ("2018", "Diplomado de estadística con R, Módulo III: análisis multivariado — Ciencias Biológicas, BUAP"),
]
WORKSHOPS_TAGS = ["investigacion", "analitica"]

CONTINUING = [
    ("2025", "Bootcamp Ecosistema Llama para desarrollo de IA — INFOTEC"),
    ("2021", "Geointeligencia computacional · Julia de alto rendimiento (IIMAS, UNAM)"),
    ("2020", "Modelado de nicho ecológico · Genómica de la conservación (INECOL)"),
]
CONTINUING_TAGS = ["mlia", "analitica", "investigacion"]

INTERESTS = ["Artes marciales", "Apreciación musical", "Observación de aves", "Fotografía científica"]
