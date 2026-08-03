
import re

with open("offers_data.js", "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    "tromso": """            "included": [
                "Vols internacionals i nacionals (BCN-OSLO-TROMSO-OSLO-BCN)",
                "Trasllats privats aeroport - hotel - aeroport",
                "4 nits d'hotel 4* al centre",
                "Esmorzar diari inclòs",
                "Excursió per veure les Aurores Boreals amb foguera",
                "Excursió en trineu de gossos Huskies",
                "Assegurança de viatge",
                "Assistència mèdica"
            ]""",
    "japo": """            "included": [
                "Vols internacionals (BCN - TOKYO / OSAKA - BCN)",
                "Trasllat privat d'arribada",
                "Japan Rail Pass de 7 o 14 dies per viatjar lliurement amb tren",
                "12 nits d'allotjament en hotels de 4*",
                "Esmorzar diari inclòs",
                "Assegurança completa de viatge",
                "Assistència mèdica"
            ]""",
    "costa_rica": """            "included": [
                "Vols internacionals",
                "Lloguer de vehicle 4x4 tipus SUV",
                "Assegurança a tot risc per al vehicle",
                "10 nits d'allotjament als millors hotels boutique 4*",
                "Esmorzar diari inclòs",
                "Tours guiats a la selva",
                "Visita al Parc Nacional",
                "Assegurança de viatge",
                "Assistència mèdica"
            ]""",
    "timisoara": """            "included": [
                "Vols internacionals (Barcelona - Timisoara - Barcelona)",
                "Trasllat privat aeroport - hotel - aeroport",
                "3 nits d'allotjament en hotel 4*",
                "Esmorzar diari inclòs",
                "Assegurança de viatge",
                "Assistència en destí"
            ]""",
    "roma": """            "included": [
                "Vols internacionals (Barcelona - Roma - Barcelona)",
                "Trasllat privat aeroport - hotel - aeroport",
                "3 nits d'allotjament en hotel 4*",
                "Esmorzar diari inclòs",
                "Assegurança de viatge",
                "Assistència en destí"
            ]""",
    "thailandia": """            "included": [
                "Vols internacionals (Barcelona - Bangkok - Barcelona)",
                "Vols domèstics (Bangkok - Chiang Mai, Chiang Mai - Krabi, Krabi - Bangkok)",
                "Tots els trasllats privats aeroport - hotel - aeroport",
                "4 nits d'allotjament a Bangkok en hotel 4*",
                "4 nits d'allotjament a Chiang Mai en hotel 4*",
                "4 nits d'allotjament a Krabi en hotel 4*",
                "Esmorzar diari inclòs",
                "Excursions amb guia",
                "Visites incloses: Palau Reial, Ayutthaya, Mercat Flotant i Phi Phi Islands",
                "Assegurança completa de viatge",
                "Assistència mèdica"
            ]""",
    "australia": """            "included": [
                "Vols internacionals (Barcelona-Sydney / Cairns-Barcelona)",
                "Vols interns a Austràlia (Sydney-Ayers Rock / Ayers Rock-Cairns)",
                "Tots els trasllats privats aeroport - hotel - aeroport",
                "4 nits d'allotjament a Sydney en hotel de categoria superior",
                "1 nit d'allotjament a Ayers Rock",
                "3 nits d'allotjament a Cairns",
                "Assegurança d'anul·lació",
                "Assistència en viatge"
            ]""",
    "srilanka-maldives": """            "included": [
                "Vols internacionals",
                "Guia privat a Sri Lanka",
                "Tots els trasllats inclosos",
                "Estada en vila Overwater a Maldives",
                "Règim de Tot Inclòs a les Maldives",
                "Trasllats en hidroavió o llanxa ràpida a les Maldives",
                "Assegurança completa de viatge",
                "Assistència mèdica"
            ]""",
    "nova-york": """            "included": [
                "Vols internacionals directes (BCN-NYC-BCN)",
                "Trasllats privats aeroport - hotel - aeroport",
                "7 nits d'allotjament en hotel cèntric de 4*",
                "Esmorzar diari opcional (segons règim escollit)",
                "Pack de Tours per la ciutat de Nova York",
                "Tour de Contrastos de Nova York",
                "Tour de l'Alt i Baix Manhattan",
                "Assegurança mèdica i d'anul·lació"
            ]""",
    "paris": """            "included": [
                "Vols directes d'anada i tornada",
                "Trasllats privats aeroport - hotel - aeroport",
                "3 nits d'allotjament en hotel romàntic de 4*",
                "Esmorzar diari inclòs",
                "Creuer panoràmic pel riu Sena",
                "Assegurança de viatge",
                "Assistència mèdica"
            ]""",
    "vietnam": """            "included": [
                "Vols internacionals d'anada i tornada",
                "Vols interns al Vietnam",
                "Tren nocturn cap a les muntanyes de Sapa",
                "Tots els trasllats inclosos",
                "Allotjament en hotels seleccionats de qualitat",
                "1 nit de creuer per la Badia de Halong",
                "Totes les excursions amb guia",
                "Tràmits i gestió del visat",
                "Assegurança de viatge",
                "Assistència mèdica"
            ]"""
}

# The javascript object has top-level keys like `"tromso": {` and then `es: {`.
# We want to replace the `included` array in both Catalan and Spanish (for simplicity, we will just apply the same replacement to both since the UI is mostly Catalan right now, but wait! Spanish should be in Spanish).
# Let's just find the Catalan included arrays and replace them.

for key, new_incl in replacements.items():
    # Find the block for the key
    pattern = r"(\"" + key + r"\":\s*\{.*?)\"included\":\s*\[(.*?)\]"
    # Replace the FIRST occurrence of \"included\" inside this key (which is the Catalan one)
    content = re.sub(pattern, r"\1" + new_incl, content, count=1, flags=re.DOTALL)

with open("offers_data.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Done")

