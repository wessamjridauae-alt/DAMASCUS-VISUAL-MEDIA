#!/usr/bin/env python3
import argparse, os, glob
import cv2
import numpy as np


def fit_canvas(img, w, h):
    ih, iw = img.shape[:2]
    scale = min(w/iw, h/ih)
    nw, nh = int(iw*scale), int(ih*scale)
    resized = cv2.resize(img, (nw, nh), interpolation=cv2.INTER_LANCZOS4)
    canvas = np.zeros((h, w, 3), dtype=np.uint8)
    x, y = (w-nw)//2, (h-nh)//2
    canvas[y:y+nh, x:x+nw] = resized
    return canvas


def align_to_reference(ref, img):
    gray_ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create(2500)
    k1, d1 = orb.detectAndCompute(gray_ref, None)
    k2, d2 = orb.detectAndCompute(gray, None)
    if d1 is None or d2 is None:
        return img, False
    matches = cv2.BFMatcher(cv2.NORM_HAMMING).knnMatch(d2, d1, k=2)
    good = [m for m, n in matches if m.distance < 0.72*n.distance]
    if len(good) < 8:
        return img, False
    src = np.float32([k2[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dst = np.float32([k1[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    M, mask = cv2.estimateAffinePartial2D(src, dst, method=cv2.RANSAC, ransacReprojThreshold=3.0)
    if M is None:
        return img, False
    out = cv2.warpAffine(img, M, (ref.shape[1], ref.shape[0]), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT_101)
    return out, True


def main():
    ap = argparse.ArgumentParser(description='Geometrically lock a style-transformation image set to the first frame.')
    ap.add_argument('--input', required=True)
    ap.add_argument('--output', required=True)
    ap.add_argument('--width', type=int, default=1080)
    ap.add_argument('--height', type=int, default=1920)
    args = ap.parse_args()
    os.makedirs(args.output, exist_ok=True)
    files = sorted(sum([glob.glob(os.path.join(args.input, f'*.{e}')) for e in ('png','jpg','jpeg','webp')], []))
    if not files:
        raise SystemExit('No images found')
    ref = fit_canvas(cv2.imread(files[0]), args.width, args.height)
    cv2.imwrite(os.path.join(args.output, '000_reference.png'), ref)
    print(f'REF {os.path.basename(files[0])}')
    for i, f in enumerate(files[1:], start=1):
        img = fit_canvas(cv2.imread(f), args.width, args.height)
        aligned, ok = align_to_reference(ref, img)
        out = os.path.join(args.output, f'{i:03d}.png')
        cv2.imwrite(out, aligned)
        print(('LOCK' if ok else 'FALLBACK'), os.path.basename(f), '->', out)

if __name__ == '__main__':
    main()
