"""Dashboard del CV en Dash.

Expone create_dash_app(requests_pathname_prefix) para montarlo dentro de FastAPI.
La app es de presentación: todos los datos viven en cv_data.py.

Filtros por área (Investigación, Analítica Avanzada, ML & IA, BI, DevOps): al
seleccionar un botón, SOLO permanecen visibles los items (y secciones) que
pertenecen a esa área; el resto se contrae. "Todos" restablece la vista.
"""
from dash import Dash, html, dcc, Input, Output, State, ctx, ALL
from dash.exceptions import PreventUpdate

import cv_data as D

C = D.COLORS
FONTS = '"Jost", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif'
SERIF = '"Coves", "Jost", system-ui, sans-serif'   # display
MONO = '"JetBrains Mono", ui-monospace, monospace'


# ============================================================ builder
class Builder:
    """Registra items y secciones filtrables y les asigna ids de patrón."""

    def __init__(self):
        self.item_tags = {}      # index -> [tags]
        self.section_tags = {}   # name  -> set(tags)

    def item(self, component, tags, sections):
        idx = len(self.item_tags)
        self.item_tags[idx] = list(tags)
        for s in sections:
            self.section_tags.setdefault(s, set()).update(tags)
        return html.Div(component, id={"type": "cv-item", "index": idx}, style={})

    def section(self, name, component):
        self.section_tags.setdefault(name, set())
        return html.Div(component, id={"type": "cv-section", "name": name}, style={})


# ============================================================ small ui
def chip(text, accent=False):
    return html.Span(text, style={
        "fontFamily": MONO, "fontSize": "11.5px",
        "padding": "5px 10px", "borderRadius": "7px",
        "background": "rgba(31,122,114,.08)" if accent else C["bg"],
        "color": C["teal"] if accent else "#3a4a54",
        "border": f"1px solid {'rgba(31,122,114,.2)' if accent else C['line']}",
        "display": "inline-block", "margin": "0 6px 6px 0",
    })


def card(children, pad="22px"):
    return html.Div(children, style={
        "background": C["surface"], "border": f"1px solid {C['line']}",
        "borderRadius": "14px", "padding": pad,
        "boxShadow": "0 1px 2px rgba(28,40,51,.04), 0 8px 24px rgba(28,40,51,.06)",
    })


def card_title(text):
    return html.H3(text, style={
        "fontSize": "13px", "letterSpacing": ".14em", "textTransform": "uppercase",
        "color": C["grey"], "fontWeight": "600", "margin": "0 0 16px",
    })


def logo_tile(asset, filename, dark=False, sm=False):
    size = "38px" if sm else "48px"
    radius = "9px" if sm else "12px"
    return html.Div(
        html.Img(src=asset(filename), alt="",
                 style={"width": "100%", "height": "100%", "objectFit": "contain", "padding": "6px"}),
        style={"width": size, "height": size, "borderRadius": radius, "flex": "none",
               "overflow": "hidden", "display": "flex", "alignItems": "center",
               "justifyContent": "center",
               "background": C["ink"] if dark else "#fff",
               "border": "none" if dark else f"1px solid {C['line']}"},
    )


def catbtn_style(active=False):
    return {
        "fontFamily": MONO, "fontSize": "12.5px", "padding": "9px 15px",
        "borderRadius": "999px", "cursor": "pointer", "fontWeight": "600",
        "transition": "all .15s",
        "border": f"1px solid {C['teal'] if active else C['line']}",
        "background": C["teal"] if active else "#fff",
        "color": "#fff" if active else C["text"],
    }


def category_buttons():
    return html.Div(
        [html.Button(label, id={"type": "cat-btn", "cat": cat}, n_clicks=0,
                     style=catbtn_style(cat == "todos"))
         for cat, label in D.CATEGORIES],
        style={"display": "flex", "flexWrap": "wrap", "gap": "9px"},
    )


def section_head(title):
    return html.Div([
        html.H2(title, style={
            "fontFamily": SERIF, "fontWeight": "300", "fontSize": "34px",
            "color": C["ink"], "letterSpacing": ".02em", "margin": "0",
            "whiteSpace": "nowrap",
        }),
        html.Div(style={"flex": "1", "height": "1px", "background": C["line"]}),
    ], style={"display": "flex", "alignItems": "center", "gap": "16px", "margin": "0 0 22px"})


