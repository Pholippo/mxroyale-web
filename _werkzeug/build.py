# -*- coding: utf-8 -*-
"""
Baut die Inhaltsseiten von mxroyale.com (EN + DE) aus einer Quelle:
  /  /tracks/  /how-to-play/  /about/      /de/  /de/strecken/  /de/anleitung/  /de/ueber/
plus sitemap.xml, robots.txt, llms.txt, llms-full.txt.

Aufruf (im Repo-Root):  python _werkzeug/build.py
Prüft am Ende selbst: Titel ≤ 60, Description ≤ 155 Zeichen, JSON-LD parsebar, hreflang-Paare vollständig.
Ordner mit „_“ veröffentlicht GitHub Pages (Jekyll) nicht – das Skript bleibt privat.
Rechtliche Seiten und Presse werden NICHT gebaut (nur ihr <head> wurde einmal von Hand ergänzt).
Spiel-Fakten stammen aus dem Spiel-Repo (src/world/track.ts, tracks/*.ts, src/i18n/en.ts, input/tastenBelegung.ts).
"""
import html
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://mxroyale.com'
PLAY = 'https://play.mxroyale.com/'
STAND = '2026-11-26'
STAND_EN = '26 November 2026'
STAND_DE = '26. November 2026'
SOCIAL = [
    'https://www.tiktok.com/@mxroyalegame',
    'https://www.instagram.com/mxroyalegame/',
    'https://www.youtube.com/@mxroyalegame',
]
LANGS = ['en', 'de', 'es', 'fr', 'pt-BR']

# Seitenpaare (EN, DE) – auch für Sitemap/hreflang der Handseiten
PAARE = [
    ('/', '/de/'),
    ('/tracks/', '/de/strecken/'),
    ('/how-to-play/', '/de/anleitung/'),
    ('/about/', '/de/ueber/'),
    ('/press/', '/presse/'),
    ('/legal/', '/impressum/'),
    ('/privacy/', '/datenschutz/'),
]
PRIO = {'/': '1.0', '/de/': '0.9', '/tracks/': '0.8', '/de/strecken/': '0.7', '/how-to-play/': '0.8',
        '/de/anleitung/': '0.7', '/about/': '0.7', '/de/ueber/': '0.6', '/press/': '0.4', '/presse/': '0.3',
        '/legal/': '0.1', '/impressum/': '0.1', '/privacy/': '0.1', '/datenschutz/': '0.1'}

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

# ── FAQ (jede Antwort steht für sich, erster Satz = Antwort) ───────────────────────────────────────
FAQ = {
    'en': [
        ('Is MX Royale free?',
         'Yes, MX Royale is completely free to play. There are no ads and no in-game purchases.'),
        ('Do I need to download or install MX Royale?',
         'No, MX Royale runs directly in the web browser with no download and no install. It works in Chrome, Edge, Firefox and Safari, and no account is needed to start riding.'),
        ('Can I play MX Royale on my phone?',
         'Yes, MX Royale works on phones and tablets in landscape mode. It has touch controls with a thumb stick, throttle and brake buttons, and optional tilt steering.'),
        ('Does MX Royale support a controller?',
         'Yes, MX Royale supports gamepads. Throttle and brake are on the analog triggers (RT/LT), the left stick steers and whips, and the right stick moves your weight and leans the bike.'),
        ('Can I race my friends online in MX Royale?',
         'Yes, MX Royale has online races with room codes. One player creates a room and shares the 5-character code, the others enter it and the track loads automatically; bots can fill up the field.'),
        ('How many tracks does MX Royale have?',
         f'MX Royale has {N_RACE} race tracks and {N_FREE} freeride maps. They include two supercross tracks and outdoor tracks in forest, desert, canyon, snow, rainforest, beach, quarry and salt-lake settings.'),
        ('Is there supercross in MX Royale?',
         'Yes, MX Royale has two supercross tracks: Larkmeadow SX in a night stadium and Neon Harbor SX in a harbour hall. Both have rhythm sections, whoops and triples.'),
        ('Which game modes does MX Royale have?',
         'MX Royale has races against AI riders, time trial with your own ghost, a Daily Challenge, a Championship of four races, freeride, a trick school and online races with friends.'),
        ('Which languages is MX Royale available in?',
         'MX Royale is available in English, German, Spanish, French and Brazilian Portuguese.'),
    ],
    'de': [
        ('Ist MX Royale kostenlos?',
         'Ja, MX Royale ist komplett kostenlos. Es gibt keine Werbung und keine In-Game-Käufe.'),
        ('Muss ich MX Royale herunterladen oder installieren?',
         'Nein, MX Royale läuft direkt im Browser, ohne Download und ohne Installation. Es funktioniert in Chrome, Edge, Firefox und Safari, und zum Losfahren braucht es kein Konto.'),
        ('Kann ich MX Royale am Handy spielen?',
         'Ja, MX Royale läuft am Handy und Tablet im Querformat. Es gibt eine Touch-Steuerung mit Daumen-Stick, Gas- und Bremstaste und auf Wunsch Neige-Steuerung.'),
        ('Kann ich MX Royale mit Controller spielen?',
         'Ja, MX Royale unterstützt Gamepads. Gas und Bremse liegen auf den analogen Triggern (RT/LT), der linke Stick lenkt und whippt, der rechte verlagert das Gewicht und kippt das Bike.'),
        ('Kann ich in MX Royale online gegen Freunde fahren?',
         'Ja, MX Royale hat Online-Rennen mit Raum-Code. Einer erstellt einen Raum und schickt den 5-stelligen Code, die anderen geben ihn ein und die Strecke lädt automatisch; Bots können das Feld auffüllen.'),
        ('Wie viele Strecken hat MX Royale?',
         f'MX Royale hat {N_RACE} Rennstrecken und {N_FREE} Freeride-Maps. Dazu gehören zwei Supercross-Strecken und Outdoor-Strecken in Wald, Wüste, Canyon, Schnee, Regenwald, am Strand, im Steinbruch und auf einem Salzsee.'),
        ('Gibt es in MX Royale Supercross?',
         'Ja, MX Royale hat zwei Supercross-Strecken: Larkmeadow SX im Nachtstadion und Neon Harbor SX in einer Hafenhalle. Beide haben Rhythmus-Sektionen, Whoops und Triples.'),
        ('Welche Spielmodi hat MX Royale?',
         'MX Royale hat Rennen gegen KI-Fahrer, Zeitfahren gegen den eigenen Geist, eine Tages-Challenge, eine Meisterschaft über vier Rennen, Freeride, eine Trick-Schule und Online-Rennen mit Freunden.'),
        ('In welchen Sprachen gibt es MX Royale?',
         'MX Royale gibt es auf Englisch, Deutsch, Spanisch, Französisch und brasilianischem Portugiesisch.'),
    ],
}

