# Metodología 4R para Meta Ads (2026)

Esta es la forma en que 4R estructura la pauta. Se basa en cómo funciona hoy el algoritmo de Meta (sistema de recuperación de anuncios "Andromeda" + Advantage+), en lo que enseñan públicamente los mejores media buyers de habla hispana y anglosajona, y **sobre todo en los datos de nuestras propias cuentas**.

## 1. La idea central: el creativo es la segmentación
Desde 2025 Meta decide a quién mostrar un anuncio leyendo el **contenido del anuncio** (imagen, video, texto, audio), no los intereses que marcamos. Consecuencias:

- **Segmentación amplia** (solo ubicación + edad mínima legal) casi siempre gana a intereses. Los intereses son, como mucho, una "sugerencia".
- Si quieres llegar a otro tipo de cliente (ej. familia vs. emprendedor vs. taxista), **haz otro creativo con otro ángulo**, no otro conjunto de anuncios con otros intereses.
- **Diversidad creativa real** = conceptos distintos (otro gancho, otro formato, otra persona, otro dolor). 5 versiones del mismo video con distinto color de texto cuentan como 1 creativo para Andromeda.

## 2. Consolidar: pocas campañas, bien alimentadas
El algoritmo necesita **~50 resultados por conjunto de anuncios por semana** para salir de la fase de aprendizaje. Fragmentar el presupuesto en muchas campañas pequeñas lo deja en aprendizaje para siempre (más caro, más inestable).

**Estructura estándar por cliente/asesor:**

```
CAMPAÑA (CBO, presupuesto a nivel campaña)
└── 1 conjunto de anuncios amplio (ubicación + edad 25-65, Advantage+ audiencia y ubicaciones)
    └── 4 a 8 anuncios con conceptos DISTINTOS
```

Regla para saber cuánto presupuesto hace falta:
`presupuesto_diario_mínimo ≈ (50 / 7) × costo_por_resultado_objetivo`
- WhatsApp a ~USD 0,80/conversación → ~USD 6/día mínimo; ideal USD 8-10/día.
- Formulario a ~USD 2,20/lead → ~USD 16/día mínimo.
Si el cliente no llega a ese presupuesto, **una sola campaña** y un solo conjunto; nunca dividir.

**Prohibido** (salvo justificación escrita en la ficha del cliente):
- Duplicar una campaña "a ver si sale mejor" mientras la original sigue viva (compiten entre sí en la subasta).
- Tener más de 2 campañas activas con el mismo objetivo en una cuenta con menos de USD 30/día.
- Lanzar una campaña nueva cada semana por cada promo: **se agregan anuncios nuevos a la campaña ganadora**, no campañas nuevas.

## 3. Ciclo de vida de una campaña
| Fase | Duración | Qué se hace | Qué NO se hace |
|---|---|---|---|
| Lanzamiento | Días 0-3 | Nada. Observar entrega y errores. | Tocar presupuesto, pausar anuncios, editar. |
| Lectura | Días 3-7 | Apagar anuncios perdedores según reglas (02). | Cambios de segmentación. |
| Estable | Semana 2+ | Escalar ganadores, añadir 2-3 creativos nuevos/semana. | Cambios >30% de presupuesto de golpe. |
| Fatiga | Cuando frecuencia y CPR suben | Rotar creativos nuevos dentro de la misma campaña. | Crear campaña nueva desde cero. |

**Cambios "significativos" que reinician el aprendizaje:** editar segmentación, cambiar evento de optimización, añadir/quitar anuncios en masa, subir/bajar presupuesto >30%, pausar >7 días. Agrúpalos en un solo momento si son necesarios.

## 4. Escalado
- **Vertical:** +20% de presupuesto cada 72 h si el CPR de los últimos 3 días está ≤ objetivo. Nunca más de +30% de una vez.
- **Horizontal:** cuando el ganador se estanca, nuevo conjunto/campaña con **creativos nuevos**, no con la misma audiencia duplicada.
- **Por creatividad:** la forma más barata de escalar es tener más anuncios ganadores. Meta 2-3 conceptos nuevos por semana por cuenta activa.

## 5. Objetivo correcto según lo que vende el cliente
| Lo que el cliente necesita | Objetivo | Optimización | Destino |
|---|---|---|---|
| Conversaciones de WhatsApp (asesores de autos) | Interacción (OUTCOME_ENGAGEMENT) o Clientes potenciales (OUTCOME_LEADS) | CONVERSATIONS | WHATSAPP |
| Datos de contacto filtrados | OUTCOME_LEADS | LEAD_GENERATION (o QUALITY_LEAD si hay CRM conectado) | Formulario instantáneo con preguntas de calificación |
| Ventas en web con píxel | OUTCOME_SALES | OFFSITE_CONVERSIONS (Purchase) | WEBSITE |
| Visitas a la sala / evento | OUTCOME_AWARENESS solo como apoyo, nunca como campaña principal | REACH | — |

**Prueba obligatoria en cuentas nuevas de WhatsApp:** Interacción→WhatsApp vs. Clientes potenciales→WhatsApp. El segundo suele dar conversaciones más caras pero de mayor intención. Se decide por **costo por cliente calificado** (ver 02), no por costo por conversación.

## 6. Nomenclatura (obligatoria)
`[CLIENTE] | [OBJ] | [DESTINO] | [OFERTA/PRODUCTO] | [AAMMDD]`
Ej.: `NELLY | INT | WA | X50 CIERRE MES | 261004`
Anuncios: `[CONCEPTO]-[FORMATO]-[V#]` → `PRECIO-REEL-V1`, `TESTIMONIO-FOTO-V2`.
Esto permite que el agente compare conceptos entre cuentas.

## 7. Medición que importa
El costo por conversación es una métrica **intermedia**. La métrica que paga el plan del cliente es:
`costo por cliente calificado` y `costo por venta`.
Por eso cada cuenta debe registrar (en Google Sheets / Make) cuántas conversaciones se volvieron: calificadas → cita/visita → venta. Sin ese dato, el agente solo puede optimizar costo por conversación y **eso favorece curiosos baratos**.
