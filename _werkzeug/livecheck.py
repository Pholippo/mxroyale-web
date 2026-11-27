# -*- coding: utf-8 -*-
"""
Live-Prüfung nach dem Push: jede Sitemap-URL 200, canonical = eigene URL, hreflang-Ziele antworten mit 200,
JSON-LD parsebar, Bilder aus der Sitemap erreichbar, dazu security.txt/humans.txt/llms.txt.
  python _werkzeug/livecheck.py [--warte-auf TEXT]   (wartet bis zu 4 min, bis TEXT auf der Startseite steht)
"""
import json
import re
import sys
import time
import urllib.request

SITE = 'https://mxroyale.com'


def hole(url):
    req = urllib.request.Request(url + ('&' if '?' in url else '?') + f'nc={time.time():.0f}', headers={'User-Agent': 'mxroyale-livecheck'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, r.read().decode('utf-8', 'replace')


def main(args):
    if args[:1] == ['--warte-auf']:
        ende = time.time() + 240
        while args[1] not in hole(SITE + '/')[1]:
            if time.time() > ende:
                print('FEHLER: neue Version nicht live')
                return 1
            time.sleep(15)
    fehler = []
    _, sm = hole(SITE + '/sitemap.xml')
    seiten = re.findall(r'<loc>([^<]+)</loc>', sm)
    bilder = sorted(set(re.findall(r'<image:loc>([^<]+)</image:loc>', sm)))
    for u in seiten:
        st, t = hole(u)
        if st != 200:
            fehler.append(f'{u} {st}')
            continue
        c = re.search(r'<link rel="canonical" href="([^"]+)">', t)
        if not c or c.group(1) != u:
            fehler.append(f'{u} canonical {c and c.group(1)}')
        for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            try:
                json.loads(b)
            except ValueError as f:
                fehler.append(f'{u} JSON-LD {f}')
        for h in set(re.findall(r'hreflang="[^"]+" href="([^"]+)"', t)):
            if h not in seiten:
                fehler.append(f'{u} hreflang-Ziel nicht in Sitemap: {h}')
    for u in bilder + [SITE + p for p in ('/.well-known/security.txt', '/humans.txt', '/llms.txt', '/llms-full.txt', '/robots.txt')]:
        try:
            st, _ = hole(u)
            if st != 200:
                fehler.append(f'{u} {st}')
        except Exception as f:  # noqa: BLE001 – jeder Fehler wird gemeldet
            fehler.append(f'{u} {f}')
    print(f'{len(seiten)} Seiten, {len(bilder)} Bilder geprüft')
    for f in fehler:
        print('FEHLER', f)
    return 1 if fehler else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
