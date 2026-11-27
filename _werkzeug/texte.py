# -*- coding: utf-8 -*-
"""
Alle Seitentexte von mxroyale.com in fünf Sprachen (en, de, es, fr, pt = pt-BR) – von build.py gelesen.
Platzhalter in {geschweiften Klammern} füllt build.py: nr/nf = Anzahl Renn-/Freeride-Strecken, sx = Supercross-Strecken,
tracks/how/about/press = Pfade derselben Sprache, ride = kleiner Fahr-Knopf (HTML).
Begriffe in es/fr/pt folgen der Spiel-Übersetzung (worktrees/n-int/src/i18n/{es,fr,pt}.ts): Contrarreloj/Contre-la-montre/
Contra o relógio, Fantasma/Fantôme, Desafío diario/Défi du jour/Desafio diário, Campeonato/Championnat, Escuela de trucos/
École de figures/Escola de manobras, Ayudas/Aides/Ajudas (Principiante|Débutant|Iniciante, Normal, Sport, Pro, Sim).
"""

# ── Pfade je Sprache ───────────────────────────────────────────────────────────────────────────────
PFAD = {
    'en': dict(home='/', tracks='/tracks/', how='/how-to-play/', about='/about/', press='/press/', legal='/legal/', privacy='/privacy/'),
    'de': dict(home='/de/', tracks='/de/strecken/', how='/de/anleitung/', about='/de/ueber/', press='/presse/', legal='/impressum/', privacy='/datenschutz/'),
    'es': dict(home='/es/', tracks='/es/pistas/', how='/es/como-jugar/', about='/es/acerca-de/', press='/press/', legal='/legal/', privacy='/privacy/'),
    'fr': dict(home='/fr/', tracks='/fr/circuits/', how='/fr/comment-jouer/', about='/fr/a-propos/', press='/press/', legal='/legal/', privacy='/privacy/'),
    'pt': dict(home='/pt/', tracks='/pt/pistas/', how='/pt/como-jogar/', about='/pt/sobre/', press='/press/', legal='/legal/', privacy='/privacy/'),
}

# ── Strecken-Texte es/fr/pt (en/de stehen in build.py bei TRACKS) ──────────────────────────────────
DIFF_INTL = {
    'Beginner': dict(es='Principiante', fr='Débutant', pt='Iniciante'),
    'Mittel': dict(es='Media', fr='Moyen', pt='Média'),
    'Mittel bis schwer': dict(es='Media–difícil', fr='Moyen–difficile', pt='Média–difícil'),
    'Schwer': dict(es='Difícil', fr='Difficile', pt='Difícil'),
    'Freeride': dict(es='Freeride', fr='Freeride', pt='Freeride'),
}
TYP_INTL = {  # Schlüssel = englischer Typ
    'Motocross': dict(es='Motocross', fr='Motocross', pt='Motocross'),
    'Supercross': dict(es='Supercross', fr='Supercross', pt='Supercross'),
    'Snow': dict(es='Nieve', fr='Neige', pt='Neve'),
    'Desert': dict(es='Desierto', fr='Désert', pt='Deserto'),
    'Forest': dict(es='Bosque', fr='Forêt', pt='Floresta'),
    'Grand Prix': dict(es='Gran Premio', fr='Grand Prix', pt='Grande Prêmio'),
    'Canyon': dict(es='Cañón', fr='Canyon', pt='Cânion'),
    'Mountain': dict(es='Montaña', fr='Montagne', pt='Montanha'),
    'Rainforest': dict(es='Selva', fr='Forêt tropicale', pt='Floresta tropical'),
    'Beach': dict(es='Playa', fr='Plage', pt='Praia'),
    'Quarry': dict(es='Cantera', fr='Carrière', pt='Pedreira'),
    'Salt lake': dict(es='Lago salado', fr='Lac salé', pt='Lago de sal'),
    'Freeride': dict(es='Freeride', fr='Freeride', pt='Freeride'),
    'Freestyle': dict(es='Freestyle', fr='Freestyle', pt='Freestyle'),
}
# id → (kurz, lang)
TRACK_TX = {
    'es': {
        'sunvale': ('La pista para principiantes: un parque de MX en el campo, con rollers, mesas pequeñas y un vado en el arroyo.',
                    'Aquí empieza casi todo el mundo. Curvas anchas sobre pasto, rollers y mesas pequeñas pasan por potreros con vacas y junto a fardos de heno, y una sección cruza directamente el arroyo. Ideal para aprender el pop y tus primeros whips.'),
        'larkmeadow': ('Supercross en un estadio de noche: secciones de ritmo, whoops, una sección de arena y un triple en la meta.',
                       'Una pista de supercross corta y cerrada bajo los reflectores del estadio. Secciones de ritmo, whoops y arena se suceden una tras otra, y la vuelta termina con un doble de SX y un triple sobre la línea de meta.'),
        'frostline': ('Pista de nieve en una pista de esquí, junto a la telesilla y sobre el Frozen Creek Gap.',
                      'Frostline baja por una pista de esquí en invierno: a lo largo de la telesilla, junto a los cañones de nieve y sobre el Frozen Creek Gap. Rollers de nieve y un gran salto hacia la recta final cierran la vuelta.'),
        'monsoon': ('Una pista fluida sobre terrazas de arroz en una ladera, con una cadena de terrazas y un acueducto de madera.',
                    'Un trazado fluido en una ladera con terrazas. Una cadena de saltos baja de terraza en terraza, la pista pasa junto al bambú y recorre un acueducto de madera. Aquí cuenta más una línea limpia que la velocidad pura.'),
        'mirage-flats': ('Parque de saltos en el desierto sobre un lago seco, con un rail gap sobre las vías y un largo washboard.',
                         'Un parque de saltos en el desierto. Con el Rail Gap pasas por encima de las vías del tren, atraviesas un washboard en el fondo del lago seco y terminas con la mesa Mirage. Mucho tiempo en el aire y poco margen de error en los aterrizajes.'),
        'herbst': ('Bosque otoñal con luz de atardecer, fuego en tres saltos, un gran step-up y un gran step-down.',
                   'Una pista en un bosque otoñal con la luz baja del atardecer. Hay fuego junto a tres saltos, la subida tiene un gran step-up y la bajada un gran step-down hacia el valle. Entre medio, hojas, raíces y secciones de ritmo.'),
        'rustleaf': ('Una pista sinuosa en el bosque otoñal, con raíces, una hondonada embarrada y un camino de arrastre de troncos.',
                     'Estrecha y sinuosa: Rustleaf serpentea por el bosque otoñal sobre alfombras de raíces, a través de una hondonada embarrada, por un camino de arrastre de troncos y junto a una excavadora. Una pista para dirigir con precisión más que para ir a fondo.'),
        'neonharbor': ('Supercross de noche en una nave del puerto: mesa de contenedores, curva bajo la grúa, whoops del muelle y un triple.',
                       'La segunda pista de supercross está en una nave del puerto, de noche. Saltas una mesa hecha de contenedores, giras bajo una grúa, peleas con los whoops del muelle y vas por el Harbor Triple.'),
        'pine-ridge': ('Un largo Gran Premio en el bosque sobre una cresta, con Horsepower Hill, el Stump Double y el Ridge Double.',
                       'Un Gran Premio clásico al aire libre por un bosque de pinos. La pista sube Horsepower Hill, recorre la cresta sobre raíces y dobles y vuelve a bajar por el bosque. Vueltas largas y una parrilla completa de 12 pilotos.'),
        'sandglass': ('Gran Premio en un cañón del desierto: escalones de roca, mesa en la meseta, cañón estrecho, drop desde el acantilado y road gap.',
                      'Sandglass te lleva por cañones rojos del desierto. Escalones y losas de roca, una mesa en lo alto de la meseta, un cañón estrecho, un drop desde un acantilado y un Road Gap sobre la carretera, y de vuelta por el cauce seco a través de los whoops.'),
        'highcrest': ('Un GP de montaña largo y rápido con 38 m de desnivel, losas de caliza, curvas en zigzag y una cascada.',
                      'La pista al aire libre más rápida: Highcrest sube 38 metros entre bosque y roca, sobre losas de caliza y por curvas en zigzag hasta la cima, y luego baja por una puerta de roca y junto a una cascada.'),
        'canopy': ('Selva en una hondonada: gap sobre un barranco, puente colgante, túnel de árboles, cascada y un dragon’s back.',
                   'Una pista sinuosa de selva en el fondo de una hondonada. Salta un gap sobre un barranco, cruza un puente colgante, atraviesa un túnel de árboles, pasa junto a una cascada y mantén el equilibrio en el dragon’s back.'),
        'tidewater': ('Un GP técnico de arena en la costa con marea baja, con un gap sobre un canal y un paso por un naufragio.',
                      'Arena en la costa con marea baja. Ondulaciones y arena blanda por todas partes, un gap sobre un canal de marea, una curva junto al faro, un pasillo entre los espigones y una línea que atraviesa un viejo naufragio.'),
        'ironcut': ('Una cantera abandonada: zigzags por las terrazas de extracción, un drop al pozo y un dragon’s back en el borde.',
                    'Ironcut sube en zigzag de terraza en terraza por una cantera abandonada. Arriba recorres un dragon’s back por el borde antes de una bajada empinada de vuelta al fondo del pozo.'),
        'saltpan': ('Un Gran Premio rápido sobre un lago salado, con el Salt Crust Triple y una mesa junto a la cinta transportadora.',
                    'Abierta y rápida: Saltpan cruza un lago salado con rectas largas y rollers. Lo más destacado son el Salt Crust Triple y una mesa junto a la cinta transportadora de la salina.'),
        'freeride': ('Mapa de freeride: líneas de saltos, un step-up, un hip y un foso de espuma, sin vueltas ni cronómetro.',
                     'Sin vueltas, sin cronómetro, sin rivales. Dust Devil es un mapa abierto con líneas de saltos, un step-up, un hip y un foso de espuma para practicar trucos sin consecuencias.'),
        'arena': ('Show nocturno de freestyle motocross en un estadio, con rampas para whips, flips y big air.',
                  'Un show de freestyle motocross de noche en un estadio. Rampas propias para whips, backflips, Nac-Nacs, Can-Cans y big air, además de un quarterpipe y fuegos artificiales.'),
    },
    'fr': {
        'sunvale': ('Le circuit débutant : un parc MX à la campagne, avec rollers, petites tables et un gué dans le ruisseau.',
                    'La plupart des pilotes commencent ici. De larges virages dans l’herbe, des rollers et de petites tables passent entre les prés à vaches et les bottes de foin, et une section traverse carrément le ruisseau. Parfait pour apprendre le pop et tes premiers whips.'),
        'larkmeadow': ('Supercross dans un stade de nuit : sections de rythme, whoops, une section de sable et un triple sur la ligne.',
                       'Un circuit de supercross court et serré sous les projecteurs du stade. Sections de rythme, whoops et sable s’enchaînent, et le tour se termine par un double SX et un triple au-dessus de la ligne d’arrivée.'),
        'frostline': ('Circuit enneigé sur une piste de ski, le long du télésiège et au-dessus du Frozen Creek Gap.',
                      'Frostline descend une piste de ski en hiver : le long du télésiège, devant les canons à neige et au-dessus du Frozen Creek Gap. Des bosses de neige et un grand saut vers la ligne droite d’arrivée bouclent le tour.'),
        'monsoon': ('Un circuit fluide sur des rizières en terrasses, avec une chaîne de terrasses et un aqueduc en bois.',
                    'Un tracé fluide sur une colline en terrasses. Une série de sauts descend de terrasse en terrasse, le circuit longe les bambous et un aqueduc en bois. Ici, une trajectoire propre compte plus que la vitesse pure.'),
        'mirage-flats': ('Parc à sauts dans le désert sur un lac asséché, avec un rail gap au-dessus des voies et une longue tôle ondulée.',
                         'Un parc à sauts dans le désert. Le Rail Gap te fait passer au-dessus de la voie ferrée, tu traverses une tôle ondulée sur le lac asséché et tu finis par la table Mirage. Beaucoup de temps en l’air, peu de marge d’erreur à la réception.'),
        'herbst': ('Forêt d’automne dans la lumière du soir, du feu à trois sauts, un grand step-up et un grand step-down.',
                   'Un circuit en forêt d’automne dans la lumière rasante du soir. Trois sauts sont bordés de feu, la montée a un grand step-up et la descente un grand step-down vers la vallée. Entre les deux : feuilles, racines et sections de rythme.'),
        'rustleaf': ('Un circuit sinueux en forêt d’automne, avec racines, un creux boueux et un layon de débardage.',
                     'Étroit et sinueux : Rustleaf serpente dans la forêt d’automne sur des tapis de racines, à travers un creux boueux, le long d’un layon de débardage et devant une pelleteuse. Un circuit qui demande de la précision plutôt que de rouler à fond.'),
        'neonharbor': ('Supercross de nuit dans un hangar du port : table en conteneurs, virage sous la grue, whoops du quai et un triple.',
                       'Le deuxième circuit de supercross se trouve de nuit dans un hangar du port. Tu sautes une table faite de conteneurs, tu tournes sous une grue, tu te bats dans les whoops du quai et tu tentes le Harbor Triple.'),
        'pine-ridge': ('Un long Grand Prix en forêt sur une crête, avec Horsepower Hill, le Stump Double et le Ridge Double.',
                       'Un Grand Prix outdoor classique dans une forêt de pins. Le circuit grimpe Horsepower Hill, longe la crête sur des racines et des doubles, puis redescend à travers la forêt. Des tours longs et une grille complète de 12 pilotes.'),
        'sandglass': ('Grand Prix dans un canyon du désert : marches rocheuses, table sur une mesa, canyon étroit, drop de falaise et road gap.',
                      'Sandglass t’emmène à travers des canyons rouges du désert. Marches et dalles rocheuses, une table au sommet d’une mesa, un canyon étroit, un drop depuis une falaise et un Road Gap au-dessus de la route, puis retour par le lit asséché à travers les whoops.'),
        'highcrest': ('Un GP de montagne long et rapide, avec 38 m de dénivelé, des dalles calcaires, des lacets et une cascade.',
                      'Le circuit outdoor le plus rapide : Highcrest grimpe de 38 mètres à travers forêt et rochers, sur des dalles calcaires et par des lacets jusqu’au sommet, puis redescend par une porte rocheuse et devant une cascade.'),
        'canopy': ('Forêt tropicale dans une cuvette : gap au-dessus d’une gorge, pont suspendu, tunnel d’arbres, cascade et dragon’s back.',
                   'Un circuit sinueux en forêt tropicale, au fond d’une cuvette. Saute un gap au-dessus d’une gorge, traverse un pont suspendu, passe dans un tunnel d’arbres et devant une cascade, et garde l’équilibre sur le dragon’s back.'),
        'tidewater': ('Un GP technique dans le sable, sur la côte à marée basse, avec un gap au-dessus d’un chenal et une épave.',
                      'Du sable sur la côte à marée basse. Des rides et du sable mou partout, un gap au-dessus d’un chenal de marée, un virage près du phare, un couloir entre les épis et une trajectoire en plein milieu d’une vieille épave.'),
        'ironcut': ('Une carrière désaffectée : lacets sur les terrasses d’extraction, un drop dans la fosse et un dragon’s back sur le bord.',
                    'Ironcut grimpe en lacets de terrasse en terrasse dans une carrière désaffectée. En haut, tu roules sur un dragon’s back le long du bord avant une descente raide qui te ramène au fond de la fosse.'),
        'saltpan': ('Un Grand Prix rapide sur un lac salé, avec le Salt Crust Triple et une table près du convoyeur.',
                    'Large et rapide : Saltpan traverse un lac salé avec de longues lignes droites et des rollers. Les temps forts sont le Salt Crust Triple et une table à côté du convoyeur des salines.'),
        'freeride': ('Carte freeride : lignes de sauts, un step-up, un hip et une fosse en mousse, sans tours ni chrono.',
                     'Pas de tours, pas de chrono, pas d’adversaires. Dust Devil est une carte ouverte avec des lignes de sauts, un step-up, un hip et une fosse en mousse pour t’entraîner aux figures sans conséquences.'),
        'arena': ('Show de freestyle motocross de nuit dans un stade, avec des kickers pour whips, flips et big air.',
                  'Un show de freestyle motocross de nuit dans un stade. Des rampes dédiées aux whips, backflips, Nac-Nacs, Can-Cans et au big air, plus un quarterpipe et un feu d’artifice.'),
    },
    'pt': {
        'sunvale': ('A pista para iniciantes: um parque de MX no campo, com rollers, mesas pequenas e uma travessia de riacho.',
                    'A maioria dos pilotos começa aqui. Curvas largas na grama, rollers e mesas pequenas passam por pastos com vacas e fardos de feno, e um trecho atravessa o riacho. Ótima para aprender o pop e seus primeiros whips.'),
        'larkmeadow': ('Supercross em um estádio à noite: seções de ritmo, whoops, um trecho de areia e um triplo na chegada.',
                       'Uma pista de supercross curta e travada sob os refletores do estádio. Seções de ritmo, whoops e areia vêm uma atrás da outra, e a volta termina com um duplo de SX e um triplo sobre a linha de chegada.'),
        'frostline': ('Pista na neve em uma pista de esqui, ao lado do teleférico e sobre o Frozen Creek Gap.',
                      'Frostline desce uma pista de esqui no inverno: ao lado do teleférico, passando por canhões de neve e sobre o Frozen Creek Gap. Ondulações de neve e um grande salto para a reta final fecham a volta.'),
        'monsoon': ('Uma pista fluida sobre terraços de arroz em uma encosta, com uma sequência de terraços e um aqueduto de madeira.',
                    'Um traçado fluido em uma encosta com terraços. Uma sequência de saltos desce de terraço em terraço, a pista passa pelo bambuzal e acompanha um aqueduto de madeira. Aqui uma linha limpa vale mais do que velocidade pura.'),
        'mirage-flats': ('Parque de saltos no deserto, sobre um lago seco, com um rail gap sobre os trilhos e um longo washboard.',
                         'Um parque de saltos no deserto. Com o Rail Gap você passa por cima da ferrovia, atravessa um washboard no leito do lago seco e termina na mesa Mirage. Muito tempo no ar e pouca margem para erro nas aterrissagens.'),
        'herbst': ('Floresta de outono na luz do fim de tarde, fogo em três saltos, um grande step-up e um grande step-down.',
                   'Uma pista em uma floresta de outono com a luz baixa do fim de tarde. Três saltos têm fogo ao lado, a subida tem um grande step-up e a descida um grande step-down para o vale. No meio, folhas, raízes e seções de ritmo.'),
        'rustleaf': ('Uma pista sinuosa na floresta de outono, com raízes, uma baixada de lama e uma trilha de arraste de toras.',
                     'Estreita e sinuosa: Rustleaf serpenteia pela floresta de outono sobre tapetes de raízes, por uma baixada de lama, ao longo de uma trilha de arraste de toras e ao lado de uma escavadeira. Uma pista para pilotar com precisão, não com o acelerador cravado.'),
        'neonharbor': ('Supercross à noite em um galpão do porto: mesa de contêineres, curva sob o guindaste, whoops do cais e um triplo.',
                       'A segunda pista de supercross fica em um galpão do porto, à noite. Você salta uma mesa feita de contêineres, faz a curva sob um guindaste, encara os whoops do cais e tenta o Harbor Triple.'),
        'pine-ridge': ('Um longo Grande Prêmio na floresta sobre uma crista, com Horsepower Hill, o Stump Double e o Ridge Double.',
                       'Um Grande Prêmio clássico ao ar livre em uma floresta de pinheiros. A pista sobe a Horsepower Hill, percorre a crista sobre raízes e duplos e volta descendo pela floresta. Voltas longas e um grid completo de 12 pilotos.'),
        'sandglass': ('Grande Prêmio em um cânion no deserto: degraus de rocha, mesa no platô, cânion estreito, drop do penhasco e road gap.',
                      'Sandglass leva você por cânions vermelhos no deserto. Degraus e lajes de rocha, uma mesa no alto do platô, um cânion estreito, um drop de um penhasco e um Road Gap sobre a rodovia, depois de volta pelo leito seco passando pelos whoops.'),
        'highcrest': ('Um GP de montanha longo e rápido, com 38 m de desnível, lajes de calcário, zigue-zagues e uma cachoeira.',
                      'A pista ao ar livre mais rápida: Highcrest sobe 38 metros entre floresta e rocha, sobre lajes de calcário e por curvas em zigue-zague até o topo, e depois desce por um portal de rocha e passa por uma cachoeira.'),
        'canopy': ('Floresta tropical em uma baixada: gap sobre um desfiladeiro, ponte pênsil, túnel de árvores, cachoeira e dragon’s back.',
                   'Uma pista sinuosa na floresta tropical, no fundo de uma baixada. Salte um gap sobre um desfiladeiro, cruze uma ponte pênsil, passe por um túnel de árvores e por uma cachoeira e mantenha o equilíbrio no dragon’s back.'),
        'tidewater': ('Um GP técnico na areia, no litoral com a maré baixa, com um gap sobre um canal e uma passagem por um naufrágio.',
                      'Areia no litoral com a maré baixa. Ondulações e areia fofa por toda parte, um gap sobre um canal de maré, uma curva junto ao farol, um corredor entre os espigões e uma linha que passa por dentro de um velho naufrágio.'),
        'ironcut': ('Uma pedreira desativada: zigue-zagues pelas bancadas de extração, um drop para a cava e um dragon’s back na borda.',
                    'Ironcut sobe em zigue-zague de bancada em bancada por uma pedreira desativada. Lá em cima você passa por um dragon’s back ao longo da borda antes de uma descida íngreme de volta para a cava.'),
        'saltpan': ('Um Grande Prêmio rápido sobre um lago de sal, com o Salt Crust Triple e uma mesa junto à esteira.',
                    'Aberta e rápida: Saltpan cruza um lago de sal com retas longas e rollers. Os destaques são o Salt Crust Triple e uma mesa ao lado da esteira transportadora da salina.'),
        'freeride': ('Mapa de freeride: linhas de saltos, um step-up, um hip e um fosso de espuma, sem voltas e sem cronômetro.',
                     'Sem voltas, sem cronômetro, sem adversários. Dust Devil é um mapa aberto com linhas de saltos, um step-up, um hip e um fosso de espuma para treinar manobras sem consequências.'),
        'arena': ('Show noturno de freestyle motocross em um estádio, com rampas para whips, flips e big air.',
                  'Um show de freestyle motocross à noite em um estádio. Rampas próprias para whips, backflips, Nac-Nacs, Can-Cans e big air, além de um quarterpipe e fogos de artifício.'),
    },
}