# ============================================================ item renderers
def meter_bar(name, right_label, level):
    return html.Div([
        html.Div([
            html.B(name, style={"fontWeight": "600"}),
            html.Em(right_label, style={"fontFamily": MONO, "fontSize": "11.5px",
                                        "color": C["grey"], "fontStyle": "normal"}),
        ], style={"display": "flex", "justifyContent": "space-between",
                  "alignItems": "baseline", "fontSize": "14px", "marginBottom": "6px"}),
        html.Div(html.Div(style={"height": "100%", "width": f"{level}%", "borderRadius": "99px",
                 "background": f"linear-gradient(90deg,{C['teal']},{C['teal_bright']})"}),
                 style={"height": "7px", "borderRadius": "99px", "background": C["bg"],
                        "overflow": "hidden"}),
    ], style={"marginBottom": "15px"})


def dot_row(name, value):
    dots = []
    for i in range(5):
        rem = value - i
        if rem >= 1:
            bg, border = C["teal"], C["teal"]
        elif rem >= 0.5:
            bg = f"linear-gradient(90deg,{C['teal']} 50%,{C['bg']} 50%)"
            border = C["teal"]
        else:
            bg, border = C["bg"], C["line"]
        dots.append(html.I(style={"width": "14px", "height": "14px", "borderRadius": "50%",
                                   "background": bg, "border": f"1px solid {border}",
                                   "display": "inline-block"}))
    return html.Div([
        html.Span(name, style={"fontFamily": MONO, "fontSize": "13.5px", "width": "126px",
                               "fontWeight": "500", "flex": "none"}),
        html.Div(dots, style={"display": "flex", "gap": "6px"}),
    ], style={"display": "flex", "alignItems": "center", "gap": "14px",
              "padding": "9px 0", "borderBottom": f"1px dashed {C['line']}"})


def job_block(job, asset):
    period, pos, org, bullets, current, logos, _tags = job
    accent = C["teal"] if current else C["grey"]
    if len(logos) == 1:
        logo_col = logo_tile(asset, logos[0][0], logos[0][1])
    else:
        logo_col = html.Div([logo_tile(asset, f, d, sm=True) for f, d in logos],
                            style={"display": "flex", "flexDirection": "column",
                                   "gap": "7px", "flex": "none"})
    body = html.Div([
        html.Div(period, style={"fontFamily": MONO, "fontSize": "12px",
                                "color": accent, "fontWeight": "500"}),
        html.Div(pos, style={"fontSize": "17px", "fontWeight": "600",
                             "color": C["ink"], "margin": "3px 0 1px"}),
        html.Div(org, style={"fontSize": "13.5px", "color": C["grey"], "marginBottom": "9px"}),
        html.Ul([
            html.Li(b, style={"marginBottom": "6px", "fontSize": "14px", "color": "#3c4a53"})
            for b in bullets
        ], style={"margin": "0", "paddingLeft": "18px"}),
    ], style={"flex": "1", "minWidth": "0"})
    return html.Div([
        html.Div(style={
            "position": "absolute", "left": "-30px", "top": "6px",
            "width": "16px", "height": "16px", "borderRadius": "50%",
            "background": C["surface"], "border": f"3px solid {accent}",
        }),
        logo_col, body,
    ], style={"position": "relative", "marginBottom": "26px", "display": "flex", "gap": "14px"})