T = {  # UI-Texte
    'en': dict(ride='Ride now', nav_tracks='Tracks', nav_how='How to play', nav_about='About', nav_press='Press & creators',
               other='Deutsch', legal='Legal notice', privacy='Privacy', home='Home', play_q='',
               foot_social='Follow us', locale='en_US', alt_locale='de_DE'),
    'de': dict(ride='Jetzt fahren', nav_tracks='Strecken', nav_how='Anleitung', nav_about='Über das Spiel', nav_press='Presse & Creator',
               other='English', legal='Impressum', privacy='Datenschutz', home='Start', play_q='?lang=de',
               foot_social='Folg uns', locale='de_DE', alt_locale='en_US'),
}
PFAD = {
    'en': dict(home='/', tracks='/tracks/', how='/how-to-play/', about='/about/', press='/press/', legal='/legal/', privacy='/privacy/'),
    'de': dict(home='/de/', tracks='/de/strecken/', how='/de/anleitung/', about='/de/ueber/', press='/presse/', legal='/impressum/', privacy='/datenschutz/'),
}

e = html.escape
LAZY = ' loading="lazy"'
FONTS = ''.join(f'<link rel="preload" as="font" type="font/woff2" href="/fonts/{f}.woff2" crossorigin>\n' for f in (
    'HTxyL3I-JCGChYJ8VI-L6OO_au7B6xTrW3bmu4kG', 'wlpigxjLBV1hqnzfr-F8sEYMB0Yybp0mudRfi6m_B2sl', 'wlpigxjLBV1hqnzfr-F8sEYMB0Yybp0mudRfw6-_B2sl'))


def gegenstueck(pfad):
    for a, b in PAARE:
        if pfad == a:
            return b
        if pfad == b:
            return a
    raise KeyError(pfad)


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
h1.claim{font:700 clamp(22px,3.6vw,30px)/1.25 "Barlow Semi Condensed",sans-serif;text-transform:none;margin:26px 0;max-width:680px}
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


def ride(lang, extra=''):
    return f'<a class="los spiel{extra}" href="{PLAY}{T[lang]["play_q"]}">{T[lang]["ride"]}</a>'


def nav(lang, pfad):
    p, t = PFAD[lang], T[lang]
    links = [(p['tracks'], t['nav_tracks']), (p['how'], t['nav_how']), (p['about'], t['nav_about']),
             (gegenstueck(pfad), t['other'])]
    other = 'de' if lang == 'en' else 'en'
    teile = []
    for h, n in links:
        attr = ' aria-current="page"' if h == pfad else ''
        if h == gegenstueck(pfad):
            attr += f' hreflang="{other}" lang="{other}"'
        teile.append(f'<li><a href="{h}"{attr}>{e(n)}</a></li>')
    li = ''.join(teile)
    return (f'<nav class="nav" aria-label="{"Main" if lang == "en" else "Hauptmenü"}"><div class="wrap">'
            f'<a class="marke" href="{p["home"]}">MX <span>ROYALE</span></a>'
            f'<ul>{li}</ul></div></nav>')


def footer(lang, pfad):
    p, t = PFAD[lang], T[lang]
    soc = ''.join(f'<li><a href="{u}" rel="me noopener">{n} @mxroyalegame</a></li>'
                  for u, n in zip(SOCIAL, ['TikTok', 'Instagram', 'YouTube']))
    return f"""<footer>
  <div class="wrap">
    <div><b>MX Royale</b><br>{"Free motocross game in your browser." if lang == "en" else "Gratis Motocross-Spiel im Browser."}<br>© 2026 MX Royale</div>
    <ul><li><a href="{p['home']}">{t['home']}</a></li><li><a href="{p['tracks']}">{t['nav_tracks']}</a></li><li><a href="{p['how']}">{t['nav_how']}</a></li><li><a href="{p['about']}">{t['nav_about']}</a></li><li><a href="{p['press']}">{e(t['nav_press'])}</a></li></ul>
    <ul>{soc}</ul>
    <ul><li><a href="mailto:info@mxroyale.com">info@mxroyale.com</a></li><li><a href="{p['legal']}">{t['legal']}</a></li><li><a href="{p['privacy']}">{t['privacy']}</a></li><li><a href="{gegenstueck(pfad)}" hreflang="{'de' if lang == 'en' else 'en'}" lang="{'de' if lang == 'en' else 'en'}">{t['other']}</a></li></ul>
  </div>
</footer>"""


def seite(lang, pfad, titel, desc, body, ld, og_titel=None, preload=''):
    assert len(titel) <= 60, (pfad, len(titel), titel)
    assert len(desc) <= 155, (pfad, len(desc), desc)
    en, de = (pfad, gegenstueck(pfad)) if lang == 'en' else (gegenstueck(pfad), pfad)
    t = T[lang]
    ldjson = json.dumps(ld, ensure_ascii=False, indent=1).replace('</', '<\\/')
    og_t = og_titel or titel
    return f"""<!doctype html>
<!-- Erzeugt von _werkzeug/build.py – Änderungen dort machen, dann neu bauen. -->
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titel)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{pfad}">
<link rel="alternate" hreflang="en" href="{SITE}{en}">
<link rel="alternate" hreflang="de" href="{SITE}{de}">
<link rel="alternate" hreflang="x-default" href="{SITE}{en}">
<meta name="theme-color" content="#15130f">
<link rel="icon" href="/img/icon.png">
<link rel="apple-touch-icon" href="/img/icon.png">
{preload}{FONTS}<link href="/fonts/fonts.css" rel="stylesheet">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MX Royale">
<meta property="og:locale" content="{t['locale']}">
<meta property="og:locale:alternate" content="{t['alt_locale']}">
<meta property="og:title" content="{e(og_t)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{SITE}{pfad}">
<meta property="og:image" content="{SITE}/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="MX Royale – {'motocross game in the browser' if lang == 'en' else 'Motocross-Spiel im Browser'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(og_t)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}/img/og.jpg">
<style>{CSS.strip()}</style>
<script type="application/ld+json">
{ldjson}
</script>
</head>
<body>
<a class="skip" href="#inhalt">{'Skip to content' if lang == 'en' else 'Zum Inhalt'}</a>
{body}
{footer(lang, pfad)}
{SCRIPT % t['play_q']}
</body>
</html>
"""