# ── FAQ (jede Antwort steht für sich, erster Satz = Antwort) ───────────────────────────────────────
FAQ = {
    'en': [
        ('Is MX Royale free?',
         'Yes, MX Royale is completely free to play. There are no ads and no in-game purchases.'),
        ('Is there a free motocross game I can play online without downloading?',
         'Yes. MX Royale is a free motocross and dirt bike game that runs in the browser on PC and phones, with no download and no account.'),
        ('Do I need to download or install MX Royale?',
         'No, MX Royale runs directly in the web browser with no download and no install. It works in Chrome, Edge, Firefox and Safari, and no account is needed to start riding.'),
        ('Can I play MX Royale on my phone?',
         'Yes, MX Royale works on phones and tablets in landscape mode. It has touch controls with a thumb stick, throttle and brake buttons, and optional tilt steering.'),
        ('Does MX Royale support a controller?',
         'Yes, MX Royale supports gamepads. Throttle and brake are on the analog triggers (RT/LT), the left stick steers and whips, and the right stick moves your weight and leans the bike.'),
        ('Can I race my friends online in MX Royale?',
         'Yes, MX Royale has online races with room codes. One player creates a room and shares the 5-character code, the others enter it and the track loads automatically; bots can fill up the field.'),
        ('How many tracks does MX Royale have?',
         'MX Royale has {nr} race tracks and {nf} freeride maps. They include two supercross tracks and outdoor tracks in forest, desert, canyon, snow, rainforest, beach, quarry and salt-lake settings.'),
        ('Is there supercross in MX Royale?',
         'Yes, MX Royale has two supercross tracks: Larkmeadow SX in a night stadium and Neon Harbor SX in a harbour hall. Both have rhythm sections, whoops and triples.'),
        ('Which game modes does MX Royale have?',
         'MX Royale has races against AI riders, time trial with your own ghost, a Daily Challenge, a Championship of four races, freeride, a trick school and online races with friends.'),
        ('Which languages is MX Royale available in?',
         'MX Royale is available in English, German, Spanish, French and Brazilian Portuguese.'),
        ('Is MX Royale like MX Bikes or MX vs ATV?',
         'MX Bikes and MX vs ATV are games you download for PC or consoles. MX Royale is an arcade motocross game that runs free in the browser, with supercross tracks, whips and online races; it is less of a simulator.'),
        ('Who makes MX Royale?',
         'MX Royale is made by three students from Austria who ride motocross themselves. It is a hobby project in open beta.'),
    ],
    'de': [
        ('Ist MX Royale kostenlos?',
         'Ja, MX Royale ist komplett kostenlos. Es gibt keine Werbung und keine In-Game-Käufe.'),
        ('Gibt es ein kostenloses Motocross-Spiel, das man online ohne Download spielen kann?',
         'Ja. MX Royale ist ein kostenloses Motocross- und Dirt-Bike-Spiel, das im Browser am PC und am Handy läuft, ohne Download und ohne Konto.'),
        ('Muss ich MX Royale herunterladen oder installieren?',
         'Nein, MX Royale läuft direkt im Browser, ohne Download und ohne Installation. Es funktioniert in Chrome, Edge, Firefox und Safari, und zum Losfahren braucht es kein Konto.'),
        ('Kann ich MX Royale am Handy spielen?',
         'Ja, MX Royale läuft am Handy und Tablet im Querformat. Es gibt eine Touch-Steuerung mit Daumen-Stick, Gas- und Bremstaste und auf Wunsch Neige-Steuerung.'),
        ('Kann ich MX Royale mit Controller spielen?',
         'Ja, MX Royale unterstützt Gamepads. Gas und Bremse liegen auf den analogen Triggern (RT/LT), der linke Stick lenkt und whippt, der rechte verlagert das Gewicht und kippt das Bike.'),
        ('Kann ich in MX Royale online gegen Freunde fahren?',
         'Ja, MX Royale hat Online-Rennen mit Raum-Code. Einer erstellt einen Raum und schickt den 5-stelligen Code, die anderen geben ihn ein und die Strecke lädt automatisch; Bots können das Feld auffüllen.'),
        ('Wie viele Strecken hat MX Royale?',
         'MX Royale hat {nr} Rennstrecken und {nf} Freeride-Maps. Dazu gehören zwei Supercross-Strecken und Outdoor-Strecken in Wald, Wüste, Canyon, Schnee, Regenwald, am Strand, im Steinbruch und auf einem Salzsee.'),
        ('Gibt es in MX Royale Supercross?',
         'Ja, MX Royale hat zwei Supercross-Strecken: Larkmeadow SX im Nachtstadion und Neon Harbor SX in einer Hafenhalle. Beide haben Rhythmus-Sektionen, Whoops und Triples.'),
        ('Welche Spielmodi hat MX Royale?',
         'MX Royale hat Rennen gegen KI-Fahrer, Zeitfahren gegen den eigenen Geist, eine Tages-Challenge, eine Meisterschaft über vier Rennen, Freeride, eine Trick-Schule und Online-Rennen mit Freunden.'),
        ('In welchen Sprachen gibt es MX Royale?',
         'MX Royale gibt es auf Englisch, Deutsch, Spanisch, Französisch und brasilianischem Portugiesisch.'),
        ('Ist MX Royale wie MX Bikes oder MX vs ATV?',
         'MX Bikes und MX vs ATV sind Spiele zum Herunterladen für PC oder Konsolen. MX Royale ist ein Arcade-Motocross-Spiel, das kostenlos im Browser läuft, mit Supercross-Strecken, Whips und Online-Rennen; eine Simulation ist es weniger.'),
        ('Wer macht MX Royale?',
         'MX Royale machen drei Schüler aus Österreich, die selbst Motocross fahren. Es ist ein Hobbyprojekt in der offenen Beta.'),
    ],
    'es': [
        ('¿MX Royale es gratis?',
         'Sí, MX Royale es completamente gratis. No tiene anuncios ni compras dentro del juego.'),
        ('¿Hay un juego de motocross gratis para jugar online sin descargar?',
         'Sí. MX Royale es un juego de motocross gratis que funciona en el navegador de PC y celular, sin descargas y sin cuenta.'),
        ('¿Tengo que descargar o instalar MX Royale?',
         'No, MX Royale se juega directamente en el navegador, sin descargas ni instalación. Funciona en Chrome, Edge, Firefox y Safari, y no necesitas una cuenta para empezar a correr.'),
        ('¿Puedo jugar MX Royale en el celular?',
         'Sí, MX Royale funciona en celulares y tablets en horizontal. Tiene controles táctiles con un stick para el pulgar, botones de gas y freno, y dirección por inclinación opcional.'),
        ('¿MX Royale es compatible con control?',
         'Sí, MX Royale es compatible con gamepads. El gas y el freno están en los gatillos analógicos (RT/LT), el stick izquierdo dirige y hace whips, y el derecho mueve tu peso e inclina la moto.'),
        ('¿Puedo correr online contra mis amigos en MX Royale?',
         'Sí, MX Royale tiene carreras online con códigos de sala. Un jugador crea una sala y comparte el código de 5 caracteres, los demás lo ingresan y la pista se carga sola; los bots pueden completar la parrilla.'),
        ('¿Cuántas pistas tiene MX Royale?',
         'MX Royale tiene {nr} pistas de carreras y {nf} mapas de freeride. Entre ellas hay dos pistas de supercross y pistas al aire libre en bosque, desierto, cañón, nieve, selva, playa, cantera y un lago salado.'),
        ('¿Hay supercross en MX Royale?',
         'Sí, MX Royale tiene dos pistas de supercross: Larkmeadow SX en un estadio de noche y Neon Harbor SX en una nave del puerto. Ambas tienen secciones de ritmo, whoops y triples.'),
        ('¿Qué modos de juego tiene MX Royale?',
         'MX Royale tiene carreras contra pilotos de la IA, contrarreloj contra tu propio fantasma, un Desafío diario, un Campeonato de cuatro carreras, freeride, una Escuela de trucos y carreras online con amigos.'),
        ('¿En qué idiomas está MX Royale?',
         'MX Royale está disponible en inglés, alemán, español, francés y portugués de Brasil.'),
        ('¿MX Royale es como MX Bikes o MX vs ATV?',
         'MX Bikes y MX vs ATV son juegos que se descargan para PC o consolas. MX Royale es un juego de motocross arcade que funciona gratis en el navegador, con pistas de supercross, whips y carreras online; es menos simulador.'),
        ('¿Quién hace MX Royale?',
         'MX Royale lo hacen tres estudiantes de Austria que también andan en motocross. Es un proyecto personal en beta abierta.'),
    ],
    'fr': [
        ('MX Royale est-il gratuit ?',
         'Oui, MX Royale est entièrement gratuit. Il n’y a ni publicité ni achats dans le jeu.'),
        ('Existe-t-il un jeu de motocross gratuit en ligne sans téléchargement ?',
         'Oui. MX Royale est un jeu de motocross gratuit qui tourne dans le navigateur sur PC et téléphone, sans téléchargement ni compte.'),
        ('Faut-il télécharger ou installer MX Royale ?',
         'Non, MX Royale se joue directement dans le navigateur, sans téléchargement ni installation. Il fonctionne dans Chrome, Edge, Firefox et Safari, et aucun compte n’est nécessaire pour rouler.'),
        ('Peut-on jouer à MX Royale sur téléphone ?',
         'Oui, MX Royale fonctionne sur téléphone et tablette en mode paysage. Les commandes tactiles ont un stick pour le pouce, des boutons de gaz et de frein et, en option, la direction par inclinaison.'),
        ('MX Royale est-il compatible avec une manette ?',
         'Oui, MX Royale prend en charge les manettes. Les gaz et le frein sont sur les gâchettes analogiques (RT/LT), le stick gauche dirige et fait les whips, le stick droit déplace ton poids et incline la moto.'),
        ('Peut-on faire des courses en ligne entre amis dans MX Royale ?',
         'Oui, MX Royale propose des courses en ligne avec code de salon. Un joueur crée un salon et partage le code à 5 caractères, les autres le saisissent et le circuit se charge tout seul ; des bots peuvent compléter la grille.'),
        ('Combien de circuits compte MX Royale ?',
         'MX Royale compte {nr} circuits de course et {nf} cartes freeride. Parmi eux, deux circuits de supercross et des circuits outdoor en forêt, dans le désert, en canyon, sur la neige, en forêt tropicale, à la plage, dans une carrière et sur un lac salé.'),
        ('Y a-t-il du supercross dans MX Royale ?',
         'Oui, MX Royale a deux circuits de supercross : Larkmeadow SX dans un stade de nuit et Neon Harbor SX dans un hangar du port. Les deux ont des sections de rythme, des whoops et des triples.'),
        ('Quels modes de jeu propose MX Royale ?',
         'MX Royale propose des courses contre des pilotes IA, le contre-la-montre contre ton propre fantôme, un Défi du jour, un Championnat de quatre courses, le freeride, une École de figures et des courses en ligne entre amis.'),
        ('En quelles langues MX Royale est-il disponible ?',
         'MX Royale est disponible en anglais, allemand, espagnol, français et portugais du Brésil.'),
        ('MX Royale ressemble-t-il à MX Bikes ou MX vs ATV ?',
         'MX Bikes et MX vs ATV sont des jeux à télécharger sur PC ou consoles. MX Royale est un jeu de motocross arcade gratuit dans le navigateur, avec des circuits de supercross, des whips et des courses en ligne ; c’est moins une simulation.'),
        ('Qui fait MX Royale ?',
         'MX Royale est fait par trois élèves autrichiens qui roulent eux-mêmes en motocross. C’est un projet personnel en bêta ouverte.'),
    ],
    'pt': [
        ('MX Royale é grátis?',
         'Sim, MX Royale é totalmente grátis. Não tem anúncios nem compras dentro do jogo.'),
        ('Existe um jogo de motocross grátis para jogar online sem baixar?',
         'Sim. MX Royale é um jogo de motocross grátis que roda no navegador do PC e do celular, sem download e sem conta.'),
        ('Preciso baixar ou instalar MX Royale?',
         'Não, MX Royale roda direto no navegador, sem download e sem instalação. Funciona no Chrome, Edge, Firefox e Safari, e você não precisa de conta para começar a pilotar.'),
        ('Dá para jogar MX Royale no celular?',
         'Sim, MX Royale funciona em celulares e tablets na horizontal. Tem controles de toque com um stick para o polegar, botões de acelerador e freio e direção por inclinação opcional.'),
        ('MX Royale funciona com controle?',
         'Sim, MX Royale é compatível com controles (gamepad). Acelerador e freio ficam nos gatilhos analógicos (RT/LT), o analógico esquerdo esterça e faz whips, e o direito move o seu peso e inclina a moto.'),
        ('Posso correr online contra meus amigos no MX Royale?',
         'Sim, MX Royale tem corridas online com código de sala. Um jogador cria uma sala e compartilha o código de 5 caracteres, os outros digitam o código e a pista carrega sozinha; bots podem completar o grid.'),
        ('Quantas pistas MX Royale tem?',
         'MX Royale tem {nr} pistas de corrida e {nf} mapas de freeride. Entre elas estão duas pistas de supercross e pistas ao ar livre em floresta, deserto, cânion, neve, floresta tropical, praia, pedreira e um lago de sal.'),
        ('MX Royale tem supercross?',
         'Sim, MX Royale tem duas pistas de supercross: Larkmeadow SX em um estádio à noite e Neon Harbor SX em um galpão do porto. As duas têm seções de ritmo, whoops e triplos.'),
        ('Quais modos de jogo MX Royale tem?',
         'MX Royale tem corridas contra pilotos da IA, contra o relógio contra o seu próprio fantasma, um Desafio diário, um Campeonato de quatro corridas, freeride, uma Escola de manobras e corridas online com amigos.'),
        ('Em quais idiomas MX Royale está disponível?',
         'MX Royale está disponível em inglês, alemão, espanhol, francês e português do Brasil.'),
        ('MX Royale é parecido com MX Bikes ou MX vs ATV?',
         'MX Bikes e MX vs ATV são jogos para baixar no PC ou em consoles. MX Royale é um jogo de motocross arcade que roda grátis no navegador, com pistas de supercross, whips e corridas online; é menos simulador.'),
        ('Quem faz o MX Royale?',
         'MX Royale é feito por três estudantes da Áustria que também andam de motocross. É um projeto pessoal em beta aberto.'),
    ],
}