def edu_block(year, deg, where, badges, logo, asset):
    badge_el = []
    for text, kind in badges:
        is_grade = kind == "grade"
        badge_el.append(html.Span(text, style={
            "fontFamily": MONO, "fontSize": "11px", "padding": "3px 9px",
            "borderRadius": "99px", "marginTop": "7px", "marginRight": "6px",
            "display": "inline-block",
            "background": "rgba(196,58,42,.08)" if is_grade else "rgba(31,122,114,.1)",
            "color": C["red"] if is_grade else C["teal"],
        }))
    return html.Div([
        html.Div(year, style={"fontFamily": SERIF, "fontSize": "22px",
                              "color": C["teal"], "width": "64px", "flex": "none"}),
        html.Div([
            html.Div(deg, style={"fontSize": "16px", "fontWeight": "600", "color": C["ink"]}),
            html.Div(where, style={"fontSize": "13.5px", "color": C["grey"]}),
            html.Div(badge_el, style={"marginTop": "2px"}),
        ], style={"flex": "1", "minWidth": "0"}),
        logo_tile(asset, logo[0], logo[1]),
    ], style={"display": "flex", "gap": "16px", "padding": "16px 0",
              "borderBottom": f"1px solid {C['line']}", "alignItems": "center"})


def pub_block(year, title, src, url):
    src_children = [src]
    if url:
        src_children = [src + " · ", html.A(url.replace("https://", ""), href=url,
                        target="_blank", style={"color": C["teal"]})]
    return html.Div([
        html.Div(year, style={"fontFamily": MONO, "fontSize": "13px", "color": C["teal"],
                             "fontWeight": "600", "width": "46px", "flex": "none"}),
        html.Div([
            html.Div(title, style={"fontSize": "14.5px", "fontWeight": "600",
                                   "color": C["ink"], "lineHeight": "1.4"}),
            html.Div(src_children, style={"fontSize": "13px", "color": C["grey"], "marginTop": "3px"}),
        ]),
    ], style={"display": "flex", "gap": "16px", "padding": "15px 0",
              "borderBottom": f"1px solid {C['line']}"})


def year_list(items):
    return html.Ul([
        html.Li([
            html.Span(yr, style={"fontFamily": MONO, "fontSize": "12px", "color": C["teal"],
                                 "fontWeight": "600", "flex": "none", "width": "42px"}),
            html.Span(text, style={"color": "#3c4a53"}),
        ], style={"display": "flex", "gap": "12px", "fontSize": "14px",
                  "alignItems": "flex-start", "marginBottom": "11px"})
        for yr, text in items
    ], style={"listStyle": "none", "margin": "0", "padding": "0"})


# closures over C
def _hero_chip():
    return {"display": "inline-flex", "alignItems": "center", "fontFamily": MONO,
            "fontSize": "12.5px", "padding": "8px 13px", "borderRadius": "999px",
            "background": "rgba(255,255,255,.07)", "border": "1px solid rgba(255,255,255,.12)",
            "color": "#e8edee", "textDecoration": "none"}


def _duo():
    return {"display": "grid", "gridTemplateColumns": "repeat(auto-fit,minmax(280px,1fr))",
            "gap": "20px"}


def _lang_meter(name, level, width):
    return html.Div([
        html.Div([html.B(name), html.Em(level, style={"fontFamily": MONO, "fontSize": "12px",
                  "color": C["grey"], "fontStyle": "normal"})],
                 style={"display": "flex", "justifyContent": "space-between",
                        "fontSize": "14px", "marginBottom": "6px"}),
        html.Div(html.Div(style={"height": "100%", "width": f"{width}%", "borderRadius": "99px",
                 "background": f"linear-gradient(90deg,{C['teal']},{C['teal_bright']})"}),
                 style={"height": "6px", "borderRadius": "99px", "background": C["bg"],
                        "overflow": "hidden"}),
    ], style={"marginBottom": "14px"})


def _link_row(label, url):
    return html.Div(html.A(label, href=url, target="_blank",
                    style={"color": C["text"], "textDecoration": "none"}),
                    style={"fontSize": "14px", "padding": "7px 0",
                           "borderBottom": f"1px solid {C['line']}"})


