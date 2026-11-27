# -*- coding: utf-8 -*-
"""
Baut die Inhaltsseiten von mxroyale.com in fünf Sprachen aus einer Quelle:
  EN  /  /tracks/  /how-to-play/  /about/          DE  /de/  /de/strecken/  /de/anleitung/  /de/ueber/
  ES  /es/  /es/pistas/  /es/como-jugar/  /es/acerca-de/   FR  /fr/  /fr/circuits/  /fr/comment-jouer/  /fr/a-propos/
  PT-BR  /pt/  /pt/pistas/  /pt/como-jogar/  /pt/sobre/
plus sitemap.xml (mit hreflang + Bildern), robots.txt, llms.txt, llms-full.txt.
Texte: _werkzeug/texte.py (alle Sprachen), Strecken-Grunddaten + EN/DE-Streckentexte hier bei TRACKS.

Aufruf (im Repo-Root):  python _werkzeug/build.py
Prüft am Ende selbst: Titel ≤ 60, Description ≤ 155 Zeichen, JSON-LD parsebar, hreflang-Gruppen vollständig und gegenseitig.
Ordner mit „_“ veröffentlicht GitHub Pages (Jekyll) nicht – das Skript bleibt privat.
Presse (/press/, /presse/) wird mit gebaut (nur EN/DE, samt ZIP-Pressepaket); rechtliche Seiten NICHT (von Hand gepflegt).
Spiel-Fakten stammen aus dem Spiel-Repo (src/world/track.ts, tracks/*.ts, src/i18n/*.ts, input/tastenBelegung.ts).
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from texte import PFAD, FAQ, TX, TRACK_TX, DIFF_INTL, TYP_INTL, BILD_ALT, IN_MX, PRESSE, PRESSE_SHOTS, NEWS, NEWS_TX  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://mxroyale.com'
PLAY = 'https://play.mxroyale.com/'
STAND = '2026-11-27'
BETA = '2026-11-26'  # Start der offenen Beta (datePublished)
STAND_TXT = {'en': '27 November 2026', 'de': '27. November 2026', 'es': '27 de noviembre de 2026',
             'fr': '27 novembre 2026', 'pt': '27 de novembro de 2026'}
SOCIAL = [
    'https://www.tiktok.com/@mxroyalegame',
    'https://www.instagram.com/mxroyalegame/',
    'https://www.youtube.com/@mxroyalegame',
]
SPRACHEN = ['en', 'de', 'es', 'fr', 'pt']          # Website-Sprachen (interner Schlüssel)
HL = {'en': 'en', 'de': 'de', 'es': 'es', 'fr': 'fr', 'pt': 'pt-BR'}  # hreflang / <html lang>
KURZ = {'en': 'EN', 'de': 'DE', 'es': 'ES', 'fr': 'FR', 'pt': 'PT'}
LANGS = ['en', 'de', 'es', 'fr', 'pt-BR']           # Sprachen des Spiels (JSON-LD)
PLAY_Q = {'en': '', 'de': '?lang=de', 'es': '?lang=es', 'fr': '?lang=fr', 'pt': '?lang=pt'}

# hreflang-Gruppen: Inhaltsseiten in allen fünf Sprachen, Presse/Recht nur EN/DE (von Hand gepflegt)
GRUPPEN = [{l: PFAD[l][k] for l in SPRACHEN} for k in ('home', 'tracks', 'how', 'about')] + \
          [{'en': PFAD['en'][k], 'de': PFAD['de'][k]} for k in ('press', 'legal', 'privacy')] + \
          [{'en': '/news/', 'de': '/de/neuigkeiten/'}]
NEWS_PFAD = {'en': '/news/', 'de': '/de/neuigkeiten/'}
PRIO = {'/': '1.0', '/de/': '0.9', '/es/': '0.9', '/fr/': '0.9', '/pt/': '0.9',
        '/tracks/': '0.8', '/how-to-play/': '0.8', '/about/': '0.7', '/press/': '0.4', '/presse/': '0.3',
        '/legal/': '0.1', '/impressum/': '0.1', '/privacy/': '0.1', '/datenschutz/': '0.1'}


def prio(p):
    return PRIO.get(p, '0.7' if p.endswith(('strecken/', 'pistas/', 'circuits/', 'anleitung/', 'como-jugar/', 'comment-jouer/', 'como-jogar/')) else '0.6')


def gruppe(pfad):
    for g in GRUPPEN:
        if pfad in g.values():
            return g
    raise KeyError(pfad)


# ── Strecken (Reihenfolge: leicht → schwer, dann Freeride) ─────────────────────────────────────────
DIFF = {
    'Beginner': ('Beginner', 'Einsteiger'), 'Mittel': ('Medium', 'Mittel'),
    'Mittel bis schwer': ('Medium–hard', 'Mittel bis schwer'), 'Schwer': ('Hard', 'Schwer'), 'Freeride': ('Freeride', 'Freeride'),
}
TRACKS = [
    dict(id='sunvale', name='Sunvale MX Park', diff='Beginner', field=10, typ=('Motocross', 'Motocross'),
         en_k='The beginner track: a farm-country MX park with rollers, small tables and a creek ford.',
         en='Most riders start here. Wide grassy turns, rollers and small tables lead over cow pastures and past hay bales, and one section runs straight through a creek. A good place to learn the pop and your first whips.',
         de_k='Die Einsteiger-Strecke: ein MX-Park zwischen Wiesen und Hof, mit Rollern, kleinen Tables und einer Bach-Furt.',
         de='Hier fangen die meisten an. Breite Wiesenkurven, Roller und kleine Tables führen über Kuhweiden und an Heuballen vorbei, ein Abschnitt geht mitten durch den Bach. Ideal, um den Pop und die ersten Whips zu lernen.'),
    dict(id='larkmeadow', name='Larkmeadow SX', diff='Mittel', field=12, typ=('Supercross', 'Supercross'),
         en_k='Supercross in a night stadium: rhythm lanes, whoops, a sand section and a finish-line triple.',
         en='A short, tight supercross track under stadium lights. Rhythm lanes, a whoops section and a sand section come one after another, and the lap ends with an SX double and a triple over the finish line.',
         de_k='Supercross im Nachtstadion: Rhythmus-Reihen, Whoops, Sand-Sektion und ein Triple über die Ziellinie.',
         de='Eine kurze, enge Supercross-Strecke unter Flutlicht. Rhythmus-Reihen, Whoops und eine Sand-Sektion folgen dicht aufeinander, am Ende der Runde warten ein SX-Double und ein Triple über die Ziellinie.'),
    dict(id='frostline', name='Frostline MX', diff='Mittel', field=12, typ=('Snow', 'Schnee'),
         en_k='Snow track down a ski slope, along the chairlift and over the Frozen Creek Gap.',
         en='Frostline runs down a ski slope in winter: along the chairlift line, past snow cannons and over the Frozen Creek Gap. Snow rollers and a big jump into the finish straight close the lap.',
         de_k='Schneestrecke auf einer Skipiste, entlang des Sessellifts und über den Frozen Creek Gap.',
         de='Frostline führt im Winter eine Skipiste hinunter: entlang der Lifttrasse, an Schneekanonen vorbei und über den Frozen Creek Gap. Schneewellen und ein großer Sprung auf die Zielgerade schließen die Runde.'),
    dict(id='monsoon', name='Monsoon Terraces', diff='Mittel', field=12, typ=('Motocross', 'Motocross'),
         en_k='A flowing track over rice terraces on a hillside, with a terrace chain and a wooden aqueduct.',
         en='A flowing layout on a terraced hillside. A chain of jumps drops from terrace to terrace, the track passes bamboo and runs along a wooden aqueduct. Rewards a smooth line more than raw speed.',
         de_k='Flow-Strecke über Reisterrassen am Hang, mit Terrassen-Kette und Holz-Aquädukt.',
         de='Ein flüssiger Kurs am Terrassenhang. Eine Sprung-Kette geht von Terrasse zu Terrasse, die Strecke führt an Bambus vorbei und entlang eines Holz-Aquädukts. Hier zählt eine saubere Linie mehr als rohes Tempo.'),
    dict(id='mirage-flats', name='Mirage Flats', diff='Mittel bis schwer', field=12, typ=('Desert', 'Wüste'),
         en_k='Desert jump park on a dry lake bed, with a rail gap over the train tracks and a long washboard.',
         en='A jump park in the desert. You clear the railway with the Rail Gap, hammer through a washboard section on the dry lake bed and finish with the Mirage table. Lots of air time, little room for mistakes on the landings.',
         de_k='Wüsten-Sprungpark auf einem ausgetrockneten See, mit Rail Gap über die Gleise und langem Waschbrett.',
         de='Ein Sprungpark in der Wüste. Mit dem Rail Gap geht es über die Bahngleise, auf dem Salzsee-Boden durch ein Waschbrett, zum Schluss über den Fata-Morgana-Table. Viel Airtime, wenig Platz für Fehler bei der Landung.'),
    dict(id='herbst', name='Glutwald MX', diff='Mittel bis schwer', field=10, typ=('Forest', 'Wald'),
         en_k='Autumn forest in evening light, with fire at three jumps, a big step-up and a big step-down.',
         en='An autumn forest track in low evening light. Three jumps have fire next to them, the climb has a big step-up and the descent a big step-down into the valley. Leaves, roots and rhythm sections in between.',
         de_k='Herbstwald im Abendlicht, Feuer an drei Sprüngen, großer Step-up und großer Step-down.',
         de='Eine Herbstwald-Strecke im Abendlicht. Neben drei Sprüngen brennt Feuer, bergauf wartet ein großer Step-up, bergab ein großer Step-down ins Tal. Dazwischen Laub, Wurzeln und Rhythmus-Passagen.'),
    dict(id='rustleaf', name='Rustleaf Hollow', diff='Mittel bis schwer', field=10, typ=('Forest', 'Wald'),
         en_k='A twisty autumn woods track with roots, a muddy hollow and a log-skidding lane.',
         en='Narrow and twisty: Rustleaf winds through autumn woods over root carpets, through a muddy hollow, along a log-skidding lane and past an excavator. A track for precise steering rather than flat-out speed.',
         de_k='Schlängel-Waldstrecke im Herbst mit Wurzeln, Matsch-Senke und Holzrücke-Gasse.',
         de='Eng und kurvig: Rustleaf schlängelt sich durch den Herbstwald, über Wurzelteppiche, durch eine Matsch-Senke, die Holzrücke-Gasse entlang und an einem Bagger vorbei. Eine Strecke für genaues Lenken statt Vollgas.'),
    dict(id='neonharbor', name='Neon Harbor SX', diff='Mittel bis schwer', field=12, typ=('Supercross', 'Supercross'),
         en_k='Supercross at night in a harbour hall: container table, crane turn, dock whoops and a triple.',
         en='The second supercross track sits in a harbour hall at night. You jump a table built from shipping containers, turn under a crane, fight through the dock whoops and go for the Harbor Triple.',
         de_k='Supercross bei Nacht in der Hafenhalle: Container-Table, Kran-Kehre, Dock-Whoops und ein Triple.',
         de='Die zweite Supercross-Strecke liegt nachts in einer Hafenhalle. Gesprungen wird über einen Table aus Containern, gewendet unter dem Kran, dazu Dock-Whoops und das Harbor Triple.'),
    dict(id='pine-ridge', name='Pine Ridge GP', diff='Schwer', field=12, typ=('Grand Prix', 'Grand Prix'),
         en_k='A long forest Grand Prix up a ridge, with Horsepower Hill, the Stump Double and the Ridge Double.',
         en='A classic outdoor Grand Prix through pine forest. The track climbs Horsepower Hill, runs along the ridge over roots and doubles and comes back down through the woods. Long laps, a full gate of 12 riders.',
         de_k='Langer Wald-Grand-Prix über einen Bergkamm, mit Horsepower Hill, Stump Double und Ridge Double.',
         de='Ein klassischer Outdoor-Grand-Prix durch den Kiefernwald. Die Strecke klettert den Horsepower Hill hinauf, führt über Wurzeln und Doubles den Kamm entlang und durch den Wald zurück. Lange Runden, volles Starterfeld mit 12 Fahrern.'),
    dict(id='sandglass', name='Sandglass Canyon GP', diff='Schwer', field=12, typ=('Canyon', 'Canyon'),
         en_k='Desert canyon Grand Prix: rock steps, a mesa table, a slot canyon, a cliff drop and a road gap.',
         en='Sandglass takes you through red desert canyons. Rock steps and slabs, a table on top of a mesa, a narrow slot canyon, a drop off a cliff and a Road Gap over the highway, then back down the wash through the whoops.',
         de_k='Canyon-Grand-Prix in der Wüste: Felsstufen, Mesa-Table, Slot-Canyon, Klippen-Drop und Road Gap.',
         de='Sandglass führt durch rote Wüsten-Canyons: Felsstufen und Felsplatten, ein Table oben auf der Mesa, ein enger Slot-Canyon, ein Drop von der Klippe und ein Road Gap über den Highway, dann durch die Whoops im Trockental zurück.'),
    dict(id='highcrest', name='Highcrest Valley GP', diff='Schwer', field=12, typ=('Mountain', 'Berg'),
         en_k='A long, fast mountain GP with 38 m of elevation, limestone slabs, switchbacks and a waterfall.',
         en='The fastest outdoor track: Highcrest climbs 38 metres through forest and rock, over limestone slabs and up switchbacks to the summit, then drops through a rock gate and past a waterfall.',
         de_k='Langer, schneller Berg-GP mit 38 m Höhenunterschied, Kalkplatten, Serpentinen und Wasserfall.',
         de='Die schnellste Outdoor-Strecke: Highcrest steigt 38 Meter durch Wald und Fels an, über Kalkplatten und Serpentinen zum Gipfel, und fällt dann durch ein Felstor und an einem Wasserfall vorbei ab.'),
    dict(id='canopy', name='Canopy Hollow', diff='Schwer', field=10, typ=('Rainforest', 'Regenwald'),
         en_k='Rainforest in a hollow: canyon gap, suspension bridge, tree tunnel, waterfall and a dragon’s back.',
         en='A twisting rainforest track down in a hollow. Jump a canyon gap, cross a suspension bridge, ride through a tunnel of trees and past a waterfall, and keep your balance on the dragon’s back.',
         de_k='Regenwald in einer Senke: Schlucht-Gap, Hängebrücke, Baumtunnel, Wasserfall und Dragon’s Back.',
         de='Eine kurvige Regenwald-Strecke in einer Senke. Es geht über einen Schlucht-Gap und eine Hängebrücke, durch einen Baumtunnel, am Wasserfall vorbei und über den Dragon’s Back.'),
    dict(id='tidewater', name='Tidewater Flats', diff='Schwer', field=10, typ=('Beach', 'Strand'),
         en_k='A technical sand GP on the coast at low tide, with a creek gap and a ride through a shipwreck.',
         en='Sand riding on the coast at low tide. Ripples and soft sand everywhere, a gap over a tidal creek, a turn by the lighthouse, a lane between the groynes and a line straight through an old shipwreck.',
         de_k='Technischer Sand-GP an der Küste bei Ebbe, mit Priel-Gap und Durchfahrt durchs Schiffswrack.',
         de='Sandfahren an der Küste bei Ebbe. Überall Rippeln und weicher Sand, ein Gap über den Priel, eine Kehre am Leuchtfeuer, eine Gasse zwischen den Buhnen und eine Linie mitten durch ein altes Schiffswrack.'),
    dict(id='ironcut', name='Ironcut Quarry', diff='Schwer', field=10, typ=('Quarry', 'Steinbruch'),
         en_k='A disused quarry: switchbacks up the mining terraces, a pit drop and a dragon’s back on the rim.',
         en='Ironcut climbs a disused quarry in switchbacks from terrace to terrace. On top you ride a dragon’s back along the rim before a steep drop back down into the pit.',
         de_k='Stillgelegter Steinbruch: Serpentinen über die Abbau-Terrassen, Grubendrop und Drachenrücken an der Kante.',
         de='Ironcut klettert in Serpentinen von Terrasse zu Terrasse durch einen stillgelegten Steinbruch. Oben an der Kante wartet ein Drachenrücken, dann geht es steil zurück in die Grube.'),
    dict(id='saltpan', name='Saltpan Speedway', diff='Schwer', field=12, typ=('Salt lake', 'Salzsee'),
         en_k='A fast Grand Prix on a salt lake, with the Salt Crust Triple and a conveyor table.',
         en='Wide open and fast: Saltpan crosses a salt lake with long straights and rollers. The highlights are the Salt Crust Triple and a table next to the salt works’ conveyor belt.',
         de_k='Schneller Grand Prix auf einem Salzsee, mit Salt Crust Triple und Förderband-Table.',
         de='Weit und schnell: Saltpan führt über einen Salzsee mit langen Geraden und Rollern. Höhepunkte sind das Salt Crust Triple und ein Table am Förderband der Saline.'),
    dict(id='freeride', name='Dust Devil Freeride', diff='Freeride', field=None, typ=('Freeride', 'Freeride'),
         en_k='Freeride map: jump lines, a step-up, a hip and a foam pit, with no laps and no timer.',
         en='No laps, no timer, no opponents. Dust Devil is an open map with jump lines, a step-up, a hip and a foam pit to practise tricks without consequences.',
         de_k='Freeride-Map: Sprung-Linien, Step-up, Hip und Foam-Pit, ohne Runden und ohne Uhr.',
         de='Keine Runden, keine Uhr, keine Gegner. Dust Devil ist eine offene Map mit Sprung-Linien, Step-up, Hip und Foam-Pit, auf der du Tricks ohne Folgen üben kannst.'),
    dict(id='arena', name='Midnight Arena', diff='Freeride', field=None, typ=('Freestyle', 'Freestyle'),
         en_k='Freestyle motocross night show in a stadium, with kickers for whips, flips and big air.',
         en='A freestyle motocross show at night in a stadium. Separate ramps for whips, backflips, Nac-Nacs, Can-Cans and big air, plus a quarterpipe and fireworks.',
         de_k='Freestyle-Motocross-Show bei Nacht im Stadion, mit Kickern für Whips, Flips und Big Air.',
         de='Eine Freestyle-Motocross-Show bei Nacht im Stadion. Eigene Rampen für Whips, Backflips, Nac-Nacs, Can-Cans und Big Air, dazu eine Quarterpipe und Feuerwerk.'),
]
N_RACE = sum(1 for t in TRACKS if t['diff'] != 'Freeride')
N_FREE = len(TRACKS) - N_RACE

e = html.escape
LAZY = ' loading="lazy"'
FONTS = ''.join(f'<link rel="preload" as="font" type="font/woff2" href="/fonts/{f}.woff2" crossorigin>\n' for f in (
    'HTxyL3I-JCGChYJ8VI-L6OO_au7B6xTrW3bmu4kG', 'wlpigxjLBV1hqnzfr-F8sEYMB0Yybp0mudRfi6m_B2sl', 'wlpigxjLBV1hqnzfr-F8sEYMB0Yybp0mudRfw6-_B2sl'))



CSS = """
:root{--bg:#15130f;--bg2:#1f1b15;--bg3:#2a251d;--text:#f4efe6;--muted:#bdb4a5;--gelb:#f5b82e;color-scheme:dark}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font:17px/1.55 "Barlow Semi Condensed",system-ui,sans-serif}
a{color:inherit}
p a,li a,td a,dd a{color:var(--gelb)}
.wrap{max-width:1080px;margin:0 auto;width:100%}
.skip{position:absolute;left:-9999px}.skip:focus{left:16px;top:8px;z-index:9;background:var(--gelb);color:var(--bg);padding:8px 12px}
.nav{position:relative;z-index:2;padding:14px 16px;text-shadow:0 1px 3px rgba(0,0,0,.6)}
.nav .wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:6px 18px}
.marke{font:italic 900 26px/1 "Barlow Condensed",sans-serif;text-decoration:none;letter-spacing:-.01em}
.marke span{background:var(--gelb);color:var(--bg);padding:1px 6px 0;display:inline-block;transform:skewX(-10deg)}
.nav ul{display:flex;flex-wrap:wrap;gap:4px 16px;list-style:none;margin:0;padding:0;font-weight:700;font-size:16px}
.nav ul a{text-decoration:none;display:inline-block;padding:6px 0}
.nav ul a:hover,.nav ul a[aria-current]{color:var(--gelb)}
.hero{position:relative;min-height:92vh;display:grid;grid-template-rows:auto 1fr;overflow:hidden}
.hero-bild{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 0;z-index:0}
.hero::after{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(21,19,15,.55),rgba(21,19,15,0) 16%),linear-gradient(0deg,var(--bg) 2%,rgba(21,19,15,.55) 40%,rgba(21,19,15,.1) 75%)}
.hero-inhalt{position:relative;z-index:2;align-self:end;padding:0 16px 9vh}
.logo{display:inline-flex;flex-direction:column;line-height:.82;font-family:"Barlow Condensed",sans-serif}
.logo .mx{font-weight:900;font-style:italic;font-size:clamp(84px,19vw,170px);letter-spacing:-.02em}
.logo .pl{align-self:flex-start;margin-top:.05em;background:var(--gelb);color:var(--bg);font-weight:900;font-style:italic;font-size:clamp(36px,8vw,72px);padding:.06em .3em 0;transform:skewX(-10deg);border:3px solid var(--bg);box-shadow:4px 4px 0 var(--bg)}
h1.claim{font:700 clamp(22px,3.6vw,30px)/1.25 "Barlow Semi Condensed",sans-serif;text-transform:none;margin:26px 0 6px;max-width:680px}
.claim-sub{font:600 clamp(17px,2.4vw,21px)/1.3 "Barlow Semi Condensed",sans-serif;margin:0 0 26px;color:var(--muted)}
.los{display:inline-block;background:var(--gelb);color:var(--bg);text-decoration:none;font:italic 900 clamp(26px,5vw,36px) "Barlow Condensed",sans-serif;text-transform:uppercase;padding:14px 40px 12px;transform:skewX(-8deg);box-shadow:5px 5px 0 #000;transition:transform .12s}
.los:hover{transform:skewX(-8deg) translateY(-2px)}
.los.klein-los{font-size:24px;padding:10px 26px 8px}
.klein{color:var(--muted);margin-top:14px;font-size:15px}
section{padding:64px 16px}
h1,h2{font:italic 900 clamp(34px,6vw,52px)/1 "Barlow Condensed",sans-serif;text-transform:uppercase;margin:0 0 28px}
h1 span,h2 span{color:var(--gelb)}
h3{font:italic 800 26px/1.1 "Barlow Condensed",sans-serif;text-transform:uppercase;margin:0 0 6px}
.lead{font-size:20px;max-width:760px;margin:0 0 28px}
.karten{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px}
.karte{background:var(--bg2);border-left:4px solid var(--gelb);padding:18px 20px}
.karte b{display:block;font:italic 800 26px "Barlow Condensed",sans-serif;text-transform:uppercase;margin-bottom:4px}
.karte p{margin:0;color:var(--muted)}
.strecken{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px;list-style:none;margin:0;padding:0}
.strecken li{background:var(--bg2)}
.strecken a{text-decoration:none;display:block;height:100%}
.strecken img,.strecke img{width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;display:block;background:var(--bg3)}
.strecken div{padding:12px 14px 16px}
.strecken p{margin:4px 0 0;color:var(--muted);font-size:16px}
.tag{display:inline-block;font-size:14px;font-weight:700;color:var(--bg);background:var(--gelb);padding:0 6px;margin-right:6px}
.tag.grau{background:var(--bg3);color:var(--text)}
@media (max-width:560px){.strecken{grid-template-columns:1fr 1fr;gap:10px}.strecken div{padding:8px 10px 12px}.strecken h3{font-size:19px}.strecken p{font-size:14px;line-height:1.4}.tag{font-size:12px;margin-bottom:2px}}
.mehr{display:inline-block;margin-top:22px;font-weight:700;color:var(--gelb)}
.faq{max-width:820px}
.faq h3{font:700 21px/1.3 "Barlow Semi Condensed",sans-serif;text-transform:none;margin:26px 0 6px}
.faq p{margin:0;color:var(--muted)}
.team,.dunkel{background:var(--bg2)}
.seitenkopf{padding:40px 16px 8px}
.strecke{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:24px;align-items:center;padding:28px 0;border-top:1px solid var(--bg3);scroll-margin-top:16px}
.strecke p{margin:8px 0 0}
.fakten{color:var(--muted);font-size:15px;margin-top:6px}
@media (max-width:720px){.strecke{grid-template-columns:1fr;gap:12px}}
.text{max-width:820px}
.text h2{font-size:clamp(28px,5vw,40px);margin:44px 0 14px}
.text ul{padding-left:20px}.text li{margin:6px 0}
kbd{display:inline-block;min-width:1.6em;text-align:center;background:var(--bg3);border:1px solid #4a4234;border-bottom-width:3px;border-radius:4px;padding:0 6px;font:700 15px/1.5 "Barlow Semi Condensed",sans-serif}
table{border-collapse:collapse;width:100%;margin:8px 0 0}
th,td{padding:9px 10px;border-bottom:1px solid var(--bg3);vertical-align:top;text-align:left}
th{color:var(--muted);font-weight:500;width:34%}
.tabelle{overflow-x:auto}
footer{padding:40px 16px 60px;color:var(--muted);font-size:15px;border-top:1px solid var(--bg3)}
footer .wrap{display:flex;flex-wrap:wrap;gap:14px 36px;justify-content:space-between}
.nav .sprachen{display:flex;gap:0 10px;font-size:14px;letter-spacing:.04em}
.nav .sprachen a{opacity:.75}.nav .sprachen a[aria-current]{opacity:1;color:var(--gelb)}
.box{background:var(--bg2);padding:16px 18px;border-left:4px solid var(--gelb);margin:8px 0 18px;white-space:pre-line}
.box b{display:block;color:var(--gelb);margin-bottom:4px}
.dl{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}
.dl a{display:block;background:var(--bg2);padding:10px;text-decoration:none;color:var(--text);font-size:15px}
.dl img{width:100%;height:auto;display:block;margin-bottom:6px}
footer ul{list-style:none;margin:0;padding:0}footer li{margin:4px 0}
footer a{text-decoration:none}footer a:hover{color:var(--gelb);text-decoration:underline}
"""

SCRIPT = """<script>
  // Adresse des Spiels (Release-Server). spiel.json pflegt der Link-Wächter auf dem Server, falls sich der Tunnel ändert.
  var SPIEL = 'https://play.mxroyale.com/', Q = '%s';
  var sofort = /[?&](los|play)(=|&|$)/.test(location.search);
  function setze(u) { SPIEL = u; document.querySelectorAll('a.spiel').forEach(function (a) { a.href = SPIEL + (location.search || Q); }); }
  setze(SPIEL);
  fetch('/spiel.json', { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (j) { if (j && /^https:\\/\\//.test(j.spiel)) setze(j.spiel); })
    .catch(function () {}).then(function () { if (sofort) location.replace(SPIEL + (location.search || Q)); });
</script>"""


def ctx(lang, **mehr):
    p = PFAD[lang]
    d = dict(nr=N_RACE, nf=N_FREE, sx=', '.join(t['name'] for t in TRACKS if t['typ'][0] == 'Supercross'),
             tracks=p['tracks'], how=p['how'], about=p['about'], press=p['press'], stand=STAND_TXT[lang],
             ride=ride(lang, ' klein-los'))
    d.update(mehr)
    return d


def tx(lang, key, **mehr):
    return TX[lang][key].format(**ctx(lang, **mehr))


def ride(lang, extra=''):
    return f'<a class="los spiel{extra}" href="{PLAY}{PLAY_Q[lang]}">{TX[lang]["ride"]}</a>'


def sprachlinks(lang, pfad, lang_codes=True):
    """Links auf dieselbe Seite in den anderen Sprachen (nur vorhandene Gegenstücke)."""
    teile = []
    for l, p in gruppe(pfad).items():
        name = KURZ[l] if lang_codes else TX[l]['lang_name']
        if l == lang:
            teile.append(f'<a href="{p}" aria-current="true" title="{TX[l]["lang_name"]}">{name}</a>')
        else:
            teile.append(f'<a href="{p}" hreflang="{HL[l]}" lang="{HL[l]}" title="{TX[l]["lang_name"]}">{name}</a>')
    return teile


def nav(lang, pfad):
    p, t = PFAD[lang], TX[lang]
    teile = []
    for h, n in ((p['tracks'], t['nav_tracks']), (p['how'], t['nav_how']), (p['about'], t['nav_about'])):
        attr = ' aria-current="page"' if h == pfad else ''
        teile.append(f'<li><a href="{h}"{attr}>{e(n)}</a></li>')
    spr = ''.join(sprachlinks(lang, pfad))
    return (f'<nav class="nav" aria-label="{e(t["nav_aria"])}"><div class="wrap">'
            f'<a class="marke" href="{p["home"]}">MX <span>ROYALE</span></a>'
            f'<ul>{"".join(teile)}<li class="sprachen">{spr}</li></ul></div></nav>')


def footer(lang, pfad):
    p, t = PFAD[lang], TX[lang]
    soc = ''.join(f'<li><a href="{u}" rel="me noopener">{n} @mxroyalegame</a></li>'
                  for u, n in zip(SOCIAL, ['TikTok', 'Instagram', 'YouTube']))
    spr = ''.join(f'<li>{a}</li>' for a in sprachlinks(lang, pfad, lang_codes=False))
    return f"""<footer>
  <div class="wrap">
    <div><b>MX Royale</b><br>{e(t['foot_claim'])}<br>© 2026 MX Royale</div>
    <ul><li><a href="{p['home']}">{e(t['home'])}</a></li><li><a href="{p['tracks']}">{e(t['nav_tracks'])}</a></li><li><a href="{p['how']}">{e(t['nav_how'])}</a></li><li><a href="{p['about']}">{e(t['nav_about'])}</a></li><li><a href="{p['press']}">{e(t['nav_press'])}</a></li><li><a href="{NEWS_PFAD.get(lang, '/news/')}">{e(NEWS_TX.get(lang, NEWS_TX['en'])['nav'])}</a></li></ul>
    <ul>{soc}</ul>
    <ul><li><a href="mailto:info@mxroyale.com">info@mxroyale.com</a></li><li><a href="{p['legal']}">{e(t['legal'])}</a></li><li><a href="{p['privacy']}">{e(t['privacy'])}</a></li></ul>
    <ul aria-label="{e(t['lang_aria'])}">{spr}</ul>
  </div>
</footer>"""


def seite(lang, pfad, titel, desc, body, ld, og_titel=None, preload='', og_bild=('/img/og.jpg', 1200, 630, None), head_extra=''):
    assert len(titel) <= 60, (pfad, len(titel), titel)
    assert len(desc) <= 155, (pfad, len(desc), desc)
    t = TX[lang]
    g = gruppe(pfad)
    alts = ''.join(f'<link rel="alternate" hreflang="{HL[l]}" href="{SITE}{p}">\n' for l, p in g.items())
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE}{g["en"]}">\n'
    og_alt_loc = ''.join(f'<meta property="og:locale:alternate" content="{TX[l]["locale"]}">\n' for l in g if l != lang)
    ldjson = json.dumps(ld, ensure_ascii=False, indent=1).replace('</', '<\\/')
    og_t = og_titel or titel
    return f"""<!doctype html>
<!-- Erzeugt von _werkzeug/build.py – Änderungen dort machen, dann neu bauen. -->
<html lang="{HL[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titel)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{pfad}">
{alts}{head_extra}<meta name="theme-color" content="#15130f">
<link rel="icon" href="/img/icon.png">
<link rel="apple-touch-icon" href="/img/icon.png">
{preload}{FONTS}<link href="/fonts/fonts.css" rel="stylesheet">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MX Royale">
<meta property="og:locale" content="{t['locale']}">
{og_alt_loc}<meta property="og:title" content="{e(og_t)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{SITE}{pfad}">
<meta property="og:image" content="{SITE}{og_bild[0]}">
<meta property="og:image:width" content="{og_bild[1]}">
<meta property="og:image:height" content="{og_bild[2]}">
<meta property="og:image:alt" content="{e(og_bild[3] or t['og_alt'])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(og_t)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}{og_bild[0]}">
<meta name="twitter:image:alt" content="{e(og_bild[3] or t['og_alt'])}">
<style>{CSS.strip()}</style>
<script type="application/ld+json">
{ldjson}
</script>
</head>
<body>
<a class="skip" href="#inhalt">{e(t['skip'])}</a>
{body}
{footer(lang, pfad)}
{SCRIPT % PLAY_Q[lang]}
</body>
</html>
"""


# ── JSON-LD ────────────────────────────────────────────────────────────────────────────────────────
ORG = {'@type': 'Organization', '@id': SITE + '/#org', 'name': 'MX Royale', 'url': SITE + '/',
       'logo': {'@type': 'ImageObject', 'url': SITE + '/img/logo-512.png', 'width': 512, 'height': 512},
       'description': 'Indie game team of three students from Austria',
       'email': 'info@mxroyale.com',
       'contactPoint': {'@type': 'ContactPoint', 'contactType': 'press', 'email': 'press@mxroyale.com'},
       'sameAs': SOCIAL}


def website(lang):
    return {'@type': 'WebSite', '@id': SITE + '/#website', 'name': 'MX Royale', 'url': SITE + '/',
            'inLanguage': [HL[l] for l in SPRACHEN], 'publisher': {'@id': SITE + '/#org'}}


def videogame(lang):
    return {
        '@type': ['VideoGame', 'WebApplication'], '@id': SITE + '/#game', 'name': 'MX Royale', 'url': SITE + '/',
        'alternateName': ['MXRoyale', 'MX Royale Motocross'],
        'description': tx(lang, 'vg_desc'), 'inLanguage': LANGS,
        'image': SITE + '/img/og.jpg',
        'screenshot': [{'@type': 'ImageObject', 'url': SITE + bild_url(t), 'caption': bild_alt(t, 'en')} for t in TRACKS[:6]],
        'keywords': 'motocross game, dirt bike game, supercross game, browser game, free racing game',
        'genre': ['Racing', 'Sports', 'Motocross'],
        'gamePlatform': ['Web browser', 'PC', 'Mobile'],
        'applicationCategory': 'GameApplication', 'applicationSubCategory': 'Racing game',
        'operatingSystem': 'Any (web browser)', 'browserRequirements': 'Requires a browser with WebGL 2',
        'playMode': ['SinglePlayer', 'MultiPlayer'],
        'numberOfPlayers': {'@type': 'QuantitativeValue', 'minValue': 1, 'maxValue': 12},
        'gameLocation': [t['name'] for t in TRACKS],
        'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'EUR', 'availability': 'https://schema.org/InStock',
                   'url': PLAY},
        'isAccessibleForFree': True,
        'datePublished': BETA,
        'publisher': {'@id': SITE + '/#org'}, 'author': {'@id': SITE + '/#org'},
        'sameAs': SOCIAL,
    }


def faq_liste(lang):
    return [(q, a.format(nr=N_RACE, nf=N_FREE)) for q, a in FAQ[lang]]


def faqpage(lang, pfad):
    return {'@type': 'FAQPage', '@id': SITE + pfad + '#faq', 'inLanguage': HL[lang],
            'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}}
                           for q, a in faq_liste(lang)]}


def breadcrumb(lang, pfad, name):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'MX Royale', 'item': SITE + PFAD[lang]['home']},
        {'@type': 'ListItem', 'position': 2, 'name': name, 'item': SITE + pfad}]}


def graph(*items):
    return {'@context': 'https://schema.org', '@graph': list(items)}


# ── Strecken-Texte je Sprache ──────────────────────────────────────────────────────────────────────
def t_kurz(t, lang):
    return {'en': t['en_k'], 'de': t['de_k']}.get(lang) or TRACK_TX[lang][t['id']][0]


def t_lang(t, lang):
    return {'en': t['en'], 'de': t['de']}.get(lang) or TRACK_TX[lang][t['id']][1]


def t_diff(t, lang):
    return {'en': DIFF[t['diff']][0], 'de': DIFF[t['diff']][1]}.get(lang) or DIFF_INTL[t['diff']][lang]


def t_typ(t, lang):
    return {'en': t['typ'][0], 'de': t['typ'][1]}.get(lang) or TYP_INTL[t['typ'][0]][lang]


def bild_slug(t):
    """Dateiname des Streckenbilds = Streckenname, z. B. 'sunvale-mx-park'."""
    return re.sub(r'[^a-z0-9]+', '-', t['name'].lower()).strip('-')


def bild_url(t, klein=False):
    return f'/img/tracks/{bild_slug(t)}{"-480" if klein else ""}.webp'


def bild_alt(t, lang):
    return f'{BILD_ALT[t["id"]][lang]} – {t["name"]} {IN_MX[lang]}'


def img(t, breit=False, lazy=True, lang='en'):
    alt = bild_alt(t, lang)
    if breit:
        return (f'<img src="{bild_url(t)}" srcset="{bild_url(t, True)} 480w, {bild_url(t)} 960w" '
                f'sizes="(max-width:720px) 100vw, 560px" width="960" height="540" alt="{e(alt)}"{LAZY if lazy else ""} decoding="async">')
    return (f'<img src="{bild_url(t, True)}" width="480" height="270" alt="{e(alt)}" loading="lazy" decoding="async">')


def diff_tag(t, lang):
    return f'<span class="tag">{e(t_diff(t, lang))}</span><span class="tag grau">{e(t_typ(t, lang))}</span>'


# ── Startseite ─────────────────────────────────────────────────────────────────────────────────────
def startseite(lang):
    pfad = PFAD[lang]['home']
    c = ctx(lang)
    karten_html = ''.join(f'<div class="karte"><b>{e(k.format(**c))}</b><p>{e(v.format(**c))}</p></div>' for k, v in TX[lang]['karten'])
    strecken = ''.join(
        f'<li><a href="{PFAD[lang]["tracks"]}#{t["id"]}">{img(t, lang=lang)}<div><h3>{e(t["name"])}</h3>{diff_tag(t, lang)}'
        f'<p>{e(t_kurz(t, lang))}</p></div></a></li>' for t in TRACKS)
    faq = ''.join(f'<h3>{e(q)}</h3><p>{e(a)}</p>' for q, a in faq_liste(lang))
    body = f"""<header class="hero">
  <picture><source media="(max-aspect-ratio: 4/5)" srcset="/img/hero-whip-hoch-720.webp" width="720" height="867"><img class="hero-bild" src="/img/hero-whip-1600.webp" srcset="/img/hero-whip-800.webp 800w, /img/hero-whip-1600.webp 1600w" sizes="100vw" width="1600" height="900" alt="{e(tx(lang, 'hero_alt'))}" fetchpriority="high"></picture>
  {nav(lang, pfad)}
  <div class="hero-inhalt" id="inhalt">
    <div class="wrap">
      <div class="logo" role="img" aria-label="MX Royale"><span class="mx" aria-hidden="true">MX</span><span class="pl" aria-hidden="true">ROYALE</span></div>
      <h1 class="claim">{e(tx(lang, 'claim'))}</h1>
      <p class="claim-sub">{e(tx(lang, 'claim_sub'))}</p>
      {ride(lang)}
      <p class="klein">{e(tx(lang, 'klein'))}</p>
    </div>
  </div>
</header>

<main>
<section>
  <div class="wrap">
    <h2>{tx(lang, 'h_get')}</h2>
    <p class="lead">{e(tx(lang, 'get_lead'))}</p>
    <div class="karten">{karten_html}</div>
  </div>
</section>

<section class="dunkel" id="tracks">
  <div class="wrap">
    <h2>{tx(lang, 'h_tracks')}</h2>
    <p class="lead">{e(tx(lang, 'lead_tracks'))}</p>
    <ul class="strecken">{strecken}</ul>
    <a class="mehr" href="{PFAD[lang]['tracks']}">{e(tx(lang, 'more_tracks'))}</a>
  </div>
</section>

<section id="faq">
  <div class="wrap faq">
    <h2>{tx(lang, 'h_faq')}</h2>
    {faq}
    <p style="margin-top:28px">{tx(lang, 'faq_more')}</p>
  </div>
</section>

<section class="team">
  <div class="wrap">
    <h2>{tx(lang, 'h_team')}</h2>
    <p style="max-width:720px;margin:0 0 26px">{tx(lang, 'team')}</p>
    {ride(lang)}
  </div>
</section>
</main>"""
    pre = ('<link rel="preload" as="image" href="/img/hero-whip-hoch-720.webp" media="(max-aspect-ratio: 4/5)" fetchpriority="high">\n'
           '<link rel="preload" as="image" href="/img/hero-whip-1600.webp" imagesrcset="/img/hero-whip-800.webp 800w, /img/hero-whip-1600.webp 1600w" '
           'imagesizes="100vw" media="(min-aspect-ratio: 801/1000)" fetchpriority="high">\n')
    ld = graph(ORG, website(lang), videogame(lang), faqpage(lang, pfad))
    return seite(lang, pfad, tx(lang, 'home_titel'), tx(lang, 'home_desc'), body, ld, og_titel=tx(lang, 'home_og'), preload=pre)


# ── Strecken-Seite ─────────────────────────────────────────────────────────────────────────────────
def streckenseite(lang):
    pfad = PFAD[lang]['tracks']
    arts = []
    for i, t in enumerate(TRACKS):
        fakten = [tx(lang, 'fakt_feld', n=t['field']), tx(lang, 'fakt_tt')] if t['field'] else [tx(lang, 'fakt_free')]
        arts.append(f"""<article class="strecke" id="{t['id']}">
  {img(t, breit=True, lazy=i > 1, lang=lang)}
  <div><h2 style="font-size:clamp(28px,5vw,40px);margin:0 0 8px">{e(t['name'])}</h2>{diff_tag(t, lang)}
  <p>{e(t_lang(t, lang))}</p><p class="fakten">{e(' · '.join(fakten))}</p></div>
</article>""")
    sprung = ' · '.join(f'<a href="#{t["id"]}">{e(t["name"])}</a>' for t in TRACKS)
    body = f"""{nav(lang, pfad)}
<main id="inhalt">
<section class="seitenkopf"><div class="wrap">
  <h1>{tx(lang, 'tracks_h1')}</h1>
  <p class="lead">{e(tx(lang, 'tracks_lead'))}</p>
  {ride(lang, ' klein-los')}
  <p class="klein" style="margin-top:24px">{sprung}</p>
</div></section>
<section style="padding-top:8px"><div class="wrap">
{chr(10).join(arts)}
<p style="margin-top:36px">{tx(lang, 'tracks_more')}</p>
{ride(lang)}
</div></section>
</main>"""
    item_list = {'@type': 'ItemList', 'name': tx(lang, 'tracks_list'),
                 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': t['name'], 'url': SITE + pfad + '#' + t['id'],
                                      'image': SITE + bild_url(t)}
                                     for i, t in enumerate(TRACKS)]}
    ld = graph(breadcrumb(lang, pfad, tx(lang, 'tracks_crumb')), item_list)
    sx = TRACKS[1]  # Larkmeadow SX als Vorschaubild der Strecken-Seite
    return seite(lang, pfad, tx(lang, 'tracks_titel'), tx(lang, 'tracks_desc'), body, ld, og_bild=(bild_url(sx), 960, 540, bild_alt(sx, lang)))


# ── Anleitung ──────────────────────────────────────────────────────────────────────────────────────
def anleitung(lang):
    pfad = PFAD[lang]['how']
    body = f"""{nav(lang, pfad)}
<main id="inhalt">
<section class="seitenkopf"><div class="wrap text">
  <h1>{tx(lang, 'how_h1')}</h1>
  {tx(lang, 'how_html')}
  <p style="margin-top:32px">{tx(lang, 'how_next')}</p>
  {ride(lang)}
</div></section>
</main>"""
    ld = graph(breadcrumb(lang, pfad, tx(lang, 'how_crumb')))
    return seite(lang, pfad, tx(lang, 'how_titel'), tx(lang, 'how_desc'), body, ld)


# ── Über / Faktenblatt ─────────────────────────────────────────────────────────────────────────────
def ueber(lang):
    pfad = PFAD[lang]['about']
    c = ctx(lang)
    absatz = ''.join(f'<h2>{e(h)}</h2><p>{e(p.format(**c))}</p>' for h, p in TX[lang]['about_abs'])
    tab = ''.join(f'<tr><th scope="row">{e(k)}</th><td>{e(v.format(**c))}</td></tr>' for k, v in TX[lang]['about_rows'])
    body = f"""{nav(lang, pfad)}
<main id="inhalt">
<section class="seitenkopf"><div class="wrap text">
  <h1>{tx(lang, 'about_h1')}</h1>
  <p class="klein"><time datetime="{STAND}">{e(tx(lang, 'about_stand'))}</time></p>
  {absatz}
  <h2>{e(tx(lang, 'about_tab'))}</h2>
  <div class="tabelle"><table>{tab}</table></div>
  <p style="margin-top:32px">{tx(lang, 'about_more')}</p>
  {ride(lang)}
</div></section>
</main>"""
    titel = tx(lang, 'about_titel')
    about = {'@type': 'AboutPage', '@id': SITE + pfad, 'url': SITE + pfad, 'name': titel, 'inLanguage': HL[lang],
             'dateModified': STAND, 'about': {'@id': SITE + '/#game'}, 'publisher': {'@id': SITE + '/#org'}}
    ld = graph(about, breadcrumb(lang, pfad, tx(lang, 'about_crumb')))
    return seite(lang, pfad, titel, tx(lang, 'about_desc'), body, ld)


# ── Presse (nur EN/DE) ─────────────────────────────────────────────────────────────────────────────
ZIP = '/presse/mx-royale-press-kit.zip'


def faktenblatt_txt():
    c = ctx('en')
    zeilen = ['MX Royale – fact sheet', f'Last updated: {STAND}', '']
    zeilen += [f'{k}: {v.format(**c)}' for k, v in TX['en']['about_rows']]
    zeilen += ['', 'Short description (100 words):', PRESSE['en']['texte'][1][1].format(**c), '',
               'Website: https://mxroyale.com/  ·  Press: https://mxroyale.com/press/  ·  Contact: press@mxroyale.com', '']
    return '\n'.join(zeilen)


def baue_zip():
    """Pressepaket als ZIP mit festen Zeitstempeln (gleicher Inhalt → gleiche Datei, kein Git-Rauschen)."""
    import zipfile
    ziel = os.path.join(ROOT, ZIP.lstrip('/'))
    dateien = [('mx-royale-logo-1080.png', 'presse/mxroyale_logo_1080.png'), ('mx-royale-key-art-1920.jpg', 'presse/mxroyale_key_art_1920.jpg')]
    dateien += [(n, 'presse/' + n) for _, n, _, _ in PRESSE_SHOTS]
    with zipfile.ZipFile(ziel + '.tmp', 'w', zipfile.ZIP_DEFLATED) as z:
        for name, rel in dateien:
            zi = zipfile.ZipInfo('mx-royale-press-kit/' + name, date_time=(2026, 11, 27, 0, 0, 0))
            z.writestr(zi, open(os.path.join(ROOT, rel), 'rb').read(), compress_type=zipfile.ZIP_STORED)
        zi = zipfile.ZipInfo('mx-royale-press-kit/factsheet.txt', date_time=(2026, 11, 27, 0, 0, 0))
        z.writestr(zi, faktenblatt_txt().encode('utf-8'), compress_type=zipfile.ZIP_DEFLATED)
    os.replace(ziel + '.tmp', ziel)
    return ziel


def pressseite(lang):
    pfad = PFAD[lang]['press']
    t, c = PRESSE[lang], ctx(lang)
    tab = ''.join(f'<tr><th scope="row">{e(k)}</th><td>{e(v.format(**c))}</td></tr>' for k, v in TX[lang]['about_rows'])
    texte = ''.join(f'<div class="box"><b>{e(k)}</b>{e(v.format(**c))}</div>' for k, v in t['texte'])
    mb = os.path.getsize(os.path.join(ROOT, ZIP.lstrip('/'))) / 1e6
    dl = ''.join(f'<a href="/presse/{f}" download><img src="/presse/{f}" alt="{e(n)}" loading="lazy" width="480" height="270" style="object-fit:contain;aspect-ratio:16/9;background:#000">{e(n)}</a>' for f, n in t['dl'])
    shots = ''.join(
        f'<a href="/presse/{n}" download><img src="/presse/vorschau/{n.replace(".jpg", "-480.webp")}" width="480" height="270" alt="{e(en_ if lang == "en" else de_)} – MX Royale" loading="lazy">{e(en_ if lang == "en" else de_)}</a>'
        for _, n, en_, de_ in PRESSE_SHOTS)
    body = f"""{nav(lang, pfad)}
<main id="inhalt">
<section class="seitenkopf"><div class="wrap text">
  <h1>{t['h1']}</h1>
  <p class="lead">{e(t['intro'])}</p>
  <h2>{e(t['h_fakten'])}</h2>
  <div class="tabelle"><table>{tab}</table></div>
  <h2>{e(t['h_texte'])}</h2>
  {texte}
  <h2>{e(t['h_dl'])}</h2>
  <p><a href="{ZIP}" download>{e(t['zip'])} · {mb:.1f} MB</a></p>
  <div class="dl">{dl}</div>
  <h3 style="margin-top:28px">{e(t['shots'])}</h3>
  <div class="dl">{shots}</div>
  <p>{e(t['clips'])}</p>
  <h2>{e(t['h_kontakt'])}</h2>
  <p>{t['kontakt']}</p>
</div></section>
</main>"""
    ld = graph(breadcrumb(lang, pfad, t['crumb']))
    return seite(lang, pfad, t['titel'], t['desc'], body, ld, og_bild=('/presse/mxroyale_key_art_1920.jpg', 1920, 1080, 'MX Royale key art'))


# ── Neuigkeiten + Atom-Feed (nur EN/DE) ────────────────────────────────────────────────────────────
def feed_url(lang):
    return NEWS_PFAD[lang] + 'feed.xml'


def newsseite(lang):
    pfad, t = NEWS_PFAD[lang], NEWS_TX[lang]
    eintraege = ''.join(
        f'<article id="{n["id"]}" style="margin:0 0 36px"><p class="klein" style="margin:0"><time datetime="{n["datum"]}">{n["datum"]}</time></p>'
        f'<h2 style="font-size:clamp(26px,4.5vw,36px);margin:6px 0 10px">{e(n[lang][0])}</h2><p>{e(n[lang][1])}</p></article>'
        for n in NEWS)
    body = f"""{nav(lang, pfad)}
<main id="inhalt">
<section class="seitenkopf"><div class="wrap text">
  <h1>{t['h1']}</h1>
  <p class="klein"><a href="{feed_url(lang)}">{e(t['feed'])}</a></p>
  {eintraege}
  {ride(lang)}
</div></section>
</main>"""
    blog = {'@type': 'Blog', '@id': SITE + pfad, 'url': SITE + pfad, 'name': t['titel'], 'inLanguage': HL[lang],
            'publisher': {'@id': SITE + '/#org'}, 'about': {'@id': SITE + '/#game'},
            'blogPost': [{'@type': 'BlogPosting', 'headline': n[lang][0], 'datePublished': n['datum'], 'url': SITE + pfad + '#' + n['id'],
                          'author': {'@id': SITE + '/#org'}} for n in NEWS]}
    feed = f'<link rel="alternate" type="application/atom+xml" title="{e(t["titel"])}" href="{SITE}{feed_url(lang)}">\n'
    return seite(lang, pfad, t['titel'], t['desc'], body, graph(blog, breadcrumb(lang, pfad, t['crumb'])), head_extra=feed)


def atom(lang):
    from xml.sax.saxutils import escape as x
    pfad, t = NEWS_PFAD[lang], NEWS_TX[lang]
    z = ['<?xml version="1.0" encoding="utf-8"?>', f'<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="{HL[lang]}">',
         f'  <title>{x(t["titel"])}</title>', f'  <id>{SITE}{pfad}</id>', f'  <link href="{SITE}{pfad}"/>',
         f'  <link rel="self" href="{SITE}{feed_url(lang)}"/>', f'  <updated>{NEWS[0]["datum"]}T12:00:00Z</updated>',
         '  <author><name>MX Royale</name><email>info@mxroyale.com</email></author>']
    for n in NEWS:
        z += ['  <entry>', f'    <title>{x(n[lang][0])}</title>', f'    <id>{SITE}{pfad}#{n["id"]}</id>',
              f'    <link href="{SITE}{pfad}#{n["id"]}"/>', f'    <updated>{n["datum"]}T12:00:00Z</updated>',
              f'    <summary>{x(n[lang][1])}</summary>', '  </entry>']
    z.append('</feed>\n')
    return '\n'.join(z)


# ── Textdateien ────────────────────────────────────────────────────────────────────────────────────
def bilder_fuer(p):
    """Bilder einer Seite für die Bilder-Sitemap."""
    if p in [PFAD[l]['home'] for l in SPRACHEN]:
        return ['/img/hero-whip-1600.webp', '/img/og.jpg'] + [bild_url(t) for t in TRACKS]
    if p in ('/press/', '/presse/'):
        return ['/presse/mxroyale_key_art_1920.jpg'] + ['/presse/' + n for _, n, _, _ in PRESSE_SHOTS]
    if p in [PFAD[l]['tracks'] for l in SPRACHEN]:
        return [bild_url(t) for t in TRACKS]
    return []


def sitemap():
    z = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" '
         'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    for g in GRUPPEN:
        for p in g.values():
            z.append(f'  <url>\n    <loc>{SITE}{p}</loc>\n    <lastmod>{STAND}</lastmod>\n    <priority>{prio(p)}</priority>')
            for l, q in g.items():
                z.append(f'    <xhtml:link rel="alternate" hreflang="{HL[l]}" href="{SITE}{q}"/>')
            z.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{g["en"]}"/>')
            for b in bilder_fuer(p):
                z.append(f'    <image:image><image:loc>{SITE}{b}</image:loc></image:image>')
            z.append('  </url>')
    z.append('</urlset>\n')
    return '\n'.join(z)


ROBOTS_BOTS = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot', 'Perplexity-User', 'ClaudeBot', 'Claude-SearchBot',
               'Claude-User', 'Google-Extended', 'Googlebot', 'Bingbot', 'Applebot', 'Applebot-Extended', 'CCBot', 'DuckAssistBot']


def robots():
    z = ['# mxroyale.com – Suchmaschinen und KI-Assistenten sind ausdrücklich willkommen.', '']
    for b in ROBOTS_BOTS:
        z += [f'User-agent: {b}', 'Allow: /', '']
    z += ['User-agent: *', 'Allow: /', '', f'Sitemap: {SITE}/sitemap.xml', '']
    return '\n'.join(z)


def llms(voll):
    fakten = f"""- Price: free. No ads, no in-game purchases.
- Platform: web browser (Chrome, Edge, Firefox, Safari) on PC, Mac, phones and tablets. No download, no install.
- Controls: keyboard (remappable), touch controls in landscape with optional tilt steering, gamepad.
- Modes: race vs. up to 11 AI riders, time trial with ghost and medal times, Daily Challenge, Championship (4 races), freeride, trick school, online races with friends via a 5-character room code (bots can fill the field).
- Tracks: {N_RACE} race tracks + {N_FREE} freeride maps, including 2 supercross tracks.
- Tricks: whips, scrubs, backflips, Superman, Nac-Nac, Can-Can, heel clicker, seat grab, cliffhanger.
- Bikes: 450 four-stroke, 250 two-stroke, electric.
- Languages: English, German, Spanish, French, Brazilian Portuguese.
- Account: optional.
- Status: open beta since {BETA}.
- Developer: three students from Austria (hobby project).
- Play: {PLAY}
- Social: TikTok, Instagram and YouTube as @mxroyalegame."""
    weitere = '\n'.join(
        f'- [{TX[l]["lang_name"]} – {TX[l]["home"]}]({SITE}{PFAD[l]["home"]}), [{TX[l]["nav_tracks"]}]({SITE}{PFAD[l]["tracks"]}), '
        f'[{TX[l]["nav_how"]}]({SITE}{PFAD[l]["how"]}), [{TX[l]["nav_about"]}]({SITE}{PFAD[l]["about"]})'
        + (f', [Presse]({SITE}/presse/)' if l == 'de' else '')
        for l in SPRACHEN if l != 'en')
    seiten = f"""## Pages

- [Home (English)]({SITE}/): overview, track list and FAQ
- [Tracks]({SITE}/tracks/): all tracks with descriptions
- [How to play]({SITE}/how-to-play/): controls for keyboard, phone and controller; whips, scrubs, pop, gate start
- [Fact sheet]({SITE}/about/): answer-first summary and feature table
- [Press & creators]({SITE}/press/): press kit, logo, key art, screenshots
- [News]({SITE}/news/): dated updates (Atom feed: {SITE}/news/feed.xml)
{weitere}

## Optional

- [Privacy]({SITE}/privacy/): no tracking, no analytics, no ads
- [Legal notice]({SITE}/legal/)
- [Full text for language models]({SITE}/llms-full.txt)
"""
    kopf = f"""# MX Royale

> MX Royale is a free motocross racing game that runs in the web browser. No download and no account are needed; it works on PC, Mac, phones and tablets with keyboard, touch controls or a gamepad. It has {N_RACE} race tracks (including supercross), {N_FREE} freeride maps, whips, scrubs and flips, races against AI, time trial with ghosts and online races with friends.

Also known as: MXRoyale

Last updated: {STAND}

## Facts

{fakten}

"""
    if not voll:
        return kopf + seiten
    strecken = '\n'.join(f'- **{t["name"]}** ({DIFF[t["diff"]][0]}, {t["typ"][0]}): {t["en"]}' for t in TRACKS)
    faq = '\n\n'.join(f'### {q}\n\n{a}' for q, a in faq_liste('en'))
    steuerung = """### Keyboard

W/S throttle/brake · A/D steer (in the air: whip) · ←/→ lean the bike (scrub, lay it flat) · ↑/↓ weight forward/back · Space crouch/pop · Shift rear brake · R respawn · C camera · Q look back · G ghost · Esc pause. All riding keys can be remapped.

### Phone (landscape)

Left thumb: a stick appears where you touch (steer, weight). Right thumb: hold GAS, brake to its left; drag left/right on the throttle to lean (scrub), drag down and release at the lip to pop. Optional tilt steering in Settings.

### Gamepad

RT throttle, LT brake (analog) · left stick steer/whip · right stick weight and lean · A crouch/pop · X rear brake · Y respawn · Start pause · freeride tricks: hold LB or RB + left stick.

### Whip, scrub, gate start

Whip: steer in just before the lip, hold in the air, let go about half a second before landing. Scrub: lay the bike down on the ramp face and stand it up before the end of the lip. Gate start: hold throttle and brake from the "5" board, release the brake when the gate drops."""
    return (kopf + f"## Tracks\n\n{strecken}\n\n## Controls\n\n{steuerung}\n\n## FAQ\n\n{faq}\n\n" + seiten)


# ── Schreiben (atomar) + Selbstprüfung ─────────────────────────────────────────────────────────────
def schreibe(rel, inhalt):
    ziel = os.path.join(ROOT, rel.lstrip('/'))
    if ziel.endswith(os.sep) or rel.endswith('/'):
        ziel = os.path.join(ziel, 'index.html')
    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    tmp = ziel + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(inhalt)
    os.replace(tmp, ziel)
    return ziel


def pruefe_ld(text, rel):
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
        d = json.loads(block)
        assert d['@context'] == 'https://schema.org', rel
        for item in d['@graph']:
            assert '@type' in item, rel


def pruefe_hreflang(seiten):
    """Jede gebaute Seite: canonical = eigene URL, hreflang-Satz = Gruppe, und jede Zielseite verweist zurück."""
    alle = {}
    for pfad, text in seiten.items():
        canon = re.search(r'<link rel="canonical" href="([^"]+)">', text).group(1)
        assert canon == SITE + pfad, (pfad, canon)
        alle[pfad] = dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="https://mxroyale\.com([^"]+)">', text))
    for pfad, alts in alle.items():
        assert alts.get('x-default') == gruppe(pfad)['en'], pfad
        for hl, ziel in alts.items():
            if hl != 'x-default' and ziel in alle:
                assert alle[ziel] == alts, (pfad, ziel)
        assert re.search(r'[{}]', re.sub(r'<style>.*?</style>|<script.*?</script>', '', seiten[pfad], flags=re.S)) is None, ('Platzhalter übrig', pfad)


def main():
    gebaut, seiten = [], {}
    for lang in SPRACHEN:
        p = PFAD[lang]
        for pfad, fn in ((p['home'], startseite), (p['tracks'], streckenseite), (p['how'], anleitung), (p['about'], ueber)):
            txt = fn(lang)
            pruefe_ld(txt, pfad)
            seiten[pfad] = txt
            gebaut.append(schreibe(pfad, txt))
    baue_zip()
    for lang in ('en', 'de'):
        txt = pressseite(lang)
        pruefe_ld(txt, PFAD[lang]['press'])
        seiten[PFAD[lang]['press']] = txt
        gebaut.append(schreibe(PFAD[lang]['press'], txt))
    for lang in ('en', 'de'):
        txt = newsseite(lang)
        pruefe_ld(txt, NEWS_PFAD[lang])
        seiten[NEWS_PFAD[lang]] = txt
        gebaut.append(schreibe(NEWS_PFAD[lang], txt))
        gebaut.append(schreibe(feed_url(lang), atom(lang)))
        import xml.dom.minidom
        xml.dom.minidom.parse(os.path.join(ROOT, feed_url(lang).lstrip('/')))
    pruefe_hreflang(seiten)
    gebaut.append(schreibe('sitemap.xml', sitemap()))
    gebaut.append(schreibe('robots.txt', robots()))
    gebaut.append(schreibe('llms.txt', llms(False)))
    gebaut.append(schreibe('llms-full.txt', llms(True)))
    import xml.dom.minidom
    xml.dom.minidom.parse(os.path.join(ROOT, 'sitemap.xml'))
    for g in gebaut:
        print('ok', os.path.relpath(g, ROOT))


if __name__ == '__main__':
    sys.exit(main())