# ── UI und Seitentexte ─────────────────────────────────────────────────────────────────────────────
TX = {}

TX['en'] = dict(
    lang_name='English', ride='Ride now', nav_tracks='Tracks', nav_how='How to play', nav_about='About', nav_press='Press & creators',
    legal='Legal notice', privacy='Privacy', home='Home', foot_social='Follow us', locale='en_US',
    nav_aria='Main', lang_aria='Language', skip='Skip to content', foot_claim='Free motocross game in your browser.',
    og_alt='MX Royale – motocross game in the browser', track_alt='track in MX Royale',
    # Startseite
    karten=[
        ('{nr} tracks + {nf} freeride maps', 'Supercross stadiums, forest GPs, desert, canyon, snow, beach and a quarry.'),
        ('Race the AI', 'Line up at the gate against up to 11 AI riders, or ride a 4-race Championship.'),
        ('Online with friends', 'Create a room, send the 5-character code and race each other.'),
        ('Time trial & ghosts', 'Chase your best lap or the top ghost, win medals and try the Daily Challenge.'),
        ('Whips, scrubs & flips', 'Backflips, Supermans, Nac-Nacs and Can-Cans. Learn them in the trick school.'),
        ('Phone, PC or controller', 'Touch controls in landscape, keyboard or gamepad. Nothing to install.'),
    ],
    claim='MX Royale – the free motocross game you play online, right in your browser',
    klein='Open beta · no account needed · runs in Chrome, Edge, Firefox and Safari',
    hero_alt='Rider jumping a motocross bike in front of a turquoise lagoon on Tidewater Flats in MX Royale',
    h_get='What you <span>get</span>', h_tracks='The <span>tracks</span>',
    lead_tracks='{nr} race tracks from a beginner MX park to supercross under lights, plus {nf} freeride maps for tricks. New tracks are added during the beta.',
    more_tracks='All tracks in detail →', h_faq='Questions & <span>answers</span>',
    faq_more='New to motocross games? Read <a href="{how}">how to play</a> or the <a href="{about}">fact sheet</a>.',
    h_team='Built by <span>riders</span>',
    team='MX Royale is built by three students who ride themselves. New tracks, tricks and fixes ship every week. Found a bug or got an idea? Write to us: <a href="mailto:feedback@mxroyale.com">feedback@mxroyale.com</a>',
    home_titel='MX Royale – Free Motocross & Dirt Bike Game, No Download',
    home_desc='Play MX Royale, a free motocross and dirt bike game in your browser: no download, on phone, PC or controller. {nr} tracks, supercross, whips, online races.',
    home_og='MX Royale – Motocross in your browser',
    vg_desc=('MX Royale is a free motocross racing game that runs in the web browser. No download, works on PC and phones, '
             'with keyboard, touch or gamepad. {nr} race tracks, {nf} freeride maps, whips, scrubs and flips, '
             'races against AI, time trial with ghosts and online races with friends.'),
    # Strecken
    fakt_feld='Race field: {n} riders', fakt_tt='Time trial with ghost and medals', fakt_free='No laps, no timer, no opponents',
    tracks_h1='Motocross <span>tracks</span>',
    tracks_lead='MX Royale has {nr} race tracks and {nf} freeride maps, all free to ride in your browser. They range from a beginner MX park to two supercross tracks and long outdoor Grand Prix tracks in forest, desert, snow and on the coast.',
    tracks_more='Want to know how whips and scrubs work? Read <a href="{how}">how to play</a>.',
    tracks_titel='Motocross Tracks – Supercross, Desert, Snow | MX Royale',
    tracks_desc='All {nr} race tracks and {nf} freeride maps in MX Royale, the free browser motocross game: supercross, forest GP, desert, snow and beach.',
    tracks_list='MX Royale tracks', tracks_crumb='Tracks',
    # Anleitung
    how_h1='How to <span>play</span>', how_next='Next: pick a track on the <a href="{tracks}">tracks page</a>.',
    how_titel='How to Play MX Royale – Controls, Whips & Scrubs',
    how_desc='How to play the free motocross game MX Royale: keyboard, phone and controller controls, how to whip, scrub and pop, plus tips for faster laps.',
    how_crumb='How to play',
    how_html="""
<p class="lead">MX Royale is easy to start and hard to master. Press <b>Ride now</b>, pick a track and go – the game runs in your browser on PC, Mac, phone or tablet. This page explains the controls for keyboard, phone and controller, and how whips, scrubs and the gate start work.</p>
{ride}
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
""",
    # Über
    about_abs=[
        ('What is MX Royale?', 'MX Royale is a free motocross racing game that runs in the web browser. It needs no download and no account, and it works on PC, Mac, phones and tablets with keyboard, touch controls or a gamepad.'),
        ('What can you do in MX Royale?', 'In MX Royale you race motocross and supercross bikes on {nr} race tracks and {nf} freeride maps. Game modes are races against up to 11 AI riders, time trial against your own ghost with medal times, a Daily Challenge, a Championship of four races, freeride, a trick school and online races with friends via a 5-character room code.'),
        ('Which tracks are there?', 'MX Royale has two supercross tracks ({sx}) and outdoor tracks in forest, desert, canyon, snow, rainforest, beach, quarry and salt-lake settings. The beginner track is Sunvale MX Park.'),
        ('Who makes MX Royale?', 'MX Royale is developed by three students from Austria as a hobby project. The game has been in open beta since 26 November 2026; it has no ads and no in-game purchases.'),
    ],
    about_rows=[
        ('Price', 'Free – no ads, no in-game purchases'), ('Download / install', 'None – runs in the browser'),
        ('Browsers', 'Chrome, Edge, Firefox, Safari'), ('Devices', 'PC, Mac, phones and tablets (landscape)'),
        ('Controls', 'Keyboard (remappable), touch with optional tilt steering, gamepad'),
        ('Single-player modes', 'Race vs. AI, time trial with ghost, Daily Challenge, Championship, freeride, trick school'),
        ('Multiplayer', 'Online races with a 5-character room code; bots can fill the field'),
        ('Tracks', '{nr} race tracks + {nf} freeride maps, including 2 supercross tracks'),
        ('Race field', 'Up to 12 riders (you + AI)'),
        ('Tricks', 'Whips, scrubs, backflips, Superman, Nac-Nac, Can-Can, heel clicker, seat grab, cliffhanger'),
        ('Bikes', '450 four-stroke, 250 two-stroke and electric'),
        ('Rider aids', 'Five levels: Beginner, Normal, Sport, Pro, Sim'),
        ('Languages', 'English, German, Spanish, French, Brazilian Portuguese'),
        ('Account', 'Optional'), ('Status', 'Open beta since 26 November 2026'),
        ('Developer', 'Three students from Austria'), ('Website', 'mxroyale.com'), ('Play', 'play.mxroyale.com'),
    ],
    about_h1='MX Royale <span>fact sheet</span>', about_stand='Last updated: {stand}', about_tab='Feature overview',
    about_more='More: <a href="{tracks}">all tracks</a> · <a href="{how}">how to play</a> · <a href="{press}">press kit</a> · <a href="/llms.txt">llms.txt</a>',
    about_titel='About MX Royale – Fact Sheet of the Browser Motocross Game',
    about_desc='Fact sheet: MX Royale is a free motocross racing game in the web browser. Platforms, controls, modes, tracks, languages and status at a glance.',
    about_crumb='About',
    claim_sub='No download, on PC, phone and controller.',
    get_lead='Race dirt bikes on {nr} motocross and supercross tracks, against the AI or online with friends – free, in any modern browser.',
)

