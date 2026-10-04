# Auditoría de portafolio — 2026-10-04 (últimos 7 días)

Alcance: 38 cuentas consultables vía MCP (2 páginas de `ads_get_ad_accounts`). Solo campañas con estado ACTIVO.
Gasto total de la semana en campañas activas: **~USD 712** en 16 cuentas. 22 cuentas sin campañas activas.

## Gasto por cuenta (7 días)
| Cuenta | Gasto | Resultado principal | Nota |
|---|---|---|---|
| AUTOMEKANO MKT | 206,52 | WA, CPR 0,49 – 1,71 | 26 campañas "activas", 13 con USD 0 → muy fragmentada |
| Novalider | 170,57 | Formulario, 0,35 – 0,73 por lead | 051 y 052 (Sierra) con USD 10/día cada una y USD 0 gastado |
| Procar Ecuador | 71,69 | WA 0,25 – 0,61 · formulario 0,52 – 1,90 | Mejor CPR del portafolio |
| Ecuasueña | 71,39 | Formulario 0,57 – 1,05 | |
| JTM Katrina | 42,00 | WA 0,27 – 0,37 | Excelente |
| JTM Shaina | 34,52 | WA 0,34 – 1,23 | |
| Autodealerec | 28,24 | Formulario 0,54 – 1,04 | |
| Bruval | 24,80 | WA 0,58 | Opportunity Score 84; Meta detecta fragmentación |
| Marketing 4R | 9,87 | WA 0,27 | 4 campañas en 0 (vacantes, Irma) |
| Promax | 9,45 | WA 0,32 – 0,78 | |
| JTM Juanita | 9,22 | WA 0,49 | |
| JTM Josseline | 8,89 | WA 1,78 | En vigilancia |
| Weichai | 6,49 | Formulario | 3 conjuntos casi iguales; Opportunity Score 76 (fragmentación, +21 pts al combinarlos) |
| Andres MKT | 7,63 | WA 1,91 | En vigilancia |
| Novalider (KEV 044 Alcance) | 8,99 | Alcance | OK como apoyo |
| Jac Samborondón | 5,31 | Alcance | |
| Pautas Scarlet MG | 4,91 | Visitas a la página de destino a 0,04 | Revisar si ese objetivo sirve para vender |

## Hallazgos
1. **El costo por resultado está sano en general.** La mediana del WhatsApp ronda USD 0,60. Con el objetivo ajustado a USD 0,80, solo **4 campañas** cruzan la regla de apagado (CPR > 1,44 con ≥ 5 resultados); ver propuesta D. El problema principal no es "trafficker caro": es estructura y escala.
2. **Fragmentación generalizada.** Presupuestos de USD 2 – 5/día repartidos en muchas campañas. Meta lo señala en Bruval y Weichai.
3. **"Campañas zombi":** unas 27 campañas ACTIVAS que no gastaron nada en 7 días (sin errores de entrega, así que sus anuncios o conjuntos están pausados por dentro). No cuestan dinero, pero ensucian la lectura y pueden reactivarse por error.
4. **Hay ganadores limitados por presupuesto** (CPR < USD 0,50 con presupuestos de USD 3 – 5/día). Ahí está el crecimiento más barato del portafolio.
5. **Patrón creativo (hipótesis fuerte):** comparar **contra un competidor** gana casi siempre. Comparar **dos modelos de la misma marca** gana menos.
   - Contra competidor: Kaiyi vs Chery 0,25 · Chery vs Skyworth 0,61 · Glory 560 vs Wigle 7 0,63 · X50 vs Dashing 0,59 – 0,82.
   - Misma marca: X70 vs X50 0,34 (excepción) · X50 vs T1 1,78 · E5 vs Glory 1,91 · E5 Plus vs Kingo 1,40.

