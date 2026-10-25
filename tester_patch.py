#!/usr/bin/env python3
"""Trasforma index.html in "pagina per reclutare i tester" SOLO tra INIZIO e FINE (date nel JS).
Fuori da quelle date la pagina torna da sola quella originale (il pulsante "Presto su Google Play" e basta).
Uso: python3 tester_patch.py [cartella ...]   (default: cartella corrente). E' idempotente.
Chiamata anche da genera.py dopo aver scritto index.html. Le date si cambiano qui sotto e si rilancia."""
import re, sys

LINK = "https://play.google.com/apps/testing/it.idq.bikermaps"   # opt-in del test chiuso (Play Console > Test chiusi > Alpha > Tester)
GRUPPO = "https://groups.google.com/g/idq-biker-maps-tester"
CODICE = "https://play.google.com/redeem?code=TESTREVISIONE"
INIZIO = "2026-10-24"   # il codice promozionale e' valido dal 24/10/2026 alle 23:30; pagina tester attiva da subito per provarla
FINE = "2027-01-22"     # dopo questa data la pagina e' di nuovo quella originale

CSS = """
.tonly{display:none}html.tst .tonly{display:block}html.tst .tbar.tonly{display:flex}html.tst .orig{display:none}
.tbar{position:fixed;left:0;right:0;bottom:0;z-index:40;background:rgba(7,7,10,.94);border-top:2px solid var(--ac);padding:10px 14px;gap:12px;align-items:center;justify-content:center;flex-wrap:wrap}
.tbar span{font-weight:700}.tbar .btn{margin:0;padding:10px 22px;border:0;cursor:pointer;font:inherit;font-weight:800}
html.tst body{padding-bottom:72px}
.ban{background:linear-gradient(90deg,#ff7a00,#ffb25b);color:#000;text-align:center;padding:9px 14px;font-weight:800}
#fin{position:fixed;inset:0;background:rgba(0,0,0,.78);display:none;align-items:center;justify-content:center;padding:14px;z-index:60}
#fin.on{display:flex}
#fin .m{background:#101016;border:1px solid var(--ac);border-radius:20px;max-width:560px;width:100%;max-height:92vh;overflow:auto;padding:22px}
#fin h3{margin:0 0 8px;font-size:24px}
#fin ol{padding-left:0;list-style:none;counter-reset:p;margin:10px 0}
#fin li{counter-increment:p;position:relative;padding:9px 0 9px 46px;border-top:1px solid var(--bd)}
#fin li::before{content:counter(p);position:absolute;left:0;top:9px;width:32px;height:32px;border-radius:50%;background:var(--ac);color:#000;font-weight:900;display:flex;align-items:center;justify-content:center}
#fin .az{display:flex;gap:10px;flex-wrap:wrap;margin-top:8px}
#fin .btn{margin:0;border:0;cursor:pointer;font:inherit;font-weight:800;padding:12px 22px}
#fin .btn.s{background:transparent;border:2px solid var(--ac2);color:#fff}
#fin .nota{color:var(--mu);font-size:14px}
"""
BAN = '<div class="ban tonly">Cerchiamo tester: usa IDQ Biker Maps GRATIS per 90 giorni</div>'
TBAR = '<div class="tbar tonly" id="tbar"><span>Prova l\'app gratis per 90 giorni</span><button class="btn p" type="button" data-tester>Voglio fare il tester</button></div>'
BTN = ('<button class="btn p tonly" type="button" data-tester style="border:0;cursor:pointer;font:inherit;font-weight:700">'
       '<span class="l" data-l="it">Voglio fare il tester (gratis 90 giorni)</span><span class="l" data-l="en">Become a tester (free 90 days)</span>'
       '<span class="l" data-l="fr">Devenir testeur (90 jours gratuits)</span><span class="l" data-l="de">Tester werden (90 Tage gratis)</span>'
       '<span class="l" data-l="es">Ser tester (90 d&iacute;as gratis)</span></button>')