# ── JSON-LD ────────────────────────────────────────────────────────────────────────────────────────
ORG = {'@type': 'Organization', '@id': SITE + '/#org', 'name': 'MX Royale', 'url': SITE + '/',
       'logo': {'@type': 'ImageObject', 'url': SITE + '/img/logo-512.png', 'width': 512, 'height': 512},
       'email': 'info@mxroyale.com', 'sameAs': SOCIAL}


def website(lang):
    return {'@type': 'WebSite', '@id': SITE + '/#website', 'name': 'MX Royale', 'url': SITE + '/',
            'inLanguage': ['en', 'de'], 'publisher': {'@id': SITE + '/#org'}}


def videogame(lang):
    d = ('MX Royale is a free motocross racing game that runs in the web browser. No download, works on PC and phones, '
         f'with keyboard, touch or gamepad. {N_RACE} race tracks, {N_FREE} freeride maps, whips, scrubs and flips, '
         'races against AI, time trial with ghosts and online races with friends.') if lang == 'en' else (
        'MX Royale ist ein kostenloses Motocross-Rennspiel, das im Browser läuft. Ohne Download, am PC und am Handy, '
        f'mit Tastatur, Touch oder Gamepad. {N_RACE} Rennstrecken, {N_FREE} Freeride-Maps, Whips, Scrubs und Flips, '
        'Rennen gegen die KI, Zeitfahren mit Geist und Online-Rennen mit Freunden.')
    return {
        '@type': 'VideoGame', '@id': SITE + '/#game', 'name': 'MX Royale', 'url': SITE + '/',
        'description': d, 'inLanguage': LANGS,
        'image': SITE + '/img/og.jpg',
        'screenshot': [SITE + f'/img/tracks/{t["id"]}.webp' for t in TRACKS[:6]],
        'genre': ['Racing', 'Sports', 'Motocross'],
        'gamePlatform': ['Web browser', 'PC', 'Mobile'],
        'applicationCategory': 'Game', 'operatingSystem': 'Any (web browser)',
        'playMode': ['SinglePlayer', 'MultiPlayer'],
        'numberOfPlayers': {'@type': 'QuantitativeValue', 'minValue': 1},
        'gameLocation': [t['name'] for t in TRACKS],
        'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'EUR', 'availability': 'https://schema.org/InStock',
                   'url': PLAY},
        'isAccessibleForFree': True,
        'datePublished': STAND,
        'publisher': {'@id': SITE + '/#org'}, 'author': {'@id': SITE + '/#org'},
        'sameAs': SOCIAL,
    }


def faqpage(lang, pfad):
    return {'@type': 'FAQPage', '@id': SITE + pfad + '#faq', 'inLanguage': lang,
            'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}}
                           for q, a in FAQ[lang]]}


def breadcrumb(lang, pfad, name):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'MX Royale', 'item': SITE + PFAD[lang]['home']},
        {'@type': 'ListItem', 'position': 2, 'name': name, 'item': SITE + pfad}]}


def graph(*items):
    return {'@context': 'https://schema.org', '@graph': list(items)}


def img(t, breit=False, lazy=True, alt_lang='en'):
    alt = f'{t["name"]} – {"track in MX Royale" if alt_lang == "en" else "Strecke in MX Royale"}'
    if breit:
        return (f'<img src="/img/tracks/{t["id"]}.webp" srcset="/img/tracks/{t["id"]}-480.webp 480w, /img/tracks/{t["id"]}.webp 960w" '
                f'sizes="(max-width:720px) 100vw, 560px" width="960" height="540" alt="{e(alt)}"{LAZY if lazy else ""} decoding="async">')
    return (f'<img src="/img/tracks/{t["id"]}-480.webp" width="480" height="270" alt="{e(alt)}" loading="lazy" decoding="async">')


def diff_tag(t, lang):
    d = DIFF[t['diff']][0 if lang == 'en' else 1]
    return f'<span class="tag">{e(d)}</span><span class="tag grau">{e(t["typ"][0 if lang == "en" else 1])}</span>'


