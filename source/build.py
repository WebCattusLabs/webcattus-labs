#!/usr/bin/env python3
"""Builds the static Webcattus Labs site into ./dist from shared partials.
Plain Python, no dependencies: python3 build.py"""
import os, shutil, json, html

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
DIST = os.path.join(ROOT, "dist")
SITE = "https://webcattuslabs.com"
EMAIL = "hello@webcattuslabs.com"
CONTACT = "contact.html"
# Business phone. Leave empty until you have one; "Call us" buttons appear only when it's set.
PHONE_E164 = "+16147211118"
PHONE_DISPLAY = "(614) 721-1118"

# ---------------------------------------------------------------- icons (24px, stroke)
def ic(path, extra=""):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"{extra}>{path}</svg>')

I = {
  "compass": ic('<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>'),
  "flow":    ic('<rect x="3" y="4" width="6" height="6" rx="1.5"/><rect x="15" y="14" width="6" height="6" rx="1.5"/><path d="M9 7h4a3 3 0 0 1 3 3v4"/>'),
  "chat":    ic('<path d="M20 12a8 8 0 0 1-11.6 7.1L4 20l1-4.1A8 8 0 1 1 20 12z"/><path d="M8.5 11h7M8.5 14h4"/>'),
  "users":   ic('<circle cx="9" cy="8" r="3.2"/><path d="M3.5 19a5.5 5.5 0 0 1 11 0"/><path d="M16 5.5a3 3 0 0 1 0 5.6M17.5 14.2A5 5 0 0 1 20.5 19"/>'),
  "check":   ic('<path d="M5 12.5l4.2 4.2L19 7"/>'),
  "shield":  ic('<path d="M12 3l7 3v5.5c0 4.2-2.9 7.9-7 9.5-4.1-1.6-7-5.3-7-9.5V6z"/><path d="M9 12l2 2 4-4"/>'),
  "badge":   ic('<circle cx="12" cy="9" r="5.5"/><path d="M8.6 13.4L7 21l5-2.6L17 21l-1.6-7.6"/>'),
  "book":    ic('<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5A2.5 2.5 0 0 1 6.5 18H20v3H6.5"/>'),
  "award":   ic('<path d="M8 3h8v5a4 4 0 0 1-8 0z"/><path d="M8 5H5v1a3 3 0 0 0 3 3M16 5h3v1a3 3 0 0 1-3 3M12 12v4M8.5 21h7M10 16h4l.5 5h-5z"/>'),
  "phone":   ic('<path d="M5 4h3.5l1.6 4-2.1 1.3a11 11 0 0 0 6.7 6.7l1.3-2.1 4 1.6V19a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>'),
  "msg":     ic('<rect x="3" y="5" width="18" height="13" rx="2"/><path d="M3.5 6.5L12 12.5l8.5-6"/>'),
  "bell":    ic('<path d="M6 16V11a6 6 0 1 1 12 0v5l1.5 2h-15z"/><path d="M10 20.5a2 2 0 0 0 4 0"/>'),
  "user":    ic('<circle cx="12" cy="8" r="3.6"/><path d="M5 20a7 7 0 0 1 14 0"/>'),
  "cal":     ic('<rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/>'),
  "clock":   ic('<circle cx="12" cy="12" r="9"/><path d="M12 7.5V12l3 2"/>'),
  "info":    ic('<circle cx="12" cy="12" r="9"/><path d="M12 11v5.5M12 7.6v.2"/>'),
  "lock":    ic('<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>'),
  "hand":    ic('<path d="M8 12V5.5a1.5 1.5 0 0 1 3 0V11M11 10V4.5a1.5 1.5 0 0 1 3 0V11M14 10.5V6a1.5 1.5 0 0 1 3 0v8a7 7 0 0 1-7 7h-.5A6.5 6.5 0 0 1 4 14.6V12a1.5 1.5 0 0 1 3 0v2"/>'),
  "key":     ic('<circle cx="8" cy="15" r="4"/><path d="M11 12l8-8M16 7l2 2M14 9l2 2"/>'),
  "chart":   ic('<path d="M4 20V4M4 20h16"/><path d="M8 16l3.5-4 3 2.5L19 9"/>'),
  "menu":    ic('<path d="M4 7h16M4 12h16M4 17h16"/>'),
  "plate":   ic('<circle cx="12" cy="13" r="6"/><circle cx="12" cy="13" r="2.8"/><path d="M3 4v5a2 2 0 0 0 2 2M5 4v16M21 4c-1.5 1-2 3-2 5s.5 2 2 2v9"/>'),
  "star":    ic('<path d="M12 3.5l2.6 5.3 5.8.8-4.2 4.1 1 5.8L12 16.8l-5.2 2.7 1-5.8-4.2-4.1 5.8-.8z"/>'),
  "thermo":  ic('<path d="M10 14.5V5a2 2 0 0 1 4 0v9.5a4 4 0 1 1-4 0z"/><path d="M12 17v-6M17 6h3M17 10h3"/>'),
  "hardhat": ic('<path d="M3 18h18v2H3zM5 18v-3a7 7 0 0 1 14 0v3"/><path d="M10 8.3V5h4v3.3M8 11v3M16 11v3"/>'),
  "store":   ic('<path d="M4 9.5L5.5 4h13L20 9.5M4 9.5V20h16V9.5M4 9.5a2.7 2.7 0 0 0 5.3 0 2.7 2.7 0 0 0 5.4 0 2.7 2.7 0 0 0 5.3 0"/><path d="M10 20v-5h4v5"/>'),
  "arrow":   '<span class="arrow" aria-hidden="true">→</span>',
}

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><defs><linearGradient id="wl-g" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#7B4DFF"/><stop offset=".6" stop-color="#C04CFD"/><stop offset="1" stop-color="#38C6F4"/>'
        '</linearGradient></defs><path d="M5 27V11.5L10.5 4l4.2 6.2h2.6L21.5 4 27 11.5V27a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1z" '
        'fill="url(#wl-g)"/><circle cx="12.2" cy="17.5" r="1.7" fill="#fff"/><circle cx="19.8" cy="17.5" r="1.7" fill="#fff"/>'
        '<path d="M13.5 22.2c1.5 1 3.5 1 5 0" stroke="#fff" stroke-width="1.6" stroke-linecap="round" fill="none"/></svg>')

