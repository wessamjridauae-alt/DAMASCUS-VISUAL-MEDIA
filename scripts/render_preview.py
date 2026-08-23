from __future__ import annotations
import argparse
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageEnhance
from common import ROOT,load_json

def font(size,bold=False):
    candidates=[
      ROOT/("assets/brand/IBMPlexSansArabic-SemiBold.ttf" if bold else "assets/brand/IBMPlexSansArabic-Regular.ttf"),
      Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")]
    for p in candidates:
      if p.exists(): return ImageFont.truetype(str(p),size)
    return ImageFont.load_default()
def fit_font(draw,text,max_width,start,bold=False,direction=None):
    size=start
    while size>20:
      f=font(size,bold); box=draw.textbbox((0,0),text,font=f,direction=direction)
      if box[2]-box[0] <= max_width:return f
      size-=2
    return font(size,bold)
def background(size):
    w,h=size
    strip=Image.new("RGB",(1,h))
    for y in range(h):
      t=y/max(1,h-1);strip.putpixel((0,y),(int(45+90*(1-t)),int(38+62*(1-t)),int(31+42*(1-t))))
    im=strip.resize(size)
    d=ImageDraw.Draw(im)
    for i in range(8):
      x=int(w*(i/7));d.rectangle((x,h*.42,x+w*.055,h*.86),fill="#8C7359")
    d.ellipse((w*.14,h*.23,w*.86,h*1.12),outline="#C89B55",width=max(4,w//180))
    return im.filter(ImageFilter.GaussianBlur(1.2))
def render(out,size,title,subtitle,label):
    load_json("config/brand.json");im=ImageEnhance.Contrast(background(size)).enhance(1.08)
    d=ImageDraw.Draw(im,"RGBA");w,h=size;m=int(w*.09);maxw=w-2*m
    d.rectangle((m,m,w-m,h-m),outline="#C89B55",width=max(3,w//360))
    d.rectangle((0,int(h*.58),w,h),fill=(17,16,15,185))
    tf=fit_font(d,title,maxw,int(w*.085),True,"rtl");sf=fit_font(d,subtitle,maxw,int(w*.035),False,"rtl")
    d.text((w-m,int(h*.68)),title,font=tf,fill="#F3EBDD",direction="rtl",anchor="ra")
    d.text((w-m,int(h*.79)),subtitle,font=sf,fill="#FFFFFF",direction="rtl",anchor="ra")
    d.text((m,m+24),label,font=fit_font(d,label,maxw,int(w*.022),True),fill="#C89B55")
    footer="SETUP PREVIEW · NOT FOR PUBLISHING"
    d.text((w-m,h-m-36),footer,font=fit_font(d,footer,maxw,int(w*.018),True),fill="#C89B55",anchor="ra")
    out.parent.mkdir(parents=True,exist_ok=True);im.save(out,"PNG",optimize=True)
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--out",required=True);ap.add_argument("--story",action="store_true");a=ap.parse_args()
    render(Path(a.out),(1080,1920) if a.story else (1080,1350),"دمشق… بهويّة تُعرف من النظرة الأولى","دفء الحجر، عمق الظلال، وذهبٌ هادئ","DAMASCUS SIGNATURE / 01")