# ── Startseite ─────────────────────────────────────────────────────────────────────────────────────
def startseite(lang):
    pfad = PFAD[lang]['home']
    en = lang == 'en'
    karten = [
        (f'{N_RACE} tracks + {N_FREE} freeride maps', 'Supercross stadiums, forest GPs, desert, canyon, snow, beach and a quarry.') if en else
        (f'{N_RACE} Strecken + {N_FREE} Freeride-Maps', 'Supercross-Hallen, Wald-GPs, Wüste, Canyon, Schnee, Strand und Steinbruch.'),
        ('Race the AI', 'Line up at the gate against up to 11 AI riders, or ride a 4-race Championship.') if en else
        ('Rennen gegen die KI', 'Gatterstart gegen bis zu 11 KI-Fahrer oder eine Meisterschaft über 4 Rennen.'),
        ('Online with friends', 'Create a room, send the 5-character code and race each other.') if en else
        ('Online mit Freunden', 'Raum erstellen, 5-stelligen Code schicken und gegeneinander fahren.'),
        ('Time trial & ghosts', 'Chase your best lap or the top ghost, win medals and try the Daily Challenge.') if en else
        ('Zeitfahren & Geist', 'Jag deine Bestzeit oder den Geist von Platz 1, hol Medaillen und die Tages-Challenge.'),
        ('Whips, scrubs & flips', 'Backflips, Supermans, Nac-Nacs and Can-Cans. Learn them in the trick school.') if en else
        ('Whips, Scrubs & Flips', 'Backflip, Superman, Nac-Nac und Can-Can. Lernen kannst du sie in der Trick-Schule.'),
        ('Phone, PC or controller', 'Touch controls in landscape, keyboard or gamepad. Nothing to install.') if en else
        ('Handy, PC oder Controller', 'Touch-Steuerung im Querformat, Tastatur oder Gamepad. Nichts zu installieren.'),
    ]
    karten_html = ''.join(f'<div class="karte"><b>{e(k)}</b><p>{e(v)}</p></div>' for k, v in karten)
    strecken = ''.join(
        f'<li><a href="{PFAD[lang]["tracks"]}#{t["id"]}">{img(t, alt_lang=lang)}<div><h3>{e(t["name"])}</h3>{diff_tag(t, lang)}'
        f'<p>{e(t["en_k"] if en else t["de_k"])}</p></div></a></li>' for t in TRACKS)
    faq = ''.join(f'<h3>{e(q)}</h3><p>{e(a)}</p>' for q, a in FAQ[lang])
    hero_alt = 'Rider whipping a motocross bike over a jump on Highcrest Valley GP in MX Royale' if en else 'Fahrer whippt sein Motocross-Bike über einen Sprung auf Highcrest Valley GP in MX Royale'
    body = f"""<header class="hero">
  <picture><source media="(max-aspect-ratio: 4/5)" srcset="/img/hero-whip-hoch-720.webp" width="720" height="867"><img class="hero-bild" src="/img/hero-whip-1600.webp" srcset="/img/hero-whip-800.webp 800w, /img/hero-whip-1600.webp 1600w" sizes="100vw" width="1600" height="900" alt="{hero_alt}" fetchpriority="high"></picture>
  {nav(lang, pfad)}
  <div class="hero-inhalt" id="inhalt">
    <div class="wrap">
      <div class="logo" role="img" aria-label="MX Royale"><span class="mx" aria-hidden="true">MX</span><span class="pl" aria-hidden="true">ROYALE</span></div>
      <h1 class="claim">{"Free motocross game you play online, right in your browser. No download, on PC, phone and controller." if en else "Motocross-Spiel online und kostenlos, direkt im Browser. Ohne Download, am PC, am Handy und mit Controller."}</h1>
      {ride(lang)}
      <p class="klein">{"Open beta · no account needed · runs in Chrome, Edge, Firefox and Safari" if en else "Offene Beta · kein Konto nötig · läuft in Chrome, Edge, Firefox und Safari"}</p>
    </div>
  </div>
</header>

<main>
<section>
  <div class="wrap">
    <h2>{"What you <span>get</span>" if en else "Was dich <span>erwartet</span>"}</h2>
    <div class="karten">{karten_html}</div>
  </div>
</section>

<section class="dunkel" id="tracks">
  <div class="wrap">
    <h2>{"The <span>tracks</span>" if en else "Die <span>Strecken</span>"}</h2>
    <p class="lead">{f"{N_RACE} race tracks from a beginner MX park to supercross under lights, plus {N_FREE} freeride maps for tricks. New tracks are added during the beta." if en else f"{N_RACE} Rennstrecken vom Einsteiger-MX-Park bis zum Supercross unter Flutlicht, dazu {N_FREE} Freeride-Maps für Tricks. In der Beta kommen laufend neue dazu."}</p>
    <ul class="strecken">{strecken}</ul>
    <a class="mehr" href="{PFAD[lang]['tracks']}">{"All tracks in detail →" if en else "Alle Strecken im Detail →"}</a>
  </div>
</section>

<section id="faq">
  <div class="wrap faq">
    <h2>{"Questions & <span>answers</span>" if en else "Fragen & <span>Antworten</span>"}</h2>
    {faq}
    <p style="margin-top:28px">{f'New to motocross games? Read <a href="{PFAD[lang]["how"]}">how to play</a> or the <a href="{PFAD[lang]["about"]}">fact sheet</a>.' if en else f'Neu bei Motocross-Spielen? Lies die <a href="{PFAD[lang]["how"]}">Anleitung</a> oder das <a href="{PFAD[lang]["about"]}">Faktenblatt</a>.'}</p>
  </div>
</section>

<section class="team">
  <div class="wrap">
    <h2>{"Built by <span>riders</span>" if en else "Von Ridern <span>gebaut</span>"}</h2>
    <p style="max-width:720px;margin:0 0 26px">{'MX Royale is built by three students who ride themselves. New tracks, tricks and fixes ship every week. Found a bug or got an idea? Write to us: <a href="mailto:feedback@mxroyale.com">feedback@mxroyale.com</a>' if en else 'MX Royale bauen drei Schüler, die selbst fahren. Jede Woche kommen neue Strecken, Tricks und Fixes dazu. Fehler gefunden oder eine Idee? Schreib uns: <a href="mailto:feedback@mxroyale.com">feedback@mxroyale.com</a>'}</p>
    {ride(lang)}
  </div>
</section>
</main>"""
    titel = 'MX Royale – Free Motocross Game Online, No Download' if en else 'MX Royale – Motocross Spiel online kostenlos im Browser'
    desc = (f'Free motocross game in your browser: no download, on phone, PC or controller. {N_RACE} tracks, supercross, whips and online races with friends.'
            if en else f'Motocross Browserspiel, kostenlos und ohne Download: am Handy, PC oder mit Controller. {N_RACE} Strecken, Supercross, Whips und Online-Rennen.')
    pre = ('<link rel="preload" as="image" href="/img/hero-whip-hoch-720.webp" media="(max-aspect-ratio: 4/5)" fetchpriority="high">\n'
           '<link rel="preload" as="image" href="/img/hero-whip-1600.webp" imagesrcset="/img/hero-whip-800.webp 800w, /img/hero-whip-1600.webp 1600w" '
           'imagesizes="100vw" media="(min-aspect-ratio: 801/1000)" fetchpriority="high">\n')
    ld = graph(ORG, website(lang), videogame(lang), faqpage(lang, pfad))
    return seite(lang, pfad, titel, desc, body, ld, og_titel=('MX Royale – Motocross in your browser' if en else 'MX Royale – Motocross im Browser'), preload=pre)