TX['de'] = dict(
    lang_name='Deutsch', ride='Jetzt fahren', nav_tracks='Strecken', nav_how='Anleitung', nav_about='Über das Spiel', nav_press='Presse & Creator',
    legal='Impressum', privacy='Datenschutz', home='Start', foot_social='Folg uns', locale='de_DE',
    nav_aria='Hauptmenü', lang_aria='Sprache', skip='Zum Inhalt', foot_claim='Gratis Motocross-Spiel im Browser.',
    og_alt='MX Royale – Motocross-Spiel im Browser', track_alt='Strecke in MX Royale',
    karten=[
        ('{nr} Strecken + {nf} Freeride-Maps', 'Supercross-Hallen, Wald-GPs, Wüste, Canyon, Schnee, Strand und Steinbruch.'),
        ('Rennen gegen die KI', 'Gatterstart gegen bis zu 11 KI-Fahrer oder eine Meisterschaft über 4 Rennen.'),
        ('Online mit Freunden', 'Raum erstellen, 5-stelligen Code schicken und gegeneinander fahren.'),
        ('Zeitfahren & Geist', 'Jag deine Bestzeit oder den Geist von Platz 1, hol Medaillen und die Tages-Challenge.'),
        ('Whips, Scrubs & Flips', 'Backflip, Superman, Nac-Nac und Can-Can. Lernen kannst du sie in der Trick-Schule.'),
        ('Handy, PC oder Controller', 'Touch-Steuerung im Querformat, Tastatur oder Gamepad. Nichts zu installieren.'),
    ],
    claim='MX Royale – das kostenlose Motocross-Spiel, online direkt im Browser',
    klein='Offene Beta · kein Konto nötig · läuft in Chrome, Edge, Firefox und Safari',
    hero_alt='Fahrer springt mit dem Motocross-Bike vor einer türkisen Lagune auf Tidewater Flats in MX Royale',
    h_get='Was dich <span>erwartet</span>', h_tracks='Die <span>Strecken</span>',
    lead_tracks='{nr} Rennstrecken vom Einsteiger-MX-Park bis zum Supercross unter Flutlicht, dazu {nf} Freeride-Maps für Tricks. In der Beta kommen laufend neue dazu.',
    more_tracks='Alle Strecken im Detail →', h_faq='Fragen & <span>Antworten</span>',
    faq_more='Neu bei Motocross-Spielen? Lies die <a href="{how}">Anleitung</a> oder das <a href="{about}">Faktenblatt</a>.',
    h_team='Von Ridern <span>gebaut</span>',
    team='MX Royale bauen drei Schüler, die selbst fahren. Jede Woche kommen neue Strecken, Tricks und Fixes dazu. Fehler gefunden oder eine Idee? Schreib uns: <a href="mailto:feedback@mxroyale.com">feedback@mxroyale.com</a>',
    home_titel='MX Royale – Motocross-Spiel kostenlos online im Browser',
    home_desc='Motocross Browserspiel, kostenlos und ohne Download: am Handy, PC oder mit Controller. {nr} Strecken, Supercross, Whips und Online-Rennen.',
    home_og='MX Royale – Motocross im Browser',
    vg_desc=('MX Royale ist ein kostenloses Motocross-Rennspiel, das im Browser läuft. Ohne Download, am PC und am Handy, '
             'mit Tastatur, Touch oder Gamepad. {nr} Rennstrecken, {nf} Freeride-Maps, Whips, Scrubs und Flips, '
             'Rennen gegen die KI, Zeitfahren mit Geist und Online-Rennen mit Freunden.'),
    fakt_feld='Starterfeld: {n} Fahrer', fakt_tt='Zeitfahren mit Geist und Medaillen', fakt_free='Ohne Runden, Uhr und Gegner',
    tracks_h1='Motocross-<span>Strecken</span>',
    tracks_lead='MX Royale hat {nr} Rennstrecken und {nf} Freeride-Maps, alle kostenlos im Browser fahrbar. Vom Einsteiger-MX-Park über zwei Supercross-Strecken bis zu langen Outdoor-Grand-Prix in Wald, Wüste, Schnee und an der Küste.',
    tracks_more='Wie Whips und Scrubs gehen, steht in der <a href="{how}">Anleitung</a>.',
    tracks_titel='Motocross-Strecken – Supercross, Wüste, Schnee | MX Royale',
    tracks_desc='Alle {nr} Strecken und {nf} Freeride-Maps von MX Royale, dem Motocross Browserspiel: Supercross, Wald-GP, Wüste, Schnee und Strand.',
    tracks_list='MX-Royale-Strecken', tracks_crumb='Strecken',
    how_h1='So wird <span>gespielt</span>', how_next='Weiter: Such dir eine Strecke auf der <a href="{tracks}">Strecken-Seite</a> aus.',
    how_titel='MX Royale Anleitung – Steuerung, Whips & Scrubs',
    how_desc='So spielst du das Motocross Browserspiel MX Royale: Steuerung für Tastatur, Handy und Controller, Whip, Scrub, Pop und Tipps für schnellere Runden.',
    how_crumb='Anleitung',
    how_html="""
<p class="lead">MX Royale ist schnell gelernt und schwer zu meistern. Auf <b>Jetzt fahren</b> tippen, Strecke wählen, los – das Spiel läuft im Browser am PC, Mac, Handy oder Tablet. Hier steht die Steuerung für Tastatur, Handy und Controller und wie Whips, Scrubs und der Gatterstart gehen.</p>
{ride}
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
""",
    about_abs=[
        ('Was ist MX Royale?', 'MX Royale ist ein kostenloses Motocross-Rennspiel, das im Webbrowser läuft. Es braucht keinen Download und kein Konto und läuft am PC, Mac, Handy und Tablet mit Tastatur, Touch-Steuerung oder Gamepad.'),
        ('Was kann man in MX Royale machen?', 'In MX Royale fährst du Motocross und Supercross auf {nr} Rennstrecken und {nf} Freeride-Maps. Spielmodi sind Rennen gegen bis zu 11 KI-Fahrer, Zeitfahren gegen den eigenen Geist mit Medaillenzeiten, eine Tages-Challenge, eine Meisterschaft über vier Rennen, Freeride, eine Trick-Schule und Online-Rennen mit Freunden über einen 5-stelligen Raum-Code.'),
        ('Welche Strecken gibt es?', 'MX Royale hat zwei Supercross-Strecken ({sx}) und Outdoor-Strecken in Wald, Wüste, Canyon, Schnee, Regenwald, am Strand, im Steinbruch und auf einem Salzsee. Die Einsteiger-Strecke ist Sunvale MX Park.'),
        ('Wer macht MX Royale?', 'MX Royale entwickeln drei Schüler aus Österreich als Hobbyprojekt. Das Spiel ist seit 26. November 2026 in der offenen Beta; es hat keine Werbung und keine In-Game-Käufe.'),
    ],
    about_rows=[
        ('Preis', 'Kostenlos – keine Werbung, keine In-Game-Käufe'), ('Download / Installation', 'Keine – läuft im Browser'),
        ('Browser', 'Chrome, Edge, Firefox, Safari'), ('Geräte', 'PC, Mac, Handy und Tablet (Querformat)'),
        ('Steuerung', 'Tastatur (frei belegbar), Touch mit optionaler Neige-Steuerung, Gamepad'),
        ('Einzelspieler', 'Rennen gegen KI, Zeitfahren mit Geist, Tages-Challenge, Meisterschaft, Freeride, Trick-Schule'),
        ('Mehrspieler', 'Online-Rennen mit 5-stelligem Raum-Code; Bots können das Feld auffüllen'),
        ('Strecken', '{nr} Rennstrecken + {nf} Freeride-Maps, davon 2 Supercross-Strecken'),
        ('Starterfeld', 'Bis zu 12 Fahrer (du + KI)'),
        ('Tricks', 'Whips, Scrubs, Backflip, Superman, Nac-Nac, Can-Can, Heel Clicker, Seat Grab, Cliffhanger'),
        ('Bikes', '450er-Viertakter, 250er-Zweitakter und Elektro'),
        ('Fahrhilfen', 'Fünf Stufen: Einsteiger, Normal, Sport, Pro, Sim'),
        ('Sprachen', 'Englisch, Deutsch, Spanisch, Französisch, brasilianisches Portugiesisch'),
        ('Konto', 'Optional'), ('Status', 'Offene Beta seit 26. November 2026'),
        ('Entwickler', 'Drei Schüler aus Österreich'), ('Website', 'mxroyale.com'), ('Spielen', 'play.mxroyale.com'),
    ],
    about_h1='MX Royale <span>Faktenblatt</span>', about_stand='Zuletzt aktualisiert: {stand}', about_tab='Funktionen im Überblick',
    about_more='Mehr: <a href="{tracks}">alle Strecken</a> · <a href="{how}">Anleitung</a> · <a href="{press}">Pressematerial</a>',
    about_titel='Über MX Royale – Faktenblatt zum Motocross Browserspiel',
    about_desc='Faktenblatt: MX Royale ist ein kostenloses Motocross-Rennspiel im Browser. Geräte, Steuerung, Modi, Strecken, Sprachen und Status im Überblick.',
    about_crumb='Über das Spiel',
    claim_sub='Ohne Download, am PC, am Handy und mit Controller.',
    get_lead='Fahr Motocross-Bikes auf {nr} Motocross- und Supercross-Strecken, gegen die KI oder online mit Freunden – kostenlos, in jedem aktuellen Browser.',
)

