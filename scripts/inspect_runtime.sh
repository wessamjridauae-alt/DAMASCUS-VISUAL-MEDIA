#!/usr/bin/env bash
set -euo pipefail
printf '== Wessam Video Lab Runtime ==\n'
command -v ffmpeg >/dev/null && ffmpeg -version | head -n 1 || echo 'ffmpeg: missing'
python - <<'PY'
mods=['cv2','numpy','PIL','moviepy','torch']
for m in mods:
    try:
        x=__import__(m)
        print(f'{m}: {getattr(x,"__version__","installed")}')
    except Exception as e:
        print(f'{m}: MISSING ({e})')
try:
    import torch
    print('cuda_available:', torch.cuda.is_available())
except Exception:
    pass
PY