# ============================================================ layout
def build_layout(asset):
    B = Builder()
    p = D.PROFILE

    # ---------- hero ----------
    hero = html.Div([
        html.Div([
            html.Div([
                html.Div(p["kicker"], style={"fontFamily": MONO, "fontSize": "12.5px",
                         "letterSpacing": ".16em", "textTransform": "uppercase",
                         "color": C["teal_bright"], "marginBottom": "14px"}),
                html.H1(["Christian Daniel ",
                         html.Span("Morán Titla", style={"color": C["teal_bright"],
                                                          "fontWeight": "700"})],
                        style={"fontFamily": SERIF, "fontWeight": "300",
                               "fontSize": "clamp(36px,6.2vw,66px)", "lineHeight": "1.0",
                               "margin": "0", "color": "#fff", "letterSpacing": ".01em"}),
                html.Div([html.Span(p["title"], style={"color": "#fff", "fontWeight": "500"}),
                          " · investigación, machine learning & bioacústica"],
                         style={"marginTop": "12px", "color": "#cdd6da", "fontWeight": "300",
                                "fontSize": "17px"}),
            ]),
            html.Div(html.Img(src=asset(p["photo"]), alt=p["name"],
                     style={"width": "100%", "height": "100%", "objectFit": "cover",
                            "objectPosition": "center"}),
                     style={"width": "132px", "height": "164px", "borderRadius": "18px",
                     "flex": "none", "overflow": "hidden",
                     "background": f"linear-gradient(145deg,{C['teal']},{C['ink2']})",
                     "border": "2px solid rgba(255,255,255,.18)"}),
        ], style={"display": "flex", "justifyContent": "space-between",
                  "alignItems": "flex-start", "gap": "28px", "flexWrap": "wrap"}),

        html.P(p["summary"], style={"maxWidth": "780px", "margin": "26px 0 0",
               "color": "#d7dee1", "fontWeight": "300", "fontSize": "15.5px"}),

        html.Div([
            html.A(f"✉  {p['email']}", href=f"mailto:{p['email']}", style=_hero_chip()),
            html.A([html.Img(src=asset("whatsapp.svg"), alt="WhatsApp",
                             style={"width": "15px", "height": "15px", "marginRight": "8px"}),
                    p["phone"]],
                   href=f"https://wa.me/52{p['phone'].replace(' ', '')}", target="_blank",
                   style=_hero_chip()),
            html.Span(f"⚲  {p['location']}", style=_hero_chip()),
            html.A("in  LinkedIn", href=p["linkedin"], target="_blank", style=_hero_chip()),
            html.A("◆  cocuidev.mx", href=p["site"], target="_blank", style=_hero_chip()),
        ], style={"display": "flex", "flexWrap": "wrap", "gap": "10px", "marginTop": "22px"}),

        html.Div([
            html.Div([
                html.Div(n, style={"fontFamily": SERIF, "fontSize": "40px", "color": "#fff",
                                   "fontWeight": "300", "lineHeight": "1"}),
                html.Div(label, style={"fontFamily": MONO, "fontSize": "11px",
                         "letterSpacing": ".05em", "color": "#aebabd",
                         "textTransform": "uppercase", "marginTop": "8px"}),
            ], style={"background": "rgba(255,255,255,.05)", "padding": "20px 20px 24px"})
            for n, label in D.KPIS
        ], style={"display": "grid", "gridTemplateColumns": "repeat(auto-fit,minmax(200px,1fr))",
                  "gap": "1px", "marginTop": "40px", "background": "rgba(255,255,255,.1)",
                  "borderRadius": "14px 14px 0 0", "overflow": "hidden"}),
    ], style={"maxWidth": "1180px", "margin": "0 auto", "padding": "56px 24px 0"})

    hero_wrap = html.Div(hero, style={
        "background": f"radial-gradient(1000px 460px at 80% -10%, rgba(42,157,143,.22), transparent 60%),"
                      f"linear-gradient(160deg,{C['ink']} 0%,{C['ink2']} 100%)",
    })

    # ---------- aside ----------
    aside = html.Div([
        card([card_title("Idiomas"),
              *[_lang_meter(n, lvl, w) for n, lvl, w in D.LANGUAGES_HUMAN]]),
        card([card_title("Enlaces"),
              _link_row("GitHub", p["github"]),
              _link_row("GitLab", p["gitlab"]),
              _link_row("cocuidev.mx", p["site"])]),
        card([card_title("Intereses"),
              html.Div([chip(i) for i in D.INTERESTS])]),
    ], style={"display": "flex", "flexDirection": "column", "gap": "18px",
              "position": "sticky", "top": "24px"})

    # ---------- main (tagged + collapsible) ----------
    exp_items = [B.item(job_block(j, asset), j[6], ["experiencia"]) for j in D.EXPERIENCE]
    experiencia = B.section("experiencia", html.Section([
        section_head("Experiencia"),
        html.Div(exp_items, style={"position": "relative", "paddingLeft": "30px",
                                   "borderLeft": f"2px solid {C['line']}", "marginLeft": "7px"}),
    ]))

    spec_items = [B.item(meter_bar(n, f"{yr} años", lvl), tags, ["especializacion"])
                  for (n, yr, lvl, tags) in D.SPECIALIZATION]
    especializacion = B.section("especializacion", html.Section([
        section_head("Especialización"),
        card(html.Div(spec_items, style={"display": "grid",
             "gridTemplateColumns": "repeat(auto-fit,minmax(260px,1fr))", "columnGap": "28px"})),
    ]))

    stack_items = [B.item(card([card_title(group),
                                html.Div([chip(t, accent=(t in feat)) for t in chips])]),
                          tags, ["stack"])
                   for (group, tags, chips, feat) in D.STACK]
    stack = B.section("stack", html.Section([
        section_head("Stack & herramientas"),
        html.Div(stack_items, style=_duo()),
    ]))

    lang_rows = [B.item(dot_row(n, v), tags, ["programacion", "prog_lenguajes"])
                 for (n, v, tags) in D.LANGUAGES_CODE]
    bi_rows = [B.item(dot_row(n, v), tags, ["programacion", "prog_bi"])
               for (n, v, tags) in D.BI_TOOLS]
    nube_rows = [B.item(dot_row(n, v), tags, ["programacion", "prog_nube"])
                 for (n, v, tags) in D.CLOUD]
    prog_cards = html.Div([
        B.section("prog_lenguajes", card([card_title("Lenguajes")] + lang_rows)),
        B.section("prog_bi", card([card_title("Business Intelligence")] + bi_rows)),
        B.section("prog_nube", card([card_title("Nube / cómputo")] + nube_rows)),
    ], style=_duo())
    programacion = B.section("programacion", html.Section([
        section_head("Programación & BI"),
        prog_cards,
    ]))

    edu_items = [B.item(edu_block(e[0], e[1], e[2], e[3], e[4], asset), e[5], ["academia"])
                 for e in D.EDUCATION]
    academia = B.section("academia", html.Section([
        section_head("Academia"),
        card(edu_items),
    ]))

    pub_items = [B.item(pub_block(pb[0], pb[1], pb[2], pb[3]), pb[4], ["publicaciones"])
                 for pb in D.PUBLICATIONS]
    publicaciones = B.section("publicaciones", html.Section([
        section_head("Publicaciones"),
        card(pub_items),
    ]))

    mas_cards = html.Div([
        B.item(card([card_title("Certificaciones"), year_list(D.CERTIFICATIONS)]),
               D.CERTIFICATIONS_TAGS, ["mas"]),
        B.item(card([card_title("Ponencias en congresos"), year_list(D.CONFERENCES)]),
               D.CONFERENCES_TAGS, ["mas"]),
        B.item(card([card_title("Talleres impartidos"), year_list(D.WORKSHOPS)]),
               D.WORKSHOPS_TAGS, ["mas"]),
        B.item(card([card_title("Educación continua"), year_list(D.CONTINUING)]),
               D.CONTINUING_TAGS, ["mas"]),
    ], style=_duo())
    mas = B.section("mas", html.Section([
        section_head("Certificaciones & congresos"),
        mas_cards,
    ]))

    main = html.Div([
        category_buttons(),
        experiencia, especializacion, stack, programacion, academia, publicaciones, mas,
    ], style={"minWidth": "0", "display": "flex", "flexDirection": "column", "gap": "40px"})

    body = html.Div([aside, main], style={
        "display": "grid", "gridTemplateColumns": "300px 1fr", "gap": "32px",
        "maxWidth": "1180px", "margin": "0 auto", "padding": "48px 24px 80px",
        "alignItems": "start",
    })

    footer = html.Div(html.Div([
        html.Div(f"{p['name']} — {p['title']} · {p['location']}"),
        html.Div([html.Img(src=asset(p["brand_logo"]), alt="Cocui Dev",
                           style={"width": "30px", "height": "30px", "borderRadius": "7px",
                                  "objectFit": "cover"}),
                  html.Span("Cocui Dev · 2026")],
                 style={"fontFamily": MONO, "fontSize": "11.5px", "display": "flex",
                        "alignItems": "center", "gap": "10px"}),
    ], style={"maxWidth": "1180px", "margin": "0 auto", "padding": "0 24px",
              "display": "flex", "justifyContent": "space-between", "flexWrap": "wrap",
              "gap": "12px", "alignItems": "center"}),
        style={"background": C["ink"], "color": "#aebabd", "padding": "30px 0",
               "fontSize": "13.5px"})

    layout = html.Div([dcc.Store(id="active-cat", data="todos"), hero_wrap, body, footer],
                      style={"background": C["bg"], "fontFamily": FONTS, "color": C["text"]})
    return layout, B