TX['es'] = dict(
    lang_name='Español', ride='Jugar ahora', nav_tracks='Pistas', nav_how='Cómo jugar', nav_about='Acerca de', nav_press='Prensa y creadores',
    legal='Aviso legal', privacy='Privacidad', home='Inicio', foot_social='Síguenos', locale='es_LA',
    nav_aria='Principal', lang_aria='Idioma', skip='Ir al contenido', foot_claim='Juego de motocross gratis en tu navegador.',
    og_alt='MX Royale – juego de motocross en el navegador', track_alt='pista en MX Royale',
    karten=[
        ('{nr} pistas + {nf} mapas de freeride', 'Estadios de supercross, GP en el bosque, desierto, cañón, nieve, playa y una cantera.'),
        ('Corre contra la IA', 'Sal desde la reja contra hasta 11 pilotos de la IA o corre un Campeonato de 4 carreras.'),
        ('Online con amigos', 'Crea una sala, manda el código de 5 caracteres y compitan entre ustedes.'),
        ('Contrarreloj y fantasmas', 'Persigue tu mejor vuelta o al mejor fantasma, gana medallas y prueba el Desafío diario.'),
        ('Whips, scrubs y flips', 'Backflips, Supermans, Nac-Nacs y Can-Cans. Apréndelos en la Escuela de trucos.'),
        ('Celular, PC o control', 'Controles táctiles en horizontal, teclado o gamepad. Nada que instalar.'),
    ],
    claim='MX Royale: el juego de motocross gratis para jugar online, directo en tu navegador',
    klein='Beta abierta · sin cuenta · funciona en Chrome, Edge, Firefox y Safari',
    hero_alt='Piloto saltando con su moto de motocross frente a una laguna turquesa en Tidewater Flats en MX Royale',
    h_get='Qué te <span>espera</span>', h_tracks='Las <span>pistas</span>',
    lead_tracks='{nr} pistas de carreras, desde un parque de MX para principiantes hasta supercross bajo los reflectores, y {nf} mapas de freeride para trucos. Durante la beta se suman pistas nuevas.',
    more_tracks='Todas las pistas en detalle →', h_faq='Preguntas y <span>respuestas</span>',
    faq_more='¿Nuevo en los juegos de motocross? Lee <a href="{how}">cómo jugar</a> o la <a href="{about}">ficha técnica</a>.',
    h_team='Hecho por <span>pilotos</span>',
    team='MX Royale lo hacen tres estudiantes que también andan en moto. Cada semana llegan pistas, trucos y correcciones nuevas. ¿Encontraste un error o tienes una idea? Escríbenos (en inglés o alemán): <a href="mailto:feedback@mxroyale.com">feedback@mxroyale.com</a>',
    home_titel='MX Royale – Juego de motocross gratis online, sin descargar',
    home_desc='Juego de motocross gratis en el navegador: sin descargas, en celular, PC o con control. {nr} pistas, supercross, whips y carreras online con amigos.',
    home_og='MX Royale – Motocross en tu navegador',
    vg_desc=('MX Royale es un juego de carreras de motocross gratis que se juega en el navegador. Sin descargas, en PC y celular, '
             'con teclado, controles táctiles o gamepad. {nr} pistas de carreras, {nf} mapas de freeride, whips, scrubs y flips, '
             'carreras contra la IA, contrarreloj con fantasma y carreras online con amigos.'),
    fakt_feld='Parrilla: {n} pilotos', fakt_tt='Contrarreloj con fantasma y medallas', fakt_free='Sin vueltas, sin cronómetro, sin rivales',
    tracks_h1='Pistas de <span>motocross</span>',
    tracks_lead='MX Royale tiene {nr} pistas de carreras y {nf} mapas de freeride, todos gratis en tu navegador. Van desde un parque de MX para principiantes hasta dos pistas de supercross y largos Grandes Premios al aire libre en bosque, desierto, nieve y en la costa.',
    tracks_more='¿Quieres saber cómo se hacen los whips y los scrubs? Lee <a href="{how}">cómo jugar</a>.',
    tracks_titel='Pistas de motocross: supercross, desierto, nieve | MX Royale',
    tracks_desc='Las {nr} pistas y {nf} mapas de freeride de MX Royale, el juego de motocross gratis en el navegador: supercross, GP en el bosque, desierto y nieve.',
    tracks_list='Pistas de MX Royale', tracks_crumb='Pistas',
    how_h1='Cómo <span>jugar</span>', how_next='Siguiente: elige una pista en la <a href="{tracks}">página de pistas</a>.',
    how_titel='Cómo jugar MX Royale – Controles, whips y scrubs',
    how_desc='Cómo jugar el juego de motocross gratis MX Royale: controles de teclado, celular y control, cómo hacer whip, scrub y pop, y consejos para ir más rápido.',
    how_crumb='Cómo jugar',
    how_html="""
<p class="lead">MX Royale es fácil de empezar y difícil de dominar. Toca <b>Jugar ahora</b>, elige una pista y arranca: el juego funciona en el navegador de tu PC, Mac, celular o tablet. Aquí te explicamos los controles de teclado, celular y control, y cómo funcionan los whips, los scrubs y la largada desde la reja.</p>
{ride}
<h2>Teclado</h2>
<div class="tabelle"><table>
<tr><th><kbd>W</kbd> / <kbd>S</kbd></th><td>Gas / freno</td></tr>
<tr><th><kbd>A</kbd> / <kbd>D</kbd></th><td>Dirigir · en el aire: whip</td></tr>
<tr><th><kbd>←</kbd> / <kbd>→</kbd></th><td>Inclinar la moto · en la rampa: scrub · en el aire: acostarla</td></tr>
<tr><th><kbd>↑</kbd> / <kbd>↓</kbd></th><td>Peso adelante / atrás · stoppie / wheelie</td></tr>
<tr><th><kbd>Espacio</kbd></th><td>Agacharse / pop · en freeride: trucos junto con las flechas</td></tr>
<tr><th><kbd>Shift</kbd></th><td>Freno trasero</td></tr>
<tr><th><kbd>R</kbd></th><td>Reaparecer en la pista</td></tr>
<tr><th><kbd>C</kbd> · <kbd>Q</kbd> · <kbd>G</kbd> · <kbd>Esc</kbd></th><td>Cámara · mirar atrás (mantener) · fantasma sí/no · pausa</td></tr>
</table></div>
<p class="klein">Puedes cambiar todas las teclas de manejo en Ajustes.</p>
<h2>Celular y tablet</h2>
<ul>
<li>Gira el celular a <b>horizontal</b>.</li>
<li><b>Pulgar izquierdo:</b> aparece un stick donde tocas. Izquierda/derecha dirige (y hace whip en el aire), arriba/abajo mueve tu peso.</li>
<li><b>Pulgar derecho:</b> mantén <b>GAS</b>; el freno está a su izquierda. Desliza a la izquierda/derecha sobre el gas para inclinar la moto (scrub), desliza hacia abajo para cargar la suspensión y suelta en el labio para hacer el pop.</li>
<li>Arriba a la derecha: cámara, reaparecer, pausa. ¿Prefieres inclinar el celular? Activa la inclinación en Ajustes → Dirección en celular.</li>
<li>En los niveles Principiante y Normal el piloto hace el pop en los saltos por ti.</li>
</ul>
<h2>Control (gamepad)</h2>
<ul>
<li><b>RT</b> gas, <b>LT</b> freno (ambos analógicos).</li>
<li><b>Stick izquierdo</b>: dirige y hace whip en el aire.</li>
<li><b>Stick derecho</b>: ↕ mueve tu peso, ↔ inclina la moto (scrub, acostarla).</li>
<li><b>A</b> agacharse/pop · <b>X</b> freno trasero · <b>Y</b> reaparecer · <b>Start</b> pausa.</li>
<li>Trucos en freeride: en el aire mantén <b>LB</b> o <b>RB</b> y usa el stick izquierdo; LB + RB = sin manos.</li>
</ul>
<h2>Cómo hacer un whip</h2>
<p>Con un whip tiras la moto de lado en el aire. Gira justo antes del labio (<kbd>A</kbd>/<kbd>D</kbd>, stick izquierdo o el stick táctil), mantenlo en el aire y suelta más o menos medio segundo antes de aterrizar para que la moto vuelva derecha. Cuanto mejor el timing, más lejos llega el whip: con buen timing, más de 180°. Un whip cuenta desde 40°.</p>
<h2>Cómo hacer un scrub</h2>
<p>Un scrub te mantiene bajo sobre el salto, así vuelves antes al suelo y vas más rápido en carrera. Acuesta la moto en la cara de la rampa (<kbd>←</kbd>/<kbd>→</kbd>, stick derecho o deslizando sobre el gas) y enderézala antes del final del labio; si no, la rueda delantera se engancha.</p>
<h2>Pop y largada desde la reja</h2>
<p><b>Pop:</b> agáchate en la rampa y suelta en el labio para saltar más alto y más lejos. <b>Largada:</b> desde el cartel “5” mantén gas y freno a la vez para subir las revoluciones y suelta el freno cuando cae la reja. Dar gas sin freno antes de eso es salida en falso.</p>
<h2>Trucos y Escuela de trucos</h2>
<p>En freeride y en la Escuela de trucos puedes hacer backflips, Supermans, Nac-Nacs, heel clickers, Can-Cans, seat grabs y cliffhangers. La Escuela de trucos te enseña cada uno paso a paso para teclado, celular y control, y te dice qué salió mal.</p>
<h2>Consejos para vueltas más rápidas</h2>
<ul>
<li>Aterriza en la bajada detrás del salto para mantener la velocidad.</li>
<li>Cortar camino no sirve: si te sales de la pista, la vuelta no cuenta.</li>
<li>¿Te trabaste? Reaparecer te devuelve al recorrido.</li>
<li>Empieza con Sunvale MX Park, la pista para principiantes, y cambia las ayudas (Principiante, Normal, Sport, Pro, Sim) en Ajustes cuando vayas más rápido.</li>
<li>En contrarreloj tu mejor vuelta corre contigo como fantasma: compite contra ella hasta superar los tiempos de medalla.</li>
<li>Cuatro cámaras: persecución dinámica, persecución clásica, dron y casco.</li>
</ul>
""",
    about_abs=[
        ('¿Qué es MX Royale?', 'MX Royale es un juego de carreras de motocross gratis que se juega en el navegador. No necesita descargas ni cuenta, y funciona en PC, Mac, celulares y tablets con teclado, controles táctiles o gamepad.'),
        ('¿Qué se puede hacer en MX Royale?', 'En MX Royale corres con motos de motocross y supercross en {nr} pistas de carreras y {nf} mapas de freeride. Los modos son carreras contra hasta 11 pilotos de la IA, contrarreloj contra tu propio fantasma con tiempos de medalla, un Desafío diario, un Campeonato de cuatro carreras, freeride, una Escuela de trucos y carreras online con amigos mediante un código de sala de 5 caracteres.'),
        ('¿Qué pistas hay?', 'MX Royale tiene dos pistas de supercross ({sx}) y pistas al aire libre en bosque, desierto, cañón, nieve, selva, playa, cantera y un lago salado. La pista para principiantes es Sunvale MX Park.'),
        ('¿Quién hace MX Royale?', 'MX Royale lo desarrollan tres estudiantes de Austria como proyecto personal. El juego está en beta abierta desde el 26 de noviembre de 2026; no tiene anuncios ni compras dentro del juego.'),
    ],
    about_rows=[
        ('Precio', 'Gratis: sin anuncios ni compras dentro del juego'), ('Descarga / instalación', 'Ninguna: funciona en el navegador'),
        ('Navegadores', 'Chrome, Edge, Firefox, Safari'), ('Dispositivos', 'PC, Mac, celulares y tablets (horizontal)'),
        ('Controles', 'Teclado (configurable), táctil con inclinación opcional, gamepad'),
        ('Un jugador', 'Carrera contra la IA, contrarreloj con fantasma, Desafío diario, Campeonato, freeride, Escuela de trucos'),
        ('Multijugador', 'Carreras online con código de sala de 5 caracteres; los bots pueden completar la parrilla'),
        ('Pistas', '{nr} pistas de carreras + {nf} mapas de freeride, incluidas 2 de supercross'),
        ('Parrilla', 'Hasta 12 pilotos (tú + IA)'),
        ('Trucos', 'Whips, scrubs, backflips, Superman, Nac-Nac, Can-Can, heel clicker, seat grab, cliffhanger'),
        ('Motos', '450 de cuatro tiempos, 250 de dos tiempos y eléctrica'),
        ('Ayudas', 'Cinco niveles: Principiante, Normal, Sport, Pro, Sim'),
        ('Idiomas', 'Inglés, alemán, español, francés, portugués de Brasil'),
        ('Cuenta', 'Opcional'), ('Estado', 'Beta abierta desde el 26 de noviembre de 2026'),
        ('Desarrollo', 'Tres estudiantes de Austria'), ('Sitio web', 'mxroyale.com'), ('Jugar', 'play.mxroyale.com'),
    ],
    about_h1='Ficha de <span>MX Royale</span>', about_stand='Última actualización: {stand}', about_tab='Resumen de funciones',
    about_more='Más: <a href="{tracks}">todas las pistas</a> · <a href="{how}">cómo jugar</a> · <a href="{press}">kit de prensa (en inglés)</a>',
    about_titel='Acerca de MX Royale – Ficha del juego de motocross',
    about_desc='Ficha técnica: MX Royale es un juego de motocross gratis en el navegador. Plataformas, controles, modos, pistas, idiomas y estado de un vistazo.',
    about_crumb='Acerca de',
    claim_sub='Sin descargas, en PC, celular y con control.',
    get_lead='Corre en motos de cross por {nr} pistas de motocross y supercross, contra la IA u online con amigos, gratis y en cualquier navegador actual.',
)

