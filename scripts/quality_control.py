from __future__ import annotations
from pathlib import Path
from PIL import Image,ImageStat
def inspect(path,expected):
    im=Image.open(path).convert("RGB"); stat=ImageStat.Stat(im)
    errors=[]
    if im.size!=tuple(expected): errors.append(f"size:{im.size}")
    if max(stat.var)<80: errors.append("low_visual_variance")
    if min(stat.mean)<5 or max(stat.mean)>250: errors.append("extreme_exposure")
    return {"passed":not errors,"errors":errors,"size":im.size}
