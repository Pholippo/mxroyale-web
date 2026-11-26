# -*- coding: utf-8 -*-
"""
Erzeugt die Web-Bilder (WebP, verkleinert) aus den Spiel-Shots.
Aufruf im Repo-Root:  python _werkzeug/bilder.py
Quellen: Shots aus abnahme/content/shots_2611/beste (4K-JPG) und – für Strecken ohne neuen Shot – die
Strecken-Vorschauen des Spiels (worktrees/n-int/public/vorschau-hd). Schreibt atomar (tmp + replace).
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = r'C:\Users\phili\Motocross\abnahme\content\shots_2611\beste'
VORSCHAU = r'C:\Users\phili\Motocross\worktrees\n-int\public\vorschau-hd'
# Strecke → bester neuer Shot (fehlt eine Strecke hier, bleibt die Vorschau aus dem Spiel)
STRECKEN_SHOTS = {
    'sunvale': 'sunvale_kurve_16x9_01.jpg',
    'frostline': 'frostline_pulk_16x9_02.jpg',
    'highcrest': 'highcrest_hero_16x9_01.jpg',
}
HERO_QUER = 'highcrest_whip_16x9_01.jpg'
HERO_HOCH = 'highcrest_whip_9x16_02.jpg'


def speichere(im, rel, q):
    ziel = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    tmp = ziel + '.tmp'
    im.save(tmp, 'WEBP', quality=q, method=6)
    os.replace(tmp, ziel)
    print(rel, im.size, os.path.getsize(ziel) // 1024, 'KB')


def main():
    for f in sorted(os.listdir(VORSCHAU)):
        tid = f[:-5]
        quelle = os.path.join(SHOTS, STRECKEN_SHOTS[tid]) if tid in STRECKEN_SHOTS else os.path.join(VORSCHAU, f)
        im = Image.open(quelle).convert('RGB')
        speichere(im.resize((960, 540), Image.LANCZOS), f'img/tracks/{tid}.webp', 72)
        speichere(im.resize((480, 270), Image.LANCZOS), f'img/tracks/{tid}-480.webp', 70)
    q = Image.open(os.path.join(SHOTS, HERO_QUER)).convert('RGB')
    speichere(q.resize((1600, 900), Image.LANCZOS), 'img/hero-whip-1600.webp', 70)
    speichere(q.resize((800, 450), Image.LANCZOS), 'img/hero-whip-800.webp', 68)
    h = Image.open(os.path.join(SHOTS, HERO_HOCH)).convert('RGB')
    # oberen Himmel wegschneiden, damit der Fahrer am Handy über dem Text steht
    h = h.crop((0, 620, 1080, 1920))
    speichere(h.resize((720, 867), Image.LANCZOS), 'img/hero-whip-hoch-720.webp', 68)


if __name__ == '__main__':
    main()
