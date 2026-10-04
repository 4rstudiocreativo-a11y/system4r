---
name: meta-ads-optimizar
description: Revisión diaria o semanal de campañas activas de Meta Ads con reglas numéricas para apagar, mantener o escalar. Úsala cuando Kevin pida "optimiza", "revisa las campañas", "qué apago", "qué escalo", o en la revisión programada.
---

# Optimización con reglas

## Pasos
1. Cuentas a revisar: las que Kevin indique, o las cuentas de un cliente, sede o marca de `trafficker/portafolio.json` (ej. "Grupo Roldán › Vía a Daule › JAC"), o todas. Presentar el resultado agrupado por cliente › sede › marca, con subtotales.
2. Para cada cuenta, `ads_get_ad_entities`:
   - Nivel `ad`, filtrar activos, `last_7d` y `last_3d`, campos `id, name, amount_spent, results, cost_per_result, impressions, frequency, cpm, ctr`.
   - Nivel `campaign`, `last_7d`, con presupuesto.
   - Ejecutar los `next_actions` de solo lectura.
3. Clasificar cada anuncio y campaña con las tablas de `conocimiento/02-metricas-y-reglas.md`. Respetar la **significancia**: si no hay datos suficientes, la decisión es "esperar".
4. No proponer cambios a campañas con < 72 h desde el último cambio significativo (ver ficha del cliente).

## Salida
```
## Optimización <fecha>
| Cuenta | Entidad (id) | Métrica clave | Regla | Acción propuesta |
|---|---|---|---|---|
Resumen: X anuncios a apagar, Y campañas a escalar (+USD __/día total), Z sin cambios.
Necesito creativos nuevos para: <cuentas con fatiga>
```

## Ejecución
- **Pausar anuncios perdedores** (`ads_update_entity` con `{"status":"PAUSED"}`): requiere OK de Kevin; puede aprobarlos en bloque ("sí, apaga todos los propuestos").
- **Cambios de presupuesto** (`daily_budget` en centavos): siempre con OK explícito y mostrando "de USD X a USD Y". Máximo +30% por cambio.
- Nunca reactivar, borrar ni archivar sin pedirlo Kevin.
- Espaciar los cambios entre cuentas (ver `conocimiento/05-seguridad-cuentas.md`).

## Después
- Anotar cada cambio en el Historial de la ficha del cliente.
- Ganadores nuevos → `bitacora/creativos-ganadores.md`.
- Si una regla produjo una mala decisión (se apagó algo que luego habría funcionado), proponer ajustar el umbral en `02-metricas-y-reglas.md`. Así el sistema mejora con el tiempo.
