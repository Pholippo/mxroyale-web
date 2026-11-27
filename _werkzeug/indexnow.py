# -*- coding: utf-8 -*-
"""
Meldet URLs per IndexNow (Bing, Yandex, Seznam, Naver, Yep …). Nach jedem Push/Live-Gang aufrufen.
  python _werkzeug/indexnow.py                 → alle URLs aus sitemap.xml
  python _werkzeug/indexnow.py --geaendert     → nur Seiten, die der letzte Commit geändert hat
  python _werkzeug/indexnow.py URL [URL …]     → nur diese
Wartet vorher, bis die erste URL live mit 200 antwortet (GitHub Pages braucht ~1 min). Fehler → Exit-Code 1.
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = 'mxroyale.com'
KEY = '1946cdc237f483b2388f8e786b02136e'


def sitemap_urls():
    return re.findall(r'<loc>([^<]+)</loc>', open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read())


def geaenderte_urls():
    dateien = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    alle = set(sitemap_urls())
    urls = []
    for d in dateien:
        if d.endswith('index.html'):
            u = f'https://{HOST}/' + d[:-len('index.html')]
            if u in alle:
                urls.append(u)
    return urls


def warte_live(url, max_s=240):
    ende = time.time() + max_s
    while True:
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'mxroyale-indexnow'}), timeout=20) as r:
                if r.status == 200:
                    return
        except urllib.error.URLError:
            pass
        if time.time() > ende:
            raise SystemExit(f'nicht live: {url}')
        time.sleep(10)


def main(args):
    if args == ['--geaendert']:
        urls = geaenderte_urls()
    else:
        urls = args or sitemap_urls()
    if not urls:
        print('keine URLs zu melden')
        return 0
    warte_live(urls[0])
    body = json.dumps({'host': HOST, 'key': KEY, 'keyLocation': f'https://{HOST}/{KEY}.txt', 'urlList': urls}).encode()
    req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body, method='POST',
                                 headers={'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'mxroyale-indexnow'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print('IndexNow', r.status, len(urls), 'URLs')
            return 0 if r.status in (200, 202) else 1
    except urllib.error.HTTPError as f:
        print('IndexNow FEHLER', f.code, f.read()[:300], file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
