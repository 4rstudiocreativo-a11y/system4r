# Sistema de edición de video — KevFortuna

Sistema para editar los videos de Kevin (marca KevFortuna) con HyperFrames.
Idioma de trabajo: español latino neutro, directo, sin adornos.

## Antes de editar cualquier video

1. Lee `02-marca/` completo (reglas, subtítulos, formatos, voz).
2. Lee `03-correcciones/feedback-general.md`.
3. Revisa `01-referencias/animaciones/`. Usa una animación cuando el guion
   coincida con el "cuándo usarla" de su ficha, sin que Kevin la nombre.
4. Usa la skill `hyperframes` para construir y renderizar.

## Durante la edición

- Cada video vive en `05-proyectos/<nombre-video>/` (guion, audio, clips, renders).
- La voz en off se genera con la voz clonada de Kevin: ver `02-marca/voz.md`.
- No inventes contenido de marca. Si falta un dato, pregunta.
- Si un paso falla 2 o 3 veces, detente y explica qué intentaste.

## Al terminar cada edición

- Guarda todo el feedback de Kevin en
  `03-correcciones/feedback-especifico/<nombre-video>.md`, aunque parezca menor.
- No actualices reglas generales por tu cuenta: deja la propuesta para el
  organizador (`04-organizador/organizador.md`).

## Entorno

- Se trabaja en sesiones en la nube de Claude Code sobre el repo `system4r`.
  El hook `.claude/hooks/session-start.sh` instala HyperFrames, Kokoro,
  MusicGen y whisper-cpp al iniciar.
- `cdn.jsdelivr.net` está bloqueado en la red de la nube: guarda librerías
  (GSAP, etc.) dentro del proyecto, como en `05-proyectos/prueba-render/assets/vendor/`.
- Los clips pesados no van a git: Kevin los comparte por Google Drive y se
  descargan a `05-proyectos/<nombre-video>/clips/` (ignorado por git).
