import json

rich_offers = {
    "costa-oest": {
        "title": "Costa Oest dels Estats Units en cotxe de lloguer",
        "subtitle": "Los Angeles - Grand Canyon - Monument Valley - Las Vegas - Death Valley - Yosemite - San Francisco",
        "duration": "15 dies / 14 nits",
        "price": "2.595 €",
        "tag": "Cotxe de lloguer",
        "badgeIcon": "fa-car",
        "heroImage": "https://images.gestionaweb.cat/1231/img-640-480/grand-canyon-copia.jpg",
        "highlights": "SIGUES TU EL PROTAGONISTA: VIU LA COSTA OEST DELS ESTATS UNITS COM SEMPRE L'HAS VIST A LES PEL·LÍCULES.",
        "gallery": [
            "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1534430480872-3498386e7856?auto=format&fit=crop&w=800&q=80"
        ],
        "itinerary": [
            {"day": "DIA 01", "title": "Barcelona - Los Angeles", "desc": "Vol cap a Los Angeles. Recollida del cotxe de lloguer a l'aeroport i trasllat a l'hotel."},
            {"day": "DIA 02-03", "title": "Los Angeles", "desc": "Explora Hollywood Walk of Fame, Beverly Hills, Santa Monica Pier i Venice Beach."},
            {"day": "DIA 04", "title": "Los Angeles - Grand Canyon", "desc": "Ruta per la mítica Ruta 66 cap a la magnificència del Gran Canó del Colorado."},
            {"day": "DIA 05", "title": "Grand Canyon - Monument Valley", "desc": "Submergeix-te en el paisatge icònic dels vaquers entre les torres de sorra vermella."},
            {"day": "DIA 06-07", "title": "Monument Valley - Las Vegas", "desc": "Arribada a la capital mundial de l'entreteniment i els llums de neó."},
            {"day": "DIA 08", "title": "Las Vegas - Death Valley", "desc": "Creua el desert més extrem d'Amèrica del Nord amb vistes espectaculars a Zabriskie Point."},
            {"day": "DIA 09-10", "title": "Death Valley - Yosemite", "desc": "Parc Nacional de Yosemite: seqüoies gegants, cascades impressionants i el massís d'El Capitan."},
            {"day": "DIA 11-13", "title": "Yosemite - San Francisco", "desc": "Visita a la ciutat de les turons, Golden Gate, tramvia històric i entrada inclosa a l'illa d'Alcatraz."},
            {"day": "DIA 14-16", "title": "San Francisco - St. Luis Obispo - Los Angeles - BCN", "desc": "Retorn per la costa de Califòrnia (Highway 1) i vol de tornada a Barcelona."}
        ],
        "included": [
            "Vols Barcelona - Los Angeles - Barcelona",
            "Cotxe de lloguer inclòs per a tots els dies amb recollida i devolució a l'aeroport",
            "14 nits d'allotjament seleccionat als millors punts de la ruta",
            "Entrades incloses a l'illa d'Alcatraz (San Francisco)",
            "Assegurança d'anul·lació i assistència en viatge",
            "Tramitació del visat d'entrada ESTA"
        ]
    },
    "aurores": {
        "title": "Tromsø & Aurores Boreals (Noruega)",
        "subtitle": "Tromsø - Cap Nord - Fiords Àrtics",
        "duration": "7 dies / 6 nits",
        "price": "1.890 €",
        "tag": "Nova Destinació",
        "badgeIcon": "fa-snowflake",
        "heroImage": "tromso/TROMSO (16).jpg",
        "highlights": "Viu l'espectacle màgic de les aurores boreals i submergeix-te en la natura àrtica en estat pur.",
        "gallery": [
            "tromso/TROMSO (14).jpg",
            "tromso/TROMSO (5).jpg",
            "tromso/TROMSO (22).jpg"
        ],
        "itinerary": [
            {"day": "DIA 01", "title": "BCN - Oslo - Tromsø", "desc": "Vols a Tromsø, la capital de les Aurores Boreals. Trasllat privat a l'hotel boutique."},
            {"day": "DIA 02", "title": "Tromsø & Caça d'Aurores", "desc": "Visita a la ciutat i per la nit excursió guiada amb fotògraf expert per caçar el fenomen de les llums del nord."},
            {"day": "DIA 03", "title": "Safari en Trineu de Gossos Husky", "desc": "Aventura inoblidable conduint el teu propi trineu de huskies a través de la vall àrtica coberta de neu."},
            {"day": "DIA 04", "title": "Creuer de Navegació pels Fiords Àrtics", "desc": "Navegació silenciosa entre majestuosos fiords noruecs amb possibilitat d'avistar balenes i àligues marines."},
            {"day": "DIA 05", "title": "Expedició a Cap Nord", "desc": "Viatge al punt més septentrional d'Europa, un penya-segat impressionant sobre l'Oceà Àrtic."},
            {"day": "DIA 06-07", "title": "Tromsø - Oslo - Barcelona", "desc": "Temps lliure per gaudir de la gastronomia local i vol de retorn."}
        ],
        "included": [
            "Vols Barcelona - Oslo - Tromsø - Barcelona",
            "6 nits d'allotjament en hotel 4* amb esmorzar bufet inclòs",
            "Excursió nocturna guiada de Caça d'Aurores Boreals amb equip tèrmic",
            "Safari en trineu de gossos Husky amb guia local",
            "Creuer panoràmic pels fiords àrtics",
            "Trasllats privats aeroport-hotel-aeroport i assegurança de viatge completa"
        ]
    },
    "bali": {
        "title": "Indonèsia & Bali Paradís Tropical",
        "subtitle": "Ubud - Illes Gili Trawangan - Nusa Dua",
        "duration": "10 dies / 8 nits",
        "price": "1.500 €",
        "tag": "Exòtic",
        "badgeIcon": "fa-umbrella-beach",
        "heroImage": "bali/Still 2025-10-11 020237_1.207.1.jpg",
        "highlights": "Temples enigmàtics entre la natura, terrasses d'arròs i platges de sorra blanca a Ubud i Gili Trawangan.",
        "gallery": [
            "bali/Still 2025-10-11 020237_1.195.1.jpg",
            "bali/Still 2025-10-11 020237_1.199.1.jpg",
            "bali/Still 2025-10-11 020237_1.176.1.jpg"
        ],
        "itinerary": [
            {"day": "DIA 01-02", "title": "Barcelona - Denpasar - Ubud", "desc": "Vol cap a Bali. Arribada a la capital cultural d'Ubud entre boscos tropicals i santuaris."},
            {"day": "DIA 03-04", "title": "Ubud, Temples & Terrasses d'Arròs", "desc": "Exploració del Sacred Monkey Forest, temple Tirta Empul, terrasses de Tegallalang i cascades amagades."},
            {"day": "DIA 05", "title": "Ubud - Ferry ràpid a Gili Trawangan", "desc": "Trasllat al port i trajecte en vaixell ràpid cap al paradís sense cotxes de les Illes Gili."},
            {"day": "DIA 06-08", "title": "Platges i Snorkel a Gili Trawangan", "desc": "Dies de relax, snorkel amb tortugues marines, postes de soles mítiques i sopars a la sorra."},
            {"day": "DIA 09-10", "title": "Gili Trawangan - Denpasar - Barcelona", "desc": "Retorn en vaixell a Bali i vol de tornada amb records inoblidables."}
        ],
        "included": [
            "Vols Barcelona - Denpasar (Bali) - Barcelona",
            "Trasllats privats en vehicle climatitzat amb xofer",
            "Ferry ràpid anada i tornada a les Illes Gili Trawangan",
            "3 nits a Ubud en hotel 4* amb esmorzar inclòs",
            "5 nits a Gili Trawangan en resort 4* davant del mar",
            "Assegurança de viatge d'anul·lació i assistència mèdica"
        ]
    },
    "londres": {
        "title": "Londres Infinita & Escapada Urbana",
        "subtitle": "Westminster - Soho - Camden Town - Borough Market",
        "duration": "4 dies / 3 nits",
        "price": "495 €",
        "tag": "Escapada",
        "badgeIcon": "fa-building-columns",
        "heroImage": "https://images.gestionaweb.cat/1231/img-640-480/xdonde-comprar-jamon-iberico-en-londres-e1519286706822-jpg-pagespeed-ic-9ptlqofzcm-1100236.jpg",
        "highlights": "Londres us espera amb mil i un plans: museus fascinants, canvi de guàrdia, London Eye i el millor street food.",
        "gallery": [
            "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1526129318478-62ed807ebdf9?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1486299267070-83823f5448dd?auto=format&fit=crop&w=800&q=80"
        ],
        "itinerary": [
            {"day": "DIA 01", "title": "Barcelona - Londres", "desc": "Vol a Londres. Trasllat privat a l'hotel. Passeig per Piccadilly Circus, Leicester Square i Soho."},
            {"day": "DIA 02", "title": "Westminster & London Eye", "desc": "Visita al Buckingham Palace, Big Ben, Abadia de Westminster i pujada inclosa a la nòria London Eye."},
            {"day": "DIA 03", "title": "Camden Town & British Museum", "desc": "Matí al mercat alternatiu de Camden. Per la tarda, visita lliure al British Museum i Borough Market."},
            {"day": "DIA 04", "title": "Hyde Park & Vol de Tornada", "desc": "Passeig pels jardins de Hyde Park o shopping a Oxford Street abans del trasllat a l'aeroport."}
        ],
        "included": [
            "Vols Barcelona - Londres - Barcelona",
            "Trasllat privat aeroport - hotel - aeroport",
            "3 nits d'allotjament a l'hotel Premier Inn o similar amb esmorzar bufet inclòs",
            "Guia recomanada de racons exclusius i assistència 24h"
        ]
    },
    "argentina": {
        "title": "Argentina Indispensable",
        "subtitle": "Buenos Aires - Calafate (Perito Moreno) - Cataractes de l'Iguazú",
        "duration": "11 dies / 8 nits",
        "price": "2.200 €",
        "tag": "Gran Viatge",
        "badgeIcon": "fa-earth-americas",
        "heroImage": "https://images.gestionaweb.cat/1231/img-640-480/iguazu.jpg",
        "highlights": "GAUDEIX D'ARGENTINA AL TEU AIRE: Des del ritme del tango fins a les glaceres de la Patagònia i la força d'Iguazú.",
        "gallery": [
            "https://images.unsplash.com/photo-1589802829985-817e51171b92?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1545830790-68595959c491?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1518638150340-f706e86654de?auto=format&fit=crop&w=800&q=80"
        ],
        "itinerary": [
            {"day": "DIA 01-02", "title": "Barcelona - Buenos Aires", "desc": "Vol internacional a la capital del Tango. Visita per San Telmo, La Boca, la Plaza de Mayo i Recoleta."},
            {"day": "DIA 03-05", "title": "El Calafate & Glacera Perito Moreno", "desc": "Vol a la Patagònia. Excursió a la majestuosa glacera Perito Moreno amb passarel·les i opció de navegació."},
            {"day": "DIA 06-08", "title": "Cataractes de l'Iguazú", "desc": "Vol al nord de l'Argentina. Descobreix la Garganta del Diablo i els senders del Parc Nacional Iguazú."},
            {"day": "DIA 09-11", "title": "Buenos Aires - Barcelona", "desc": "Última nit a Buenos Aires amb sopar xou de Tango opcional i vol de retorn a Barcelona."}
        ],
        "included": [
            "Vols internacionals Barcelona - Buenos Aires - Barcelona",
            "Vols domèstics: Buenos Aires - Calafate - Iguazú - Buenos Aires",
            "3 nits a Buenos Aires amb esmorzar inclòs",
            "3 nits a El Calafate amb esmorzar inclòs",
            "2 nits a Iguazú amb esmorzar inclòs",
            "Tots els trasllats aeroport - hotel - aeroport i assegurança de viatge"
        ]
    },
    "timisoara": {
        "title": "Timișoara & Encants de Transilvània",
        "subtitle": "Timișoara - Castell de Corvin - Alba Iulia",
        "duration": "5 dies / 4 nits",
        "price": "450 €",
        "tag": "Cultura",
        "badgeIcon": "fa-landmark",
        "heroImage": "timisoara/Still 2025-12-03 141455_1.33.1.jpg",
        "highlights": "Descobreix l'arquitectura barroca, la història vibrant i els palaus de la que va ser Capital Europea de la Cultura.",
        "gallery": [
            "timisoara/Still 2025-12-03 141455_1.1.1.jpg",
            "timisoara/Still 2025-12-03 141455_1.20.1.jpg",
            "timisoara/Still 2025-12-03 141455_1.45.1.jpg"
        ],
        "itinerary": [
            {"day": "DIA 01", "title": "Barcelona - Timișoara", "desc": "Vol a la petita Viena de Romania. Arribada i trasllat a l'hotel situat al barri històric."},
            {"day": "DIA 02", "title": "Centre Històric & Plaça de la Victòria", "desc": "Visita guiada a la Catedral Ortodoxa, el Palau Lloyd, la Plaça de la Llibertat i arquitectura Secession."},
            {"day": "DIA 03", "title": "Excursió al Castell de Corvin i Alba Iulia", "desc": "Excursió de dia sencer al castell gòtic més espectacular de Romania i la fortalesa d'Alba Iulia."},
            {"day": "DIA 04-05", "title": "Passeig pels Parcs del Riu Bega & Tornada", "desc": "Temps lliure per gaudir de terrasses, museus i vol de tornada a Barcelona."}
        ],
        "included": [
            "Vols Barcelona - Timișoara - Barcelona",
            "4 nits en hotel 4* al centre històric amb esmorzar bufet inclòs",
            "Trasllats privats aeroport - hotel - aeroport",
            "Visita guiada en català/castellà pel barri monumental",
            "Assegurança de viatge completa"
        ]
    },
    "roma": {
        "title": "Roma Eterna & Escapada Històrica",
        "subtitle": "Colosseu - Vaticà - Trastevere - Font de Trevi",
        "duration": "4 dies / 3 nits",
        "price": "395 €",
        "tag": "Escapada",
        "badgeIcon": "fa-monument",
        "heroImage": "https://images.gestionaweb.cat/1231/img-640-480/vertic-880-0-1100242.jpg",
        "highlights": "Caminar pels seus carrers és passejar per milers d'anys d'història, art de Miquel Àngel, Bernini i Caravaggio.",
        "gallery": [
            "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1531572753322-ad063cecc140?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1529260830199-42c24126f198?auto=format&fit=crop&w=800&q=80"
        ],
        "itinerary": [
            {"day": "DIA 01", "title": "Barcelona - Roma", "desc": "Vol a la Ciutat Eterna. Trasllat a l'hotel. Primera passejada fins a la Font de Trevi i Piazza Navona."},
            {"day": "DIA 02", "title": "Colosseu, Fòrum Romà & Palatí", "desc": "Visita monumental a les restes de l'Imperi Romà i tarda de gelato al barri de Trastevere."},
            {"day": "DIA 03", "title": "Museus Vaticans & Capella Sixtina", "desc": "Visita als Museus Vaticans, la Basílica de Sant Pere i el Castell Sant'Angelo."},
            {"day": "DIA 04", "title": "Piazza del Popolo & Vol de Tornada", "desc": "Passeig pels jardins de Villa Borghese i retorn a Barcelona."}
        ],
        "included": [
            "Vols Barcelona - Roma - Barcelona",
            "Trasllat privat aeroport - hotel - aeroport",
            "3 nits d'allotjament en hotel 4* amb esmorzar inclòs",
            "Assegurança de viatge i assistència en destí"
        ]
    },
    "thailandia": {
        "title": "Tailàndia al Complet",
        "subtitle": "Bangkok - Chiang Mai - Illes Krabi",
        "duration": "13 dies / 12 nits",
        "price": "1.600 €",
        "tag": "Àsia",
        "badgeIcon": "fa-vihara",
        "heroImage": "https://images.gestionaweb.cat/1231/img-640-480/colo8.jpg",
        "highlights": "Circuits en privat, guies en català/castellà, temples daurats i les millors platges de les illes del Sud.",
        "gallery": [
            "https://images.unsplash.com/photo-1506665531195-3566fe2966e4?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1528181304800-259b08848526?auto=format&fit=crop&w=800&q=80"
        ],
        "itinerary": [
            {"day": "DIA 01-02", "title": "Barcelona - Bangkok", "desc": "Vol internacional. Arribada a la vibrant capital tailandesa. Allotjament en hotel 4*."},
            {"day": "DIA 03-05", "title": "Bangkok, Temples & Mercats Flotants", "desc": "Visita al Palau Reial, Wat Pho, Ayutthaya amb creuer pel riu i Mercat Flotant de Damnoen Saduak."},
            {"day": "DIA 06-08", "title": "Chiang Mai & Muntanyes del Nord", "desc": "Vol al nord. Trekking d'un dia, cascada, santuari d'elefants ètic i mercat nocturn."},
            {"day": "DIA 09-12", "title": "Illes de Krabi & Phi Phi Islands", "desc": "Vol a Krabi. Dies de relaxació total en platges de sorra blanca, snorkel i excursió en Longtail boat a Phi Phi."},
            {"day": "DIA 13", "title": "Krabi - Bangkok - Barcelona", "desc": "Vol domèstic a Bangkok i connexió amb el vol de tornada."}
        ],
        "included": [
            "Vols internacionals Barcelona - Bangkok - Barcelona",
            "Vols domèstics: Bangkok - Chiang Mai / Chiang Mai - Krabi / Krabi - Bangkok",
            "Tots els trasllats privats aeroport - hotel - aeroport",
            "4 nits a Bangkok, 4 nits a Chiang Mai i 4 nits a Krabi en hotels 4* amb esmorzar",
            "Excursions incloses amb guia en català/castellà (Palau Reial, Ayutthaya, Mercat Flotant, Phi Phi Islands)",
            "Assegurança completa de viatge i assistència mèdica"
        ]
    }
}

js_content = 'const offersData = ' + json.dumps(rich_offers, indent=4, ensure_ascii=False) + ';\n'
with open('offers_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print('Rich offers_data.js created successfully!')
