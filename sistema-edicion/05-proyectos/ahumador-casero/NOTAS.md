# Ahumador casero — notas de edición

- Composición: `index.html` (cortes, voz, efectos), `compositions/textos.html`
  (textos en pantalla) y `compositions/subtitulos.html` (subtítulos).
- Voz: Kokoro `em_santa`, generada frase por frase (`audio/lineas/`) y montada
  en `assets/voz.mp3` con las pausas del guion v7 (37 s, -16 LUFS).
- Tiempos de palabras: estimados por pausas y largo de cada palabra
  (`assets/palabras.json`); whisper no pudo descargar su modelo en la nube.
- Clips: `clips/IMG_XXXX.MOV` (no van a git). En la nube se usaron clips de
  relleno con el mismo nombre; en el Mac van los reales.

## Primera sesión en el Mac (hacer en este orden)
1. Si falta algo, correr `bash sistema-edicion/setup-mac.sh`.
2. Confirmar que `clips/` tiene los 26 IMG_XXXX.MOV reales.
3. Transcribir la voz con whisper (`hyperframes transcribe assets/voz.mp3
   --model small --language es`) y rehacer los tiempos de los subtítulos.
4. Ver cada clip (fotogramas + duración) y ajustar `data-media-start`
   al mejor momento según el guion v7.
5. `hyperframes check`, snapshot, abrir la vista previa para Kevin y renderizar.

## Pendiente
- Ajustar `data-media-start` de cada `<video>` al mejor momento de cada clip
  (hoy todos empiezan en 0 salvo las tomas repetidas).
- Plano del cierre: se usó IMG_4186 de relleno; confirmar con Kevin.
- Revisar legibilidad de textos y subtítulos sobre las tomas reales.
- Tipografía: Archivo Black en lugar de Sequel (la demo no trae tildes, ñ ni números).
- Verde: `#39FF14` provisional, sin confirmar.
- Sin música de fondo (no hubo fuente disponible).
