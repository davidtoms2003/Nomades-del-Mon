replacements = {
    # Monument Valley in galeria costa-oest AND mon-dels-nomades
    'photo-1605627079912-97c3810a11a4': 'photo-1509316785289-025f5b846b35',
    # Florence/Italy Duomo (replacing wrong Florencia photo)
    'photo-1543429776-2782fc8e1acd': 'photo-1542752540-e3a056bf6709',
    # Amazon river (replacing wrong amazon photo)
    'photo-1516939884455-1445c8652f83': 'photo-1649681357620-54170d946bb0',
}

for fname in ['offers_data.js', 'index.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements.items():
        count = content.count(old)
        if count:
            content = content.replace(old, new)
            print(f'{fname}: {count}x {old[-20:]} -> {new[-20:]}')
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done!')
