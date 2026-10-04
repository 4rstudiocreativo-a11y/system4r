# Métricas, umbrales y reglas de decisión

Valores de referencia iniciales para **autos / asesores en Guayaquil y Quito, destino WhatsApp**, tomados de las cuentas reales de 4R (ver `trafficker/cuentas/`). Actualízalos cada mes con `/meta-ads-auditoria` — los números propios mandan sobre cualquier benchmark genérico.

## Benchmarks propios (base: JTM Nelly, últimos 90 días a oct-2026)
| Métrica | Malo | Normal | Bueno |
|---|---|---|---|
| CPM (USD) | > 9 | 4 – 7 | < 4,5 |
| CTR (todos) | < 2% | 2,5 – 3,5% | > 3,5% |
| Costo por conversación WA | > 1,80 | 0,90 – 1,50 | < 0,85 |
| Costo por lead formulario | > 4,00 | 2,00 – 3,50 | < 2,20 |
| Frecuencia 7 días | > 3,5 | 1,5 – 2,5 | — |

Objetivo por defecto si el cliente no tiene histórico: **CPR objetivo = USD 1,00 por conversación WhatsApp** y **USD 2,50 por lead de formulario**.

## Significancia: cuándo se puede decidir
No se decide nada sobre un anuncio hasta que cumpla **al menos una**:
- Gastó ≥ 2 × CPR objetivo, o
- Tiene ≥ 1.500 impresiones, o
- Lleva ≥ 72 h activo.
Para decidir sobre una campaña completa: ≥ 7 días o ≥ 20 resultados.

## Reglas de ANUNCIO (revisión diaria)
| Situación | Acción |
|---|---|
| Gastó 2,5 × CPR objetivo y 0 resultados | **Apagar** |
| CPR > 1,8 × objetivo con ≥ 5 resultados | **Apagar** |
| CTR < 1,2% tras 2.000 impresiones | **Apagar** (el gancho no funciona) |
| CPR ≤ objetivo y recibe < 10% del gasto | Dejarlo; si en 5 días sigue sin gasto, sacarlo a su propio conjunto como prueba |
| CPR ≤ 0,8 × objetivo con ≥ 10 resultados | **Ganador** → anotar concepto en bitácora y pedir 2 variantes del mismo ángulo |
| Frecuencia 7d > 3,5 y CPR subiendo 3 días seguidos | **Fatiga** → añadir creativos nuevos |

Nunca apagar el **último** anuncio con entrega de un conjunto sin tener reemplazo listo.

## Reglas de CAMPAÑA (revisión cada 72 h)
| Situación (últimos 3 días vs. 7 días previos) | Acción |
|---|---|
| CPR ≤ objetivo y presupuesto se gasta completo | **Escalar +20%** |
| CPR entre 1 y 1,3 × objetivo | Mantener, revisar creativos |
| CPR > 1,3 × objetivo durante 5 días | Bajar 20% y renovar creativos |
| CPR > 2 × objetivo durante 7 días | Proponer pausar y reconstruir (requiere OK de Kevin) |
| No gasta el presupuesto | Revisar `ads_get_errors`, audiencia demasiado pequeña, o creativos rechazados |

## Diagnóstico rápido por embudo
| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| CPM alto (> 9) | Audiencia chica, creativo de baja calidad, competencia de temporada (dic, cierre de mes) | Ampliar radio/segmentación, mejorar creativo |
| CPM normal, CTR bajo | Gancho débil, primer segundo aburrido | Nuevos ganchos (ver 04) |
| CTR bueno, costo por conversación alto | Fricción entre clic y mensaje (mensaje de bienvenida, botón) | Revisar plantilla de saludo WA, CTA |
| Conversaciones baratas pero nadie compra | Curiosos: el anuncio atrae al público equivocado o la oferta no es clara (precio, requisitos) | Poner precio/cuota/entrada en el anuncio, probar objetivo Leads→WA, preguntas de calificación |
| Leads de formulario no contestan | Formulario de "más volumen" | Cambiar a "mayor intención" + pregunta de calificación |

## Métricas que el agente debe pedir siempre al MCP
`amount_spent, results, cost_per_result, impressions, reach, frequency, cpm, ctr, effective_status` — y a nivel anuncio, además, el nombre (para leer el concepto).

## Calidad (la métrica real)
Pedir a cada asesor/cliente, semanalmente: conversaciones recibidas, calificadas (preguntaron precio/cuota y dieron datos), citas/visitas, ventas.
- **Costo por calificado** = gasto / calificados. Objetivo: ≤ 4 × costo por conversación.
- **Tasa de calificación** < 25% → problema de público/anuncio, no de presupuesto.
