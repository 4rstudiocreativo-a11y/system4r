---
name: meta-ads-creativos
description: Genera conceptos creativos, ganchos y textos de anuncios para Meta Ads basados en lo que ya ganó en las cuentas 4R y en la competencia (Biblioteca de Anuncios). Úsala cuando Kevin pida "ideas de anuncios", "nuevos creativos", "ganchos", "copy", o cuando la optimización detecte fatiga.
---

# Creativos basados en datos

## Pasos
1. **Qué ya funciona:** leer `trafficker/bitacora/creativos-ganadores.md` y la ficha del cliente. Si hace falta, `ads_get_ad_entities` nivel `ad` últimos 30-90 días ordenado por resultados para ver qué anuncios ganan, y `ads_get_creatives` para leer su texto.
2. **Qué hace la competencia:** `ads_library_search` con la marca/modelo y competidores directos en Ecuador. Priorizar anuncios activos hace > 30 días. Extraer ángulo, gancho, formato y oferta (no copiar).
3. **Generar la matriz** con `conocimiento/04-creativos.md` y el playbook `03-whatsapp-autos-ecuador.md`:
   - 2 variantes del ángulo ganador actual (iterar).
   - 2-3 ángulos nuevos no probados en la cuenta (explorar).
4. Para cada concepto entregar:
```
### Concepto N — <ángulo> (<iterar|explorar>)
Formato: Reel 9:16 / foto / carrusel · Duración
Gancho (0-2 s): visual + texto en pantalla
Desarrollo: 3-4 beats
CTA:
Texto principal (≤ 4 líneas):
Titular:
Nombre del anuncio: <CONCEPTO>-<FORMATO>-V1
Por qué debería funcionar: <dato de la bitácora o de la competencia>
```
5. Para guiones completos de reel de autos, delegar en la skill `guiones-ads-autos-chinos`; para maquetarlos en PDF, `guiones-pdf-4r`.

## Reglas
- No prometer resultados garantizados ni usar afirmaciones sobre atributos personales (políticas de Meta).
- Precios y ofertas solo si Kevin/el cliente los confirmó.
- Conceptos **realmente distintos**: otro gancho, otra escena o persona, otro formato. Variaciones de color no cuentan.
