# WESSAM VIDEO LAB — Human Animation Runbook

## Goal
Animate the same reference character from a character sheet so he can walk, turn, sit, interact with environments, and remain identity-consistent across a vertical Reel.

## Non-negotiable quality rule
Do not fake full-body AI animation with pan/zoom/warping and present it as generative motion. A result is considered `AI-HUMAN-ANIMATION READY` only after a real model inference pass succeeds.

## Current runtime truth
- CPU only
- ~5.8 GB RAM
- no CUDA
- terminal internet unavailable
- FFmpeg/OpenCV/MoviePy/Pillow available
- ONNX Runtime currently missing

## Tier A — CPU candidate
### LivePortrait ONNX
Repository: https://github.com/hpc203/liveportrait-onnxrun
Purpose: face/head/upper-body motion and identity-preserving closeups.
Needs:
1. onnxruntime
2. LivePortrait ONNX model weights
3. source portrait extracted from the character sheet
4. driving video or motion template

Acceptance test:
- 3–5 second output
- face similarity visually acceptable
- no severe mouth/eye deformation
- no frame tearing

This tier is not enough for realistic walking.

## Tier B — Full-body generation
### MimicMotion
Repository: https://github.com/tencent/MimicMotion
Purpose: pose-guided full-body image animation.
Best fit for: walking, turning, gesturing, seated interaction.
Constraint: GPU required for practical use.

### MusePose
Repository: https://github.com/TMElyralab/MusePose
Purpose: pose-driven full-body character animation.
Important: released trained-model terms are non-commercial research. Do not use its restricted weights for commercial WJ1.SY publishing unless licensing is cleared.

### Moore-AnimateAnyone
Repository: https://github.com/MooreThreads/Moore-AnimateAnyone
Purpose: reference-image + pose sequence human animation.
Evaluate current model/code licenses before use.

## Production pipeline when GPU is available
1. Character sheet -> select clean full-body master frame.
2. Identity prep -> crop, normalize, background isolate.
3. Driving motion -> real walking/turning reference or pose sequence.
4. Full-body model -> generate 4–8 second shots.
5. Face repair/closeup -> LivePortrait where useful.
6. Composition Lock -> OpenCV landmarks / homography only where needed.
7. Interpolation -> RIFE if required.
8. Restoration -> Real-ESRGAN only when detail gain beats identity drift.
9. Edit -> FFmpeg 9:16, 30fps, sound design optional.
10. Watermark -> WJ1.SY fixed safe-zone placement.
11. QC -> identity, hands, feet, temporal flicker, Damascus scene integrity.

## Damascus Reel target structure
- Shot 1: close-up, subtle head turn, Old Damascus alley.
- Shot 2: full-body walk toward camera in a stone lane.
- Shot 3: side-profile walking match cut through souq lighting.
- Shot 4: seated cafe interaction, hand reaches for cup.
- Shot 5: rooftop / city overlook, turn toward skyline.
- Final: clean WJ1.SY mark, no intrusive title card.

## Runtime gate
Before any new AI video claim, run:
- dependency check
- weight availability check
- one real inference test
- inspect produced MP4

If any gate fails, report the exact blocker instead of substituting fake motion.
