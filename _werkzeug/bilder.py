# -*- coding: utf-8 -*-
"""
Erzeugt die Web-Bilder (WebP, verkleinert) aus den Spiel-Shots.
Aufruf im Repo-Root:  python _werkzeug/bilder.py
Quelle: Shots aus abnahme/content/shots_2611/beste (4K-JPG). Dateinamen = Streckenname als Slug
(z. B. img/tracks/sunvale-mx-park.webp), damit der Name auch in der Bildersuche steht. Schreibt atomar (tmp + replace)
und räumt alte Streckenbilder weg, die nicht mehr verwendet werden.
"""
import os
import sys
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import TRACKS, bild_slug  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = r'C:\Users\phili\Motocross\abnahme\content\shots_2611\beste'
# Strecke → bester Shot (Standard: <id>_hero_16x9_01.jpg)
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
    return os.path.basename(ziel)


def main():
    behalten = set()
    for t in TRACKS:
        quelle = os.path.join(SHOTS, STRECKEN_SHOTS.get(t['id'], f'{t["id"]}_hero_16x9_01.jpg'))
        im = Image.open(quelle).convert('RGB')
        s = bild_slug(t)
        behalten.add(speichere(im.resize((960, 540), Image.LANCZOS), f'img/tracks/{s}.webp', 72))
        behalten.add(speichere(im.resize((480, 270), Image.LANCZOS), f'img/tracks/{s}-480.webp', 70))
    ordner = os.path.join(ROOT, 'img', 'tracks')
    for f in os.listdir(ordner):
        if f.endswith('.webp') and f not in behalten:
            os.remove(os.path.join(ordner, f))
            print('entfernt', f)
    q = Image.open(os.path.join(SHOTS, HERO_QUER)).convert('RGB')
    speichere(q.resize((1600, 900), Image.LANCZOS), 'img/hero-whip-1600.webp', 70)
    speichere(q.resize((800, 450), Image.LANCZOS), 'img/hero-whip-800.webp', 68)
    h = Image.open(os.path.join(SHOTS, HERO_HOCH)).convert('RGB')
    # oberen Himmel wegschneiden, damit der Fahrer am Handy über dem Text steht
    h = h.crop((0, 620, 1080, 1920))
    speichere(h.resize((720, 867), Image.LANCZOS), 'img/hero-whip-hoch-720.webp', 68)


if __name__ == '__main__':
    main()