## Propuesta (pendiente de aprobación de Kevin)
### A. Escalar ganadores +20% (regla 02: CPR ≤ objetivo y presupuesto gastado completo)
| Cuenta | Campaña (id) | CPR 7 días | Presupuesto diario |
|---|---|---|---|
| Procar | 001 CLPT - Sedán / Kaiyi vs Chery (120249273291220208) | 0,25 | 3,00 → 3,60 |
| Procar | 003 CLPT - Camioneta / RICH (120249278054810208) | 0,40 | 3,00 → 3,60 |
| JTM Shaina | 001 CLPT - x70 vs x50 (120248815028040674) | 0,34 | 3,00 → 3,60 |
| Novalider | 054 CLPT - HuangHai Cotopaxi (120246761530790335) | 0,35 lead | 5,50 → 6,60 |
| Ecuasueña | 018 CLPT / HuangHai (120249174676500517) | 0,57 lead | 5,00 → 6,00 |
Total: **+USD 3,90/día** (≈ USD 117/mes).
Katrina (USD 0,27) **no** está en la lista: solo gastó USD 25,63 de USD 70 posibles, así que no le falta presupuesto.

### D. Apagar perdedoras (CPR > 1,8 × objetivo con ≥ 5 resultados)
| Cuenta | Campaña (id) | Gasto 7 días | Conversaciones | CPR |
|---|---|---|---|---|
| JTM Josseline | 002 CLPT - Jetour X50 vs Jetour T1 (120249592032570521) | 8,89 | 5 | 1,78 |
| AUTOMEKANO MKT | ASESOR YANINA 03/03 (120240090318810006) | 10,25 | 6 | 1,71 |
| AUTOMEKANO MKT | 082 CLPT - E5 Plus (Freddy) 1 (120250271234500006) | 11,74 | 7 | 1,68 |
| AUTOMEKANO MKT | 081 CLPT - Glory 560 (Freddy) 1 (120250169102290006) | 17,49 | 12 | 1,46 |
Ahorro: ~USD 48/semana. **Antes de apagar** hay que confirmar que el asesor tenga otra campaña activa; si no, cambiar el creativo en vez de dejarlo sin pauta.
En vigilancia: Andres MKT 004 E5 Supreme vs Glory 560 (1,91 con 4 conversaciones; aún no cumple el mínimo de datos).

### B. Limpieza: pausar campañas zombi (USD 0 en 7 días)
No cambia la entrega ni el gasto; solo ordena las cuentas. Listado en la sección de abajo.

### C. Consolidar Weichai (3 conjuntos → 1) y Bruval (2 → 1)
Lo recomienda Meta. Requiere rehacer los conjuntos de anuncios: se hace con `/meta-ads-lanzar` y con tu OK.

## Campañas zombi detectadas
- Samantha Ramirez: SAMANTA NEW (120248831239530441)
- Beatriz MKT: BEATRIZ 21/03 (120241847270310465)
- Elizabeth MKT: 003 CLPT - CHERY / TIGGO y ARIZO (120247458779560643)
- TreeHouse: 004 CLPT - Curso de muebles (120247500090970094)
- JESSICA MKT: 003 Interacción - Productor audiovisual (120253342581280273)
- Marketing 4R: Irma Jac T9 vs T1 (120249258432700016), Reclutamiento Postproductor (120249158099450016), 020 Vacante Postproductor (120248513408350016), 019 Vacante Media Buyer (120248497017880016)
- JTM Juanita: 01 CPL SUV (120248381419390438)
- Jannethe: jannethe potencial (120251011408660345), 001 CLPT - Jetour (120248039139130345)
- Tannia: 001 CLPT - Glory 560 y E5 Supreme (120253598627490672)
- JTM Nelly: 009 CLPT / Jetour x50 vs Dashing (52514920454975)
- Novalider: 052 S3 PRO Sierra (120245661455940335), 051 X3 PIQUERO PRO Sierra (120245570923550335)
- AUTOMEKANO MKT: FORTUNE AND 082 Erika (x2: 120250168994810006, 120250023733120006), 65 Yanina (120249044237030006), 074.1 Hannibal (120249792422620006), Mayra 74.6-1 (120249706894020006), 065.8 Show Yanina (120249613541550006), 065.7 Show Mary (120249613473180006), Ericka 060 (120249137602040006), Mari Mantuano 058-1 (120248960500270006), 023 Johanna E5 Luxury (120244581881960006), 020 Johanna Glory 560 (120243200045500006)
