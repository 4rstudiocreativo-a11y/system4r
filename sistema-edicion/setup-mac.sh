#!/bin/bash
# Instala en el Mac todo lo que usa el sistema de edición (se corre una sola vez).
# Uso: bash sistema-edicion/setup-mac.sh
set -e

if ! command -v brew >/dev/null 2>&1; then
  echo "Instalando Homebrew (te pedirá la contraseña del Mac)..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  eval "$(/opt/homebrew/bin/brew shellenv 2>/dev/null || /usr/local/bin/brew shellenv)"
fi

brew install node ffmpeg whisper-cpp
npm install -g hyperframes@0.8.191

# Voz local de respaldo (Kokoro). Opcional: si falla, se sigue igual.
python3 -m pip install --user kokoro-onnx soundfile \
  || echo "Aviso: Kokoro no se instaló (opcional, no hace falta para editar)."

# Mover los clips de la carpeta vieja (video-01) a la del ahumador
cd "$(dirname "$0")/05-proyectos"
if [ -d video-01/clips ]; then
  mkdir -p ahumador-casero/clips
  mv video-01/clips/* ahumador-casero/clips/ 2>/dev/null || true
  rmdir video-01/clips video-01 2>/dev/null || true
fi

echo
echo "Clips en ahumador-casero/clips:"
ls ahumador-casero/clips | head -40
echo
hyperframes doctor | grep -E "✓|✗"
echo
echo "Listo. Abre Claude Code en esta carpeta y escribe: edita el video del ahumador con los clips reales"