FIN = f"""<div id="fin" role="dialog" aria-modal="true" aria-labelledby="fint"><div class="m">
<h3 id="fint">Prima di scaricare: come avere l'app gratis</h3>
<p>L'app è in abbonamento, ma <b>per i tester è gratis per 90 giorni</b>. Ti servono 3 minuti:</p>
<ol>
<li><b>Usa il telefono Android</b>, con lo stesso account Google che usi nel Play Store. Dal computer l'ultimo passaggio può restare bianco.</li>
<li>Iscriviti al <a href="{GRUPPO}" target="_blank" rel="noopener">gruppo dei tester</a>: tocca "Partecipa al gruppo". Se Google chiede conferme, accetta.</li>
<li>Tocca "Vai al download" qui sotto e poi "Diventa un tester".</li>
<li>Tocca il link per scaricare l'app da Google Play e installa. <b>Se compare una finestra bianca o vuota di Google Play, non è un errore tuo né dell'app:</b> Google non ti ha ancora riconosciuto come tester, e succede quasi sempre nella prima ora dopo l'iscrizione al gruppo. Chiudi la finestra, <b>aspetta 30-60 minuti</b> (puoi anche spegnere e riaccendere il telefono) e riapri lo stesso link con lo stesso account. Poi, nell'app <b>Play Store</b> del telefono, cerca "IDQ Biker Maps": quando compare il pulsante Installa, ci sei. Se dopo un'ora è ancora bianco, scrivici a <a href="mailto:info@idq-developer.com">info@idq-developer.com</a>.</li>
<li>Apri l'app: compare la schermata dei piani. Tocca <b>Abbonati</b> sul piano annuale.</li>
<li>Nella finestra di pagamento di Google Play tocca la <b>freccia accanto al metodo di pagamento</b>, poi <b>Riscatta codice</b>, scrivi <b>TESTREVISIONE</b> (tutto maiuscolo, senza spazi) e conferma. Il codice funziona solo da qui, non dal campo "Riscatta codice" del Play Store. L'abbonamento parte a 0 € per 90 giorni.</li>
</ol>
<p class="nota">Ti chiediamo di tenere l'app installata per 14 giorni e di scriverci se trovi problemi: <a href="mailto:info@idq-developer.com">info@idq-developer.com</a>. Dopo 90 giorni l'abbonamento si rinnova a pagamento (19,99 € il primo anno) se non lo annulli da Google Play: Pagamenti e abbonamenti, Abbonamenti, IDQ Biker Maps, Annulla.</p>
<div class="az"><a class="btn p" href="{LINK}" target="_blank" rel="noopener">Vai al download</a><button class="btn s" id="chiudi" type="button">Chiudi</button></div>
</div></div>
"""
JS = f"""<script>
(function(){{
var INIZIO="{INIZIO}",FINE="{FINE}"; // tra queste date la pagina e' quella "per tester"; fuori, quella originale
var oggi=new Date().toISOString().slice(0,10);
if(oggi<INIZIO||oggi>FINE)return;
document.documentElement.classList.add("tst");
var fin=document.getElementById("fin"),bt=document.querySelectorAll("[data-tester]");
function apri(){{fin.classList.add("on")}}function chiudi(){{fin.classList.remove("on")}}
for(var j=0;j<bt.length;j++)bt[j].addEventListener("click",apri);
document.getElementById("chiudi").addEventListener("click",chiudi);
fin.addEventListener("click",function(e){{if(e.target===fin)chiudi()}});
document.addEventListener("keydown",function(e){{if(e.key==="Escape")chiudi()}});
}})();
</script>"""


def patch(h):
    if 'data-tester' in h:
        return h
    n = 0
    # il pulsante originale resta (classe orig) e il pulsante tester gli viene affiancato
    h, k = re.subn(r'<span class="btn p off">(.*?)</span></span>',
                   lambda m: '<span class="btn p off orig">' + m.group(1) + '</span></span>' + BTN, h, count=1, flags=re.S); n += k
    h, k = re.subn(r'</style></head><body>', lambda m: CSS + '</style></head><body>\n' + BAN, h, count=1); n += k
    h, k = re.subn(r'</body></html>', lambda m: TBAR + FIN + JS + '</body></html>', h, count=1); n += k
    assert n == 3, 'struttura di index.html cambiata: %d/3' % n
    return h


# Voci che parlano della prova di 7 giorni: nascoste durante il periodo tester (classe "orig"), tornano alla fine
SENZA_PROVA = [
    ('<a href="#prova">', '<a class="orig" href="#prova">'),
    ('<section id="prova">', '<section id="prova" class="orig">'),
    ('<a href="#prezzi">', '<a class="orig" href="#prezzi">'),
    ('<section id="prezzi">', '<section id="prezzi" class="orig">'),
    ('<span><span class="l" data-l="it">Prova gratis 7 giorni', '<span class="orig"><span class="l" data-l="it">Prova gratis 7 giorni'),
    ('<details class="f"><summary><span class="l" data-l="it">Quanto costa', '<details class="f orig"><summary><span class="l" data-l="it">Quanto costa'),
    ('<details class="f"><summary><span class="l" data-l="it">Posso provare', '<details class="f orig"><summary><span class="l" data-l="it">Posso provare'),
]


def senza_prova(h):
    for a, b in SENZA_PROVA:
        if b in h:
            continue
        assert h.count(a) == 1, 'non trovato: ' + a[:50]
        h = h.replace(a, b)
    return h


if __name__ == '__main__':
    for d in (sys.argv[1:] or ['.']):
        p = d.rstrip('/') + '/index.html'
        h = open(p, encoding='utf-8').read()
        o = senza_prova(patch(h))
        if o != h:
            open(p, 'w', encoding='utf-8').write(o); print(p, 'ok: pagina tester dal', INIZIO, 'al', FINE)
        else:
            print(p, 'gia\' presente')
