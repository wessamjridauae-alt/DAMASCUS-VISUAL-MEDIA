#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-$HOME/wessam-local-stack}"
SRC="$ROOT/src"
MODELS="$ROOT/models"
BIN="$ROOT/bin"
mkdir -p "$SRC" "$MODELS" "$BIN"

echo "[1/4] Preflight"
command -v git >/dev/null || { echo "git is required"; exit 1; }
command -v cmake >/dev/null || { echo "cmake is required to build llama.cpp"; exit 1; }
command -v make >/dev/null || { echo "make is required to build llama.cpp"; exit 1; }

echo "[2/4] Download open-source sources"
clone_or_update() {
  local url="$1" dir="$2" branch="$3"
  if [ -d "$dir/.git" ]; then
    git -C "$dir" fetch --depth 1 origin "$branch"
    git -C "$dir" reset --hard "origin/$branch"
  else
    git clone --depth 1 --branch "$branch" "$url" "$dir"
  fi
}
clone_or_update https://github.com/awesome-selfhosted/awesome-selfhosted.git "$SRC/awesome-selfhosted" master
clone_or_update https://github.com/ggml-org/llama.cpp.git "$SRC/llama.cpp" master
clone_or_update https://github.com/Significant-Gravitas/AutoGPT.git "$SRC/AutoGPT" master

echo "[3/4] Build llama.cpp CPU locally"
cmake -S "$SRC/llama.cpp" -B "$SRC/llama.cpp/build" -DGGML_NATIVE=ON -DGGML_OPENMP=ON -DGGML_CUDA=OFF
cmake --build "$SRC/llama.cpp/build" --config Release -j"$(getconf _NPROCESSORS_ONLN 2>/dev/null || echo 2)"

for exe in llama-cli llama-server llama-quantize; do
  found="$(find "$SRC/llama.cpp/build" -type f -name "$exe" -perm -111 | head -n1 || true)"
  [ -n "$found" ] && ln -sf "$found" "$BIN/$exe"
done

echo "[4/4] Create local-only environment template"
cat > "$ROOT/local.env" <<'EOF'
# Local-only policy: do not add cloud API keys.
WESSAM_LOCAL_ONLY=true
LLAMA_SERVER_HOST=127.0.0.1
LLAMA_SERVER_PORT=8080
LLAMA_CONTEXT=8192
# Put a local GGUF model path here after downloading it once.
LLAMA_MODEL=

# AutoGPT AutoPilot can talk to any OpenAI-compatible endpoint you control.
CHAT_USE_LOCAL=true
CHAT_BASE_URL=http://host.docker.internal:8080/v1
CHAT_API_KEY=local-only
# Must match the local model name/alias exposed by your llama.cpp server.
CHAT_FAST_STANDARD_MODEL=local-model
EOF

cat <<EOF

Installed source tree: $ROOT
  $SRC/awesome-selfhosted
  $SRC/llama.cpp
  $SRC/AutoGPT

llama.cpp binaries: $BIN
models directory:   $MODELS

IMPORTANT:
- This script installs source code and builds llama.cpp locally.
- It deliberately does NOT configure OpenAI, Anthropic, OpenRouter, or any paid API.
- A GGUF model file is still required for LLM inference. Once that model file exists locally, llama.cpp can run fully offline.
- AutoGPT must be pointed only at the local llama.cpp OpenAI-compatible endpoint.
EOF
