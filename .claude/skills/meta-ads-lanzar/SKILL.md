---
name: meta-ads-lanzar
description: Convierte un brief en una campaña de Meta Ads montada en borrador/pausada vía MCP, siguiendo la metodología 4R (CBO, segmentación amplia, creativos diversos). Úsala cuando Kevin pida "créame una campaña", "pauta para X", "lanza la promo de Y", "monta la campaña de WhatsApp de Z".
---

# Lanzar campaña

## 1. Brief (no avanzar sin esto)
Completar `trafficker/briefs/_plantilla-brief.md` (guardar como `briefs/AAMMDD-cliente.md`). Datos **obligatorios** que hay que pedir si faltan — nunca suponerlos:
- Cuenta publicitaria, **presupuesto diario en USD dicho por Kevin**, destino, ciudad/radio, producto/oferta, creativos disponibles.

Leer la ficha del cliente (`trafficker/cuentas/`) y la bitácora de ganadores: **empezar desde lo que ya funcionó** en esa cuenta o en cuentas del mismo nicho.

## 2. Revisar antes de crear
- ¿Ya existe una campaña activa con el mismo objetivo en esa cuenta? → La regla es **agregar anuncios a la campaña existente**, no crear otra. Proponerlo a Kevin.
- Presupuesto vs. mínimo de aprendizaje (`conocimiento/01-metodologia.md` §2). Si no alcanza, avisar y recomendar.
- ¿La oferta principal es crédito? → categoría especial (ver `03`).
- Página e Instagram correctos: `ads_get_ad_account_pages`, `ads_get_ig_accounts`.
- Creativos: `ads_get_ad_videos` / `ads_get_ad_images`, o subir con `ads_creative_upload_media`.

## 3. Presentar el plan (y esperar OK)
```
Campaña: <nombre según nomenclatura>
Objetivo / optimización / destino:
Presupuesto: USD __/día (CBO) → en centavos: ____
Conjunto: ubicación, radio, edad sugerida, Advantage+ audiencia y ubicaciones
Anuncios (4-8 conceptos distintos): concepto · formato · gancho · texto · CTA
Mensaje de bienvenida WhatsApp:
CPR objetivo y criterio de éxito a 7 días:
```
No crear nada hasta que Kevin confirme el plan.

## 4. Montar (todo queda PAUSADO / BORRADOR)
1. `ads_create_campaign` — objetivo ODAX, `campaign_daily_budget` en centavos (CBO), `special_ad_categories` correcto.
2. `ads_create_ad_set` — usar `optimization_goal` de la lista que devolvió la campaña; `destination_type` (ej. WHATSAPP); `promoted_object` con `page_id`; targeting amplio por `geo_locations` (ciudad con radio). **No inventar IDs de intereses.**
3. `ads_create_creative` por concepto (video con miniatura; CTA `WHATSAPP_MESSAGE` cuando el destino es WhatsApp) y `ads_create_ad` para cada uno.
4. Verificar con `ads_get_ad_entities` (`object_state` draft o live según corresponda) y `ads_get_ad_preview`. Revisar `ads_get_errors`.
5. Mostrar a Kevin: IDs, previsualizaciones, presupuesto final.

## 5. Activar (solo con "sí, actívala" explícito)
`ads_activate_entity` sobre la campaña. Después:
- Registrar en la ficha del cliente (Historial de decisiones) con fecha, presupuesto y CPR objetivo.
- Recordar a Kevin: **no tocar en 72 h**; la primera revisión es con `/meta-ads-optimizar`.
