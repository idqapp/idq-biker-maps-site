#!/usr/bin/env python3
"""Genera il sito di IDQ Biker Maps (index, privacy, funzioni) in 5 lingue.
Parte dal sito di IDQ Navigator (~/idq-navigator-site) per struttura e informativa, e dalle guide di Biker Maps
(~/idq-navigator/android/app/src/biker/assets/guida*.html) per le funzioni. Uso: python3 genera.py"""
import os, re
NAVI = os.path.expanduser('~/idq-navigator-site/'); GUIDE = os.path.expanduser('~/idq-navigator/android/app/src/biker/assets/')
LG = ['it', 'en', 'fr', 'de', 'es']; G = {'it': 'guida.html', 'en': 'guida-en.html', 'fr': 'guida-fr.html', 'de': 'guida-de.html', 'es': 'guida-es.html'}
NOME = 'IDQ Biker Maps'
def leggi(p): return open(p, encoding='utf-8').read()

# --- grafica: nero con arancione e blu delle montagne, come il logo -------------------------------------------------
TEMA = ':root{--bg:#0a0a0c;--tx:#f3f3f3;--mu:#a8a8b0;--ac:#ff7a00;--ac2:#2f8cff;--card:#16161a;--bd:#2b2b31;--hero:#000}'
def tema(s):
    s = re.sub(r':root\{[^}]*\}\n@media \(prefers-color-scheme:dark\)\{:root\{[^}]*\}\}', TEMA, s, count=1)
    s = s.replace('.hero img{width:120px;height:120px;border-radius:28px;box-shadow:0 8px 30px rgba(0,0,0,.4)}',
                  '.hero img{width:min(300px,70vw);height:auto;border-radius:50%;box-shadow:0 0 0 3px #ff7a00,0 12px 50px rgba(255,122,0,.35)}')
    s = s.replace('.soon{display:inline-block;margin-top:22px;background:#1a73e8;color:#fff;',
                  '.soon{display:inline-block;margin-top:22px;background:#ff7a00;color:#000;')
    s = s.replace('.hero p{max-width:640px;margin:0 auto;color:#cfd8ee;', '.hero p{max-width:640px;margin:0 auto;color:#d6d6dc;')
    s = s.replace('.lingue button.on{background:var(--ac);color:#fff;border-color:var(--ac)}', '.lingue button.on{background:var(--ac);color:#000;border-color:var(--ac);font-weight:700}')
    s = s.replace('.card b{display:block;margin-bottom:4px}', '.card b{display:block;margin-bottom:4px;color:var(--ac)}.card{border-top:3px solid var(--ac2)}')
    s = s.replace('header.top img{width:36px;height:36px;border-radius:9px}', 'header.top img{width:38px;height:38px;border-radius:50%}')
    s = s.replace('.hero{background:var(--hero);', '.hero{background:radial-gradient(ellipse at 50% 0%,#1b2a44 0%,#000 70%);')
    return s
def marchio(s):
    s = s.replace('immagini/icona.png', 'immagini/icona.png')
    s = s.replace('<img src="immagini/icona.png" alt="">', '<img src="immagini/icona.png" alt="">')
    return s.replace('IDQ Navigator', NOME).replace('IDQ MAPS', NOME).replace('nav.assistente-joker.win', 'biker.assistente-joker.win')

# --- pagina principale ----------------------------------------------------------------------------------------------
HERO = {
 'it': ("La mappa e il navigatore per chi va in moto", "Percorsi pensati per la moto, mappe online e offline, voce nella tua lingua e avvisi sulla strada. Senza pubblicità e senza account.", "Presto su Google Play", "Cosa fa"),
 'en': ("The map and navigator for riders", "Routes made for motorcycles, online and offline maps, voice in your language and road alerts. No ads and no account.", "Coming soon on Google Play", "What it does"),
 'fr': ("La carte et le GPS pour les motards", "Des itinéraires pensés pour la moto, des cartes en ligne et hors ligne, la voix dans votre langue et des alertes sur la route. Sans publicité et sans compte.", "Bientôt sur Google Play", "Ce qu'elle fait"),
 'de': ("Die Karte und das Navi für Motorradfahrer", "Routen für das Motorrad, Online- und Offline-Karten, Sprachansagen in Ihrer Sprache und Warnungen auf der Strecke. Ohne Werbung und ohne Konto.", "Bald bei Google Play", "Was sie kann"),
 'es': ("El mapa y el navegador para motoristas", "Rutas pensadas para la moto, mapas online y sin conexión, voz en tu idioma y avisos en la carretera. Sin publicidad y sin cuenta.", "Próximamente en Google Play", "Qué hace")}
