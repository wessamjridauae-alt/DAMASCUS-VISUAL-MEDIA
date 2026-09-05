# WESSAM VIDEO LAB

Open-source production lab for cinematic short-form video, AI-assisted visual experiments, and Syria Reframed workflows.

## Mission
Build original, premium, fast, visually distinctive vertical videos using a reproducible pipeline rather than random filters or templates.

## Runtime tiers

### Tier A — works in the current ChatGPT execution environment
- FFmpeg 7.1.5 — encode, crop, grade, speed ramps, transitions, overlays, motion, stabilization filters, audio removal.
- OpenCV 4.13 — tracking, optical flow, alignment, masks, geometric transforms, composition lock.
- Pillow 12.3 — graphics, typography, masks, textures, image prep.
- MoviePy 2.1.2 — Python timeline assembly when useful.
- NumPy — procedural animation and frame math.
- PyTorch 2.10 CPU — light inference only; not intended for large video diffusion models.

### Tier B — open-source / open-weight tools requiring GPU or a separate runtime
- ComfyUI — node-based generative workflow engine.
- Wan2.2 — advanced text/image-to-video generation.
- CogVideoX — text/image-to-video models.
- LTX-Video — fast generative video workflows.
- Real-ESRGAN — restoration / super-resolution.
- RIFE — frame interpolation / slow motion / smoother motion.
- Whisper — transcription and subtitle timing.

> Model weights may have licenses different from the source code. Commercial use must be checked per model before publication.

## Core production pipelines

1. **Composition Lock Reel** — aligns a face/object/location to a fixed anchor across radically different styles.
2. **Cinematic Damascus** — real-photo/video montage with motion design, parallax, speed changes, grade and fast editorial rhythm.
3. **Hypercut Reel** — beatless silent reel using visual impact cuts, match cuts, whip/zoom/flash transitions and motion continuity.
4. **AI + Real Hybrid** — real source is the truth anchor; AI creates controlled transformations while preserving subject identity and position.
5. **Restoration Chain** — denoise → deblock → upscale → interpolate → sharpen → grain → final encode.
6. **Infinite Loop** — final shot geometrically returns to opening shot for replay-friendly reels.

## Repository layout

- `scripts/` production utilities that can run locally here.
- `pipelines/` reusable production recipes.
- `registry/` vetted open-source tools and licensing notes.
- `docs/` architecture, creative systems and GPU notes.
- `experiments/` unusual visual concepts worth testing.
- `assets/` local inputs; large/generated media should not be committed unless intentional.
- `output/` rendered results (gitignored by default).

## Immediate commands

```bash
python scripts/composition_lock.py --input frames --output aligned --width 1080 --height 1920
python scripts/hypercut.py --input clips --output output/reel.mp4 --seconds 12
bash scripts/inspect_runtime.sh
```

## Quality principles

- Real locations remain truthful and recognizable.
- No fake documentary context.
- No random composition drift.
- Every transition must serve motion or visual logic.
- Prefer silent design when sound is not essential.
- Export master: 1080x1920, 30 fps, H.264 high profile, yuv420p, faststart.
- Run a visual QC pass before declaring any file final.

## North star
The competitive advantage is not one model. It is the orchestration: real source control + geometric alignment + generative transformation + cinematic post + repeatable QC.
