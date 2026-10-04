# system4r — 4R Marketing

Este repo contiene dos cosas:
1. `index.html` — Sistema XP de gamificación del equipo (app estática, ver README.md).
2. `trafficker/` — **Sistema de trafficker IA para Meta Ads** (ver `trafficker/README.md`).

## Cuando la tarea sea de pauta / Meta Ads
- Actúa como el agente definido en `.claude/agents/trafficker-4r.md` (o delega en él).
- Usa las skills `/meta-ads-auditoria`, `/meta-ads-lanzar`, `/meta-ads-optimizar`, `/meta-ads-creativos`.
- Reglas no negociables: nada se activa ni sube de presupuesto sin un "sí" explícito de Kevin con el monto; todo se crea pausado/borrador; nunca inventar datos ni IDs; registrar cada decisión en la ficha del asesor dentro de `trafficker/cuentas/<cliente>/<sede>/<marca>/`. La estructura de clientes está en `trafficker/portafolio.json`.
- Idioma: español.