TX['fr'] = dict(
    lang_name='Français', ride='Jouer', nav_tracks='Circuits', nav_how='Comment jouer', nav_about='À propos', nav_press='Presse & créateurs',
    legal='Mentions légales', privacy='Confidentialité', home='Accueil', foot_social='Suis-nous', locale='fr_FR',
    nav_aria='Menu principal', lang_aria='Langue', skip='Aller au contenu', foot_claim='Jeu de motocross gratuit dans ton navigateur.',
    og_alt='MX Royale – jeu de motocross dans le navigateur', track_alt='circuit dans MX Royale',
    karten=[
        ('{nr} circuits + {nf} cartes freeride', 'Stades de supercross, GP en forêt, désert, canyon, neige, plage et une carrière.'),
        ('Course contre l’IA', 'Pars de la grille contre jusqu’à 11 pilotes IA, ou dispute un Championnat de 4 courses.'),
        ('En ligne entre amis', 'Crée un salon, envoie le code à 5 caractères et affrontez-vous.'),
        ('Contre-la-montre & fantômes', 'Chasse ton meilleur tour ou le meilleur fantôme, gagne des médailles et tente le Défi du jour.'),
        ('Whips, scrubs & flips', 'Backflips, Supermans, Nac-Nacs et Can-Cans. Apprends-les à l’École de figures.'),
        ('Téléphone, PC ou manette', 'Commandes tactiles en paysage, clavier ou manette. Rien à installer.'),
    ],
    claim='MX Royale, le jeu de motocross gratuit en ligne, directement dans ton navigateur',
    klein='Bêta ouverte · sans compte · fonctionne dans Chrome, Edge, Firefox et Safari',
    hero_alt='Pilote sautant avec sa moto de motocross devant un lagon turquoise à Tidewater Flats dans MX Royale',
    h_get='Ce qui <span>t’attend</span>', h_tracks='Les <span>circuits</span>',
    lead_tracks='{nr} circuits de course, d’un parc MX pour débutants au supercross sous les projecteurs, plus {nf} cartes freeride pour les figures. De nouveaux circuits arrivent pendant la bêta.',
    more_tracks='Tous les circuits en détail →', h_faq='Questions & <span>réponses</span>',
    faq_more='Nouveau dans les jeux de motocross ? Lis <a href="{how}">comment jouer</a> ou la <a href="{about}">fiche du jeu</a>.',
    h_team='Fait par des <span>pilotes</span>',
    team='MX Royale est développé par trois élèves qui roulent eux-mêmes. Chaque semaine arrivent de nouveaux circuits, figures et correctifs. Un bug ou une idée ? Écris-nous (en anglais ou en allemand) : <a href="mailto:feedback@mxroyale.com">feedback@mxroyale.com</a>',
    home_titel='MX Royale – Jeu de motocross gratuit dans le navigateur',
    home_desc='Jeu de motocross gratuit dans le navigateur : sans téléchargement, sur téléphone, PC ou manette. {nr} circuits, supercross, whips et courses en ligne.',
    home_og='MX Royale – Le motocross dans ton navigateur',
    vg_desc=('MX Royale est un jeu de course de motocross gratuit qui se joue dans le navigateur. Sans téléchargement, sur PC et téléphone, '
             'au clavier, en tactile ou à la manette. {nr} circuits de course, {nf} cartes freeride, whips, scrubs et flips, '
             'courses contre l’IA, contre-la-montre avec fantôme et courses en ligne entre amis.'),
    fakt_feld='Grille : {n} pilotes', fakt_tt='Contre-la-montre avec fantôme et médailles', fakt_free='Pas de tours, pas de chrono, pas d’adversaires',
    tracks_h1='Circuits de <span>motocross</span>',
    tracks_lead='MX Royale compte {nr} circuits de course et {nf} cartes freeride, tous gratuits dans ton navigateur. Ils vont d’un parc MX pour débutants à deux circuits de supercross et de longs Grands Prix outdoor en forêt, dans le désert, sur la neige et sur la côte.',
    tracks_more='Tu veux savoir comment faire un whip ou un scrub ? Lis <a href="{how}">comment jouer</a>.',
    tracks_titel='Circuits motocross – supercross, désert, neige | MX Royale',
    tracks_desc='Les {nr} circuits et {nf} cartes freeride de MX Royale, le jeu de motocross gratuit dans le navigateur : supercross, GP en forêt, désert et neige.',
    tracks_list='Circuits de MX Royale', tracks_crumb='Circuits',
    how_h1='Comment <span>jouer</span>', how_next='Ensuite : choisis un circuit sur la <a href="{tracks}">page des circuits</a>.',
    how_titel='Comment jouer à MX Royale – Commandes, whips, scrubs',
    how_desc='Comment jouer au jeu de motocross gratuit MX Royale : commandes clavier, téléphone et manette, whip, scrub et pop, et astuces pour des tours plus rapides.',
    how_crumb='Comment jouer',
    how_html="""
<p class="lead">MX Royale est facile à prendre en main et difficile à maîtriser. Appuie sur <b>Jouer</b>, choisis un circuit et c’est parti : le jeu tourne dans le navigateur sur PC, Mac, téléphone ou tablette. Cette page explique les commandes au clavier, sur téléphone et à la manette, et comment marchent les whips, les scrubs et le départ derrière la grille.</p>
{ride}
<h2>Clavier</h2>
<div class="tabelle"><table>
<tr><th><kbd>W</kbd> / <kbd>S</kbd></th><td>Gaz / frein</td></tr>
<tr><th><kbd>A</kbd> / <kbd>D</kbd></th><td>Diriger · en l’air : whip</td></tr>
<tr><th><kbd>←</kbd> / <kbd>→</kbd></th><td>Incliner la moto · sur la rampe : scrub · en l’air : la coucher</td></tr>
<tr><th><kbd>↑</kbd> / <kbd>↓</kbd></th><td>Poids vers l’avant / l’arrière · stoppie / wheelie</td></tr>
<tr><th><kbd>Espace</kbd></th><td>S’accroupir / pop · en freeride : figures avec les flèches</td></tr>
<tr><th><kbd>Maj</kbd></th><td>Frein arrière</td></tr>
<tr><th><kbd>R</kbd></th><td>Revenir sur la piste</td></tr>
<tr><th><kbd>C</kbd> · <kbd>Q</kbd> · <kbd>G</kbd> · <kbd>Échap</kbd></th><td>Caméra · regarder derrière (maintenir) · fantôme oui/non · pause</td></tr>
</table></div>
<p class="klein">Tu peux changer toutes les touches de pilotage dans Options. Les touches suivent leur position sur le clavier : sur un clavier AZERTY, W/A/S/D correspondent à Z/Q/S/D.</p>
<h2>Téléphone et tablette</h2>
<ul>
<li>Tourne le téléphone en mode <b>paysage</b>.</li>
<li><b>Pouce gauche :</b> un stick apparaît là où tu touches. Gauche/droite dirige (et fait le whip en l’air), haut/bas déplace ton poids.</li>
<li><b>Pouce droit :</b> maintiens <b>GAS</b>, le frein est juste à gauche. Glisse à gauche/droite sur les gaz pour incliner la moto (scrub), glisse vers le bas pour charger la suspension et relâche au bord du saut pour le pop.</li>
<li>En haut à droite : caméra, retour sur la piste, pause. Tu préfères incliner ? Active l’inclinaison dans Options → Direction mobile.</li>
<li>Aux niveaux Débutant et Normal, le pilote fait le pop tout seul sur les sauts.</li>
</ul>
<h2>Manette</h2>
<ul>
<li><b>RT</b> gaz, <b>LT</b> frein (tous deux analogiques).</li>
<li><b>Stick gauche</b> : diriger et faire le whip en l’air.</li>
<li><b>Stick droit</b> : ↕ déplace ton poids, ↔ incline la moto (scrub, la coucher).</li>
<li><b>A</b> s’accroupir/pop · <b>X</b> frein arrière · <b>Y</b> retour sur la piste · <b>Start</b> pause.</li>
<li>Figures en freeride : en l’air, maintiens <b>LB</b> ou <b>RB</b> et utilise le stick gauche ; LB + RB = sans les mains.</li>
</ul>
<h2>Faire un whip</h2>
<p>Un whip jette la moto de travers en l’air. Braque juste avant le bord du saut (<kbd>A</kbd>/<kbd>D</kbd>, stick gauche ou stick tactile), garde la position en l’air et relâche environ une demi-seconde avant la réception pour que la moto revienne droite. Plus le timing est bon, plus le whip est grand : au-delà de 180° si tu le réussis. Un whip compte à partir de 40°.</p>
<h2>Faire un scrub</h2>
<p>Un scrub te garde bas au-dessus du saut : tu retouches le sol plus tôt et tu vas plus vite en course. Couche la moto sur la face de la rampe (<kbd>←</kbd>/<kbd>→</kbd>, stick droit ou en glissant sur les gaz) et redresse-la avant la fin du bord, sinon la roue avant accroche.</p>
<h2>Pop et départ derrière la grille</h2>
<p><b>Pop :</b> accroupis-toi sur la rampe et relâche au bord pour sauter plus haut et plus loin. <b>Départ :</b> dès le panneau « 5 », maintiens gaz et frein ensemble pour monter les tours, puis lâche le frein quand la grille tombe. Accélérer sans frein avant, c’est un faux départ.</p>
<h2>Figures et École de figures</h2>
<p>En freeride et à l’École de figures, tu peux faire des backflips, Supermans, Nac-Nacs, heel clickers, Can-Cans, seat grabs et cliffhangers. L’École de figures t’apprend chacune pas à pas au clavier, sur téléphone et à la manette, et te dit ce qui n’a pas marché.</p>
<h2>Astuces pour des tours plus rapides</h2>
<ul>
<li>Pose-toi dans la pente derrière le saut pour garder ta vitesse.</li>
<li>Couper ne sert à rien : si tu quittes la piste, le tour ne compte pas.</li>
<li>Bloqué ? Le retour sur la piste te remet sur le parcours.</li>
<li>Commence par Sunvale MX Park, le circuit débutant, et change les aides (Débutant, Normal, Sport, Pro, Sim) dans Options quand tu vas plus vite.</li>
<li>En contre-la-montre, ton meilleur tour roule avec toi en fantôme : bats-le jusqu’à décrocher les temps des médailles.</li>
<li>Quatre caméras : poursuite dynamique, poursuite classique, drone et casque.</li>
</ul>
""",
    about_abs=[
        ('Qu’est-ce que MX Royale ?', 'MX Royale est un jeu de course de motocross gratuit qui se joue dans le navigateur. Il ne demande ni téléchargement ni compte, et fonctionne sur PC, Mac, téléphones et tablettes au clavier, en tactile ou à la manette.'),
        ('Que peut-on faire dans MX Royale ?', 'Dans MX Royale, tu pilotes des motos de motocross et de supercross sur {nr} circuits de course et {nf} cartes freeride. Les modes de jeu sont la course contre jusqu’à 11 pilotes IA, le contre-la-montre contre ton propre fantôme avec des temps de médaille, un Défi du jour, un Championnat de quatre courses, le freeride, une École de figures et des courses en ligne entre amis avec un code de salon à 5 caractères.'),
        ('Quels circuits y a-t-il ?', 'MX Royale a deux circuits de supercross ({sx}) et des circuits outdoor en forêt, dans le désert, en canyon, sur la neige, en forêt tropicale, à la plage, dans une carrière et sur un lac salé. Le circuit débutant est Sunvale MX Park.'),
        ('Qui fait MX Royale ?', 'MX Royale est développé par trois élèves autrichiens, comme projet personnel. Le jeu est en bêta ouverte depuis le 26 novembre 2026 ; il n’a ni publicité ni achats dans le jeu.'),
    ],
    about_rows=[
        ('Prix', 'Gratuit – sans publicité ni achats dans le jeu'), ('Téléchargement / installation', 'Aucun – fonctionne dans le navigateur'),
        ('Navigateurs', 'Chrome, Edge, Firefox, Safari'), ('Appareils', 'PC, Mac, téléphones et tablettes (paysage)'),
        ('Commandes', 'Clavier (touches modifiables), tactile avec inclinaison en option, manette'),
        ('Solo', 'Course contre l’IA, contre-la-montre avec fantôme, Défi du jour, Championnat, freeride, École de figures'),
        ('Multijoueur', 'Courses en ligne avec code de salon à 5 caractères ; des bots peuvent compléter la grille'),
        ('Circuits', '{nr} circuits de course + {nf} cartes freeride, dont 2 circuits de supercross'),
        ('Grille', 'Jusqu’à 12 pilotes (toi + IA)'),
        ('Figures', 'Whips, scrubs, backflips, Superman, Nac-Nac, Can-Can, heel clicker, seat grab, cliffhanger'),
        ('Motos', '450 quatre-temps, 250 deux-temps et électrique'),
        ('Aides', 'Cinq niveaux : Débutant, Normal, Sport, Pro, Sim'),
        ('Langues', 'Anglais, allemand, espagnol, français, portugais du Brésil'),
        ('Compte', 'Facultatif'), ('Statut', 'Bêta ouverte depuis le 26 novembre 2026'),
        ('Développement', 'Trois élèves autrichiens'), ('Site web', 'mxroyale.com'), ('Jouer', 'play.mxroyale.com'),
    ],
    about_h1='Fiche <span>MX Royale</span>', about_stand='Dernière mise à jour : {stand}', about_tab='Fonctions en bref',
    about_more='Plus : <a href="{tracks}">tous les circuits</a> · <a href="{how}">comment jouer</a> · <a href="{press}">kit presse (en anglais)</a>',
    about_titel='À propos de MX Royale – Fiche du jeu de motocross',
    about_desc='Fiche du jeu : MX Royale est un jeu de motocross gratuit dans le navigateur. Plateformes, commandes, modes, circuits, langues et statut en bref.',
    about_crumb='À propos',
    claim_sub='Sans téléchargement, sur PC, téléphone et manette.',
    get_lead='Pilote des motos de cross sur {nr} circuits de motocross et de supercross, contre l’IA ou en ligne entre amis, gratuitement et dans n’importe quel navigateur récent.',
)