# ── Strecken-Seite ─────────────────────────────────────────────────────────────────────────────────
def streckenseite(lang):
    en = lang == 'en'
    pfad = PFAD[lang]['tracks']
    arts = []
    for i, t in enumerate(TRACKS):
        fakten = []
        if t['field']:
            fakten.append((f'Race field: {t["field"]} riders' if en else f'Starterfeld: {t["field"]} Fahrer'))
            fakten.append('Time trial with ghost and medals' if en else 'Zeitfahren mit Geist und Medaillen')
        else:
            fakten.append('No laps, no timer, no opponents' if en else 'Ohne Runden, Uhr und Gegner')
        arts.append(f"""<article class="strecke" id="{t['id']}">
  {img(t, breit=True, lazy=i > 1, alt_lang=lang)}
  <div><h2 style="font-size:clamp(28px,5vw,40px);margin:0 0 8px">{e(t['name'])}</h2>{diff_tag(t, lang)}
  <p>{e(t['en'] if en else t['de'])}</p><p class="fakten">{e(' · '.join(fakten))}</p></div>
</article>""")
    sprung = ' · '.join(f'<a href="#{t["id"]}">{e(t["name"])}</a>' for t in TRACKS)
    body = f"""{nav(lang, pfad)}
<main id="inhalt">
<section class="seitenkopf"><div class="wrap">
  <h1>{"Motocross <span>tracks</span>" if en else "Motocross-<span>Strecken</span>"}</h1>
  <p class="lead">{f"MX Royale has {N_RACE} race tracks and {N_FREE} freeride maps, all free to ride in your browser. They range from a beginner MX park to two supercross tracks and long outdoor Grand Prix tracks in forest, desert, snow and on the coast." if en else f"MX Royale hat {N_RACE} Rennstrecken und {N_FREE} Freeride-Maps, alle kostenlos im Browser fahrbar. Vom Einsteiger-MX-Park über zwei Supercross-Strecken bis zu langen Outdoor-Grand-Prix in Wald, Wüste, Schnee und an der Küste."}</p>
  {ride(lang, ' klein-los')}
  <p class="klein" style="margin-top:24px">{sprung}</p>
</div></section>
<section style="padding-top:8px"><div class="wrap">
{chr(10).join(arts)}
<p style="margin-top:36px">{f'Want to know how whips and scrubs work? Read <a href="{PFAD[lang]["how"]}">how to play</a>.' if en else f'Wie Whips und Scrubs gehen, steht in der <a href="{PFAD[lang]["how"]}">Anleitung</a>.'}</p>
{ride(lang)}
</div></section>
</main>"""
    titel = 'Motocross Tracks – Supercross, Desert, Snow | MX Royale' if en else 'Motocross-Strecken – Supercross, Wüste, Schnee | MX Royale'
    desc = (f'All {N_RACE} race tracks and {N_FREE} freeride maps in MX Royale, the free browser motocross game: supercross, forest GP, desert, snow and beach.'
            if en else f'Alle {N_RACE} Strecken und {N_FREE} Freeride-Maps von MX Royale, dem Motocross Browserspiel: Supercross, Wald-GP, Wüste, Schnee und Strand.')
    item_list = {'@type': 'ItemList', 'name': 'MX Royale tracks' if en else 'MX-Royale-Strecken',
                 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': t['name'], 'url': SITE + pfad + '#' + t['id']}
                                     for i, t in enumerate(TRACKS)]}
    ld = graph(breadcrumb(lang, pfad, 'Tracks' if en else 'Strecken'), item_list)
    return seite(lang, pfad, titel, desc, body, ld)


