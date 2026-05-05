# 🎮 Sistema XP 4R Marketing

Sistema de gamificación y gestión de productividad para equipos de marketing digital.

## 🚀 Demo en Vivo

**URL:** [https://tu-proyecto.vercel.app](https://tu-proyecto.vercel.app)

## 📋 Características

### ✅ **Sistema de XP y Gamificación**
- Registro de tareas con timer automático (iniciar/terminar)
- Cálculo automático de eficiencia según tiempo estándar
- Tope diario de 250 XP por colaborador
- 54+ tipos de tareas predefinidas con XP específico
- Estados de desempeño: EXCELENTE, MUY BUENO, ACEPTABLE, LENTO

### 👥 **Gestión de Equipo**
- Sistema de autenticación con roles (Admin/Colaborador)
- Perfiles individuales con foto personalizada
- Dashboard con top performer destacado
- Ranking en tiempo real con medallas
- Feed de actividad personal

### 🎁 **Sistema de Premios**
- 4 categorías: Pequeños (500 XP), Medios (1,200 XP), Buenos (2,500 XP), TOP (5,000 XP)
- Solicitud de premios por colaboradores
- Aprobación/rechazo por administradores
- Descuento automático de XP al aprobar
- Sugerencias inteligentes según XP disponible
- CRUD completo para administrar catálogo

### 📋 **Módulo de Pendientes (To-Do)**
- Tablero Kanban con 3 columnas (Pendiente, En Progreso, Completado)
- Sistema de prioridades (Alta, Media, Baja)
- Asignación de tareas a colaboradores
- Fechas límite con alertas visuales
- Filtros por estado y asignado
- Vista detallada con tabla completa

### ⏰ **Sistema de Asistencia**
- Registro de entrada/salida
- Bonos por puntualidad (0-30 XP según hora de llegada)
- Tracking diario de asistencias

### 🏖️ **Gestión de Ausencias**
- Registro de días libres (vacaciones, permisos)
- Registro de horas libres (permisos parciales)
- Motivos documentados

### 📊 **Analytics y Reportes**
- Filtros por período (día, semana, mes)
- Comparación entre períodos
- Historial completo de tareas
- Stats en tiempo real

### ⚙️ **Panel de Administración (Solo Admins)**
- CRUD de colaboradores
- CRUD de clientes
- CRUD de tipos de tarea (XP y tiempos estándar)
- CRUD de premios
- Gestión de días libres
- Gestión de horas libres
- Aprobación de solicitudes de premios

## 🛠️ Tecnologías

- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Almacenamiento:** LocalStorage (navegador)
- **Diseño:** Responsive, Mobile-first
- **Hosting:** Vercel

## 📦 Instalación Local

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/sistema-xp-4r.git

# Abrir directamente en navegador
open index.html
```

No requiere instalación de dependencias. Es un archivo HTML standalone.

## 🔐 Usuarios de Prueba

### Administradores:
- **Kevin** - Password: `admin2024`
- **Carla** - Password: `admin2024`

### Colaboradores:
- **Melanie Muentes** - Password: `1234`
- **Bryan Aquino** - Password: `1234`
- **Bryan Guaranda** - Password: `1234`
- **Paulet** - Password: `1234`
- **Gabriela** - Password: `1234`

## 🎨 Diseño

Inspirado en apps de fitness tracking con:
- Paleta oscura (Dark theme)
- Acentos en naranja (#FF6B35)
- Gradientes suaves
- Animaciones fluidas
- Cards con glassmorphism

## 📱 Responsive

Optimizado para:
- 💻 Desktop (1920x1080)
- 📱 Tablet (768x1024)
- 📱 Mobile (375x667)

## 🚀 Deploy en Vercel

```bash
# Instalar Vercel CLI
npm i -g vercel

# Deploy
vercel
```

O conectar directamente desde el dashboard de Vercel:
1. Importar repositorio de GitHub
2. Deploy automático
3. URL generada instantáneamente

## 📖 Uso

### Para Colaboradores:
1. Iniciar sesión con tu usuario
2. Ir a "Registrar Tarea"
3. Seleccionar cliente y tipo de tarea
4. Click en "▶️ Iniciar Tarea"
5. Trabajar normalmente
6. Click en "🛑 Terminar Tarea"
7. El sistema calcula XP automáticamente
8. Ir a "Premios" para solicitar canjes
9. Ver "Pendientes" para tus tareas asignadas

### Para Administradores:
1. Acceso a todas las funcionalidades de colaborador
2. Panel "Administración" visible
3. Gestionar equipo, clientes, tareas, premios
4. Aprobar/rechazar solicitudes de premios en "Solicitudes"
5. Crear y asignar tareas en "Pendientes"
6. Ver historial completo del equipo

## 🔒 Seguridad

- Roles de usuario separados
- Validación de permisos por funcionalidad
- Datos almacenados localmente (no servidor)
- Sin exposición de credenciales

## 🤝 Contribuir

Las contribuciones son bienvenidas:
1. Fork del proyecto
2. Crear rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📄 Licencia

Proyecto propietario de **4R Marketing** - Todos los derechos reservados.

## 👨‍💻 Autor

**Kevin Villafuerte (KevFortuna)**  
4R Marketing - Studio Creativo  
Guayaquil, Ecuador

---

**Versión:** 1.0.0  
**Última actualización:** Mayo 2026
