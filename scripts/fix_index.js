const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const startIndex = html.indexOf('id="ofertesGrid"');
const endIndex = html.indexOf('</section>', startIndex);

let ofertesSection = html.substring(startIndex, endIndex);

ofertesSection = ofertesSection.replace(/<a href="#contacte" class="btn btn-sm btn-gold btn-pill" data-target="contacte">/g, '<a href="#oferta-detall" class="btn btn-sm btn-gold btn-pill btn-view-offer" data-target="oferta-detall">');
ofertesSection = ofertesSection.replace(/<span data-i18n="btn_ask_offer">Demanar oferta<\/span>/g, '<span data-i18n="btn_view_offer">Veure detalls</span>');
ofertesSection = ofertesSection.replace(/<i class="fa-solid fa-arrow-up-right-from-square btn-arrow-icon"><\/i>/g, '<i class="fa-solid fa-arrow-right btn-arrow-icon"></i>');

const ids = ['costa-oest', 'aurores', 'bali', 'londres', 'argentina', 'timisoara', 'roma', 'thailandia'];
let i = 0;
ofertesSection = ofertesSection.replace(/<article class="offer-card([^"]*)" data-category="([^"]+)">/g, (match, p1, p2) => {
    const id = ids[i++];
    return '<article class="offer-card' + p1 + '" data-category="' + p2 + '" data-offer-id="' + id + '">';
});

html = html.substring(0, startIndex) + ofertesSection + html.substring(endIndex);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Replaced ' + i + ' articles in view-ofertes.');