TX['pt'] = dict(
    lang_name='Português', ride='Jogar agora', nav_tracks='Pistas', nav_how='Como jogar', nav_about='Sobre', nav_press='Imprensa e criadores',
    legal='Aviso legal', privacy='Privacidade', home='Início', foot_social='Siga a gente', locale='pt_BR',
    nav_aria='Principal', lang_aria='Idioma', skip='Ir para o conteúdo', foot_claim='Jogo de motocross grátis no seu navegador.',
    og_alt='MX Royale – jogo de motocross no navegador', track_alt='pista no MX Royale',
    karten=[
        ('{nr} pistas + {nf} mapas de freeride', 'Estádios de supercross, GPs na floresta, deserto, cânion, neve, praia e uma pedreira.'),
        ('Corra contra a IA', 'Largue do gate contra até 11 pilotos da IA ou dispute um Campeonato de 4 corridas.'),
        ('Online com amigos', 'Crie uma sala, mande o código de 5 caracteres e corram uns contra os outros.'),
        ('Contra o relógio e fantasmas', 'Persiga sua melhor volta ou o melhor fantasma, ganhe medalhas e encare o Desafio diário.'),
        ('Whips, scrubs e flips', 'Backflips, Supermans, Nac-Nacs e Can-Cans. Aprenda na Escola de manobras.'),
        ('Celular, PC ou controle', 'Controles de toque na horizontal, teclado ou gamepad. Nada para instalar.'),
    ],
    claim='MX Royale: o jogo de motocross grátis para jogar online, direto no navegador',
    klein='Beta aberto · sem conta · funciona no Chrome, Edge, Firefox e Safari',
    hero_alt='Piloto saltando com a moto de motocross diante de uma lagoa turquesa em Tidewater Flats no MX Royale',
    h_get='O que você <span>encontra</span>', h_tracks='As <span>pistas</span>',
    lead_tracks='{nr} pistas de corrida, de um parque de MX para iniciantes até supercross sob os refletores, além de {nf} mapas de freeride para manobras. Novas pistas chegam durante o beta.',
    more_tracks='Todas as pistas em detalhe →', h_faq='Perguntas e <span>respostas</span>',
    faq_more='Novo em jogos de motocross? Leia <a href="{how}">como jogar</a> ou a <a href="{about}">ficha do jogo</a>.',
    h_team='Feito por <span>pilotos</span>',
    team='MX Royale é feito por três estudantes que também andam de moto. Toda semana chegam novas pistas, manobras e correções. Achou um bug ou tem uma ideia? Escreva pra gente (em inglês ou alemão): <a href="mailto:feedback@mxroyale.com">feedback@mxroyale.com</a>',
    home_titel='MX Royale – Jogo de motocross grátis online, sem download',
    home_desc='Jogo de motocross grátis no navegador: sem download, no celular, PC ou com controle. {nr} pistas, supercross, whips e corridas online com amigos.',
    home_og='MX Royale – Motocross no seu navegador',
    vg_desc=('MX Royale é um jogo de corrida de motocross grátis que roda no navegador. Sem download, no PC e no celular, '
             'com teclado, toque ou gamepad. {nr} pistas de corrida, {nf} mapas de freeride, whips, scrubs e flips, '
             'corridas contra a IA, contra o relógio com fantasma e corridas online com amigos.'),
    fakt_feld='Grid: {n} pilotos', fakt_tt='Contra o relógio com fantasma e medalhas', fakt_free='Sem voltas, sem cronômetro, sem adversários',
    tracks_h1='Pistas de <span>motocross</span>',
    tracks_lead='MX Royale tem {nr} pistas de corrida e {nf} mapas de freeride, todos grátis no seu navegador. Vão de um parque de MX para iniciantes a duas pistas de supercross e longos Grandes Prêmios ao ar livre na floresta, no deserto, na neve e no litoral.',
    tracks_more='Quer saber como fazer whip e scrub? Leia <a href="{how}">como jogar</a>.',
    tracks_titel='Pistas de motocross – Supercross, deserto, neve | MX Royale',
    tracks_desc='As {nr} pistas e {nf} mapas de freeride do MX Royale, o jogo de motocross grátis no navegador: supercross, GP na floresta, deserto e neve.',
    tracks_list='Pistas do MX Royale', tracks_crumb='Pistas',
    how_h1='Como <span>jogar</span>', how_next='Próximo passo: escolha uma pista na <a href="{tracks}">página de pistas</a>.',
    how_titel='Como jogar MX Royale – Controles, whips e scrubs',
    how_desc='Como jogar o jogo de motocross grátis MX Royale: controles de teclado, celular e controle, como fazer whip, scrub e pop, e dicas para voltas mais rápidas.',
    how_crumb='Como jogar',
    how_html="""
<p class="lead">MX Royale é fácil de começar e difícil de dominar. Toque em <b>Jogar agora</b>, escolha uma pista e acelere: o jogo roda no navegador do PC, Mac, celular ou tablet. Esta página explica os controles de teclado, celular e controle, e como funcionam o whip, o scrub e a largada no gate.</p>
{ride}
<h2>Teclado</h2>
<div class="tabelle"><table>
<tr><th><kbd>W</kbd> / <kbd>S</kbd></th><td>Acelerador / freio</td></tr>
<tr><th><kbd>A</kbd> / <kbd>D</kbd></th><td>Esterçar · no ar: whip</td></tr>
<tr><th><kbd>←</kbd> / <kbd>→</kbd></th><td>Inclinar a moto · na rampa: scrub · no ar: deitar a moto</td></tr>
<tr><th><kbd>↑</kbd> / <kbd>↓</kbd></th><td>Peso para frente / para trás · stoppie / wheelie</td></tr>
<tr><th><kbd>Espaço</kbd></th><td>Agachar / pop · no freeride: manobras junto com as setas</td></tr>
<tr><th><kbd>Shift</kbd></th><td>Freio traseiro</td></tr>
<tr><th><kbd>R</kbd></th><td>Voltar para a pista</td></tr>
<tr><th><kbd>C</kbd> · <kbd>Q</kbd> · <kbd>G</kbd> · <kbd>Esc</kbd></th><td>Câmera · olhar para trás (segurar) · fantasma ligado/desligado · pausa</td></tr>
</table></div>
<p class="klein">Você pode mudar todas as teclas de pilotagem em Opções.</p>
<h2>Celular e tablet</h2>
<ul>
<li>Vire o celular na <b>horizontal</b>.</li>
<li><b>Polegar esquerdo:</b> um stick aparece onde você toca. Esquerda/direita esterça (e faz whip no ar), cima/baixo move o seu peso.</li>
<li><b>Polegar direito:</b> segure <b>GAS</b>; o freio fica à esquerda. Arraste para a esquerda/direita no acelerador para inclinar a moto (scrub), arraste para baixo para carregar a suspensão e solte na borda do salto para o pop.</li>
<li>No canto superior direito: câmera, voltar para a pista, pausa. Prefere inclinar? Ative a inclinação em Opções → Direção no celular.</li>
<li>Nos níveis Iniciante e Normal o piloto faz o pop nos saltos sozinho.</li>
</ul>
<h2>Controle (gamepad)</h2>
<ul>
<li><b>RT</b> acelerador, <b>LT</b> freio (ambos analógicos).</li>
<li><b>Analógico esquerdo</b>: esterça e faz whip no ar.</li>
<li><b>Analógico direito</b>: ↕ move o seu peso, ↔ inclina a moto (scrub, deitar a moto).</li>
<li><b>A</b> agachar/pop · <b>X</b> freio traseiro · <b>Y</b> voltar para a pista · <b>Start</b> pausa.</li>
<li>Manobras no freeride: no ar, segure <b>LB</b> ou <b>RB</b> e use o analógico esquerdo; LB + RB = sem as mãos.</li>
</ul>
<h2>Como fazer um whip</h2>
<p>No whip você joga a moto de lado no ar. Esterce logo antes da borda do salto (<kbd>A</kbd>/<kbd>D</kbd>, analógico esquerdo ou o stick de toque), segure no ar e solte mais ou menos meio segundo antes de pousar para a moto voltar reta. Quanto melhor o timing, maior o whip: passa de 180° se você acertar. Um whip conta a partir de 40°.</p>
<h2>Como fazer um scrub</h2>
<p>O scrub mantém você baixo sobre o salto, então você volta ao chão mais cedo e fica mais rápido na corrida. Deite a moto na face da rampa (<kbd>←</kbd>/<kbd>→</kbd>, analógico direito ou arrastando no acelerador) e endireite antes do fim da borda; senão a roda dianteira engancha.</p>
<h2>Pop e largada no gate</h2>
<p><b>Pop:</b> agache na rampa e solte na borda para saltar mais alto e mais longe. <b>Largada:</b> a partir da placa “5”, segure acelerador e freio juntos para subir o giro e solte o freio quando o gate cair. Acelerar sem freio antes disso é largada queimada.</p>
<h2>Manobras e Escola de manobras</h2>
<p>No freeride e na Escola de manobras você pode fazer backflips, Supermans, Nac-Nacs, heel clickers, Can-Cans, seat grabs e cliffhangers. A Escola de manobras ensina cada uma passo a passo para teclado, celular e controle, e mostra o que deu errado.</p>
<h2>Dicas para voltas mais rápidas</h2>
<ul>
<li>Pouse na descida depois do salto para manter a velocidade.</li>
<li>Cortar caminho não compensa: se sair da pista, a volta não conta.</li>
<li>Travou? Voltar para a pista coloca você de novo no traçado.</li>
<li>Comece pela Sunvale MX Park, a pista para iniciantes, e mude as ajudas (Iniciante, Normal, Sport, Pro, Sim) em Opções quando ficar mais rápido.</li>
<li>No contra o relógio, sua melhor volta corre junto como fantasma: dispute com ela até bater os tempos das medalhas.</li>
<li>Quatro câmeras: perseguição dinâmica, perseguição clássica, drone e capacete.</li>
</ul>
""",
    about_abs=[
        ('O que é MX Royale?', 'MX Royale é um jogo de corrida de motocross grátis que roda no navegador. Não precisa de download nem de conta, e funciona no PC, Mac, celulares e tablets com teclado, controles de toque ou gamepad.'),
        ('O que dá para fazer no MX Royale?', 'No MX Royale você pilota motos de motocross e supercross em {nr} pistas de corrida e {nf} mapas de freeride. Os modos de jogo são corridas contra até 11 pilotos da IA, contra o relógio contra o seu próprio fantasma com tempos de medalha, um Desafio diário, um Campeonato de quatro corridas, freeride, uma Escola de manobras e corridas online com amigos usando um código de sala de 5 caracteres.'),
        ('Quais pistas existem?', 'MX Royale tem duas pistas de supercross ({sx}) e pistas ao ar livre em floresta, deserto, cânion, neve, floresta tropical, praia, pedreira e um lago de sal. A pista para iniciantes é a Sunvale MX Park.'),
        ('Quem faz o MX Royale?', 'MX Royale é desenvolvido por três estudantes da Áustria como projeto pessoal. O jogo está em beta aberto desde 26 de novembro de 2026; não tem anúncios nem compras dentro do jogo.'),
    ],
    about_rows=[
        ('Preço', 'Grátis – sem anúncios e sem compras dentro do jogo'), ('Download / instalação', 'Nenhum – roda no navegador'),
        ('Navegadores', 'Chrome, Edge, Firefox, Safari'), ('Aparelhos', 'PC, Mac, celulares e tablets (horizontal)'),
        ('Controles', 'Teclado (teclas configuráveis), toque com inclinação opcional, gamepad'),
        ('Um jogador', 'Corrida contra a IA, contra o relógio com fantasma, Desafio diário, Campeonato, freeride, Escola de manobras'),
        ('Multijogador', 'Corridas online com código de sala de 5 caracteres; bots podem completar o grid'),
        ('Pistas', '{nr} pistas de corrida + {nf} mapas de freeride, incluindo 2 de supercross'),
        ('Grid', 'Até 12 pilotos (você + IA)'),
        ('Manobras', 'Whips, scrubs, backflips, Superman, Nac-Nac, Can-Can, heel clicker, seat grab, cliffhanger'),
        ('Motos', '450 quatro tempos, 250 dois tempos e elétrica'),
        ('Ajudas', 'Cinco níveis: Iniciante, Normal, Sport, Pro, Sim'),
        ('Idiomas', 'Inglês, alemão, espanhol, francês, português do Brasil'),
        ('Conta', 'Opcional'), ('Status', 'Beta aberto desde 26 de novembro de 2026'),
        ('Desenvolvimento', 'Três estudantes da Áustria'), ('Site', 'mxroyale.com'), ('Jogar', 'play.mxroyale.com'),
    ],
    about_h1='Ficha do <span>MX Royale</span>', about_stand='Última atualização: {stand}', about_tab='Recursos em resumo',
    about_more='Mais: <a href="{tracks}">todas as pistas</a> · <a href="{how}">como jogar</a> · <a href="{press}">kit de imprensa (em inglês)</a>',
    about_titel='Sobre o MX Royale – Ficha do jogo de motocross',
    about_desc='Ficha do jogo: MX Royale é um jogo de motocross grátis no navegador. Plataformas, controles, modos, pistas, idiomas e status em resumo.',
    about_crumb='Sobre',
    claim_sub='Sem download, no PC, no celular e com controle.',
    get_lead='Pilote motos de motocross em {nr} pistas de motocross e supercross, contra a IA ou online com amigos, de graça e em qualquer navegador atual.',
)

# ── Alt-Texte der Streckenbilder (beschreiben, was auf dem Bild zu sehen ist) ─────────────────────────
BILD_ALT = {
    'sunvale': {'en': 'Motocross riders racing through a grass turn, dirt flying', 'de': 'Motocross-Fahrer im Pulk in einer Wiesenkurve, Erde fliegt', 'es': 'Pilotos de motocross en una curva de pasto, con tierra volando', 'fr': 'Pilotes de motocross dans un virage herbeux, la terre vole', 'pt': 'Pilotos de motocross em uma curva na grama, com terra voando'},
    'larkmeadow': {'en': 'Rider in the air under stadium floodlights at night', 'de': 'Fahrer in der Luft unter Stadion-Flutlicht bei Nacht', 'es': 'Piloto en el aire bajo los focos del estadio de noche', 'fr': 'Pilote en l’air sous les projecteurs du stade la nuit', 'pt': 'Piloto no ar sob os refletores do estádio à noite'},
    'frostline': {'en': 'Rider jumping in front of mountain peaks glowing in the evening sun', 'de': 'Fahrer springt vor Bergspitzen im Abendrot', 'es': 'Piloto saltando frente a picos de montaña al atardecer', 'fr': 'Pilote sautant devant des sommets éclairés par le soleil du soir', 'pt': 'Piloto saltando diante de picos iluminados pelo sol da tarde'},
    'monsoon': {'en': 'Dirt track between rice terraces and palm trees', 'de': 'Erdpiste zwischen Reisterrassen und Palmen', 'es': 'Pista de tierra entre terrazas de arroz y palmeras', 'fr': 'Piste en terre entre rizières en terrasses et palmiers', 'pt': 'Pista de terra entre terraços de arroz e palmeiras'},
    'mirage-flats': {'en': 'Rider jumping a dirt bike over freight wagons in the desert', 'de': 'Fahrer springt mit dem Motocross-Bike über Güterwaggons in der Wüste', 'es': 'Piloto saltando con su moto sobre vagones de carga en el desierto', 'fr': 'Pilote sautant au-dessus de wagons de marchandises dans le désert', 'pt': 'Piloto saltando com a moto sobre vagões de carga no deserto'},
    'herbst': {'en': 'Rider on an autumn forest track between jets of fire', 'de': 'Fahrer auf einer Herbstwald-Strecke zwischen Feuersäulen', 'es': 'Piloto en una pista de bosque otoñal entre columnas de fuego', 'fr': 'Pilote sur un circuit en forêt d’automne entre des jets de feu', 'pt': 'Piloto em uma pista de floresta de outono entre jatos de fogo'},
    'rustleaf': {'en': 'Track under a start bridge in autumn woods', 'de': 'Strecke unter einer Startbrücke im Herbstwald', 'es': 'Pista bajo un puente de salida en el bosque otoñal', 'fr': 'Piste sous une passerelle de départ en forêt d’automne', 'pt': 'Pista sob uma ponte de largada na floresta de outono'},
    'neonharbor': {'en': 'Night jump past a glowing neon sign at a harbour supercross track', 'de': 'Sprung bei Nacht an einem leuchtenden Neon-Schild auf einer Hafen-Supercross-Strecke', 'es': 'Salto nocturno junto a un letrero de neón en una pista de supercross portuaria', 'fr': 'Saut de nuit devant une enseigne néon sur un circuit de supercross portuaire', 'pt': 'Salto noturno ao lado de um letreiro de neon em uma pista de supercross no porto'},
    'pine-ridge': {'en': 'Bermed turn on a pine forest Grand Prix track', 'de': 'Anlieger-Kurve auf einer Grand-Prix-Strecke im Kiefernwald', 'es': 'Curva peraltada en un Gran Premio en un bosque de pinos', 'fr': 'Virage relevé sur un Grand Prix en forêt de pins', 'pt': 'Curva inclinada em um Grande Prêmio na floresta de pinheiros'},
    'sandglass': {'en': 'Desert track below red canyon walls', 'de': 'Wüstenstrecke unter roten Canyon-Wänden', 'es': 'Pista en el desierto bajo paredes rojas de cañón', 'fr': 'Piste dans le désert sous des parois de canyon rouges', 'pt': 'Pista no deserto sob paredões vermelhos de cânion'},
    'highcrest': {'en': 'Rider in the air next to a stone arch above a mountain valley', 'de': 'Fahrer in der Luft neben einem Steinbogen über einem Bergtal', 'es': 'Piloto en el aire junto a un arco de piedra sobre un valle de montaña', 'fr': 'Pilote en l’air à côté d’une arche de pierre au-dessus d’une vallée de montagne', 'pt': 'Piloto no ar ao lado de um arco de pedra sobre um vale de montanha'},
    'canopy': {'en': 'Rider on a red dirt rainforest track with spectators', 'de': 'Fahrer auf roter Erde im Regenwald, Zuschauer am Rand', 'es': 'Piloto en una pista de tierra roja en la selva con público', 'fr': 'Pilote sur une piste de terre rouge en forêt tropicale, avec des spectateurs', 'pt': 'Piloto em uma pista de terra vermelha na floresta tropical com público'},
    'tidewater': {'en': 'Rider scrubbing a jump on a beach track with palm trees', 'de': 'Fahrer scrubbt einen Sprung auf einer Strandstrecke mit Palmen', 'es': 'Piloto haciendo un scrub en un salto de una pista de playa con palmeras', 'fr': 'Pilote en scrub sur un saut d’une piste de plage bordée de palmiers', 'pt': 'Piloto fazendo scrub em um salto de uma pista de praia com palmeiras'},
    'ironcut': {'en': 'Dirt berm turn in a grey stone quarry', 'de': 'Anlieger-Kurve in einem grauen Steinbruch', 'es': 'Curva peraltada en una cantera de piedra gris', 'fr': 'Virage relevé dans une carrière de pierre grise', 'pt': 'Curva inclinada em uma pedreira de pedra cinza'},
    'saltpan': {'en': 'Track across a white salt flat with salt piles', 'de': 'Strecke über einen weißen Salzsee mit Salzhaufen', 'es': 'Pista sobre un salar blanco con montones de sal', 'fr': 'Piste sur un lac salé blanc avec des tas de sel', 'pt': 'Pista sobre uma salina branca com montes de sal'},
    'freeride': {'en': 'Desert freeride map with jump lines seen from above', 'de': 'Wüsten-Freeride-Map mit Sprung-Linien von oben', 'es': 'Mapa de freeride en el desierto con líneas de saltos visto desde arriba', 'fr': 'Carte freeride dans le désert avec des lignes de sauts, vue d’en haut', 'pt': 'Mapa de freeride no deserto com linhas de saltos visto de cima'},
    'arena': {'en': 'Freestyle rider seen from below in the stadium at night', 'de': 'Freestyle-Fahrer von unten gesehen im Stadion bei Nacht', 'es': 'Piloto de freestyle visto desde abajo en el estadio de noche', 'fr': 'Pilote de freestyle vu d’en bas dans le stade de nuit', 'pt': 'Piloto de freestyle visto de baixo no estádio à noite'},
}
IN_MX = {'en': 'in MX Royale', 'de': 'in MX Royale', 'es': 'en MX Royale', 'fr': 'dans MX Royale', 'pt': 'no MX Royale'}

