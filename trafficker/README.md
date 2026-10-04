# Trafficker IA de 4R Marketing

Un agente de Meta Ads que trabaja con **tus cuentas reales** (vía el MCP de Meta Ads), sigue una metodología escrita y **aprende de los resultados de tus propias campañas**.

## Cómo se usa (en Claude Code, dentro de este repo)
| Quieres… | Escribe |
|---|---|
| Saber qué está pasando en una cuenta | `/meta-ads-auditoria Nelly` |
| Ver el estado de toda la agencia | `/meta-ads-auditoria todas las cuentas, últimos 7 días` |
| Montar una campaña | `/meta-ads-lanzar campaña WhatsApp X50 para Leslie, USD 10 diarios, Guayaquil` |
| Revisar qué apagar y qué escalar | `/meta-ads-optimizar` |
| Ideas de anuncios nuevos | `/meta-ads-creativos Jetour X70 para Xiomara` |

El agente **siempre** te muestra el plan y espera tu "sí" antes de gastar dinero. Todo se crea pausado o en borrador.

## Cómo "aprende"
No es un modelo reentrenado: es un sistema que lee y escribe su propia memoria en este repo.

```
conocimiento/        → la metodología (cómo trabajamos)       ← la editas tú o el agente propone cambios
  fuentes-externas/  → notas de cursos y mentores              ← las traes tú
portafolio.json      → estructura cliente › sede › marca › cuenta (Grupo Roldán, Ecuasueña, Novalider, Automekano GYE/UIO, Weichai…)
cuentas/             → una carpeta por cliente con la ficha de cada asesor: datos, decisiones, aprendizajes
bitacora/            → experimentos y creativos ganadores de TODAS las cuentas
briefs/              → pedidos de campaña
```

Cada auditoría y optimización deja registro. Con el tiempo, la bitácora de 4R (50 cuentas del mismo nicho) vale más que cualquier curso, porque son **tus datos, en tu mercado**.

## Primeras 2 semanas recomendadas
1. **Día 1:** `/meta-ads-auditoria` de las 5 cuentas con más gasto. Crear sus fichas.
2. **Día 2:** consolidar: 1 campaña WhatsApp CBO por asesor, con los ángulos ganadores.
3. **Día 3:** pedir a cada asesor el reporte semanal (conversaciones → calificados → citas → ventas). Sin esto solo se optimiza costo por mensaje.
4. **Diario:** `/meta-ads-optimizar` (5 minutos).
5. **Semanal:** `/meta-ads-creativos` para 2-3 conceptos nuevos por cuenta activa.
6. Agrega tus notas de cursos en `conocimiento/fuentes-externas/`.
