import json

with open('offers_data.js', 'r', encoding='utf-8') as f:
    content = f.read()
    # Extract the JS object
    json_str = content.replace('const offersData = ', '').rstrip(';\n')
    data = json.loads(json_str)

# Add Spanish (es) sub-objects to each offer
translations_es = {
    "costa-oest": {
        "title": "Costa Oeste de Estados Unidos en coche de alquiler",
        "subtitle": "Los Ángeles - Gran Cañón - Monument Valley - Las Vegas - Death Valley - Yosemite - San Francisco",
        "duration": "15 días / 14 noches",
        "price": "2.595 €",
        "tag": "Coche de alquiler",
        "badgeIcon": "fa-car",
        "highlights": "Sé el protagonista: Vive la Costa Oeste de los Estados Unidos como siempre la has visto en las películas.",
        "itinerary": [
            {"day": "DÍA 01", "title": "Barcelona - Los Ángeles", "desc": "Vuelo a Los Ángeles. Recogida del vehículo de alquiler en el aeropuerto y traslado al hotel."},
            {"day": "DÍA 02-03", "title": "Los Ángeles", "desc": "Explora el paseo de la fama en Hollywood, Beverly Hills, el muelle de Santa Mónica y Venice Beach."},
            {"day": "DÍA 04", "title": "Los Ángeles - Gran Cañón", "desc": "Ruta por la mítica Ruta 66 hacia la magnificencia del Gran Cañón del Colorado."},
            {"day": "DÍA 05", "title": "Gran Cañón - Monument Valley", "desc": "Sumérgete en el paisaje icónico del Oeste entre las majestuosas torres de arenisca roja."},
            {"day": "DÍA 06-07", "title": "Monument Valley - Las Vegas", "desc": "Llegada a la capital mundial del entretenimiento y las luces de neón."},
            {"day": "DÍA 08", "title": "Las Vegas - Death Valley", "desc": "Cruza el desierto del Valle de la Muerte con vistas espectaculares en Zabriskie Point."},
            {"day": "DÍA 09-10", "title": "Death Valley - Yosemite", "desc": "Parque Nacional de Yosemite: secuoyas gigantes, cascadas impresionantes y el macizo de El Capitan."},
            {"day": "DÍA 11-13", "title": "Yosemite - San Francisco", "desc": "Visita a la ciudad de las colinas, el Golden Gate, el tranvía histórico y entrada incluida a la isla de Alcatraz."},
            {"day": "DÍA 14-16", "title": "San Francisco - St. Luis Obispo - Los Ángeles - BCN", "desc": "Retorno panorámico por la costa de California (Highway 1) y vuelo de regreso a Barcelona."}
        ],
        "included": [
            "Vuelos Barcelona - Los Ángeles - Barcelona",
            "Coche de alquiler incluido para todos los días con recogida y devolución en el aeropuerto",
            "14 noches de alojamiento seleccionado en los mejores puntos de la ruta",
            "Entradas incluidas a la isla de Alcatraz (San Francisco)",
            "Seguro de cancelación y asistencia en viaje",
            "Tramitación del visado de entrada ESTA"
        ]
    },
    "aurores": {
        "title": "Tromsø y Auroras Boreales (Noruega)",
        "subtitle": "Tromsø - Cabo Norte - Fiordos Árticos",
        "duration": "7 días / 6 noches",
        "price": "1.890 €",
        "tag": "Nuevo Destino",
        "badgeIcon": "fa-snowflake",
        "highlights": "Vive el espectáculo mágico de las auroras boreales y sumérgete en la naturaleza ártica en estado puro.",
        "itinerary": [
            {"day": "DÍA 01", "title": "Barcelona - Oslo - Tromsø", "desc": "Vuelos a Tromsø, la capital de las auroras boreales. Traslado privado al hotel."},
            {"day": "DÍA 02", "title": "Tromsø y Búsqueda de Auroras", "desc": "Visita de la ciudad y excursión nocturna guiada con fotógrafo experto para observar las luces del norte."},
            {"day": "DÍA 03", "title": "Safari en trineo de perros husky", "desc": "Aventura inolvidable conduciendo tu propio trineo de huskies a través de los valles árticos nevados."},
            {"day": "DÍA 04", "title": "Navegación por los fiordos árticos", "desc": "Crucero panorámico entre majestuosos fiordos noruegos con posibilidad de avistar fauna local."},
            {"day": "DÍA 05", "title": "Expedición a Cabo Norte", "desc": "Viaje al punto más septentrional de Europa, un acantilado impresionante sobre el Océano Ártico."},
            {"day": "DÍA 06-07", "title": "Tromsø - Oslo - Barcelona", "desc": "Tiempo libre para disfrutar de la gastronomía local y vuelo de regreso."}
        ],
        "included": [
            "Vuelos Barcelona - Oslo - Tromsø - Barcelona",
            "6 noches de alojamiento en hotel 4* con desayuno bufet incluido",
            "Excursión nocturna guiada de búsqueda de auroras boreales con equipo térmico",
            "Safari en trineo de perros husky con guía local",
            "Crucero panorámico por los fiordos árticos",
            "Traslados privados aeropuerto-hotel-aeropuerto y seguro de viaje completo"
        ]
    },
    "bali": {
        "title": "Indonesia y Bali Paraíso Tropical",
        "subtitle": "Ubud - Islas Gili Trawangan - Nusa Dua",
        "duration": "10 días / 8 noches",
        "price": "1.500 €",
        "tag": "Exótico",
        "badgeIcon": "fa-umbrella-beach",
        "highlights": "Templos enigmáticos entre la naturaleza, terrazas de arroz y playas de arena blanca en Ubud y Gili Trawangan.",
        "itinerary": [
            {"day": "DÍA 01-02", "title": "Barcelona - Denpasar - Ubud", "desc": "Vuelo a Bali. Llegada al corazón cultural de Ubud entre bosques tropicales y santuarios."},
            {"day": "DÍA 03-04", "title": "Ubud, templos y terrazas de arroz", "desc": "Exploración del Sacred Monkey Forest, templo Tirta Empul, terrazas de Tegallalang y cascadas escondidas."},
            {"day": "DÍA 05", "title": "Ubud - Trayecto a Gili Trawangan", "desc": "Traslado al puerto y trayecto en barco rápido hacia el paraíso sin coches de las Islas Gili."},
            {"day": "DÍA 06-08", "title": "Playas e inmersión en Gili Trawangan", "desc": "Días de relajación, buceo con tortugas marinas, puestas de sol míticas y cenas en la arena."},
            {"day": "DÍA 09-10", "title": "Gili Trawangan - Denpasar - Barcelona", "desc": "Regreso en barco a Bali y vuelo de regreso a Barcelona."}
        ],
        "included": [
            "Vuelos Barcelona - Denpasar (Bali) - Barcelona",
            "Traslados privados en vehículo climatizado con chófer",
            "Barco rápido de ida y vuelta a las Islas Gili Trawangan",
            "3 noches en Ubud en hotel 4* con desayuno incluido",
            "5 noches en Gili Trawangan en resort 4* frente al mar",
            "Seguro de viaje de cancelación y asistencia médica"
        ]
    },
    "londres": {
        "title": "Londres Infinita y Escapada Urbana",
        "subtitle": "Westminster - Soho - Camden Town - Borough Market",
        "duration": "4 días / 3 noches",
        "price": "495 €",
        "tag": "Escapada",
        "badgeIcon": "fa-building-columns",
        "highlights": "Londres os espera con mil y un planes: museos fascinantes, cambio de guardia, la noria London Eye y el mejor street food.",
        "itinerary": [
            {"day": "DÍA 01", "title": "Barcelona - Londres", "desc": "Vuelo a Londres. Traslado privado al hotel. Paseo por Piccadilly Circus, Leicester Square y el barrio de Soho."},
            {"day": "DÍA 02", "title": "Westminster y London Eye", "desc": "Visita al palacio de Buckingham, Big Ben, abadía de Westminster y subida incluida a la noria London Eye."},
            {"day": "DÍA 03", "title": "Camden Town y Museo Británico", "desc": "Mañana en el mercado alternativo de Camden. Por la tarde, visita al Museo Británico y degustación gastronómica en Borough Market."},
            {"day": "DÍA 04", "title": "Hyde Park y vuelo de regreso", "desc": "Paseo por los jardines de Hyde Park o shopping en Oxford Street antes del traslado al aeropuerto."}
        ],
        "included": [
            "Vuelos Barcelona - Londres - Barcelona",
            "Traslado privado aeropuerto - hotel - aeropuerto",
            "3 noches de alojamiento en el hotel Premier Inn o similar con desayuno bufet incluido",
            "Guía recomendada de rincones exclusivos y asistencia 24h"
        ]
    },
    "argentina": {
        "title": "Argentina Indispensable",
        "subtitle": "Buenos Aires - El Calafate (Perito Moreno) - Cataratas del Iguazú",
        "duration": "11 días / 8 noches",
        "price": "2.200 €",
        "tag": "Gran Viaje",
        "badgeIcon": "fa-earth-americas",
        "highlights": "Disfruta Argentina a tu aire: desde el ritmo del tango hasta los glaciares de la Patagonia y la fuerza de Iguazú.",
        "itinerary": [
            {"day": "DÍA 01-02", "title": "Barcelona - Buenos Aires", "desc": "Vuelo internacional a la capital del tango. Visita por San Telmo, La Boca, la Plaza de Mayo y Recoleta."},
            {"day": "DÍA 03-05", "title": "El Calafate y Glaciar Perito Moreno", "desc": "Vuelo a la Patagonia. Excursión al majestuoso glaciar Perito Moreno con pasarelas y opción de navegación."},
            {"day": "DÍA 06-08", "title": "Cataratas del Iguazú", "desc": "Vuelo al norte de Argentina. Descubre la Garganta del Diablo y los senderos del Parque Nacional Iguazú."},
            {"day": "DÍA 09-11", "title": "Buenos Aires - Barcelona", "desc": "Última noche en Buenos Aires con cena espectáculo de tango opcional y vuelo de regreso a Barcelona."}
        ],
        "included": [
            "Vuelos internacionales Barcelona - Buenos Aires - Barcelona",
            "Vuelos domésticos: Buenos Aires - El Calafate - Iguazú - Buenos Aires",
            "3 noches en Buenos Aires con desayuno incluido",
            "3 noches en El Calafate con desayuno incluido",
            "2 noches en Iguazú con desayuno incluido",
            "Todos los traslados aeropuerto - hotel - aeropuerto y seguro de viaje"
        ]
    },
    "timisoara": {
        "title": "Timișoara y Encantos de Transilvania",
        "subtitle": "Timișoara - Castillo de Corvin - Alba Iulia",
        "duration": "5 días / 4 noches",
        "price": "450 €",
        "tag": "Cultura",
        "badgeIcon": "fa-landmark",
        "highlights": "Descubre la arquitectura barroca, la historia vibrante y los palacios de la que fue Capital Europea de la Cultura.",
        "itinerary": [
            {"day": "DÍA 01", "title": "Barcelona - Timișoara", "desc": "Vuelo a la pequeña Viena de Rumanía. Llegada y traslado al hotel situado en el barrio histórico."},
            {"day": "DÍA 02", "title": "Centro histórico y Plaza de la Victoria", "desc": "Visita guiada a la Catedral Ortodoxa, el Palacio Lloyd, la Plaza de la Libertad y la arquitectura Secesión."},
            {"day": "DÍA 03", "title": "Excursión al Castillo de Corvin y Alba Iulia", "desc": "Excursión de día completo al castillo gótico más espectacular de Rumanía y la fortaleza de Alba Iulia."},
            {"day": "DÍA 04-05", "title": "Paseo por los parques del río Bega y regreso", "desc": "Tiempo libre para disfrutar de terrazas, museos y vuelo de regreso a Barcelona."}
        ],
        "included": [
            "Vuelos Barcelona - Timișoara - Barcelona",
            "4 noches en hotel 4* en el centro histórico con desayuno bufet incluido",
            "Traslados privados aeropuerto - hotel - aeropuerto",
            "Visita guiada en catalán/castellano por el barrio monumental",
            "Seguro de viaje completo"
        ]
    },
    "roma": {
        "title": "Roma Eterna y Escapada Histórica",
        "subtitle": "Coliseo - Vaticano - Trastevere - Fontana de Trevi",
        "duration": "4 días / 3 noches",
        "price": "395 €",
        "tag": "Escapada",
        "badgeIcon": "fa-monument",
        "highlights": "Caminar por sus calles es pasear por miles de años de historia, cuna de grandes pintores y arquitectos como Miguel Ángel, Bernini y Caravaggio.",
        "itinerary": [
            {"day": "DÍA 01", "title": "Barcelona - Roma", "desc": "Vuelo a la Ciudad Eterna. Traslado al hotel. Primer paseo hasta la Fontana de Trevi y Piazza Navona."},
            {"day": "DÍA 02", "title": "Coliseo, Foro Romano y Palatino", "desc": "Visita monumental a los restos del Imperio Romano y tarde gastronómica en el barrio de Trastevere."},
            {"day": "DÍA 03", "title": "Museos Vaticanos y Capilla Sixtina", "desc": "Visita a los Museos Vaticanos, la basílica de San Pedro y el castillo Sant'Angelo."},
            {"day": "DÍA 04", "title": "Piazza del Popolo y vuelo de regreso", "desc": "Paseo por los jardines de Villa Borghese y regreso a Barcelona."}
        ],
        "included": [
            "Vuelos Barcelona - Roma - Barcelona",
            "Traslado privado aeropuerto - hotel - aeropuerto",
            "3 noches de alojamiento en hotel 4* con desayuno incluido",
            "Seguro de viaje y asistencia en destino"
        ]
    },
    "thailandia": {
        "title": "Tailandia al Completo",
        "subtitle": "Bangkok - Chiang Mai - Islas de Krabi",
        "duration": "13 días / 12 noches",
        "price": "1.600 €",
        "tag": "Asia",
        "badgeIcon": "fa-vihara",
        "highlights": "Circuitos en privado, guías en catalán o castellano, templos dorados y las mejores playas de las islas del sur.",
        "itinerary": [
            {"day": "DÍA 01-02", "title": "Barcelona - Bangkok", "desc": "Vuelo internacional. Llegada a la vibrante capital tailandesa. Alojamiento en hotel 4*."},
            {"day": "DÍA 03-05", "title": "Bangkok, templos y mercados flotantes", "desc": "Visita al Palacio Real, Wat Pho, Ayutthaya con crucero por el río y mercado flotante de Damnoen Saduak."},
            {"day": "DÍA 06-08", "title": "Chiang Mai y montañas del Norte", "desc": "Vuelo al norte. Excursión de un día con senderismo, cascadas, santuario de elefantes ético y mercado nocturno."},
            {"day": "DÍA 09-12", "title": "Islas de Krabi y Phi Phi Islands", "desc": "Vuelo a Krabi. Días de relajación en playas de arena blanca, buceo y excursión en barca a Phi Phi."},
            {"day": "DÍA 13", "title": "Krabi - Bangkok - Barcelona", "desc": "Vuelo doméstico a Bangkok y conexión con el vuelo de regreso."}
        ],
        "included": [
            "Vuelos internacionales Barcelona - Bangkok - Barcelona",
            "Vuelos domésticos: Bangkok - Chiang Mai / Chiang Mai - Krabi / Krabi - Bangkok",
            "Todos los traslados privados aeropuerto - hotel - aeropuerto",
            "4 noches en Bangkok, 4 noches en Chiang Mai y 4 noches en Krabi en hoteles 4* con desayuno",
            "Excursiones incluidas con guía en catalán/castellano (Palacio Real, Ayutthaya, Mercado Flotante, Phi Phi Islands)",
            "Seguro completo de viaje y asistencia médica"
        ]
    }
}

# Add shared fields (same for both langs) + es sub-object
for offer_id, es_data in translations_es.items():
    if offer_id in data:
        # Copy shared fields from CA root that don't change per language
        es_data['heroImage'] = data[offer_id].get('heroImage', '')
        es_data['gallery'] = data[offer_id].get('gallery', [])
        # Store ES as nested
        data[offer_id]['es'] = es_data
        # Also add CA as nested (copy of root) for completeness
        ca_fields = {
            'title': data[offer_id]['title'],
            'subtitle': data[offer_id]['subtitle'],
            'duration': data[offer_id]['duration'],
            'price': data[offer_id]['price'],
            'tag': data[offer_id]['tag'],
            'badgeIcon': data[offer_id]['badgeIcon'],
            'heroImage': data[offer_id]['heroImage'],
            'gallery': data[offer_id]['gallery'],
            'highlights': data[offer_id]['highlights'],
            'itinerary': data[offer_id]['itinerary'],
            'included': data[offer_id]['included'],
        }
        data[offer_id]['ca'] = ca_fields

with open('offers_data.js', 'w', encoding='utf-8') as f:
    f.write('const offersData = ' + json.dumps(data, indent=4, ensure_ascii=False) + ';\n')

print('offers_data.js updated with bilingual content!')
