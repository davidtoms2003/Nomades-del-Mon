import json

with open('offers_data.js', 'r', encoding='utf-8') as f:
    text = f.read().replace('const offersData = ', '').replace(';\n', '')

try:
    data = json.loads(json.loads(text))
except Exception:
    data = json.loads(text)
    if isinstance(data, str):
        data = json.loads(data)

data['aurores'] = 'Aurores boreals a Noruega 7 dies/6 nits\n\nTromsø - Cap Nord - Fiords\n\nViu l\'espectacle màgic de les aurores boreals i submergeix-te en la natura àrtica en estat pur.\n\nPREU 1.850€/PER PERSONA\n\nITINERARI:\n\nDIA 1: BCN - OSLO - TROMSØ\nDIA 2: TROMSØ (Caça d\'Aurores Boreals)\nDIA 3: TROMSØ (Trineu de gossos Husky)\nDIA 4: TROMSØ - CREUER PELS FIORDS\nDIA 5: TROMSØ - CAP NORD\nDIA 6: CAP NORD - OSLO\nDIA 7: OSLO - BCN\n\nEL PREU INCLOU:\n- VOLS BCN - OSLO - TROMSØ\n- 6 NITS D\'ALLOTJAMENT EN HOTELS 4* AMB ESMORZAR\n- EXCURSIONS: CAÇA D\'AURORES, TRINEU DE GOSSOS, CREUER\n- TRASLLATS PRIVATS\n- ASSEGURANÇA DE VIATGE I ASSISTÈNCIA\n\nPREU: 1.850 € PER PERSONA'
data['timisoara'] = 'Timișoara i voltants 5 dies/4 nits\n\nLa petita Viena de Romania\n\nDescobreix l\'arquitectura barroca, la història vibrant i els palaus de la que va ser Capital Europea de la Cultura.\n\nPREU 450€/PER PERSONA\n\nITINERARI:\n\nDIA 1: BCN - TIMIȘOARA\nDIA 2: VISITA GUIADA PEL CENTRE HISTÒRIC (Plaça de la Victòria, Catedral Ortodoxa)\nDIA 3: EXCURSIÓ ALS CASTELLS DE CORVIN I ALBA IULIA\nDIA 4: DIA LLIURE PER DESCOBRIR L\'ARQUITECTURA SECESSION\nDIA 5: TIMIȘOARA - BCN\n\nEL PREU INCLOU:\n- VOLS BCN - TIMIȘOARA - BCN\n- 4 NITS EN HOTEL 4* AL CENTRE AMB ESMORZAR\n- TRASLLATS AEROPORT-HOTEL-AEROPORT\n- VISITA GUIADA EN CATALÀ O CASTELLÀ\n- ASSEGURANÇA BÀSICA DE VIATGE\n\nPREU: 450 € PER PERSONA'

final_data = {}
for k, v in data.items():
    paragraphs = [p for p in v.split('\n\n') if p.strip()]
    html = ''.join([f'<p>{p.replace(chr(10), "<br>")}</p>' for p in paragraphs])
    final_data[k] = html

js_content = 'const offersData = ' + json.dumps(final_data, indent=4, ensure_ascii=False) + ';\n'
with open('offers_data.js', 'w', encoding='utf-8') as out:
    out.write(js_content)
print('Success')