CARTE = {
 'it': [("Percorsi per la moto", "Il percorso è calcolato per la moto. Puoi evitare pedaggi, autostrade e traghetti e aggiungere quante tappe intermedie vuoi."),
        ("Online e offline", "Prima online: mappa, percorsi e ricerca sempre aggiornati. Se manca la rete passa da sola alle mappe scaricate sul telefono (l'Italia si scarica una volta sola): non resti mai senza."),
        ("Voce in 5 lingue", "Italiano, inglese, francese, tedesco e spagnolo, con voce maschile o femminile. Tutta l'app cambia lingua."),
        ("Avvisi sulla strada", "Autovelox, Tutor, telecamere ai semafori, varchi ZTL, passaggi a livello, dossi e le segnalazioni degli altri utenti: controlli mobili, incidenti, traffico, strade chiuse."),
        ("Limiti di velocità", "Il limite sul percorso e la tua velocità sempre in vista; rosso se lo superi."),
        ("Segnalazioni in tempo reale", "Un tocco per segnalare un controllo, un incidente o un pericolo; agli altri l'app chiede \"c'è ancora?\" quando passano."),
        ("Servizi e distributori", "Cerca distributori (con il prezzo aggiornato), ristoranti, parcheggi, farmacie...: li vedi con distanza e orari di apertura."),
        ("Mappa 2D o 3D", "Grafica chiara di giorno e di notte, in 3D inclinata o in 2D piatta, con la moto sempre al centro."),
        ("Tracce e itinerari", "Registra i tuoi giri in moto, salva gli itinerari e condividili in GPX o con un link."),
        ("Privacy", "Senza pubblicità, senza account e senza strumenti di analisi. Con le mappe scaricate la tua posizione non esce dal telefono.")],
 'en': [("Routes for motorcycles", "The route is calculated for the motorcycle. You can avoid tolls, motorways and ferries and add as many intermediate stops as you like."),
        ("Online and offline", "Online first: map, routes and search always up to date. If the network drops it switches by itself to the maps downloaded on your phone (you download Italy just once): you are never left without."),
        ("Voice in 5 languages", "Italian, English, French, German and Spanish, with a male or female voice. The whole app changes language."),
        ("Road alerts", "Speed cameras, Tutor sections, traffic-light cameras, ZTL gates, level crossings, speed bumps and reports from other users: mobile checks, accidents, traffic, closed roads."),
        ("Speed limits", "The limit on your route and your speed always in view; red when you go over."),
        ("Live reports", "One tap to report a check, an accident or a hazard; the app asks other riders \"is it still there?\" as they pass."),
        ("Services and fuel", "Search fuel stations (with the current price), restaurants, parking, pharmacies...: you see them with distance and opening hours."),
        ("2D or 3D map", "Clear graphics day and night, tilted in 3D or flat in 2D, with the motorcycle always in the centre."),
        ("Tracks and routes", "Record your rides, save routes and share them as GPX or with a link."),
        ("Privacy", "No ads, no account and no analytics. With downloaded maps your position never leaves the phone.")],
 'fr': [("Itinéraires pour la moto", "L'itinéraire est calculé pour la moto. Vous pouvez éviter péages, autoroutes et ferries et ajouter autant d'étapes intermédiaires que vous voulez."),
        ("En ligne et hors ligne", "D'abord en ligne : carte, itinéraires et recherche toujours à jour. Si le réseau manque, l'application passe toute seule aux cartes téléchargées sur le téléphone (l'Italie se télécharge une seule fois) : vous n'êtes jamais sans carte."),
        ("Voix en 5 langues", "Italien, anglais, français, allemand et espagnol, avec une voix masculine ou féminine. Toute l'application change de langue."),
        ("Alertes sur la route", "Radars, Tutor, caméras aux feux, portes ZTL, passages à niveau, dos d'âne et signalements des autres utilisateurs : contrôles mobiles, accidents, trafic, routes fermées."),
        ("Limites de vitesse", "La limite sur votre itinéraire et votre vitesse toujours visibles ; en rouge si vous la dépassez."),
        ("Signalements en direct", "Un geste pour signaler un contrôle, un accident ou un danger ; l'application demande aux autres « est-il toujours là ? » quand ils passent."),
        ("Services et stations", "Cherchez stations-service (avec le prix à jour), restaurants, parkings, pharmacies... : vous les voyez avec distance et horaires."),
        ("Carte 2D ou 3D", "Graphismes clairs de jour et de nuit, en 3D inclinée ou en 2D à plat, avec la moto toujours au centre."),
        ("Traces et itinéraires", "Enregistrez vos balades à moto, sauvegardez vos itinéraires et partagez-les en GPX ou par lien."),
        ("Confidentialité", "Sans publicité, sans compte et sans outil d'analyse. Avec les cartes téléchargées, votre position ne quitte pas le téléphone.")],
 'de': [("Routen fürs Motorrad", "Die Route wird für das Motorrad berechnet. Sie können Mautstraßen, Autobahnen und Fähren meiden und beliebig viele Zwischenstopps hinzufügen."),
        ("Online und offline", "Zuerst online: Karte, Routen und Suche immer aktuell. Fällt das Netz aus, wechselt die App von selbst zu den auf dem Handy geladenen Karten (Italien lädt man nur einmal): Sie stehen nie ohne da."),
        ("Sprache in 5 Sprachen", "Italienisch, Englisch, Französisch, Deutsch und Spanisch, mit männlicher oder weiblicher Stimme. Die ganze App wechselt die Sprache."),
        ("Warnungen auf der Strecke", "Blitzer, Tutor, Ampelkameras, ZTL-Zufahrten, Bahnübergänge, Bodenschwellen und Meldungen anderer Nutzer: mobile Kontrollen, Unfälle, Verkehr, gesperrte Straßen."),
        ("Tempolimits", "Das Limit auf Ihrer Route und Ihre Geschwindigkeit immer im Blick; rot, wenn Sie es überschreiten."),
        ("Live-Meldungen", "Ein Fingertipp meldet eine Kontrolle, einen Unfall oder eine Gefahr; die App fragt andere beim Vorbeifahren \"ist es noch da?\"."),
        ("Services und Tankstellen", "Suchen Sie Tankstellen (mit aktuellem Preis), Restaurants, Parkplätze, Apotheken...: mit Entfernung und Öffnungszeiten."),
        ("2D- oder 3D-Karte", "Klare Grafik bei Tag und Nacht, geneigt in 3D oder flach in 2D, mit dem Motorrad immer in der Mitte."),
        ("Tracks und Routen", "Zeichnen Sie Ihre Touren auf, speichern Sie Routen und teilen Sie sie als GPX oder per Link."),
        ("Datenschutz", "Ohne Werbung, ohne Konto und ohne Analyse-Tools. Mit geladenen Karten verlässt Ihre Position nie das Handy.")],
 'es': [("Rutas para la moto", "La ruta se calcula para la moto. Puedes evitar peajes, autopistas y transbordadores y añadir todas las paradas intermedias que quieras."),
        ("Online y sin conexión", "Primero online: mapa, rutas y búsqueda siempre al día. Si falta la red, pasa sola a los mapas descargados en el teléfono (Italia se descarga una sola vez): nunca te quedas sin mapa."),
        ("Voz en 5 idiomas", "Italiano, inglés, francés, alemán y español, con voz masculina o femenina. Toda la app cambia de idioma."),
        ("Avisos en la carretera", "Radares, Tutor, cámaras en semáforos, accesos ZTL, pasos a nivel, badenes y avisos de otros usuarios: controles móviles, accidentes, tráfico, carreteras cortadas."),
        ("Límites de velocidad", "El límite de tu ruta y tu velocidad siempre a la vista; en rojo si lo superas."),
        ("Avisos en directo", "Un toque para avisar de un control, un accidente o un peligro; la app pregunta a los demás \"¿sigue ahí?\" al pasar."),
        ("Servicios y gasolineras", "Busca gasolineras (con el precio actual), restaurantes, aparcamientos, farmacias...: con distancia y horario."),
        ("Mapa 2D o 3D", "Gráficos claros de día y de noche, en 3D inclinado o en 2D plano, con la moto siempre en el centro."),
        ("Tracks y rutas", "Graba tus salidas en moto, guarda rutas y compártelas en GPX o con un enlace."),
        ("Privacidad", "Sin publicidad, sin cuenta y sin herramientas de análisis. Con los mapas descargados tu posición no sale del teléfono.")]}
