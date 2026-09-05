# AI VIDEO STACK

## What we can do now
The current execution environment is excellent for deterministic post-production but CPU-only for PyTorch. Therefore:

- Use FFmpeg/OpenCV locally for edit, motion, alignment, tracking, masks, compositing, color, timing and export.
- Use AI video diffusion only when a GPU runtime is available.
- Bring the generated frames/clips back into the deterministic pipeline for finishing and QC.

## Recommended GPU stack

### Wan2.2
Official repo: https://github.com/Wan-Video/Wan2.2
Use for: image-to-video and text-to-video experiments with cinematic motion. Code repository is Apache-2.0; verify the specific model-weight terms before commercial use.

### ComfyUI
Official repo: https://github.com/Comfy-Org/ComfyUI
Use for: graph-based orchestration, reproducible generation, masks, conditioning, image/video nodes, control workflows.

### CogVideoX
Official repo: https://github.com/zai-org/CogVideo
Use for: alternative image/text-to-video generation. Code is Apache-2.0; model licenses vary.

### LTX-Video
Official repo: https://github.com/Lightricks/LTX-Video
Use for: fast image/text-to-video experimentation and controllable pipelines. Always re-check current repo/model license before commercial deployment.

## Post-production AI
- Real-ESRGAN: restoration and super-resolution.
- RIFE: interpolation and slow-motion.
- SAM 2: subject/object video segmentation.
- Whisper: subtitle timing and transcription when audio exists.

## Syria Reframed hybrid recipe
1. Start from a real verified Damascus photo/video.
2. Lock the master crop at 1080x1920.
3. Generate controlled variants from the same master rather than re-inventing the location.
4. Align every result back to the master geometry.
5. Use masks to separate subject, architecture and depth layers.
6. Add subtle parallax / camera push in post.
7. Use 0.5–0.9 s visual beats for high-energy reels.
8. Restore/upscale only after structure is stable.
9. Finish with consistent grade + texture + grain.
10. QC for identity, geometry, location truthfulness, clipping, flicker and seams.

## Experimental visual systems worth developing
- Frozen Subject / Exploding World: subject stays pixel-locked while every material/background transforms.
- Time-Slice Damascus: same viewpoint morphs through historical visual treatments without claiming generated frames are archival evidence.
- Architectural Match-Cut Engine: detect arches, doors, windows and domes and cut between matching shapes.
- Depth Tunnel: monocular depth + layered parallax + speed-ramped push-through.
- Mosaic-to-Reality: geometric mosaic reconstructs into the real location while the camera position stays fixed.
- Ink-to-Stone: line art progressively gains texture until it becomes the original photograph.
- Impossible Seamless Loop: final geometry and luminance are optimized to return to frame 1.