LANG = "en"   # set by the build before each language's content module is imported

STR = {
  "en": {
    "nav": [("services.html", "Services"), ("industries.html", "Industries"), ("use-cases.html", "Use cases"), ("about.html", "About"), ("faq.html", "FAQ")],
    "skip": "Skip to content", "home_aria": "Webcattus Labs home", "tagline": "AI for small business",
    "menu_aria": "Open menu", "nav_aria": "Main", "cta": "Book an AI Readiness Audit", "lang_aria": "Language",
    "blurb": "Practical AI and automation for small businesses in Dallas–Fort Worth and beyond. Set up properly, explained in plain English, measured every month.",
    "h_services": "Services", "h_company": "Company", "h_talk": "Talk to us",
    "l_workshop": "AI Discovery Workshop", "l_agents": "Custom AI Agents", "l_rest": "For restaurants", "l_fix": "Problems we fix",
    "l_advisory": "Monthly Advisory", "l_training": "Team AI Training", "l_about": "About", "l_cases": "Use cases", "l_faq": "FAQ",
    "l_privacy": "Data &amp; privacy", "l_consult": "Book a free consultation", "city": "Dallas, Texas",
    "rights": "All rights reserved.", "nosell": "We never sell or share your information.",
    "call": "Call", "closer_label": "Free · 30 minutes · Video or phone",
    "closer_title": "Let's make running your business easier.",
    "closer_text": "Tell us what's slowing you down. In a free 30-minute consultation we'll pick the problems worth fixing first, show you how we'd fix them, and estimate what each is worth. No slides and no pressure.",
    "consult": "Book a free consultation", "note1": "Reply within one business day", "note2": "No obligation",
  },
  "es": {
    "nav": [("services.html", "Servicios"), ("industries.html", "Industrias"), ("use-cases.html", "Casos de uso"), ("about.html", "Nosotros"), ("faq.html", "Preguntas")],
    "skip": "Saltar al contenido", "home_aria": "Inicio de Webcattus Labs", "tagline": "IA para pequeños negocios",
    "menu_aria": "Abrir menú", "nav_aria": "Principal", "cta": "Agende su consulta", "lang_aria": "Idioma",
    "blurb": "IA y automatización prácticas para pequeños negocios en Dallas–Fort Worth y más allá. Bien configuradas, explicadas en palabras sencillas y medidas cada mes.",
    "h_services": "Servicios", "h_company": "Empresa", "h_talk": "Hable con nosotros",
    "l_workshop": "Taller de descubrimiento de IA", "l_agents": "Agentes de IA a la medida", "l_rest": "Para restaurantes", "l_fix": "Problemas que resolvemos",
    "l_advisory": "Asesoría mensual", "l_training": "Capacitación en IA para su equipo", "l_about": "Nosotros", "l_cases": "Casos de uso", "l_faq": "Preguntas frecuentes",
    "l_privacy": "Datos y privacidad", "l_consult": "Reserve una consulta gratuita", "city": "Dallas, Texas",
    "rights": "Todos los derechos reservados.", "nosell": "Nunca vendemos ni compartimos su información.",
    "call": "Llamar al", "closer_label": "Gratis · 30 minutos · Por video o teléfono",
    "closer_title": "Hagamos más fácil la gestión de su negocio.",
    "closer_text": "Cuéntenos qué lo está frenando. En una consulta gratuita de 30 minutos elegiremos los problemas que conviene resolver primero, le mostraremos cómo los resolveríamos y estimaremos cuánto vale cada uno. Sin presentaciones y sin presión.",
    "consult": "Reserve una consulta gratuita", "note1": "Respuesta en un día hábil", "note2": "Sin compromiso",
  },
}

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=Manrope:wght@400;500;600;700;800&family=Sora:wght@500;600;700&display=swap">')

