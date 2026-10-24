#!/bin/bash
# Instala HyperFrames y sus herramientas opcionales en cada sesión en la nube.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

if ! command -v hyperframes >/dev/null 2>&1; then
  npm install -g hyperframes@0.8.191
fi

# MusicGen (música de fondo) y Kokoro (voz)
if ! python3 -c "import torch" >/dev/null 2>&1; then
  pip install -q --index-url https://download.pytorch.org/whl/cpu --extra-index-url https://pypi.org/simple torch
fi
if ! python3 -c "import kokoro_onnx, soundfile, transformers, numpy" >/dev/null 2>&1; then
  pip install -q kokoro-onnx soundfile transformers numpy
fi

# whisper-cpp (transcripción)
if ! command -v whisper-cli >/dev/null 2>&1; then
  if [ ! -d /opt/whisper.cpp ]; then
    git clone --depth 1 https://github.com/ggml-org/whisper.cpp.git /opt/whisper.cpp
  fi
  cmake -S /opt/whisper.cpp -B /opt/whisper.cpp/build -DCMAKE_BUILD_TYPE=Release >/dev/null
  cmake --build /opt/whisper.cpp/build -j4 --config Release >/dev/null
  ln -sf /opt/whisper.cpp/build/bin/whisper-cli /usr/local/bin/whisper-cli
fi

# Skills de HyperFrames a nivel usuario (también están en .claude/skills del repo)
for s in hyperframes hyperframes-cli hyperframes-registry media-use; do
  if [ ! -d "$HOME/.claude/skills/$s" ] && [ -d "$CLAUDE_PROJECT_DIR/.claude/skills/$s" ]; then
    mkdir -p "$HOME/.claude/skills"
    cp -r "$CLAUDE_PROJECT_DIR/.claude/skills/$s" "$HOME/.claude/skills/"
  fi
done
