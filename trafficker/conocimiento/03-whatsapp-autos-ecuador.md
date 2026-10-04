# Playbook: asesores y concesionarias de autos → WhatsApp (Ecuador)

El 80% de las cuentas 4R son asesores comerciales (Jetour, DFSK, Chery, Mazda, Chevrolet, etc.) de Guayaquil y Quito. Este es el playbook específico.

## Configuración base de la campaña
- **Objetivo:** Interacción (OUTCOME_ENGAGEMENT) → optimización CONVERSATIONS → destino WHATSAPP. Alternativa a probar: OUTCOME_LEADS → CONVERSATIONS → WHATSAPP.
- **Presupuesto:** CBO, USD 8-15/día por asesor. Menos de USD 6/día = no sale de aprendizaje.
- **Ubicación:** la ciudad del asesor con radio. Guayaquil: radio 25-40 km incluye Samborondón, Vía a la Costa, Daule, Durán. Excluir ciudades que el asesor no atiende solo si lo pide.
- **Edad:** 25-65 como sugerencia (Advantage+ audiencia activado). No limitar por género.
- **Ubicaciones:** Advantage+ (automáticas). Reels + Stories suelen llevar la mayoría del gasto; es normal.
- **Horario:** sin programación por horas salvo que el asesor no conteste de noche. Si no contesta → programar 7:00-21:00 (requiere presupuesto total, no diario).
- **Mensaje de bienvenida WA:** con pregunta que califica. Ej.: "¡Hola! Soy Nelly de Jetour 👋 ¿Qué modelo te interesa y lo buscas al contado o con financiamiento?" + respuestas rápidas.

## Categoría especial (¡cuidado!)
Si el anuncio **ofrece crédito/financiamiento como mensaje principal** ("cuotas desde USD 299", "crédito aprobado en 24 h"), Meta puede exigir la categoría **FINANCIAL_PRODUCTS_SERVICES**. Consecuencias: sin segmentación por edad/género y radio mínimo ~17 km. Opciones:
1. Mensaje centrado en el **vehículo** (precio, equipamiento, prueba de manejo) y mencionar financiamiento como secundario → sin categoría especial.
2. Si la oferta es el crédito → declarar la categoría. **Nunca ocultarlo**: rechazos repetidos ponen en riesgo la cuenta.

## Ángulos que funcionan en el nicho (validar con datos de cada cuenta)
1. **Precio / cuota visible** — "X50 desde USD XX.XXX" o "entrada desde USD X.XXX". Filtra curiosos.
2. **Comparativo** — "X50 vs Dashing", "¿por qué la X70 y no la [competidor]?". En JTM Nelly fue de lo mejor (USD 0,59-0,82 por conversación).
3. **Urgencia real** — cierre de mes, autoshow, bono por tiempo limitado. Solo si es verdad.
4. **Asesor como persona** — el asesor hablando a cámara, en la sala, con el auto. Genera confianza (la gente le escribe a una persona, no a una marca).
5. **Prueba social** — entrega de auto a cliente real (con permiso), "esta semana entregamos 5 X50".
6. **Objeciones** — "¿Los autos chinos duran?", garantía, repuestos, reventa.
7. **Recorrido / detalle** — tour de 20-30 s del interior, tecnología, espacio para la familia.

## Lo que aprendimos de las cuentas reales
Ver `trafficker/cuentas/jtm-nelly.md`. Resumen:
- Las campañas con **un modelo concreto** (X50) rinden mejor que las genéricas ("Vehículos Jetour", "Venta de Jetour": ~USD 2,1 por conversación).
- Demasiadas campañas pequeñas: 24 campañas en 90 días con ~USD 270 en total → casi ninguna salió de aprendizaje. **Consolidar** es la mejora número 1.

## Coordinación con el equipo
- El costo por conversación lo controla el trafficker; **la venta la controla el asesor**. Pedir tiempo de respuesta < 5 min en horario laboral: cada hora de demora baja fuertemente la tasa de cierre.
- Guiones de reels: usar la skill `guiones-ads-autos-chinos` (cuenta de Claude de Kevin).
- Plantilla operativa para replicar campañas entre asesores: skill `pauta-whatsapp-interaccion`.