FAVICON = "data:image/svg+xml," + LOGO.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"').replace("#", "%23").replace('"', "'")

def url_for(path, lang):
    tail = "" if path == "index.html" else path
    return SITE + "/" + ("es/" if lang == "es" else "") + tail

def head_tags(title, desc, path, lang):
    url = url_for(path, lang)
    pre = "../" if lang == "es" else ""
    return f"""<title>{html.escape(title)}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{url_for(path, 'en')}"><link rel="alternate" hreflang="es" href="{url_for(path, 'es')}"><link rel="alternate" hreflang="x-default" href="{url_for(path, 'en')}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Webcattus Labs"><meta property="og:locale" content="{'es_US' if lang == 'es' else 'en_US'}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{url}">
<meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)"><meta name="theme-color" content="#0F0E14" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{FAVICON}">
{FONTS}
<link rel="stylesheet" href="{pre}assets/site.css">"""

def lang_switch(path, lang):
    en_href = ("../" + path) if lang == "es" else path
    es_href = path if lang == "es" else ("es/" + path)
    en_cur = ' aria-current="true"' if lang == "en" else ""
    es_cur = ' aria-current="true"' if lang == "es" else ""
    return (f'<div class="lang" role="group" aria-label="{STR[lang]["lang_aria"]}">'
            f'<a href="{en_href}" hreflang="en" lang="en"{en_cur}><span class="sr-only">English</span><span aria-hidden="true">EN</span></a>'
            f'<a href="{es_href}" hreflang="es" lang="es"{es_cur}><span class="sr-only">Español</span><span aria-hidden="true">ES</span></a></div>')

def header(active, lang="en"):
    t = STR[lang]
    cur = ' aria-current="page"'
    links = "".join(f'<li><a href="{href}"{cur if href == active else ""}>{label}</a></li>' for href, label in t["nav"])
    return f"""<a class="skip" href="#main">{t["skip"]}</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="{t["home_aria"]}">{LOGO}<span>Webcattus Labs<small>{t["tagline"]}</small></span></a>
    {lang_switch(active, lang)}
    <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-menu" aria-label="{t["menu_aria"]}">{I["menu"]}</button>
    <div class="nav__menu" id="nav-menu">
      <nav aria-label="{t["nav_aria"]}"><ul class="nav__links">{links}</ul></nav>
      <a class="btn btn--primary nav__cta" href="{CONTACT}">{t["cta"]}</a>
    </div>
  </div>
</header>"""

def footer(lang="en"):
    t = STR[lang]
    pre = "../" if lang == "es" else ""
    phone = f'<li><a href="tel:{PHONE_E164}">{PHONE_DISPLAY}</a></li>' if PHONE_E164 else ""
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="stack">
        <a class="brand" href="index.html">{LOGO}<span>Webcattus Labs</span></a>
        <p>{t["blurb"]}</p>
      </div>
      <div><h4>{t["h_services"]}</h4><ul>
        <li><a href="services.html#workshop">{t["l_workshop"]}</a></li>
        <li><a href="services.html#agents">{t["l_agents"]}</a></li>
        <li><a href="services.html#restaurants">{t["l_rest"]}</a></li>
        <li><a href="industries.html">{t["l_fix"]}</a></li>
        <li><a href="services.html#advisory">{t["l_advisory"]}</a></li>
        <li><a href="services.html#training">{t["l_training"]}</a></li></ul></div>
      <div><h4>{t["h_company"]}</h4><ul>
        <li><a href="about.html">{t["l_about"]}</a></li>
        <li><a href="use-cases.html">{t["l_cases"]}</a></li>
        <li><a href="faq.html">{t["l_faq"]}</a></li>
        <li><a href="faq.html#privacy">{t["l_privacy"]}</a></li></ul></div>
      <div><h4>{t["h_talk"]}</h4><ul>
        <li><a href="{CONTACT}">{t["l_consult"]}</a></li>{phone}
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><span class="muted">{t["city"]}</span></li></ul></div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Webcattus Labs Inc. {t["rights"]}</span>
      <span>{t["nosell"]}</span>
    </div>
  </div>
