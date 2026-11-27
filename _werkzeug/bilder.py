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
SIEGER = os.environ.get('MX_SIEGER') or r'C:\Users\phili\Motocross\abnahme\mxroyale\bild-turnier\sieger_aktuell'
# Strecke → bester Shot (Standard: <id>_hero_16x9_01.jpg). Absoluter Pfad = Blender-Render (Bild-Turnier-Sieger, 4K).
STRECKEN_SHOTS = {
    'sunvale': 'sunvale_kurve_16x9_01.jpg',
    'frostline': os.path.join(SIEGER, 'B12.png'),
    'highcrest': os.path.join(SIEGER, 'B06.png'),
    'tidewater': os.path.join(SIEGER, 'B04.png'),
    'neonharbor': os.path.join(SIEGER, 'B17.png'),
    'larkmeadow': os.path.join(SIEGER, 'B19.png'),
    'herbst': os.path.join(SIEGER, 'B09.png'),
    'arena': os.path.join(SIEGER, 'B30.png'),
}
HERO_QUER = os.path.join(SIEGER, 'B02.png')
HERO_HOCH = os.path.join(SIEGER, 'B02_916.png')
HERO_NAME = 'hero-beach-jump'
HERO_HOCH_Y = 700  # oberer Rand des 1080×1300-Ausschnitts aus dem 9:16-Render


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
        behalten.add(speichere(im.resize((320, 180), Image.LANCZOS), f'img/tracks/{s}-320.webp', 68))
    ordner = os.path.join(ROOT, 'img', 'tracks')
    for f in os.listdir(ordner):
        if f.endswith('.webp') and f not in behalten:
            os.remove(os.path.join(ordner, f))
            print('entfernt', f)
    # Pressefotos 1920×1080 JPG + Vorschau 480 (WebP) für /press/ und das ZIP
    from texte import PRESSE_SHOTS
    for quelle, name, _, _ in PRESSE_SHOTS:
        im = Image.open(os.path.join(SHOTS, quelle)).convert('RGB')
        ziel = os.path.join(ROOT, 'presse', name)
        im.resize((1920, 1080), Image.LANCZOS).save(ziel + '.tmp', 'JPEG', quality=86, optimize=True, progressive=True)
        os.replace(ziel + '.tmp', ziel)
        print('presse/' + name, os.path.getsize(ziel) // 1024, 'KB')
        speichere(im.resize((480, 270), Image.LANCZOS), 'presse/vorschau/' + name.replace('.jpg', '-480.webp'), 70)
    q = Image.open(HERO_QUER).convert('RGB')
    speichere(q.resize((1600, 900), Image.LANCZOS), f'img/{HERO_NAME}-1600.webp', 70)
    speichere(q.resize((800, 450), Image.LANCZOS), f'img/{HERO_NAME}-800.webp', 68)
    h = Image.open(HERO_HOCH).convert('RGB')
    # Ausschnitt 1080×1300 (= 720×867), Fahrer im oberen Teil, damit er am Handy über dem Text steht
    h = h.crop((0, HERO_HOCH_Y, 1080, HERO_HOCH_Y + 1300))
    speichere(h.resize((720, 867), Image.LANCZOS), f'img/{HERO_NAME}-hoch-720.webp', 68)
    for alt in ('hero-whip-1600.webp', 'hero-whip-800.webp', 'hero-whip-hoch-720.webp'):
        if os.path.exists(os.path.join(ROOT, 'img', alt)):
            os.remove(os.path.join(ROOT, 'img', alt))
            print('entfernt', alt)


if __name__ == '__main__':
    main()