# ── Anleitung ──────────────────────────────────────────────────────────────────────────────────────
def anleitung(lang):
    en = lang == 'en'
    pfad = PFAD[lang]['how']
    if en:
        inhalt = f"""
<p class="lead">MX Royale is easy to start and hard to master. Press <b>Ride now</b>, pick a track and go – the game runs in your browser on PC, Mac, phone or tablet. This page explains the controls for keyboard, phone and controller, and how whips, scrubs and the gate start work.</p>
{ride(lang, ' klein-los')}
<h2>Keyboard</h2>
<div class="tabelle"><table>
<tr><th><kbd>W</kbd> / <kbd>S</kbd></th><td>Throttle / brake</td></tr>
<tr><th><kbd>A</kbd> / <kbd>D</kbd></th><td>Steer · in the air: whip the bike</td></tr>
<tr><th><kbd>←</kbd> / <kbd>→</kbd></th><td>Lean the bike · on the ramp: scrub · in the air: lay it flat</td></tr>
<tr><th><kbd>↑</kbd> / <kbd>↓</kbd></th><td>Weight forward / back · stoppie / wheelie</td></tr>
<tr><th><kbd>Space</kbd></th><td>Crouch / pop · in freeride: tricks together with the arrow keys</td></tr>
<tr><th><kbd>Shift</kbd></th><td>Rear brake</td></tr>
<tr><th><kbd>R</kbd></th><td>Respawn on the track</td></tr>
<tr><th><kbd>C</kbd> · <kbd>Q</kbd> · <kbd>G</kbd> · <kbd>Esc</kbd></th><td>Camera · look back (hold) · ghost on/off · pause</td></tr>
</table></div>
<p class="klein">You can change every riding key in Settings.</p>
<h2>Phone and tablet</h2>
<ul>
<li>Turn the phone to <b>landscape</b>.</li>
<li><b>Left thumb:</b> a stick appears where you touch. Left/right steers (and whips in the air), up/down moves your weight.</li>
<li><b>Right thumb:</b> hold <b>GAS</b>, brake sits to its left. Drag left/right on the throttle to lean the bike (scrub), drag down to load the suspension and let go at the lip to pop.</li>
<li>Top right: camera, respawn, pause. Prefer tilting? Switch on tilt steering under Settings → Phone steering.</li>
<li>On the Beginner and Normal levels the rider pops off jumps for you.</li>
</ul>
<h2>Controller (gamepad)</h2>
<ul>
<li><b>RT</b> throttle, <b>LT</b> brake (both analog).</li>
<li><b>Left stick</b> steers and whips in the air.</li>
<li><b>Right stick</b> ↕ moves your weight, ↔ leans the bike (scrub, lay it flat).</li>
<li><b>A</b> crouch/pop · <b>X</b> rear brake · <b>Y</b> respawn · <b>Start</b> pause.</li>
<li>Tricks in freeride: hold <b>LB</b> or <b>RB</b> in the air and use the left stick; LB + RB = no hands.</li>
</ul>
<h2>How to whip</h2>
<p>A whip throws the bike sideways in the air. Steer in just before the lip (<kbd>A</kbd>/<kbd>D</kbd>, left stick or the touch stick), hold it in the air and let go about half a second before landing so the bike comes back straight. The better the timing, the further the whip goes – past 180° if you get it right. A whip counts from 40°.</p>
<h2>How to scrub</h2>
<p>A scrub keeps you low over a jump so you are back on the ground sooner, which is faster in a race. Lay the bike down on the face of the ramp (<kbd>←</kbd>/<kbd>→</kbd>, right stick, or drag on the throttle) and stand it back up before the end of the lip – otherwise the front wheel hooks.</p>
<h2>Pop and gate start</h2>
<p><b>Pop:</b> hold crouch on the ramp and release it at the lip to jump higher and further. <b>Gate start:</b> from the “5” board hold throttle and brake together to build revs, then release the brake when the gate drops. Throttle without brake before that is a jump start.</p>
<h2>Tricks and the trick school</h2>
<p>In freeride and in the trick school you can do backflips, Supermans, Nac-Nacs, heel clickers, Can-Cans, seat grabs and cliffhangers. The trick school teaches each one step by step for keyboard, phone and controller, and tells you what went wrong.</p>
<h2>Tips for faster laps</h2>
<ul>
<li>Land on the downslope behind a jump to keep your speed.</li>
<li>Cutting does not pay: leave the track and the lap does not count.</li>
<li>Stuck? Respawn puts you back on the course.</li>
<li>Start with Sunvale MX Park, the beginner track, and switch the rider aids (Beginner, Normal, Sport, Pro, Sim) under Settings when you get faster.</li>
<li>In time trial your own best lap rides along as a ghost – race it until you beat the medal times.</li>
<li>Four cameras: dynamic chase, classic chase, drone and helmet.</li>
</ul>
"""
    else:
        inhalt = f"""
<p class="lead">MX Royale ist schnell gelernt und schwer zu meistern. Auf <b>Jetzt fahren</b> tippen, Strecke wählen, los – das Spiel läuft im Browser am PC, Mac, Handy oder Tablet. Hier steht die Steuerung für Tastatur, Handy und Controller und wie Whips, Scrubs und der Gatterstart gehen.</p>
{ride(lang, ' klein-los')}
<h2>Tastatur</h2>
<div class="tabelle"><table>
<tr><th><kbd>W</kbd> / <kbd>S</kbd></th><td>Gas / Bremse</td></tr>
<tr><th><kbd>A</kbd> / <kbd>D</kbd></th><td>Lenken · in der Luft: Whip</td></tr>
<tr><th><kbd>←</kbd> / <kbd>→</kbd></th><td>Bike kippen · an der Rampe: Scrub · in der Luft: flach legen</td></tr>
<tr><th><kbd>↑</kbd> / <kbd>↓</kbd></th><td>Gewicht vor / zurück · Stoppie / Wheelie</td></tr>
<tr><th><kbd>Leertaste</kbd></th><td>Ducken / Pop · im Freeride: Tricks zusammen mit den Pfeiltasten</td></tr>
<tr><th><kbd>Shift</kbd></th><td>Hinterradbremse</td></tr>
<tr><th><kbd>R</kbd></th><td>Zurück auf die Strecke</td></tr>
<tr><th><kbd>C</kbd> · <kbd>Q</kbd> · <kbd>G</kbd> · <kbd>Esc</kbd></th><td>Kamera · zurückschauen (halten) · Geist an/aus · Pause</td></tr>
</table></div>
<p class="klein">Alle Fahr-Tasten lassen sich in den Einstellungen ändern.</p>
<h2>Handy und Tablet</h2>
<ul>
<li>Handy ins <b>Querformat</b> drehen.</li>
<li><b>Linker Daumen:</b> Wo du hintippst, erscheint ein Stick. Links/rechts lenkt (und whippt in der Luft), hoch/runter verlagert das Gewicht.</li>
<li><b>Rechter Daumen:</b> <b>GAS</b> halten, die Bremse liegt links daneben. Auf dem Gas nach links/rechts ziehen kippt das Bike (Scrub), nach unten ziehen lädt die Federung – an der Kante loslassen ist der Pop.</li>
<li>Oben rechts: Kamera, Neustart-Punkt, Pause. Lieber neigen? Neige-Steuerung unter Einstellungen → Handy-Steuerung einschalten.</li>
<li>Auf den Stufen Einsteiger und Normal springt der Fahrer an Sprüngen von selbst ab.</li>
</ul>
<h2>Controller (Gamepad)</h2>
<ul>
<li><b>RT</b> Gas, <b>LT</b> Bremse (beide analog).</li>
<li><b>Linker Stick</b> lenkt und whippt in der Luft.</li>
<li><b>Rechter Stick</b> ↕ Gewicht, ↔ Bike kippen (Scrub, flach legen).</li>
<li><b>A</b> Ducken/Pop · <b>X</b> Hinterradbremse · <b>Y</b> zurück auf die Strecke · <b>Start</b> Pause.</li>
<li>Tricks im Freeride: in der Luft <b>LB</b> oder <b>RB</b> halten und den linken Stick nutzen; LB + RB = freihändig.</li>
</ul>
<h2>So geht der Whip</h2>
<p>Beim Whip wirfst du das Bike in der Luft quer. Kurz vor der Kante einlenken (<kbd>A</kbd>/<kbd>D</kbd>, linker Stick oder Touch-Stick), in der Luft halten und etwa eine halbe Sekunde vor der Landung loslassen, dann kommt das Bike gerade zurück. Je besser das Timing, desto weiter geht der Whip – mit gutem Timing über 180°. Gewertet wird ab 40°.</p>
<h2>So geht der Scrub</h2>
<p>Ein Scrub hält dich flach über dem Sprung, du bist früher wieder am Boden und im Rennen schneller. Leg das Bike an der Rampe flach (<kbd>←</kbd>/<kbd>→</kbd>, rechter Stick oder auf dem Gas ziehen) und richte es vor dem Ende der Kante wieder auf – sonst hängt das Vorderrad.</p>
<h2>Pop und Gatterstart</h2>
<p><b>Pop:</b> An der Rampe ducken und an der Kante loslassen – du springst höher und weiter. <b>Gatterstart:</b> Ab der „5“-Tafel Gas und Bremse zusammen halten (Drehzahl), wenn das Gatter fällt, die Bremse loslassen. Gas ohne Bremse vorher ist ein Frühstart.</p>
<h2>Tricks und Trick-Schule</h2>
<p>Im Freeride und in der Trick-Schule gehen Backflip, Superman, Nac-Nac, Heel Clicker, Can-Can, Seat Grab und Cliffhanger. Die Trick-Schule erklärt jeden Trick Schritt für Schritt für Tastatur, Handy und Controller und sagt dir, was schiefging.</p>
<h2>Tipps für schnellere Runden</h2>
<ul>
<li>Lande im Gefälle hinter dem Sprung, dann behältst du dein Tempo.</li>
<li>Abkürzen lohnt sich nicht: Wer die Strecke verlässt, dessen Runde zählt nicht.</li>
<li>Festgefahren? Der Neustart-Punkt setzt dich zurück auf die Strecke.</li>
<li>Fang mit Sunvale MX Park an, der Einsteiger-Strecke, und stell die Fahrhilfen (Einsteiger, Normal, Sport, Pro, Sim) in den Einstellungen um, wenn du schneller wirst.</li>
<li>Im Zeitfahren fährt deine Bestzeit als Geist mit – fahr gegen ihn, bis du die Medaillenzeiten knackst.</li>
<li>Vier Kameras: dynamische Verfolger-Kamera, klassische Verfolger-Kamera, Drohne und Helm.</li>
</ul>
"""
    body = f"""{nav(lang, pfad)}
<main id="inhalt">
<section class="seitenkopf"><div class="wrap text">
  <h1>{"How to <span>play</span>" if en else "So wird <span>gespielt</span>"}</h1>
  {inhalt}
  <p style="margin-top:32px">{f'Next: pick a track on the <a href="{PFAD[lang]["tracks"]}">tracks page</a>.' if en else f'Weiter: Such dir eine Strecke auf der <a href="{PFAD[lang]["tracks"]}">Strecken-Seite</a> aus.'}</p>
  {ride(lang)}
</div></section>
</main>"""
    titel = 'How to Play MX Royale – Controls, Whips & Scrubs' if en else 'MX Royale Anleitung – Steuerung, Whips & Scrubs'
    desc = ('How to play the free motocross game MX Royale: keyboard, phone and controller controls, how to whip, scrub and pop, plus tips for faster laps.'
            if en else 'So spielst du das Motocross Browserspiel MX Royale: Steuerung für Tastatur, Handy und Controller, Whip, Scrub, Pop und Tipps für schnellere Runden.')
    ld = graph(breadcrumb(lang, pfad, 'How to play' if en else 'Anleitung'))
    return seite(lang, pfad, titel, desc, body, ld)