# ── Presse-Seite (nur EN/DE, /press/ und /presse/) ─────────────────────────────────────────────────
PRESSE = {
    'en': dict(
        titel='MX Royale – Press Kit: Facts, Logo, Screenshots',
        desc='MX Royale press kit: facts, short texts in 50/100/200 words, logo, key art and screenshots of the free browser motocross game. For press and creators.',
        h1='Press &amp; <span>creators</span>', crumb='Press & creators',
        intro='Want to write about MX Royale, make a video or stream it? Go ahead, no need to ask. Everything you need is on this page.',
        h_fakten='Facts', h_texte='Short texts to copy', h_dl='Downloads', h_kontakt='Contact',
        texte=[
            ('50 words', 'MX Royale is a free motocross game that runs right in the browser, on PC and phones, with keyboard, touch or controller. No download, no account. {nr} race tracks from supercross stadiums to a desert Grand Prix, {nf} freeride maps, whips and flips, ghost laps and online races with friends.'),
            ('100 words', 'MX Royale is a free motocross game that runs right in the browser, on PC and phones, with keyboard, touch or controller. No download, no account. {nr} race tracks from supercross stadiums to a desert Grand Prix, {nf} freeride maps, whips and flips. Riders line up at the gate against up to 11 AI opponents, chase their own ghost in time trial, take on the Daily Challenge or a four-race Championship. Online, one player creates a room and shares a five-character code. MX Royale is built by three students from Austria who ride motocross themselves. It has been in open beta since 26 November 2026.'),
            ('200 words', 'MX Royale is a free motocross game that runs right in the browser. It works on PC, Mac, phones and tablets, with keyboard, touch controls or a gamepad, and needs no download and no account.\n\nThere are {nr} race tracks and {nf} freeride maps: two supercross tracks under stadium lights, a beginner MX park, forest Grand Prix tracks, a desert jump park with a rail gap, a red-rock canyon, a snow track down a ski slope, a rainforest hollow, a beach at low tide, a quarry and a salt lake. Riders race up to 11 AI opponents, ride time trial against their own ghost for medal times and a top-10 leaderboard, take on the Daily Challenge or a four-race Championship. Online races work with a five-character room code; bots fill up the field.\n\nThe riding is arcade, but with real technique: whips, scrubs, the pop off the lip and a proper gate start. In freeride there are backflips, Supermans, Nac-Nacs and Can-Cans, and a trick school explains each one. The game is available in English, German, Spanish, French and Brazilian Portuguese.\n\nMX Royale is built by three students from Austria who ride motocross themselves. It has been in open beta since 26 November 2026, with no ads and no in-game purchases.'),
        ],
        dl=[('mxroyale_logo_1080.png', 'Logo (PNG, 1080 × 1080)'), ('mxroyale_key_art_1920.jpg', 'Key art (JPG, 1920 × 1080)')],
        zip='Complete press kit (ZIP: logo, key art, 8 screenshots 1920 × 1080, fact sheet)',
        shots='Screenshots (1920 × 1080, click to download)',
        clips='You can also record your own clips in the game (Replay → Share).',
        kontakt='Press and partnerships: <a href="mailto:press@mxroyale.com">press@mxroyale.com</a><br>General: <a href="mailto:info@mxroyale.com">info@mxroyale.com</a><br>Social: @mxroyalegame on TikTok, Instagram and YouTube',
    ),
    'de': dict(
        titel='MX Royale – Pressematerial: Fakten, Logo, Screenshots',
        desc='Pressematerial zu MX Royale: Fakten, Kurztexte mit 50/100/200 Wörtern, Logo, Key Art und Screenshots des kostenlosen Motocross Browserspiels.',
        h1='Presse &amp; <span>Creator</span>', crumb='Presse & Creator',
        intro='Ihr wollt über MX Royale schreiben, ein Video machen oder es streamen? Gerne, ohne Nachfrage. Alles, was ihr braucht, steht hier.',
        h_fakten='Fakten', h_texte='Kurztexte zum Kopieren', h_dl='Downloads', h_kontakt='Kontakt',
        texte=[
            ('50 Wörter', 'MX Royale ist ein kostenloses Motocross-Spiel, das direkt im Browser läuft, am PC und am Handy, mit Tastatur, Touch oder Controller. Kein Download, kein Konto. {nr} Rennstrecken von der Supercross-Halle bis zum Wüsten-Grand-Prix, {nf} Freeride-Maps, Whips und Flips, Geister-Runden und Online-Rennen mit Freunden.'),
            ('100 Wörter', 'MX Royale ist ein kostenloses Motocross-Spiel, das direkt im Browser läuft, am PC und am Handy, mit Tastatur, Touch oder Controller. Kein Download, kein Konto. {nr} Rennstrecken von der Supercross-Halle bis zum Wüsten-Grand-Prix, {nf} Freeride-Maps, Whips und Flips. Man startet am Gatter gegen bis zu 11 KI-Fahrer, jagt im Zeitfahren den eigenen Geist, fährt die Tages-Challenge oder eine Meisterschaft über vier Rennen. Online erstellt einer einen Raum und schickt einen 5-stelligen Code. MX Royale bauen drei Schüler aus Österreich, die selbst Motocross fahren. Seit 26. November 2026 ist das Spiel in der offenen Beta.'),
            ('200 Wörter', 'MX Royale ist ein kostenloses Motocross-Spiel, das direkt im Browser läuft. Es funktioniert am PC, Mac, Handy und Tablet, mit Tastatur, Touch-Steuerung oder Gamepad, ohne Download und ohne Konto.\n\nEs gibt {nr} Rennstrecken und {nf} Freeride-Maps: zwei Supercross-Strecken unter Flutlicht, einen Einsteiger-MX-Park, Wald-Grand-Prix, einen Wüsten-Sprungpark mit Rail Gap, einen roten Canyon, eine Schneestrecke auf der Skipiste, einen Regenwald, einen Strand bei Ebbe, einen Steinbruch und einen Salzsee. Man fährt gegen bis zu 11 KI-Fahrer, im Zeitfahren gegen den eigenen Geist um Medaillenzeiten und die Top 10 der Strecke, die Tages-Challenge oder eine Meisterschaft über vier Rennen. Online-Rennen laufen über einen 5-stelligen Raum-Code; Bots füllen das Feld auf.\n\nDas Fahren ist Arcade, aber mit echter Technik: Whips, Scrubs, der Pop an der Kante und ein richtiger Gatterstart. Im Freeride gibt es Backflips, Superman, Nac-Nac und Can-Can, eine Trick-Schule erklärt jeden Trick. Das Spiel gibt es auf Englisch, Deutsch, Spanisch, Französisch und brasilianischem Portugiesisch.\n\nMX Royale bauen drei Schüler aus Österreich, die selbst Motocross fahren. Seit 26. November 2026 ist es in der offenen Beta, ohne Werbung und ohne In-Game-Käufe.'),
        ],
        dl=[('mxroyale_logo_1080.png', 'Logo (PNG, 1080 × 1080)'), ('mxroyale_key_art_1920.jpg', 'Key Art (JPG, 1920 × 1080)')],
        zip='Komplettes Pressepaket (ZIP: Logo, Key Art, 8 Screenshots 1920 × 1080, Faktenblatt)',
        shots='Screenshots (1920 × 1080, Klick lädt herunter)',
        clips='Clips dürft ihr auch selbst im Spiel aufnehmen (Replay → Teilen).',
        kontakt='Presse und Kooperationen: <a href="mailto:presse@mxroyale.com">presse@mxroyale.com</a><br>Allgemein: <a href="mailto:info@mxroyale.com">info@mxroyale.com</a><br>Social: @mxroyalegame auf TikTok, Instagram und YouTube',
    ),
}
# Pressefotos: Quelle (shots_2611/beste) → Dateiname in /presse/, Bildbeschreibung EN/DE
PRESSE_SHOTS = [
    ('larkmeadow_hero_16x9_01.jpg', 'mx-royale-supercross-larkmeadow-sx.jpg', 'Supercross stadium at night: Larkmeadow SX', 'Supercross-Stadion bei Nacht: Larkmeadow SX'),
    ('highcrest_whip_16x9_01.jpg', 'mx-royale-whip-highcrest-valley-gp.jpg', 'Whip over a jump on Highcrest Valley GP', 'Whip über einen Sprung auf Highcrest Valley GP'),
    ('mirage-flats_hero_16x9_01.jpg', 'mx-royale-rail-gap-mirage-flats.jpg', 'Rail gap over freight wagons on Mirage Flats', 'Rail Gap über Güterwaggons auf Mirage Flats'),
    ('herbst_hero_16x9_01.jpg', 'mx-royale-fire-jumps-glutwald-mx.jpg', 'Fire jumps on the autumn forest track Glutwald MX', 'Feuer-Sprünge auf der Herbstwald-Strecke Glutwald MX'),
    ('frostline_pulk_16x9_02.jpg', 'mx-royale-snow-race-frostline-mx.jpg', 'Race on snow at Frostline MX', 'Rennen im Schnee auf Frostline MX'),
    ('sunvale_kurve_16x9_01.jpg', 'mx-royale-gate-pack-sunvale-mx-park.jpg', 'Pack of riders on Sunvale MX Park', 'Fahrerfeld auf Sunvale MX Park'),
    ('neonharbor_whip_16x9_01.jpg', 'mx-royale-night-whip-neon-harbor-sx.jpg', 'Night whip at Neon Harbor SX', 'Whip bei Nacht auf Neon Harbor SX'),
    ('tidewater_air_16x9_01.jpg', 'mx-royale-beach-jump-tidewater-flats.jpg', 'Beach jump on Tidewater Flats', 'Sprung am Strand auf Tidewater Flats'),
]

# ── Neuigkeiten (nur echte Updates; neueste zuerst) ────────────────────────────────────────────────
NEWS = [
    dict(datum='2026-11-27', id='website-five-languages',
         en=('Website in five languages, new screenshots and a press kit',
             'mxroyale.com now has pages in English, German, Spanish, French and Brazilian Portuguese – the same five languages as the game. Every track has a new in-game screenshot, and the press page has a downloadable press kit with logo, key art, eight screenshots and a fact sheet. In the game, the track menu now shows real shots of each track and the time-trial leaderboard got a new look.'),
         de=('Website in fünf Sprachen, neue Screenshots und Pressepaket',
             'mxroyale.com gibt es jetzt auf Englisch, Deutsch, Spanisch, Französisch und brasilianischem Portugiesisch – in denselben fünf Sprachen wie das Spiel. Jede Strecke hat einen neuen Screenshot aus dem Spiel, und auf der Presse-Seite gibt es ein Pressepaket zum Herunterladen mit Logo, Key Art, acht Screenshots und Faktenblatt. Im Spiel zeigt das Strecken-Menü jetzt echte Bilder jeder Strecke und die Zeitfahren-Bestenliste hat ein neues Aussehen.')),
    dict(datum='2026-11-26', id='open-beta',
         en=('Open beta: MX Royale is live',
             'MX Royale is now open to everyone at play.mxroyale.com – free, in the browser, with no download and no account needed. The open beta starts with 15 race tracks and 2 freeride maps, races against AI riders, time trial with ghosts, the Daily Challenge, a Championship, the trick school and online races with friends via room code. Found a bug? Write to feedback@mxroyale.com.'),
         de=('Offene Beta: MX Royale ist online',
             'MX Royale ist ab sofort für alle offen unter play.mxroyale.com – kostenlos, im Browser, ohne Download und ohne Konto. Die offene Beta startet mit 15 Rennstrecken und 2 Freeride-Maps, Rennen gegen KI-Fahrer, Zeitfahren mit Geist, Tages-Challenge, Meisterschaft, Trick-Schule und Online-Rennen mit Freunden per Raum-Code. Fehler gefunden? Schreib an feedback@mxroyale.com.')),
]
NEWS_TX = {
    'en': dict(titel='MX Royale News – Updates of the Browser Motocross Game', desc='What is new in MX Royale, the free motocross game in your browser: new tracks, features and fixes from the open beta.',
               h1='News &amp; <span>updates</span>', crumb='News', nav='News', feed='Atom feed'),
    'de': dict(titel='MX Royale Neuigkeiten – Updates zum Motocross Browserspiel', desc='Was es Neues in MX Royale gibt, dem kostenlosen Motocross-Spiel im Browser: neue Strecken, Funktionen und Fixes aus der offenen Beta.',
               h1='Was ist <span>neu</span>', crumb='Neuigkeiten', nav='Neuigkeiten', feed='Atom-Feed'),
}