#!/usr/bin/env python3
import argparse, glob, os, subprocess, tempfile


def sh(cmd):
    subprocess.run(cmd, check=True)


def main():
    p=argparse.ArgumentParser(description='Fast silent 9:16 reel builder from clips.')
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--seconds', type=float, default=12.0)
    p.add_argument('--shot', type=float, default=0.75)
    p.add_argument('--fps', type=int, default=30)
    a=p.parse_args()
    clips=sorted(sum([glob.glob(os.path.join(a.input,f'*.{e}')) for e in ('mp4','mov','mkv','webm')],[]))
    if not clips: raise SystemExit('No video clips found')
    n=max(1, round(a.seconds/a.shot))
    chosen=(clips*((n+len(clips)-1)//len(clips)))[:n]
    os.makedirs(os.path.dirname(a.output) or '.', exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        segs=[]
        for i,f in enumerate(chosen):
            o=os.path.join(td,f'{i:03d}.mp4')
            vf=("scale=1080:1920:force_original_aspect_ratio=increase,"
                "crop=1080:1920,setsar=1,"
                "eq=contrast=1.04:saturation=1.06:brightness=-0.01,"
                "unsharp=5:5:0.45:5:5:0")
            sh(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss','0','-t',str(a.shot),'-i',f,
                '-an','-vf',vf,'-r',str(a.fps),'-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p',o])
            segs.append(o)
        listfile=os.path.join(td,'list.txt')
        with open(listfile,'w') as h:
            for s in segs: h.write("file '%s'\n"%s.replace("'","'\\''"))
        sh(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',listfile,
            '-an','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',a.output])
    print(a.output)

if __name__=='__main__': main()
