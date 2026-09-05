# WJ1.SY Human Animation Production Stack

## Goal
Create publish-ready vertical Reels in which the same WJ1.SY character from a supplied character sheet can walk, turn, sit, gesture, and interact inside real Damascus scenes while preserving identity and composition.

## Pipeline
1. Prepare locked character reference at 9:16.
2. Extract or author motion/pose guidance.
3. Use DWPose for whole-body pose extraction when available.
4. Run MimicMotion as the primary full-body animation engine on a suitable GPU runtime.
5. Use LivePortrait / LivePortrait-ONNX for close-up head and expression shots.
6. Isolate and composite the generated subject with RobustVideoMatting or SAM 2 when scene integration needs cleanup.
7. Correct identity drift with CodeFormer or GFPGAN only when needed; avoid over-restoring faces.
8. Run Real-ESRGAN for final restoration/upscale.
9. Run Practical-RIFE only when frame interpolation improves motion; do not fabricate slow motion unnecessarily.
10. Finish locally with OpenCV + FFmpeg: composition lock, stabilization, crop, grade, motion blur, transitions, watermark WJ1.SY, H.264 export.

## Quality gates
- Character must remain recognizable across all shots.
- Face position/scale drift must be rejected before final edit.
- Hands/limbs with obvious deformation are rejected.
- Damascus backgrounds must be real or clearly disclosed if generated.
- 9:16 final delivery, 1080x1920 preferred, 30fps unless source requires another rate.
- WJ1.SY watermark stays inside Instagram safe area.
- No model is marked READY until a real inference test succeeds in the target runtime.

## Runtime tiers
### CPU current
FFmpeg, OpenCV, MoviePy, Pillow, MediaPipe.

### CPU candidate once dependencies/weights are available
LivePortrait-ONNXRun, DWPose ONNX, RobustVideoMatting ONNX.

### GPU production
MimicMotion + DWPose + Real-ESRGAN + CodeFormer/GFPGAN + RIFE.

### Generative environment expansion
Wan2.2, LTX-Video, CogVideoX, ComfyUI and SAM 2 after GPU availability and license verification.

## First production test
Character sheet -> 4-6 second natural walking shot -> DWPose/MimicMotion -> face QC -> composition lock -> Real-ESRGAN -> RIFE if needed -> cinematic FFmpeg pass -> WJ1.SY -> final Reel shot.