def index_vecchio():
    s = marchio(tema(leggi(NAVI + 'index.html')))
    s = re.sub(r'<title>.*?</title>', f'<title>{NOME}</title>', s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{NOME}: {HERO["en"][0]}. {HERO["en"][1]}">', s, count=1)
    hero = ''.join(f'<div class="l" data-l="{l}"><h1>{HERO[l][0]}</h1><p>{HERO[l][1]}</p><div class="soon">{HERO[l][2]}</div></div>' for l in LG)
    s = re.sub(r'(<section class="hero"><img src="immagini/icona.png" alt="[^"]*">).*?</section>', lambda m: f'<section class="hero"><img src="immagini/logo.png" alt="{NOME}">{hero}</section>', s, count=1, flags=re.S)
    main = ''.join(f'<div class="l" data-l="{l}"><h2>{HERO[l][3]}</h2><div class="grid">' + ''.join(f'<div class="card"><b>{t}</b>{x}</div>' for t, x in CARTE[l]) + '</div></div>' for l in LG)
    s = re.sub(r'<main>.*?</main>', '<main>' + main + '</main>', s, count=1, flags=re.S)
    return s

# --- informativa sulla privacy: quella di Navigator senza la parte dell'orologio e con "in moto" ---------------------
def privacy():
    s = marchio(tema(leggi(NAVI + 'privacy.html')))
    # via la sezione dell'orologio (h2 + paragrafo) in ogni lingua
    s, n = re.subn(r'<h2>[^<]*(Wear OS)[^<]*</h2><p>.*?</p>', '', s, flags=re.S); assert n == 5, n
    for vecchio, nuovo in (("Mentre navighi in auto", "Mentre navighi in moto"), ("While navigating by car", "While navigating by motorcycle"),
                           ("Pendant la navigation en voiture", "Pendant la navigation à moto"), ("Beim Navigieren im Auto", "Beim Navigieren mit dem Motorrad"),
                           ("Mientras navegas en coche", "Mientras navegas en moto")):
        s = s.replace(vecchio, nuovo)
    for h, nuovo in METEO_PRIVACY.items():
        if h in s: s = s.replace(h, nuovo + VIAGGIO_PRIVACY[h] + GRUPPO_PRIVACY[h] + h, 1)

    # con internet l'app e' "online first" e usa il nostro server: l'affermazione "non invia niente" vale solo senza internet
    for vecchio, nuovo in (("con le mappe scaricate: in quel caso la tua posizione non viene inviata a nessuno", "con le mappe scaricate e senza internet: in quel caso la tua posizione non viene inviata a nessuno"),
                           ("with downloaded maps: in that case your position is not sent to anyone", "with downloaded maps and no internet: in that case your position is not sent to anyone"),
                           ("avec les cartes téléchargées : dans ce cas votre position n'est envoyée à personne", "avec les cartes téléchargées et sans internet : dans ce cas votre position n'est envoyée à personne"),
                           ("Mit heruntergeladenen Karten können Sie sie vollständig auf dem Telefon nutzen: dann wird", "Mit heruntergeladenen Karten und ohne Internet können Sie sie vollständig auf dem Telefon nutzen: dann wird"),
                           ("con los mapas descargados: en ese caso tu posición no se envía a nadie", "con los mapas descargados y sin internet: en ese caso tu posición no se envía a nadie")):
        s = s.replace(vecchio, nuovo)
    print('privacy: ancora "auto":', len(re.findall(r'in auto|by car|en voiture|im Auto|en coche', s)))
    for vecchio, nuovo in (("16 ottobre 2026", "18 ottobre 2026"), ("16 October 2026", "18 October 2026"), ("16 octobre 2026", "18 octobre 2026"),
                           ("16. Oktober 2026", "18. Oktober 2026"), ("16 de octubre de 2026", "18 de octubre de 2026")):
        s = s.replace(vecchio, nuovo)
    # nell'informativa di Navigator la prima frase di "In breve" e' scritta due volte: qui una sola
    def senza_doppia(m):
        t = m.group(0); r = re.match(r'(<p>)([^<]*?\.) \2( .*)', t, re.S)
        return r.group(1) + r.group(2) + r.group(3) if r else t
    s = re.sub(r'<p>[^<]*</p>', senza_doppia, s)
    return s

METEO_PRIVACY = {   # sezione aggiunta all'informativa di Biker Maps: gli avvisi di pioggia mandano punti del percorso al nostro server
 '<h2>SOS in caso di caduta e tasto Aiuto</h2>': '<h2>Meteo e pioggia lungo il percorso</h2><p>Se lasci accesi gli avvisi di pioggia e temporale, mentre navighi l\'app manda al nostro server alcuni punti del percorso (circa uno ogni 8-25 km) con l\'orario previsto di passaggio, senza nome né identificativi, per sapere che tempo troverai. Il server li usa per chiedere le previsioni a MET Norway e per leggere il radar della pioggia della Protezione Civile, e non li conserva. Puoi spegnere questa funzione da Menu › Impostazioni › Funzioni in sella.</p>',
 '<h2>SOS in case of a fall and the Help button</h2>': '<h2>Weather and rain along the route</h2><p>If you leave the rain and thunderstorm alerts on, while you navigate the app sends our server a few points of the route (about one every 8-25 km) with the expected time of passage, with no name or identifiers, to know what weather you will find. The server uses them to ask MET Norway for forecasts and to read the Civil Protection rain radar, and does not keep them. You can turn this feature off from Menu › Settings › Riding features.</p>',
 '<h2>SOS en cas de chute et bouton Aide</h2>': '<h2>Météo et pluie sur l\'itinéraire</h2><p>Si vous laissez activées les alertes de pluie et d\'orage, pendant la navigation l\'application envoie à notre serveur quelques points de l\'itinéraire (environ un tous les 8 à 25 km) avec l\'heure de passage prévue, sans nom ni identifiant, pour savoir quel temps vous allez trouver. Le serveur les utilise pour demander les prévisions à MET Norway et lire le radar de pluie de la Protection civile, et ne les conserve pas. Vous pouvez désactiver cette fonction dans Menu › Réglages › Fonctions en selle.</p>',
 '<h2>SOS bei einem Sturz und Hilfe-Taste</h2>': '<h2>Wetter und Regen entlang der Route</h2><p>Wenn Sie die Regen- und Gewitterwarnungen eingeschaltet lassen, sendet die App während der Navigation einige Punkte der Route (etwa einen alle 8–25 km) mit der erwarteten Durchfahrtszeit an unseren Server, ohne Namen oder Kennungen, um zu wissen, welches Wetter Sie erwartet. Der Server nutzt sie, um bei MET Norway die Vorhersagen abzufragen und das Regenradar des Zivilschutzes zu lesen, und speichert sie nicht. Sie können diese Funktion unter Menü › Einstellungen › Funktionen unterwegs ausschalten.</p>',
 '<h2>SOS en caso de caída y botón Ayuda</h2>': '<h2>Tiempo y lluvia en la ruta</h2><p>Si dejas activados los avisos de lluvia y tormenta, mientras navegas la app envía a nuestro servidor algunos puntos de la ruta (uno cada 8-25 km aprox.) con la hora prevista de paso, sin nombre ni identificadores, para saber qué tiempo encontrarás. El servidor los usa para pedir las previsiones a MET Norway y leer el radar de lluvia de Protección Civil, y no los conserva. Puedes desactivar esta función en Menú › Ajustes › Funciones en ruta.</p>',
}

VIAGGIO_PRIVACY = {   # "Segui il mio viaggio" e allarme di mancato arrivo (fase 11)
 '<h2>SOS in caso di caduta e tasto Aiuto</h2>': '<h2>Segui il mio viaggio e allarme di mancato arrivo</h2><p>Solo se tocchi "Segui il mio viaggio", l\'app crea sul nostro server un link con un codice casuale e, mentre navighi, gli manda la tua posizione e la velocità circa ogni 15 secondi (e le ultime posizioni del tragitto). Chi riceve il link la vede su una mappa; non servono account. Non salviamo il tuo indirizzo IP né il tuo nome (a meno che tu l\'abbia scritto nelle impostazioni SOS, perché compaia nella pagina). Il link e i dati vengono cancellati alla scadenza che scegli (da 2 a 24 ore), quando termini la navigazione o quando tocchi "Smetti di condividere il viaggio". L\'allarme di mancato arrivo (spento di base) e la scatola nera (spenta di base) funzionano solo sul telefono: l\'allarme manda un SMS ai numeri che hai scelto, la scatola nera non esce mai dal telefono salvo che la esporti tu.</p>',
 '<h2>SOS in case of a fall and the Help button</h2>': '<h2>Follow my trip and missed-arrival alarm</h2><p>Only if you tap "Follow my trip", the app creates a link with a random code on our server and, while you navigate, sends it your position and speed about every 15 seconds (and the latest positions of the route). Whoever receives the link sees it on a map; no accounts are needed. We do not store your IP address or your name (unless you wrote it in the SOS settings so that it appears on the page). The link and data are deleted at the expiry you choose (2 to 24 hours), when you end navigation or when you tap "Stop sharing the trip". The missed-arrival alarm (off by default) and the black box (off by default) work only on the phone: the alarm sends an SMS to the numbers you chose, the black box never leaves the phone unless you export it.</p>',
 '<h2>SOS en cas de chute et bouton Aide</h2>': '<h2>Suivre mon trajet et alarme d\'arrivée manquée</h2><p>Seulement si vous touchez "Suivre mon trajet", l\'application crée sur notre serveur un lien avec un code aléatoire et, pendant la navigation, lui envoie votre position et votre vitesse environ toutes les 15 secondes (et les dernières positions du trajet). Le destinataire du lien la voit sur une carte ; aucun compte n\'est nécessaire. Nous ne conservons ni votre adresse IP ni votre nom (sauf si vous l\'avez saisi dans les réglages SOS pour qu\'il apparaisse sur la page). Le lien et les données sont effacés à l\'expiration choisie (de 2 à 24 heures), quand vous terminez la navigation ou quand vous touchez "Arrêter de partager le trajet". L\'alarme d\'arrivée manquée (désactivée par défaut) et la boîte noire (désactivée par défaut) fonctionnent uniquement sur le téléphone : l\'alarme envoie un SMS aux numéros choisis, la boîte noire ne quitte jamais le téléphone sauf si vous l\'exportez.</p>',
 '<h2>SOS bei einem Sturz und Hilfe-Taste</h2>': '<h2>Meine Fahrt verfolgen und Alarm bei Nichtankunft</h2><p>Nur wenn Sie "Meine Fahrt verfolgen" antippen, erstellt die App auf unserem Server einen Link mit einem Zufallscode und sendet ihm während der Navigation etwa alle 15 Sekunden Ihre Position und Geschwindigkeit (und die letzten Positionen der Strecke). Wer den Link erhält, sieht sie auf einer Karte; Konten sind nicht nötig. Wir speichern weder Ihre IP-Adresse noch Ihren Namen (außer Sie haben ihn in den SOS-Einstellungen eingetragen, damit er auf der Seite erscheint). Link und Daten werden zum gewählten Ablauf (2 bis 24 Stunden), beim Beenden der Navigation oder bei "Fahrt nicht mehr teilen" gelöscht. Der Alarm bei Nichtankunft (standardmäßig aus) und die Blackbox (standardmäßig aus) funktionieren nur auf dem Telefon: Der Alarm sendet eine SMS an die gewählten Nummern, die Blackbox verlässt das Telefon nur, wenn Sie sie exportieren.</p>',
 '<h2>SOS en caso de caída y botón Ayuda</h2>': '<h2>Seguir mi viaje y alarma de llegada</h2><p>Solo si tocas "Seguir mi viaje", la app crea en nuestro servidor un enlace con un código aleatorio y, mientras navegas, le envía tu posición y velocidad cada 15 segundos aproximadamente (y las últimas posiciones del trayecto). Quien recibe el enlace la ve en un mapa; no hacen falta cuentas. No guardamos tu dirección IP ni tu nombre (salvo que lo hayas escrito en los ajustes de SOS para que aparezca en la página). El enlace y los datos se borran al caducar según lo elegido (de 2 a 24 horas), al terminar la navegación o al tocar "Dejar de compartir el viaje". La alarma de llegada (apagada por defecto) y la caja negra (apagada por defecto) funcionan solo en el teléfono: la alarma envía un SMS a los números elegidos, la caja negra no sale nunca del teléfono salvo que la exportes.</p>',
}

GRUPPO_PRIVACY = {'<h2>SOS in caso di caduta e tasto Aiuto</h2>': '<p><b>Giro di gruppo.</b> Solo se crei o entri in un gruppo, mentre navighi l\'app manda al nostro server il nome che hai scelto (quello delle impostazioni SOS, o "Rider"), la posizione e la velocità circa ogni 10 secondi, e riceve quelle degli altri membri. Il gruppo ha un codice casuale e non servono account; non salviamo il tuo indirizzo IP. Il gruppo e i dati si cancellano alla scadenza (da 6 a 24 ore) o quando esci. Chi non ha l\'app può vedere il gruppo su una pagina web con il link. Le funzioni "comandi dal casco", "note stile rally", "riepilogo del giro" e "le mie strade" funzionano solo sul telefono.</p>', '<h2>SOS in case of a fall and the Help button</h2>': '<p><b>Group ride.</b> Only if you create or join a group, while you navigate the app sends our server the name you chose (the one in the SOS settings, or "Rider"), your position and speed about every 10 seconds, and receives those of the other members. The group has a random code and no accounts are needed; we do not store your IP address. The group and its data are deleted at expiry (6 to 24 hours) or when you leave. Anyone without the app can see the group on a web page with the link. "Helmet controls", "rally-style notes", "ride summary" and "my roads" work on the phone only.</p>', '<h2>SOS en cas de chute et bouton Aide</h2>': "<p><b>Sortie de groupe.</b> Seulement si vous créez un groupe ou le rejoignez, pendant la navigation l'application envoie à notre serveur le nom choisi (celui des réglages SOS, ou « Rider »), la position et la vitesse environ toutes les 10 secondes, et reçoit celles des autres membres. Le groupe a un code aléatoire et aucun compte n'est nécessaire ; nous ne conservons pas votre adresse IP. Le groupe et les données sont effacés à l'expiration (de 6 à 24 heures) ou quand vous le quittez. Ceux qui n'ont pas l'application peuvent voir le groupe sur une page web avec le lien. Les fonctions « commandes du casque », « notes de style rallye », « résumé du trajet » et « mes routes » fonctionnent uniquement sur le téléphone.</p>", '<h2>SOS bei einem Sturz und Hilfe-Taste</h2>': '<p><b>Gruppenfahrt.</b> Nur wenn Sie eine Gruppe erstellen oder ihr beitreten, sendet die App während der Navigation den gewählten Namen (aus den SOS-Einstellungen, oder „Rider“), Position und Geschwindigkeit etwa alle 10 Sekunden an unseren Server und empfängt die der anderen Mitglieder. Die Gruppe hat einen Zufallscode, Konten sind nicht nötig; wir speichern Ihre IP-Adresse nicht. Gruppe und Daten werden bei Ablauf (6 bis 24 Stunden) oder beim Austritt gelöscht. Wer die App nicht hat, kann die Gruppe mit dem Link auf einer Webseite sehen. „Helmsteuerung“, „Rallye-Aufschriebe“, „Fahrtzusammenfassung“ und „meine Straßen“ funktionieren nur auf dem Telefon.</p>', '<h2>SOS en caso de caída y botón Ayuda</h2>': '<p><b>Ruta en grupo.</b> Solo si creas un grupo o entras en uno, mientras navegas la app envía a nuestro servidor el nombre elegido (el de los ajustes de SOS, o «Rider»), la posición y la velocidad cada 10 segundos aproximadamente, y recibe las de los demás miembros. El grupo tiene un código aleatorio y no hacen falta cuentas; no guardamos tu dirección IP. El grupo y sus datos se borran al caducar (de 6 a 24 horas) o al salir. Quien no tiene la app puede ver el grupo en una página web con el enlace. «Controles del casco», «notas estilo rally», «resumen de la ruta» y «mis carreteras» funcionan solo en el teléfono.</p>'}

# --- tutte le funzioni: dalle guide di Biker Maps -------------------------------------------------------------------
def funzioni():
    s = marchio(tema(leggi(NAVI + 'funzioni.html')))
    blocchi = []
    for lg in LG:
        g = leggi(GUIDE + G[lg]); h1 = re.search(r'<h1>(.*?)</h1>', g, re.S).group(1); sotto = re.search(r'<p class="sotto">(.*?)</p>', g, re.S).group(1)
        corpo = g[g.index('<nav>'):g.index('</body>')]
        corpo = re.sub(r'id="([a-z]+)"', lambda m: f'id="{m.group(1)}-{lg}"', corpo); corpo = re.sub(r'href="#([a-z]+)"', lambda m: f'href="#{m.group(1)}-{lg}"', corpo)
        blocchi.append(f'<div class="l fz" data-l="{lg}">\n<h1>{h1}</h1>\n<p class="sotto">{sotto}</p>\n\n{corpo}</div>\n')
    a = s.index('<main>') + len('<main>'); b = s.index('</main>')
    return s[:a] + ''.join(blocchi) + s[b:]

import home
def autosufficiente(h):
    """Logo e icona dentro il file (data URI): la pagina si vede anche se si ricevono solo i file .html senza la cartella immagini."""
    import io, base64
    from PIL import Image
    def uri(path, lato):
        im = Image.open(path).convert('RGBA'); im.thumbnail((lato, lato), Image.LANCZOS); im = im.quantize(256, method=Image.Quantize.FASTOCTREE); b = io.BytesIO(); im.save(b, 'PNG', optimize=True)
        return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
    return h.replace('immagini/logo.png', uri('immagini/logo.png', 520)).replace('immagini/icona.png', uri('immagini/icona.png', 96))
def index(): return home.pagina()
if __name__ == '__main__':
    for nome, f in (('index.html', index), ('privacy.html', privacy), ('funzioni.html', funzioni)):
        open(nome, 'w', encoding='utf-8').write(autosufficiente(f())); print(nome, 'scritto')