</footer>
<script src="{pre}assets/site.js" defer></script>"""

def call_button(cls):
    if not PHONE_E164:
        return ""
    icon = I["phone"].replace('aria-hidden="true"', 'aria-hidden="true" width="18" height="18"')
    return f'<a class="{cls}" href="tel:{PHONE_E164}">{icon} {STR[LANG]["call"]} {PHONE_DISPLAY}</a>'

def closer(title=None, text=None):
    t = STR[LANG]
    title = title or t["closer_title"]
    text = text or t["closer_text"]
    second = "btn--ghost-light" if PHONE_E164 else "btn--light"
    return f"""<section class="section" aria-labelledby="closer-title">
  <div class="wrap">
    <div class="closer aurora">
      <div class="stack">
        <p class="label">{t["closer_label"]}</p>
        <h2 id="closer-title">{title}</h2>
        <p>{text}</p>
      </div>
      <div class="stack">
        <div class="cta-row">{call_button("btn btn--light")}<a class="btn {second}" href="{CONTACT}">{t["consult"]} {I["arrow"]}</a></div>
        <p class="cta-note"><span>{t["note1"]}</span><span>{t["note2"]}</span></p>
      </div>
    </div>
  </div>
</section>"""

JSONLD = json.dumps({
  "@context": "https://schema.org", "@type": "ProfessionalService", "name": "Webcattus Labs Inc",
  "url": SITE, "email": EMAIL, "telephone": PHONE_E164, "areaServed": ["Dallas–Fort Worth", "United States"],
  "address": {"@type": "PostalAddress", "addressLocality": "Dallas", "addressRegion": "TX", "addressCountry": "US"},
  "description": "AI consulting and automation for small businesses: AI strategy, workflow automation, custom AI assistants and team training.",
  "founder": {"@type": "Person", "name": "Jayant Jaishwin Shanmugam Kavitha"}
})

def page(path, title, desc, body, lang="en", full=True):
    ld = f'\n<script type="application/ld+json">{JSONLD}</script>' if path == "index.html" else ""
    inner_head = head_tags(title, desc, path, lang)
    if not full:
        return f"""{inner_head}
<script>document.documentElement.classList.add("no-js")</script>
{header(path, lang)}
<main id="main">
{body}
</main>
{footer(lang)}{ld}
"""
    return f"""<!doctype html>
<html lang="{lang}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{inner_head}
</head>
<body>
{header(path, lang)}
<main id="main">
{body}
</main>
{footer(lang)}{ld}
</body>
</html>
"""

def build(pages_en, pages_es):
    if os.path.exists(DIST): shutil.rmtree(DIST)
    os.makedirs(os.path.join(DIST, "assets"))
    os.makedirs(os.path.join(DIST, "es"))
    for f in os.listdir(os.path.join(SRC, "assets")):
        shutil.copy(os.path.join(SRC, "assets", f), os.path.join(DIST, "assets", f))
    for lang, pages in (("en", pages_en), ("es", pages_es)):
        for p in pages:
            out = os.path.join(DIST, "es" if lang == "es" else "", p["path"])
            with open(out, "w") as fh:
                fh.write(page(p["path"], p["title"], p["desc"], p["body"], lang))
    # Preview variant of the English home page (the artifact host supplies the document skeleton).
    home = next(p for p in pages_en if p["path"] == "index.html")
    with open(os.path.join(ROOT, "preview-index.html"), "w") as fh:
        fh.write(page("index.html", home["title"], home["desc"], home["body"], "en", full=False))
    print("built en:", len(pages_en), "pages; es:", len(pages_es), "pages")

if __name__ == "__main__":
    import importlib
    import build as B          # content modules import this module by name
    B.LANG = "en"
    import pages_content
    B.LANG = "es"
    import pages_content_es
    B.build(pages_content.PAGES, pages_content_es.PAGES)