# ── Über / Faktenblatt ─────────────────────────────────────────────────────────────────────────────
def ueber(lang):
    en = lang == 'en'
    pfad = PFAD[lang]['about']
    sx = ', '.join(t['name'] for t in TRACKS if t['typ'][0] == 'Supercross')
    if en:
        abs_ = [
            ('What is MX Royale?', 'MX Royale is a free motocross racing game that runs in the web browser. It needs no download and no account, and it works on PC, Mac, phones and tablets with keyboard, touch controls or a gamepad.'),
            ('What can you do in MX Royale?', f'In MX Royale you race motocross and supercross bikes on {N_RACE} race tracks and {N_FREE} freeride maps. Game modes are races against up to 11 AI riders, time trial against your own ghost with medal times, a Daily Challenge, a Championship of four races, freeride, a trick school and online races with friends via a 5-character room code.'),
            ('Which tracks are there?', f'MX Royale has two supercross tracks ({sx}) and outdoor tracks in forest, desert, canyon, snow, rainforest, beach, quarry and salt-lake settings. The beginner track is Sunvale MX Park.'),
            ('Who makes MX Royale?', 'MX Royale is developed by three students from Austria as a hobby project. The game has been in open beta since 26 November 2026; it has no ads and no in-game purchases.'),
        ]
        rows = [
            ('Price', 'Free – no ads, no in-game purchases'), ('Download / install', 'None – runs in the browser'),
            ('Browsers', 'Chrome, Edge, Firefox, Safari'), ('Devices', 'PC, Mac, phones and tablets (landscape)'),
            ('Controls', 'Keyboard (remappable), touch with optional tilt steering, gamepad'),
            ('Single-player modes', 'Race vs. AI, time trial with ghost, Daily Challenge, Championship, freeride, trick school'),
            ('Multiplayer', 'Online races with a 5-character room code; bots can fill the field'),
            ('Tracks', f'{N_RACE} race tracks + {N_FREE} freeride maps, including 2 supercross tracks'),
            ('Race field', 'Up to 12 riders (you + AI)'),
            ('Tricks', 'Whips, scrubs, backflips, Superman, Nac-Nac, Can-Can, heel clicker, seat grab, cliffhanger'),
            ('Bikes', '450 four-stroke, 250 two-stroke and electric'),
            ('Rider aids', 'Five levels: Beginner, Normal, Sport, Pro, Sim'),
            ('Languages', 'English, German, Spanish, French, Brazilian Portuguese'),
            ('Account', 'Optional'), ('Status', 'Open beta since 26 November 2026'),
            ('Developer', 'Three students from Austria'), ('Website', 'mxroyale.com'), ('Play', 'play.mxroyale.com'),
        ]
        h1 = 'MX Royale <span>fact sheet</span>'
        stand = f'Last updated: {STAND_EN}'
        tab_h = 'Feature overview'
    else:
        abs_ = [
            ('Was ist MX Royale?', 'MX Royale ist ein kostenloses Motocross-Rennspiel, das im Webbrowser läuft. Es braucht keinen Download und kein Konto und läuft am PC, Mac, Handy und Tablet mit Tastatur, Touch-Steuerung oder Gamepad.'),
            ('Was kann man in MX Royale machen?', f'In MX Royale fährst du Motocross und Supercross auf {N_RACE} Rennstrecken und {N_FREE} Freeride-Maps. Spielmodi sind Rennen gegen bis zu 11 KI-Fahrer, Zeitfahren gegen den eigenen Geist mit Medaillenzeiten, eine Tages-Challenge, eine Meisterschaft über vier Rennen, Freeride, eine Trick-Schule und Online-Rennen mit Freunden über einen 5-stelligen Raum-Code.'),
            ('Welche Strecken gibt es?', f'MX Royale hat zwei Supercross-Strecken ({sx}) und Outdoor-Strecken in Wald, Wüste, Canyon, Schnee, Regenwald, am Strand, im Steinbruch und auf einem Salzsee. Die Einsteiger-Strecke ist Sunvale MX Park.'),
            ('Wer macht MX Royale?', 'MX Royale entwickeln drei Schüler aus Österreich als Hobbyprojekt. Das Spiel ist seit 26. November 2026 in der offenen Beta; es hat keine Werbung und keine In-Game-Käufe.'),
        ]
        rows = [
            ('Preis', 'Kostenlos – keine Werbung, keine In-Game-Käufe'), ('Download / Installation', 'Keine – läuft im Browser'),
            ('Browser', 'Chrome, Edge, Firefox, Safari'), ('Geräte', 'PC, Mac, Handy und Tablet (Querformat)'),
            ('Steuerung', 'Tastatur (frei belegbar), Touch mit optionaler Neige-Steuerung, Gamepad'),
            ('Einzelspieler', 'Rennen gegen KI, Zeitfahren mit Geist, Tages-Challenge, Meisterschaft, Freeride, Trick-Schule'),
            ('Mehrspieler', 'Online-Rennen mit 5-stelligem Raum-Code; Bots können das Feld auffüllen'),
            ('Strecken', f'{N_RACE} Rennstrecken + {N_FREE} Freeride-Maps, davon 2 Supercross-Strecken'),
            ('Starterfeld', 'Bis zu 12 Fahrer (du + KI)'),
            ('Tricks', 'Whips, Scrubs, Backflip, Superman, Nac-Nac, Can-Can, Heel Clicker, Seat Grab, Cliffhanger'),
            ('Bikes', '450er-Viertakter, 250er-Zweitakter und Elektro'),
            ('Fahrhilfen', 'Fünf Stufen: Einsteiger, Normal, Sport, Pro, Sim'),
            ('Sprachen', 'Englisch, Deutsch, Spanisch, Französisch, brasilianisches Portugiesisch'),
            ('Konto', 'Optional'), ('Status', 'Offene Beta seit 26. November 2026'),
            ('Entwickler', 'Drei Schüler aus Österreich'), ('Website', 'mxroyale.com'), ('Spielen', 'play.mxroyale.com'),
        ]
        h1 = 'MX Royale <span>Faktenblatt</span>'
        stand = f'Zuletzt aktualisiert: {STAND_DE}'
        tab_h = 'Funktionen im Überblick'
    absatz = ''.join(f'<h2>{e(h)}</h2><p>{e(p)}</p>' for h, p in abs_)
    tab = ''.join(f'<tr><th scope="row">{e(k)}</th><td>{e(v)}</td></tr>' for k, v in rows)
    body = f"""{nav(lang, pfad)}
<main id="inhalt">
<section class="seitenkopf"><div class="wrap text">
  <h1>{h1}</h1>
  <p class="klein"><time datetime="{STAND}">{stand}</time></p>
  {absatz}
  <h2>{tab_h}</h2>
  <div class="tabelle"><table>{tab}</table></div>
  <p style="margin-top:32px">{f'More: <a href="{PFAD[lang]["tracks"]}">all tracks</a> · <a href="{PFAD[lang]["how"]}">how to play</a> · <a href="{PFAD[lang]["press"]}">press kit</a> · <a href="/llms.txt">llms.txt</a>' if en else f'Mehr: <a href="{PFAD[lang]["tracks"]}">alle Strecken</a> · <a href="{PFAD[lang]["how"]}">Anleitung</a> · <a href="{PFAD[lang]["press"]}">Pressematerial</a>'}</p>
  {ride(lang)}
</div></section>
</main>"""
    titel = 'About MX Royale – Fact Sheet of the Browser Motocross Game' if en else 'Über MX Royale – Faktenblatt zum Motocross Browserspiel'
    desc = ('Fact sheet: MX Royale is a free motocross racing game in the web browser. Platforms, controls, modes, tracks, languages and status at a glance.'
            if en else 'Faktenblatt: MX Royale ist ein kostenloses Motocross-Rennspiel im Browser. Geräte, Steuerung, Modi, Strecken, Sprachen und Status im Überblick.')
    about = {'@type': 'AboutPage', '@id': SITE + pfad, 'url': SITE + pfad, 'name': titel, 'inLanguage': lang,
             'dateModified': STAND, 'about': {'@id': SITE + '/#game'}, 'publisher': {'@id': SITE + '/#org'}}
    ld = graph(about, breadcrumb(lang, pfad, 'About' if en else 'Über das Spiel'))
    return seite(lang, pfad, titel, desc, body, ld)


