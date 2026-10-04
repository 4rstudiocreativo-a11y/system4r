---
name: meta-ads-auditoria
description: Audita una cuenta de Meta Ads de un cliente de 4R con datos reales del MCP y entrega un diagnóstico con acciones priorizadas. Úsala cuando Kevin pida "audita la cuenta de X", "qué está pasando con la pauta de X", "por qué está caro", o al tomar una cuenta nueva.
---

# Auditoría de cuenta Meta Ads (solo lectura)

Esta skill **no modifica nada** en la cuenta. Solo lee y propone.

## Pasos
1. **Identificar la cuenta.** Buscar en `trafficker/portafolio.json` (cliente › sede › marca › cuenta). Si no está, `ads_get_ad_accounts` y buscar por nombre. Verificar `is_queryable`, `is_ads_mcp_enabled`, `account_status`, `has_payment_method`. Si hay problema → reportarlo primero (ver `conocimiento/05-seguridad-cuentas.md`).
2. **Leer contexto:** ficha del cliente en `trafficker/cuentas/` + `conocimiento/02-metricas-y-reglas.md`.
3. **Extraer datos** con `ads_get_ad_entities`:
   - Nivel `campaign`, `last_90d`, campos: `id, name, effective_status, amount_spent, results, cost_per_result, impressions, cpm, ctr`.
   - Nivel `ad`, `last_30d`, mismos campos + `frequency`, ordenado por gasto.
   - Ejecutar todos los `next_actions` de solo lectura que devuelva el MCP (trend, opportunity score).
   - `ads_get_errors` si hay campañas activas sin entrega.
4. **Analizar** contra la metodología:
   - **Estructura:** nº de campañas vs. presupuesto (fragmentación), duplicados, campañas en aprendizaje permanente (< 50 resultados/semana).
   - **Eficiencia:** CPR por campaña y por anuncio vs. benchmarks; detectar ganadores y perdedores con las reglas de significancia.
   - **Creativo:** cuántos conceptos distintos hay, fatiga (frecuencia), qué ángulos ganan (leer nombres).
   - **Medición:** ¿sabemos cuántas conversaciones se volvieron ventas? Si no, es un hallazgo.
5. **Entregar** el reporte con este formato:

```
## Auditoría <cuenta> — <fecha>
**Veredicto en una línea:** ...
### Números clave (periodo)
gasto · resultados · CPR medio · mejor/peor campaña
### Top 3 problemas (por impacto en USD)
1. <problema> — evidencia numérica — acción
### Lo que está funcionando (no tocar)
### Plan propuesto (requiere OK)
- Acción · entidad (id) · de → a · impacto esperado
### Próximos pasos
```

6. **Guardar:** actualizar/crear la ficha `trafficker/cuentas/<cliente>/<sede>/<marca>/<asesor>.md` (clientes de una sola sede: `trafficker/cuentas/<cliente>/<asesor>.md`) (sección Auditoría + Aprendizajes + Historial) y añadir ganadores a `bitacora/creativos-ganadores.md`. Si los benchmarks propios difieren mucho de `02-metricas-y-reglas.md`, proponer actualizarlos.

## Auditoría de portafolio
Si Kevin pide "audita todas" o "cómo va la agencia": recorrer las cuentas de `trafficker/portafolio.json` (o solo el cliente/sede/marca pedido), `last_7d`, y entregar una tabla agrupada por cliente › sede › marca con subtotales con CPR y una columna "atención" (🟢/🟡/🔴) según las reglas. Profundizar solo en las 🔴.
