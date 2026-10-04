# Seguridad de cuentas publicitarias

A oct-2026, dos cuentas del portafolio están **deshabilitadas por "actividad inusual"** (Arrozito y JTM MKT) y tres aparecen como no consultables (Miguel Automekano Uio, FATIMA DFSK: estado UNSETTLED = saldo pendiente). Perder una cuenta cuesta más que cualquier campaña mala.

## Reglas para el agente
1. **No crear ráfagas.** Máximo 1 campaña nueva por cuenta por día, y espaciar cambios masivos (no editar 10 cuentas en 5 minutos desde la misma sesión).
2. **Nada de afirmaciones prohibidas:** resultados garantizados, "crédito 100% aprobado", antes/después engañosos, atributos personales ("¿Tienes deudas?", "¿Estás desempleado?").
3. **Categoría especial correcta** cuando la oferta principal es crédito (ver 03).
4. **No reciclar creativos rechazados** cambiando un detalle. Si Meta rechazó, entender el motivo (`ads_get_errors`) antes de volver a subir.
5. **Revisar estado de cuenta** (`ads_get_ad_accounts`) al iniciar cada sesión: `account_status`, `has_payment_method`, `is_queryable`. Si algo está mal, avisar primero a Kevin.

## Higiene que debe hacer el equipo (no el agente)
- Autenticación en dos pasos en todos los perfiles con acceso al Business Manager.
- Verificar el negocio en el Business Manager de cada cliente.
- Método de pago a nombre del cliente y con fondos; pagar saldos UNSETTLED.
- No compartir perfiles personales; cada persona su usuario.
- Para cuentas deshabilitadas: solicitar revisión desde Business Support Home con documentos del negocio. No crear cuentas nuevas para "saltar" el bloqueo (eso termina en bloqueo del Business Manager completo).