# ── Textdateien ────────────────────────────────────────────────────────────────────────────────────
def sitemap():
    z = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for a, b in PAARE:
        for p in (a, b):
            z.append(f'  <url>\n    <loc>{SITE}{p}</loc>\n    <lastmod>{STAND}</lastmod>\n    <priority>{PRIO[p]}</priority>')
            z.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{SITE}{a}"/>')
            z.append(f'    <xhtml:link rel="alternate" hreflang="de" href="{SITE}{b}"/>')
            z.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{a}"/>\n  </url>')
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
- Status: open beta since 2026-11-26.
- Developer: three students from Austria (hobby project).
- Play: {PLAY}
- Social: TikTok, Instagram and YouTube as @mxroyalegame."""
    seiten = f"""## Pages

- [Home (English)]({SITE}/): overview, track list and FAQ
- [Tracks]({SITE}/tracks/): all tracks with descriptions
- [How to play]({SITE}/how-to-play/): controls for keyboard, phone and controller; whips, scrubs, pop, gate start
- [Fact sheet]({SITE}/about/): answer-first summary and feature table
- [Press & creators]({SITE}/press/): press kit, logo, key art
- [Deutsch – Startseite]({SITE}/de/), [Strecken]({SITE}/de/strecken/), [Anleitung]({SITE}/de/anleitung/), [Faktenblatt]({SITE}/de/ueber/), [Presse]({SITE}/presse/)

## Optional

- [Privacy]({SITE}/privacy/): no tracking, no analytics, no ads
- [Legal notice]({SITE}/legal/)
- [Full text for language models]({SITE}/llms-full.txt)
"""
    kopf = f"""# MX Royale

> MX Royale is a free motocross racing game that runs in the web browser. No download and no account are needed; it works on PC, Mac, phones and tablets with keyboard, touch controls or a gamepad. It has {N_RACE} race tracks (including supercross), {N_FREE} freeride maps, whips, scrubs and flips, races against AI, time trial with ghosts and online races with friends.

Last updated: {STAND}

## Facts

{fakten}

"""
    if not voll:
        return kopf + seiten
    strecken = '\n'.join(f'- **{t["name"]}** ({DIFF[t["diff"]][0]}, {t["typ"][0]}): {t["en"]}' for t in TRACKS)
    faq = '\n\n'.join(f'### {q}\n\n{a}' for q, a in FAQ['en'])
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
    import re
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
        d = json.loads(block)
        assert d['@context'] == 'https://schema.org', rel
        for item in d['@graph']:
            assert '@type' in item, rel


def main():
    gebaut = []
    for lang in ('en', 'de'):
        p = PFAD[lang]
        for pfad, fn in ((p['home'], startseite), (p['tracks'], streckenseite), (p['how'], anleitung), (p['about'], ueber)):
            txt = fn(lang)
            pruefe_ld(txt, pfad)
            gebaut.append(schreibe(pfad, txt))
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
