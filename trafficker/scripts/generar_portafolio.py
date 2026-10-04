"""Regenera la estructura de clientes a partir de trafficker/portafolio.json.

Uso (desde la raíz del repo):  python3 trafficker/scripts/generar_portafolio.py
- Crea una carpeta por cliente / sede / marca en trafficker/cuentas/ (con README por cliente).
- Reescribe trafficker/cuentas/_portafolio.md.
- Actualiza el mapa PORTFOLIO embebido en pautas/index.html.
No borra fichas de asesores existentes.
"""
import json, os, re, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
T = os.path.join(ROOT, "trafficker")
P = json.load(open(os.path.join(T, "portafolio.json"), encoding="utf-8"))


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def multi(c):
    return len(c["sedes"]) > 1


def nota(a):
    return "; ".join(x for x in [a.get("estado"), a.get("nota")] if x) or "—"


md = ["# Portafolio 4R por cliente", "",
      "Estructura: **cliente › sede › marca › cuenta**. Fuente de verdad: `trafficker/portafolio.json` "
      "(la usan el agente y el panel 4R Pautas). Para cambiarla, edita el JSON y corre "
      "`python3 trafficker/scripts/generar_portafolio.py`.", "",
      "Las fichas de cada asesor viven en `cuentas/<cliente>/<sede>/<marca>/<asesor>.md` "
      "(clientes de una sola sede: `cuentas/<cliente>/<asesor>.md`). Plantilla: `_plantilla.md`.", ""]
groups = []
for c in P["clientes"]:
    croot = os.path.join(T, "cuentas", c["carpeta"])
    os.makedirs(croot, exist_ok=True)
    readme = [f"# {c['cliente']}", "", "Cuentas de este cliente. Fuente: `trafficker/portafolio.json`.", ""]
    md.append(f"## {c['cliente']}")
    md.append("")
    for s in c["sedes"]:
        if multi(c):
            h = f"### {s['sede']}" + (f" — {s['nota']}" if s.get("nota") else "")
            md += [h, ""]
            readme += [h, ""]
        for m in s["marcas"]:
            d = os.path.join(croot, slug(s["sede"]), slug(m["marca"])) if multi(c) else croot
            os.makedirs(d, exist_ok=True)
            if multi(c) and not os.listdir(d):
                open(os.path.join(d, ".gitkeep"), "w").close()
            md += [f"**{m['marca']}**", "", "| Asesor | Cuenta | ID | Estado / nota |", "|---|---|---|---|"]
            readme += [f"**{m['marca']}**", ""]
            for a in m["cuentas"]:
                md.append(f"| {a['asesor']} | {a['nombre']} | {a['id']} | {nota(a)} |")
                readme.append(f"- {a['asesor']} — {a['nombre']} (`{a['id']}`)" + ("" if nota(a) == "—" else f" · {nota(a)}"))
            md.append("")
            readme.append("")
            path = [c["cliente"]] + ([s["sede"], m["marca"]] if multi(c) else [])
            g = {"path": path, "ids": [a["id"] for a in m["cuentas"]]}
            if s.get("tipo") == "awareness":
                g["aw"] = True
            groups.append(g)
    open(os.path.join(croot, "README.md"), "w", encoding="utf-8").write("\n".join(readme) + "\n")

md += ["## Otros clientes (por organizar)", "", "| Cuenta | ID | Estado | Nota |", "|---|---|---|---|"]
md += [f"| {a['nombre']} | {a['id']} | {a.get('estado','')} | {a.get('nota','')} |" for a in P.get("sin_asignar", [])]
md += ["", "Leyenda: ✅ disponible · ⚠️ con problema · ⛔ deshabilitada/cerrada · 🕒 MCP aún no habilitado por Meta"]
open(os.path.join(T, "cuentas", "_portafolio.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")

page = os.path.join(ROOT, "pautas", "index.html")
html = open(page, encoding="utf-8").read()
html = re.sub(r"const PORTFOLIO = .*?;\n", lambda _: "const PORTFOLIO = " + json.dumps(groups, ensure_ascii=False) + ";\n", html, count=1)
open(page, "w", encoding="utf-8").write(html)
print(f"{len(groups)} grupos, {sum(len(g['ids']) for g in groups)} cuentas asignadas, {len(P.get('sin_asignar', []))} sin asignar")