# ============================================================ factory
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  {%metas%}
  <title>Christian Daniel Morán Titla — Científico de datos</title>
  {%favicon%}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,300;0,400;0,500;0,600;1,300&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  {%css%}
  <style>
    @font-face{font-family:'Coves';src:url('assets/fonts/Coves-Light.woff2') format('woff2'),url('assets/fonts/Coves-Light.otf') format('opentype');font-weight:300;font-style:normal;font-display:swap}
    @font-face{font-family:'Coves';src:url('assets/fonts/Coves-Bold.woff2') format('woff2'),url('assets/fonts/Coves-Bold.otf') format('opentype');font-weight:700;font-style:normal;font-display:swap}
    body{margin:0}
    @media (max-width:880px){
      div[style*="grid-template-columns: 300px 1fr"]{grid-template-columns:1fr !important}
    }
  </style>
</head>
<body>{%app_entry%}<footer>{%config%}{%scripts%}{%renderer%}</footer></body>
</html>"""


def create_dash_app(requests_pathname_prefix: str = "/") -> Dash:
    app = Dash(
        __name__,
        requests_pathname_prefix=requests_pathname_prefix,
        title="Christian Daniel Morán Titla — CV",
        index_string=INDEX_TEMPLATE,
        update_title=None,
    )
    layout, B = build_layout(app.get_asset_url)
    app.layout = layout

    @app.callback(
        Output("active-cat", "data"),
        Input({"type": "cat-btn", "cat": ALL}, "n_clicks"),
        State("active-cat", "data"),
        prevent_initial_call=True,
    )
    def _set_active(_clicks, current):
        trig = ctx.triggered_id
        if not trig:
            raise PreventUpdate
        cat = trig["cat"]
        if cat == "todos":
            return "todos"
        return "todos" if cat == current else cat

    @app.callback(
        Output({"type": "cv-item", "index": ALL}, "style"),
        Input("active-cat", "data"),
        State({"type": "cv-item", "index": ALL}, "id"),
    )
    def _filter_items(active, ids):
        out = []
        for ident in ids:
            tags = B.item_tags.get(ident["index"], [])
            show = active == "todos" or active in tags
            out.append({} if show else {"display": "none"})
        return out

    @app.callback(
        Output({"type": "cv-section", "name": ALL}, "style"),
        Input("active-cat", "data"),
        State({"type": "cv-section", "name": ALL}, "id"),
    )
    def _filter_sections(active, ids):
        out = []
        for ident in ids:
            tags = B.section_tags.get(ident["name"], set())
            show = active == "todos" or active in tags
            out.append({} if show else {"display": "none"})
        return out

    @app.callback(
        Output({"type": "cat-btn", "cat": ALL}, "style"),
        Input("active-cat", "data"),
        State({"type": "cat-btn", "cat": ALL}, "id"),
    )
    def _style_buttons(active, ids):
        return [catbtn_style(ident["cat"] == active) for ident in ids]

    return app


if __name__ == "__main__":
    create_dash_app().run(debug=True, port=8050)
