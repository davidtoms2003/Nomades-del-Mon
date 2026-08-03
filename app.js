/* ==========================================
   NÒMADES DEL MÓN - INTERACTIVE REDESIGN JS
   ========================================== */

// --- PRELOADER ---
window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        setTimeout(() => {
            preloader.classList.add('fade-out');
            setTimeout(() => preloader.style.display = 'none', 600);
        }, 800); // 800ms minimum display time for the elegant animation
    }
});

document.addEventListener('DOMContentLoaded', () => {

    // --- 0. SMART IMAGE LOADING (EARTH SPINNER) ---
    const lazySelectors = '.hero-slide, .floating-card-image img, .offer-image-wrap img, .gallery-item img, .rounded-image img';
    const elementsToLoad = document.querySelectorAll(lazySelectors);
    
    elementsToLoad.forEach(el => {
        const isImg = el.tagName.toLowerCase() === 'img';
        
        // If image is already loaded, skip
        if (isImg && el.complete && el.naturalHeight !== 0) return;

        const spinner = document.createElement('div');
        spinner.className = 'img-loading-spinner';
        spinner.innerHTML = '<i class="fa-solid fa-earth-americas earth-spin"></i>';
        
        let wrapper;
        let urlToLoad = '';

        if (isImg) {
            urlToLoad = el.src;
            wrapper = el.parentElement;
            
            el.style.opacity = '0';
            el.style.transition = 'opacity 0.5s ease';
            
            el.addEventListener('load', () => {
                if (spinner.parentNode) spinner.remove();
                el.style.opacity = '1';
            });
            el.addEventListener('error', () => {
                spinner.innerHTML = '<i class="fa-solid fa-link-slash" style="color:var(--text-muted); font-size:1.5rem;"></i>';
                el.style.opacity = '0.3';
            });
        } else {
            const bg = el.style.backgroundImage || window.getComputedStyle(el).backgroundImage;
            const urlMatch = bg.match(/url\(['"]?(.*?)['"]?\)/);
            if (urlMatch && urlMatch[1]) {
                urlToLoad = urlMatch[1];
                wrapper = el; // .hero-slide
                
                const imgObj = new Image();
                imgObj.onload = () => {
                    if (spinner.parentNode) spinner.remove();
                };
                imgObj.onerror = () => {
                    if (spinner.parentNode) spinner.remove();
                };
                imgObj.src = urlToLoad;
                if (imgObj.complete) {
                    return; // skip if cached
                }
            } else {
                return;
            }
        }

        if (wrapper) {
            const style = window.getComputedStyle(wrapper);
            if (style.position === 'static') {
                wrapper.style.position = 'relative';
            }
            wrapper.appendChild(spinner);
        }
    });

    // --- 0.1. COMPLETE BILINGUAL TRANSLATION DICTIONARY (CA / ES) ---
    const i18nDict = {
        ca: {
            // Top & Theme & Nav
            theme_dark: "Mode Fosc",
            theme_light: "Mode Clar",
            nav_inici: "Inici",
            nav_sobre: "Sobre nosaltres",
            nav_ofertes: "Ofertes",
            nav_nomades: "El món dels nòmades",
            nav_comentaris: "Comentaris",
            nav_contacte: "Contacte",
            cta_design_trip: "Dissenya el teu viatge",

            // Hero
            hero_badge_1: "EXPERIÈNCIES ÚNIQUES A MIDA",
            hero_title_1: "El món dels nòmades",
            hero_desc_1: "Som una agència de viatges online personalitzats que neix de la passió. El nostre objectiu és transmetre aquest sentiment i utilitzar-lo per ajudar als nostres clients a realitzar el viatge dels seus somnis.",
            hero_btn_more: "Veure més",
            hero_btn_quote: "Demana pressupost",

            hero_badge_2: "PREUS EXCLUSIUS",
            hero_title_2: "Viatges econòmics al millor preu",
            hero_desc_2: "No et perdis els viatges que t'oferim perquè gaudeixis de les vacances que et mereixes.",
            hero_btn_offers: "Explorar Ofertes",

            hero_badge_3: "DESTINACIONS INSPIRADORES",
            hero_title_3: "Explora Europa i el Món",
            hero_desc_3: "Viatges dissenyats 100% al teu ritme amb atenció pròxima i personalitzada.",
            hero_btn_gallery: "Galeria de viatgers",

            // Offers
            offers_sub: "SELECCIÓ ESPECIAL",
            offers_title: "Ofertes destacades",
            view_all_offers: "Veure totes les ofertes",
            tag_car: "Cotxe de lloguer",
            tag_new: "Nova Destinació",
            tag_exotic: "Exòtic",
            tag_getaway: "Escapada",
            tag_great_trip: "Gran Viatge",
            tag_culture: "Cultura",
            tag_asia: "Àsia",
            tag_asia_exotic: "Àsia Exòtica",
            tag_aurora: "Aurores Boreals",
            tag_south_america: "Amèrica del Sud",

            btn_request_info: "Sol·licitar informació",
            btn_custom_booking: "Reserva a mida",
            btn_ask_offer: "Demanar oferta",
            btn_view_offer: "Veure detalls",

            offer_1_title: "Costa Oest dels Estats Units en cotxe de lloguer",
            offer_1_title_full: "Costa Oest dels Estats Units en cotxe de lloguer 15 dies/14 nits",
            offer_1_dur: "15 dies / 14 nits",
            offer_1_desc: "Ruta en cotxe descobrint el Gran Canó, Monument Valley, Las Vegas, Yosemite i San Francisco.",
            offer_1_desc_full: "Ruta completa des de Los Ángeles fins a San Francisco passant pel Gran Canó, Monument Valley i Las Vegas.",

            offer_2_title: "Tromsø & Aurores Boreals (Noruega)",
            offer_2_title_full: "Tromsø Nord & Aurores Boreals (Noruega)",
            offer_2_dur: "7 dies / 6 nits",
            offer_2_desc: "Viu l'espectacle màgic de les aurores boreals, fiords de somni i passejos en trineu.",
            offer_2_desc_full: "Cerca d'aurores boreals al Cercle Polar Àrtic, hotels boutique i experiència amb gossos de trineu.",

            offer_3_title: "Indonesia & Bali Paradís Tropical",
            offer_3_title_full: "Indonesia 10 dies/8 nits",
            offer_3_dur: "10 dies / 8 nits",
            offer_3_desc: "Temples enigmàtics entre la natura, terrasses d'arròs i platges de sorra blanca a Ubud i Nusa Dua.",
            offer_3_desc_full: "Experiència inoblidable per Bali, temples enigmàtics, selva d'Ubud i descans a la costa tropical.",

            offer_4_title: "Londres infinita",
            offer_4_title_full: "Londres infinita 4 dies/3 nits",
            offer_4_dur: "4 dies / 3 nits",
            offer_4_desc: "Gaudeix de la capital britànica, museus emblemàtics, teatre i la millor oferta cultural.",
            offer_4_desc_full: "Vols inclosos, allotjament cèntric i recomanacions exclusives per gaudir de la ciutat.",

            offer_5_title: "Argentina indispensable",
            offer_5_title_full: "Argentina indispensable 11 dies/8 nits",
            offer_5_dur: "11 dies / 8 nits",
            offer_5_desc: "Des de Buenos Aires fins a les majestuoses Cataractes de l'Iguazú i les glaceres de la Patagònia.",
            offer_5_desc_full: "Combina el ritme del tango a Buenos Aires amb la grandesa de les cataractes d'Iguazú.",

            offer_6_title: "Timișoara & Encants de Transilvània",
            offer_6_title_full: "Timișoara Cultural & Romania 5 dies/4 nits",
            offer_6_dur: "5 dies / 4 nits",
            offer_6_desc: "Descobreix l'arquitectura barroca, la història vibrant i els palaus de la petita Viena de Romania.",
            offer_6_desc_full: "Endinsa't en la rica història d'Europa Central amb visites guiades i allotjament de gran encant.",

            offer_7_title: "Roma eterna",
            offer_7_title_full: "Roma eterna 4 dies/3 nits",
            offer_7_dur: "4 dies / 3 nits",
            offer_7_desc: "Camina per la història mil·lenària entre el Colosseu, la Fontana de Trevi i la millor gastronomia.",
            offer_7_desc_full: "Una escapada romàntica o cultural a la Ciutat Eterna amb tota l'assistència personalitzada.",

            offer_8_title: "Thailandia al complet",
            offer_8_title_full: "Thailandia al complet 13 dies/12 nits",
            offer_8_dur: "13 dies / 12 nits",
            offer_8_desc: "De la vibrant Bangkok als temples de Chiang Mai i les platges de somni del Sud.",
            offer_8_desc_full: "Circuits en privat, guies en català/castellà i les millors platges de les illes del Sud.",

            // Value Proposition
            val_sub: "SERVEI PERSONALITZAT",
            val_title: "Aprofita les millors ofertes en vols i allotjaments",
            val_p1: "Informa't de les diferents ofertes en vols que tenim per a tu i gaudeix de la seva seguretat i comoditat. També podràs escollir entre una gran varietat d'allotjaments que et faran sentir com a casa.",
            val_p2: "I no t'oblidis de consultar els diferents packs econòmics que posem a la teva disposició.",
            feat_1_h: "Atenció personalitzada",
            feat_1_p: "Estem al teu costat abans, durant i després del teu viatge.",
            feat_2_h: "Itineraris 100% a mida",
            feat_2_p: "Cada detall adaptat als teus gustos, pressupost i ritme.",
            feat_3_h: "Seguretat i garanties",
            feat_3_p: "Agència autoritzada amb la màxima cobertura i confort.",
            quote_text: "\"Fem de la nostra passió la nostra professió.\"",
            quote_author: "— Equip Nòmades Del Món",

            // Sobre nosaltres
            about_sub: "QUI SOM",
            about_page_title: "Sobre nosaltres",
            about_h2: "Fem de la nostra passió la nostra professió",
            about_p1: "Nòmades del món és una agència de viatges online personalitzats que neix de la passió. El nostre objectiu és transmetre aquest sentiment i utilitzar-lo per ajudar als nostres clients a realitzar el viatge dels seus somnis.",
            about_p2: "Per nosaltres cada client és únic i especial amb unes motivacions, gustos i preferències diferents, per això creem un viatge a mida per a cada client.",
            about_highlight: "Explica'ns el teu viatge i nosaltres te'l dissenyem a mida.",
            about_gallery_sub: "Moments i experiències",

            // Ofertes Page Filters
            off_page_sub: "LES NOSTRES PROPOSTES",
            off_page_title: "Ofertes i Itineraris",
            flt_all: "Totes les ofertes",
            flt_europa: "Europa",
            flt_asia: "Àsia",
            flt_america: "Amèrica",
            flt_escapada: "Escapades",

            // Galeria
            nomades_sub: "GALERIA DE VIATGERS",
            nomades_page_title: "El món dels nòmades",
            nomades_page_desc: "En aquest apartat trobareu fotografies dels nostres viatgers pel món.",

            // Comentaris
            comments_sub: "EXPERIÈNCIES DE CLIENTS",
            comments_page_title: "Comentaris i Opinions",
            comments_h2: "Què diuen els nostres viatgers",
            review_1_date: "Febrer 2024 · Viatge a Tailàndia",
            review_1_title: "\"Un viatge a mida inoblidable!\"",
            review_1_text: "Vàrem organitzar el nostre viatge per Sukothai i Ayutthaya amb Nòmades del Món i l'atenció de l'Elisabet va ser impecable. Tot perfectament quadrat, hotels excel·lents i un tracte humà inmillorable. Repeatirem segur!",
            review_2_date: "Agost 2023 · Ruta Costa Oest USA",
            review_2_title: "\"La millor agència per viatjar tranquils\"",
            review_2_text: "L'assessorament en la ruta en cotxe de lloguer pels Parcs Nacionals dels EUA va ser decisiu. Vam poder gaudir de Nova York i Yosemite amb total seguretat i recomanacions úniques.",
            review_3_date: "Febrer 2024 · Viatge a Florència",
            review_3_title: "\"Organització de grup de 10!\"",
            review_3_text: "Gràcies per ajudar-nos a coordinar el viatge de grup a Florència. Gestió ràpida, facilitats i un preu excel·lent.",

            form_comment_h3: "Deixa el teu comentari",
            form_comment_sub: "Comparteix la teva experiència de viatge amb la comunitat de Nòmades Del Món.",
            lbl_comment_title: "Títol del comentari",
            lbl_comment_text: "Comentari",
            lbl_name: "Nom",
            lbl_email: "Correu electrònic",
            chk_public_info: "El titular d'aquest web es reserva el dret de fer pública la informació facilitada en aquest formulari a excepció del correu electrònic.",
            chk_privacy_1: "He llegit i accepto la",
            link_privacy: "política de privacitat",
            chk_newsletter: "Accepto rebre informació sobre les activitats, serveis i productes de Elisabet de la Fuente Ejarque.",
            btn_send_comment: "Enviar comentari",

            // Contacte
            contact_sub: "ESTAM AL TEU COSTAT",
            contact_h2: "Envia'ns la teva consulta",
            contact_lead: "Prepara el teu proper viatge a mida amb nosaltres. Emplea el següent formulari i et respondrem al més aviat possible.",
            lbl_name_full: "Nom i cognoms",
            lbl_phone: "Número de telèfon",
            lbl_message: "Missatge",
            legal_box_title: "INFORMACIÓ SOBRE EL TRACTAMENT DE DADES (RGPD / LO 3/2018)",
            legal_box_resp_label: "Responsable del tractament:",
            legal_box_purpose_label: "Finalitat:",
            legal_box_purpose: "Oferir, prestar i facturar els nostres serveis i productes.",
            legal_box_legit_label: "Legitimació:",
            legal_box_legit: "Consentiment de l'interessat.",
            legal_box_recip_label: "Destinataris:",
            legal_box_recip: "Les dades no es cediran a tercers, llevat que ho exigeixi una llei o sigui necessari per a complir amb la finalitat del tractament.",
            legal_box_rights_label: "Drets:",
            legal_box_rights: "Accedir, rectificar i suprimir dades, així com la resta de drets explicats en la política de privacitat.",
            btn_send_inquiry: "Envia la teva consulta",
            info_phones: "Telèfons d'atenció",
            info_email: "Correu electrònic",
            map_where: "On som a Banyoles",

            // Legal & Cookies
            link_legal: "Avís legal",
            link_cookies: "Política de cookies",
            link_config_cookies: "Configuració de cookies",
            legal_p1: "En compliment de l'article 10 de la Llei 34/2002, de 11 de juliol, de Serveis de la Societat de la Informació i Comerç Electrònic (LSSI-CE), s'informa que aquest lloc web és propietat de:",
            legal_h3: "Propietat Intel·lectual i Industrial",
            legal_p2: "Tots els continguts d'aquest lloc web, incloent textos, imatges, gràfics, dissenys i codis font, estan protegits per la normativa de propietat intel·lectual i industrial. Queda prohibida la reproducció o distribució sense autorització expressa.",
            priv_p1: "D'acord amb el Reglament (UE) 2016/679 (RGPD) i la Llei Orgànica 3/2018 (LOPDGDD), us informem del tractament de les dades personals recollides en aquest lloc web:",
            priv_resp_label: "Responsable:",
            priv_purpose_label: "Finalitat:",
            priv_purpose: "Respondre les consultes dels usuaris, organitzar els viatges sol·licitats i enviar informació comercial quan hagi estat autoritzada.",
            priv_rights_label: "Drets:",
            priv_rights: "Podeu exercir els vostres drets d'accés, rectificació, supressió, limitació i oposició enviant un correu a info@nomadesdelmon.com juntament amb una còpia del vostre document d'identitat.",
            cook_p1: "Aquest lloc web utilitza cookies pròpies i de tercers per millorar l'experiència de navegació i analitzar l'ús de la pàgina web.",
            cook_p2: "Podeu configurar les vostres preferències de cookies en qualsevol moment fent clic al botó de configuració de cookies situat a la part inferior del web.",

            cookie_banner_text: "Fem servir cookies pròpies i de tercers per millorar la teva experiència de navegació i oferir contingut personalitzat.",
            btn_config: "Configurar",
            btn_accept_all: "Acceptar totes",

            // Footer
            footer_desc: "Som una agència de viatges online personalitzats que neix de la passió. Fem del teu viatge una experiència única i inoblidable a mida.",
            footer_nav_h: "Navegació",
            footer_legal_h: "Informació Legal",
            copyright_text: "© 2026 NÒMADES DEL MÓN. Tots els drets reservats. Elisabet de la Fuente Ejarque.",
            credits_text: "Disseny Modern Premium & Experiències de Viatge"
        },
        es: {
            // Top & Theme & Nav
            theme_dark: "Modo Oscuro",
            theme_light: "Modo Claro",
            nav_inici: "Inicio",
            nav_sobre: "Sobre nosotros",
            nav_ofertes: "Ofertas",
            nav_nomades: "El mundo de los nómadas",
            nav_comentaris: "Comentarios",
            nav_contacte: "Contacto",
            cta_design_trip: "Diseña tu viaje",

            // Hero
            hero_badge_1: "EXPERIENCIAS ÚNICAS A MEDIDA",
            hero_title_1: "El mundo de los nómadas",
            hero_desc_1: "Somos una agencia de viajes online personalizados que nace de la pasión. Nuestro objetivo es transmitir este sentimiento y utilizarlo para ayudar a nuestros clientes a realizar el viaje de sus sueños.",
            hero_btn_more: "Ver más",
            hero_btn_quote: "Pide presupuesto",

            hero_badge_2: "PRECIOS EXCLUSIVOS",
            hero_title_2: "Viajes económicos al mejor precio",
            hero_desc_2: "No te pierdas los viajes que te ofrecemos para que disfrutes de las vacaciones que te mereces.",
            hero_btn_offers: "Explorar Ofertas",

            hero_badge_3: "DESTINOS INSPIRADORES",
            hero_title_3: "Explora Europa y el Mundo",
            hero_desc_3: "Viajes diseñados 100% a tu ritmo con atención cercana y personalizada.",
            hero_btn_gallery: "Galería de viajeros",

            // Offers
            offers_sub: "SELECCIÓN ESPECIAL",
            offers_title: "Ofertas destacadas",
            view_all_offers: "Ver todas las ofertas",
            tag_car: "Coche de alquiler",
            tag_new: "Nuevo Destino",
            tag_exotic: "Exótico",
            tag_getaway: "Escapada",
            tag_great_trip: "Gran Viaje",
            tag_culture: "Cultura",
            tag_asia: "Asia",
            tag_asia_exotic: "Asia Exótica",
            tag_aurora: "Auroras Boreales",
            tag_south_america: "América del Sur",

            btn_request_info: "Solicitar información",
            btn_custom_booking: "Reserva a medida",
            btn_ask_offer: "Pedir oferta",
            btn_view_offer: "Ver detalles",

            offer_1_title: "Costa Oeste de Estados Unidos en coche de alquiler",
            offer_1_title_full: "Costa Oeste de Estados Unidos en coche de alquiler 15 días/14 noches",
            offer_1_dur: "15 días / 14 noches",
            offer_1_desc: "Ruta en coche descubriendo el Gran Cañón, Monument Valley, Las Vegas, Yosemite y San Francisco.",
            offer_1_desc_full: "Ruta completa desde Los Ángeles hasta San Francisco pasando por el Gran Cañón, Monument Valley y Las Vegas.",

            offer_2_title: "Tromsø y Auroras Boreales (Noruega)",
            offer_2_title_full: "Tromsø Norte y Auroras Boreales (Noruega)",
            offer_2_dur: "7 días / 6 noches",
            offer_2_desc: "Vive el espectáculo mágico de las auroras boreales, fiordos de ensueño y paseos en trineo.",
            offer_2_desc_full: "Búsqueda de auroras boreales en el Círculo Polar Ártico, hoteles boutique y experiencia con perros de trineo.",

            offer_3_title: "Indonesia y Bali Paraíso Tropical",
            offer_3_title_full: "Indonesia 10 días/8 noches",
            offer_3_dur: "10 días / 8 noches",
            offer_3_desc: "Templos enigmáticos entre la naturaleza, terrazas de arroz y playas de arena blanca en Ubud y Nusa Dua.",
            offer_3_desc_full: "Experiencia inolvidable por Bali, templos enigmáticos, selva de Ubud y descanso en la costa tropical.",

            offer_4_title: "Londres infinita",
            offer_4_title_full: "Londres infinita 4 días/3 noches",
            offer_4_dur: "4 días / 3 noches",
            offer_4_desc: "Disfruta de la capital británica, museos emblemáticos, teatro y la mejor oferta cultural.",
            offer_4_desc_full: "Vuelos incluidos, alojamiento céntrico y recomendaciones exclusivas para disfrutar de la ciudad.",

            offer_5_title: "Argentina indispensable",
            offer_5_title_full: "Argentina indispensable 11 días/8 noches",
            offer_5_dur: "11 días / 8 noches",
            offer_5_desc: "Desde Buenos Aires hasta las majestuosas Cataratas del Iguazú y los glaciares de la Patagonia.",
            offer_5_desc_full: "Combina el ritmo del tango en Buenos Aires con la grandeza de las cataratas de Iguazú.",

            offer_6_title: "Timișoara y Encantos de Transilvania",
            offer_6_title_full: "Timișoara Cultural y Rumanía 5 días/4 noches",
            offer_6_dur: "5 días / 4 noches",
            offer_6_desc: "Descubre la arquitectura barroca, la historia vibrante y los palacios de la pequeña Viena de Rumanía.",
            offer_6_desc_full: "Adéntrate en la rica historia de Europa Central con visitas guiadas y alojamiento de gran encanto.",

            offer_7_title: "Roma eterna",
            offer_7_title_full: "Roma eterna 4 días/3 noches",
            offer_7_dur: "4 días / 3 noches",
            offer_7_desc: "Camina por la historia milenaria entre el Coliseo, la Fontana de Trevi y la mejor gastronomía.",
            offer_7_desc_full: "Una escapada romántica o cultural a la Ciudad Eterna con toda la asistencia personalizada.",

            offer_8_title: "Tailandia al completo",
            offer_8_title_full: "Tailandia al completo 13 días/12 noches",
            offer_8_dur: "13 días / 12 noches",
            offer_8_desc: "De la vibrante Bangkok a los templos de Chiang Mai y las playas de ensueño del Sur.",
            offer_8_desc_full: "Circuitos en privado, guías en español/catalán y las mejores playas de las islas del Sur.",

            // Value Proposition
            val_sub: "SERVICIO PERSONALIZADO",
            val_title: "Aprovecha las mejores ofertas en vuelos y alojamientos",
            val_p1: "Infórmate de las diferentes ofertas en vuelos que tenemos para ti y disfruta de su seguridad y comodidad. También podrás elegir entre una gran variedad de alojamientos que te harán sentir como en casa.",
            val_p2: "Y no olvides consultar los diferentes packs económicos que ponemos a tu disposición.",
            feat_1_h: "Atención personalizada",
            feat_1_p: "Estamos a tu lado antes, durante y después de tu viaje.",
            feat_2_h: "Itinerarios 100% a medida",
            feat_2_p: "Cada detalle adaptado a tus gustos, presupuesto y ritmo.",
            feat_3_h: "Seguridad y garantías",
            feat_3_p: "Agencia autorizada con la máxima cobertura y confort.",
            quote_text: "\"Hacemos de nuestra pasión nuestra profesión.\"",
            quote_author: "— Equipo Nòmades Del Món",

            // Sobre nosaltres
            about_sub: "QUIÉNES SOMOS",
            about_page_title: "Sobre nosotros",
            about_h2: "Hacemos de nuestra pasión nuestra profesión",
            about_p1: "Nòmades del món es una agencia de viajes online personalizados que nace de la pasión. Nuestro objetivo es transmitir este sentimiento y utilizarlo para ayudar a nuestros clientes a realizar el viaje de sus sueños.",
            about_p2: "Para nosotros cada cliente es único y especial con unas motivaciones, gustos y preferencias diferentes, por eso creamos un viaje a medida para cada cliente.",
            about_highlight: "Cuéntanos tu viaje y nosotros te lo diseñamos a medida.",
            about_gallery_sub: "Momentos y experiencias",

            // Ofertes Page Filters
            off_page_sub: "NUESTRAS PROPUESTAS",
            off_page_title: "Ofertas e Itinerarios",
            flt_all: "Todas las ofertas",
            flt_europa: "Europa",
            flt_asia: "Asia",
            flt_america: "América",
            flt_escapada: "Escapadas",

            // Galeria
            nomades_sub: "GALERÍA DE VIAJEROS",
            nomades_page_title: "El mundo de los nómadas",
            nomades_page_desc: "En este apartado encontraréis fotografías de nuestros viajeros por el mundo.",

            // Comentaris
            comments_sub: "EXPERIENCIAS DE CLIENTES",
            comments_page_title: "Comentarios y Opiniones",
            comments_h2: "Qué dicen nuestros viajeros",
            review_1_date: "Febrero 2024 · Viaje a Tailandia",
            review_1_title: "\"¡Un viaje a medida inolvidable!\"",
            review_1_text: "Organizamos nuestro viaje por Sukothai y Ayutthaya con Nòmades del Món y la atención de Elisabet fue impecable. Todo perfectamente cuadrado, hoteles excelentes y un trato humano inmejorable. ¡Repetiremos seguro!",
            review_2_date: "Agosto 2023 · Ruta Costa Oeste USA",
            review_2_title: "\"La mejor agencia para viajar tranquilos\"",
            review_2_text: "El asesoramiento en la ruta en coche de alquiler por los Parques Nacionales de EE.UU. fue decisivo. Pudimos disfrutar de Nueva York y Yosemite con total seguridad y recomendaciones únicas.",
            review_3_date: "Febrero 2024 · Viaje a Florencia",
            review_3_title: "\"¡Organización de grupo de 10!\"",
            review_3_text: "Gracias por ayudarnos a coordinar el viaje de grupo a Florencia. Gestión rápida, facilidades y un precio excelente.",

            form_comment_h3: "Deja tu comentario",
            form_comment_sub: "Comparte tu experiencia de viaje con la comunidad de Nòmades Del Món.",
            lbl_comment_title: "Título del comentario",
            lbl_comment_text: "Comentario",
            lbl_name: "Nombre",
            lbl_email: "Correo electrónico",
            chk_public_info: "El titular de esta web se reserva el derecho de hacer pública la información facilitada en este formulario a excepción del correo electrónico.",
            chk_privacy_1: "He leído y acepto la",
            link_privacy: "política de privacidad",
            chk_newsletter: "Acepto recibir información sobre las actividades, servicios y productos de Elisabet de la Fuente Ejarque.",
            btn_send_comment: "Enviar comentario",

            // Contacte
            contact_sub: "ESTAMOS A TU LADO",
            contact_h2: "Envíanos tu consulta",
            contact_lead: "Prepara tu próximo viaje a medida con nosotros. Utiliza el siguiente formulario y te responderemos lo antes posible.",
            lbl_name_full: "Nombre y apellidos",
            lbl_phone: "Número de teléfono",
            lbl_message: "Mensaje",
            legal_box_title: "INFORMACIÓN SOBRE EL TRATAMIENTO DE DATOS (RGPD / LO 3/2018)",
            legal_box_resp_label: "Responsable del tratamiento:",
            legal_box_purpose_label: "Finalidad:",
            legal_box_purpose: "Ofrecer, prestar y facturar nuestros servicios y productos.",
            legal_box_legit_label: "Legitimación:",
            legal_box_legit: "Consentimiento del interesado.",
            legal_box_recip_label: "Destinatarios:",
            legal_box_recip: "Los datos no se cederán a terceros, salvo exigencia legal o necesidad para cumplir con la finalidad del tratamiento.",
            legal_box_rights_label: "Derechos:",
            legal_box_rights: "Acceder, rectificar y suprimir datos, así como el resto de derechos explicados en la política de privacidad.",
            btn_send_inquiry: "Envía tu consulta",
            info_phones: "Teléfonos de atención",
            info_email: "Correo electrónico",
            map_where: "Dónde estamos en Banyoles",

            // Legal & Cookies
            link_legal: "Aviso legal",
            link_cookies: "Política de cookies",
            link_config_cookies: "Configuración de cookies",
            legal_p1: "En cumplimiento del artículo 10 de la Ley 34/2002, de 11 de julio, de Servicios de la Sociedad de la Información y Comercio Electrónico (LSSI-CE), se informa que este sitio web es propiedad de:",
            legal_h3: "Propiedad Intelectual e Industrial",
            legal_p2: "Todos los contenidos de este sitio web, incluyendo textos, imágenes, gráficos, diseños y códigos fuente, están protegidos por la normativa de propiedad intelectual e industrial. Queda prohibida la reproducción o distribución sin autorización expresa.",
            priv_p1: "De acuerdo con el Reglamento (UE) 2016/679 (RGPD) y la Ley Orgánica 3/2018 (LOPDGDD), le informamos del tratamiento de los datos personales recogidos en este sitio web:",
            priv_resp_label: "Responsable:",
            priv_purpose_label: "Finalidad:",
            priv_purpose: "Responder a las consultas de los usuarios, organizar los viajes solicitados y enviar información comercial cuando haya sido autorizada.",
            priv_rights_label: "Derechos:",
            priv_rights: "Puede ejercer sus derechos de acceso, rectificación, supresión, limitación y oposición enviando un correo a info@nomadesdelmon.com junto con una copia de su documento de identidad.",
            cook_p1: "Este sitio web utiliza cookies propias y de terceros para mejorar la experiencia de navegación y analizar el uso de la página web.",
            cook_p2: "Puede configurar sus preferencias de cookies en cualquier momento haciendo clic en el botón de configuración de cookies situado en la parte inferior de la web.",

            cookie_banner_text: "Utilizamos cookies propias y de terceros para mejorar tu experiencia de navegación y ofrecer contenido personalizado.",
            btn_config: "Configurar",
            btn_accept_all: "Aceptar todas",

            // Footer
            footer_desc: "Somos una agencia de viajes online personalizados que nace de la pasión. Hacemos de tu viaje una experiencia única e inolvidable a medida.",
            footer_nav_h: "Navegación",
            footer_legal_h: "Información Legal",
            copyright_text: "© 2026 NÒMADES DEL MÓN. Todos los derechos reservados. Elisabet de la Fuente Ejarque.",
            credits_text: "Diseño Moderno Premium & Experiencias de Viaje"
        }
    };

    // --- LANGUAGE SWITCHER IMPLEMENTATION ---
    let currentLang = localStorage.getItem('nomadesLang') || 'ca';

    function setLanguage(lang) {
        if (!i18nDict[lang]) lang = 'ca';
        currentLang = lang;
        localStorage.setItem('nomadesLang', lang);

        // Update document lang
        document.documentElement.lang = lang;

        // Update language selector active buttons
        document.querySelectorAll('.lang-btn').forEach(b => {
            b.classList.toggle('active', b.dataset.lang === lang);
        });

        // Translate all data-i18n elements
        const dict = i18nDict[lang];
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.dataset.i18n;
            if (dict[key]) {
                el.textContent = dict[key];
            }
        });

        // Also update placeholders
        updatePlaceholders(lang);

        // Update Theme label in current language
        const isLight = document.body.classList.contains('theme-light');
        const themeLabel = document.querySelector('.theme-label');
        if (themeLabel) {
            themeLabel.textContent = isLight ? dict.theme_light : dict.theme_dark;
        }

        // Re-render offer detail instantly if user is on that view
        const detailView = document.getElementById('view-oferta-detall');
        if (detailView && detailView.classList.contains('active')) {
            const savedId = localStorage.getItem('lastOfferId');
            if (savedId) {
                const card = document.querySelector(`[data-offer-id="${savedId}"]`);
                const btn = card && card.querySelector('.btn-view-offer');
                if (btn) btn.click();
            }
        }
    }


    function updatePlaceholders(lang) {
        const ph = {
            ca: {
                'comentari-titol': "Ex: El nostre viatge de somni a Bali",
                'comentari-text': "Explica'ns detalls sobre el teu viatge, l'atenció rebuda...",
                'comentari-nom': "El teu nom i cognoms",
                'comentari-email': "nom@exemple.com",
                'contacte-nom': "Ex: Maria Garcia Pujol",
                'contacte-telefon': "Ex: 654 596 998",
                'contacte-email': "Ex: maria@exemple.com",
                'contacte-missatge': "Explica'ns quin viatge t'agradaria fer, dates aproximades, nombre de viatgers, destinacions preferides..."
            },
            es: {
                'comentari-titol': "Ej: Nuestro viaje de ensueño a Bali",
                'comentari-text': "Cuéntanos detalles sobre tu viaje, la atención recibida...",
                'comentari-nom': "Tu nombre y apellidos",
                'comentari-email': "nombre@ejemplo.com",
                'contacte-nom': "Ej: María García Pujol",
                'contacte-telefon': "Ej: 654 596 998",
                'contacte-email': "Ej: maria@ejemplo.com",
                'contacte-missatge': "Cuéntanos qué viaje te gustaría hacer, fechas aproximadas, número de viajeros, destinos preferidos..."
            }
        };

        const currentPh = ph[lang] || ph['ca'];
        Object.keys(currentPh).forEach(id => {
            const input = document.getElementById(id);
            if (input) {
                input.placeholder = currentPh[id];
            }
        });
    }

    // Attach click events to CA / ES language buttons
    const langBtns = document.querySelectorAll('.lang-btn');
    langBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const selectedLang = btn.dataset.lang;
            setLanguage(selectedLang);
        });
    });

    // --- 0. THEME SWITCHER (DARK / LIGHT MODE & LOGO SWAP) ---
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const headerLogoImg = document.getElementById('headerLogoImg');
    const footerLogoImg = document.getElementById('footerLogoImg');

    const logoBlanc = 'img/Logos/LogoBlanc.jpg';
    const logoNegro = 'img/Logos/LogoNegro.jpg';

    function setTheme(theme) {
        if (theme === 'light') {
            document.body.classList.remove('theme-dark');
            document.body.classList.add('theme-light');
            if (headerLogoImg) headerLogoImg.src = logoNegro;
            if (footerLogoImg) footerLogoImg.src = logoNegro;
            if (themeToggleBtn) {
                themeToggleBtn.innerHTML = `<i class="fa-solid fa-sun"></i>`;
                themeToggleBtn.setAttribute('title', 'Canviar a mode fosc');
            }
            localStorage.setItem('nomadesTheme', 'light');
        } else {
            document.body.classList.remove('theme-light');
            document.body.classList.add('theme-dark');
            if (headerLogoImg) headerLogoImg.src = logoBlanc;
            if (footerLogoImg) footerLogoImg.src = logoBlanc;
            if (themeToggleBtn) {
                themeToggleBtn.innerHTML = `<i class="fa-solid fa-moon"></i>`;
                themeToggleBtn.setAttribute('title', 'Canviar a mode clar');
            }
            localStorage.setItem('nomadesTheme', 'dark');
        }
    }

    // Load saved theme or default to dark
    const savedTheme = localStorage.getItem('nomadesTheme') || 'dark';
    setTheme(savedTheme);

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const isCurrentlyLight = document.body.classList.contains('theme-light');
            setTheme(isCurrentlyLight ? 'dark' : 'light');
        });
    }

    // Initialize Default Language (Catalan first!)
    setLanguage(currentLang);

    // --- 1. SPA NAVIGATION & ROUTING ---
    const navLinks = document.querySelectorAll('[data-target]');
    const pageViews = document.querySelectorAll('.page-view');
    const mobileToggle = document.getElementById('mobileToggle');
    const navMenu = document.getElementById('navMenu');

    function switchView(targetId) {
        if (!targetId) targetId = 'inici';
        targetId = targetId.replace('#', '');

        // Hide all views
        pageViews.forEach(view => {
            view.classList.remove('active');
        });

        // Show target view
        const targetView = document.getElementById(`view-${targetId}`);
        if (targetView) {
            targetView.classList.add('active');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // Update Nav Link Active States
        document.querySelectorAll('.nav-link').forEach(link => {
            if (link.dataset.target === targetId) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });

        // Close mobile drawer if open
        if (navMenu) navMenu.classList.remove('active');
        if (mobileToggle) mobileToggle.classList.remove('active');

        // Initialize Map if navigating to contacte
        if (targetId === 'contacte') {
            setTimeout(initMap, 200);
        }
    }

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const target = link.dataset.target || link.getAttribute('href');
            if (target && target.startsWith('#')) {
                e.preventDefault();
                const targetId = target.replace('#', '');
                window.location.hash = targetId;
                switchView(targetId);
            }
        });
    });

    // Handle back/forward browser navigation
    window.addEventListener('hashchange', () => {
        const hash = window.location.hash.substring(1) || 'inici';
        if (hash === 'oferta-detall') {
            restoreOfferDetail();
        } else {
            switchView(hash);
        }
    });

    // Restore offer detail from localStorage (used when user refreshes on #oferta-detall)
    function restoreOfferDetail() {
        const savedId = localStorage.getItem('lastOfferId');
        if (savedId && typeof offersData !== 'undefined' && offersData[savedId]) {
            // Find a card with this offer id and simulate click — or render directly
            const card = document.querySelector(`.offer-card[data-offer-id="${savedId}"]`);
            if (card) {
                const btn = card.querySelector('.btn-view-offer');
                if (btn) { btn.click(); return; }
            }
            // Fallback: redirect to ofertes
            window.location.hash = 'ofertes';
            switchView('ofertes');
        } else {
            // No saved offer — go to offers list
            window.location.hash = 'ofertes';
            switchView('ofertes');
        }
    }

    // Initial View Load
    const initialHash = window.location.hash.substring(1) || 'inici';
    if (initialHash === 'oferta-detall') {
        restoreOfferDetail();
    } else {
        switchView(initialHash);
    }

    // Mobile Toggle Menu
    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            mobileToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }

    // --- 2. HERO SLIDER ---
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.hero-dots .dot');
    const prevBtn = document.querySelector('.hero-prev');
    const nextBtn = document.querySelector('.hero-next');
    let currentSlide = 0;
    let slideInterval;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
        });
        dots.forEach((dot, i) => {
            dot.classList.toggle('active', i === index);
        });
        currentSlide = index;
    }

    function nextSlide() {
        const next = (currentSlide + 1) % slides.length;
        showSlide(next);
    }

    function prevSlide() {
        const prev = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(prev);
    }

    if (slides.length > 0) {
        slideInterval = setInterval(nextSlide, 6000);

        if (nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); resetInterval(); });
        if (prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); resetInterval(); });
        
        const goOfferBtns = document.querySelectorAll('.hero-go-offer');
        goOfferBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const offerId = btn.dataset.offerId;
                const realOfferCardBtn = document.querySelector(`.offer-card[data-offer-id="${offerId}"] .btn-view-offer`);
                if (realOfferCardBtn) {
                    realOfferCardBtn.click();
                } else {
                    window.location.hash = 'ofertes';
                }
            });
        });

        dots.forEach(dot => {
            dot.addEventListener('click', () => {
                const slideIdx = parseInt(dot.dataset.slide);
                showSlide(slideIdx);
                resetInterval();
            });
        });

        function resetInterval() {
            clearInterval(slideInterval);
            slideInterval = setInterval(nextSlide, 6000);
        }
    }

    // --- 3. OFFERS FILTERING & PAGINATION ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    const offerCards = document.querySelectorAll('#ofertesGrid .offer-card');
    const viewAllWrap = document.getElementById('viewAllOffersWrap');
    const btnViewAll = document.getElementById('btnViewAllOffers');
    
    let showingAll = false;

    function renderOffers(filter) {
        let visibleCount = 0;
        let totalMatches = 0;

        offerCards.forEach(card => {
            if (filter === 'all' || card.dataset.category.includes(filter)) {
                totalMatches++;
                if (!showingAll && filter === 'all' && totalMatches > 6) {
                    card.style.display = 'none';
                } else {
                    card.style.display = 'flex';
                    visibleCount++;
                }
            } else {
                card.style.display = 'none';
            }
        });

        // Hide the "View All" button if there are 6 or fewer total matches, or if we are already showing all, or if we are filtering
        if (viewAllWrap) {
            if (showingAll || filter !== 'all' || totalMatches <= 6) {
                viewAllWrap.style.display = 'none';
            } else {
                viewAllWrap.style.display = 'block';
            }
        }
        
        // Toggle view-all class for CSS
        if (showingAll || filter !== 'all') {
            ofertesGrid.classList.add('view-all');
        } else {
            ofertesGrid.classList.remove('view-all');
        }
    }

    if (btnViewAll) {
        btnViewAll.addEventListener('click', () => {
            showingAll = true;
            renderOffers('all');
        });
    }

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            showingAll = false; 
            renderOffers(btn.dataset.filter);
        });
    });
    
    // Initial render
    renderOffers('all');

    // --- 4. LIGHTBOX FOR GALLERY ---
    const galleryItems = document.querySelectorAll('.gallery-item');
    const lightboxModal = document.getElementById('lightboxModal');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxCaption = document.getElementById('lightboxCaption');
    const lightboxClose = document.getElementById('lightboxClose');

    window.openLightbox = function(src, caption) {
        if (lightboxModal && lightboxImg) {
            lightboxImg.src = src;
            if (lightboxCaption) lightboxCaption.textContent = caption || '';
            lightboxModal.classList.add('active');
        }
    };

    galleryItems.forEach(item => {
        item.addEventListener('click', () => {
            const img = item.querySelector('img');
            const caption = item.dataset.caption || img.alt;
            window.openLightbox(img.src, caption);
        });
    });

    if (lightboxClose) {
        lightboxClose.addEventListener('click', () => {
            lightboxModal.classList.remove('active');
        });
    }

    if (lightboxModal) {
        lightboxModal.addEventListener('click', (e) => {
            if (e.target === lightboxModal) {
                lightboxModal.classList.remove('active');
            }
        });
    }

    // GALLERY CATEGORY FILTERING LOGIC
    const galleryFilterBtns = document.querySelectorAll('.gallery-filter-btn');
    galleryFilterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const filter = btn.dataset.galleryFilter;
            
            // Toggle active class on buttons
            galleryFilterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Filter items
            galleryItems.forEach(item => {
                const category = item.dataset.category;
                if (filter === 'all' || category === filter) {
                    item.classList.remove('hidden');
                } else {
                    item.classList.add('hidden');
                }
            });
        });
    });

    // --- 5. LEAFLET INTERACTIVE MAP ---
    let mapInitialized = false;
    function initMap() {
        if (mapInitialized) return;
        const mapContainer = document.getElementById('contactMap');
        if (!mapContainer || typeof L === 'undefined') return;

        // Banyoles Coordinates
        const lat = 42.1184029;
        const lng = 2.7654778;

        const map = L.map('contactMap').setView([lat, lng], 15);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        const customIcon = L.divIcon({
            className: 'custom-map-pin',
            html: `<div style="background-color:#D4AF37; width:28px; height:28px; border-radius:50%; border:3px solid #0B0F19; box-shadow:0 0 10px rgba(212,175,55,0.8); display:flex; align-items:center; justify-content:center; color:#000;"><i class="fa-solid fa-compass" style="font-size:14px;"></i></div>`,
            iconSize: [28, 28],
            iconAnchor: [14, 14]
        });

        L.marker([lat, lng], { icon: customIcon }).addTo(map)
            .bindPopup('<b>NÒMADES DEL MÓN</b><br>Plaça Major, 4, Banyoles (Girona)')
            .openPopup();

        mapInitialized = true;
    }

    // --- 6. COMMENT FORM SUBMISSION ---
    const formComentari = document.getElementById('formComentari');
    const commentsFeed = document.getElementById('commentsFeed');

    if (formComentari) {
        formComentari.addEventListener('submit', (e) => {
            e.preventDefault();

            const titol = document.getElementById('comentari-titol').value;
            const text = document.getElementById('comentari-text').value;
            const nom = document.getElementById('comentari-nom').value;

            const msgSuccess = currentLang === 'es' ? 
                '¡Muchas gracias! Tu comentario se ha publicado correctamente.' : 
                'Moltes gràcies! El teu comentari s’ha publicat correctament.';

            const newComment = document.createElement('div');
            newComment.className = 'comment-card';
            newComment.style.border = '1px solid var(--primary-gold)';
            newComment.innerHTML = `
                <div class="comment-header">
                    <div class="avatar">${nom.charAt(0).toUpperCase()}</div>
                    <div>
                        <h4 class="author-name">${nom}</h4>
                        <span class="comment-date"><i class="fa-regular fa-calendar"></i> ${currentLang === 'es' ? 'Ahora mismo' : 'Ara mateix'}</span>
                    </div>
                    <div class="stars">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                </div>
                <h5 class="comment-title">"${titol}"</h5>
                <p class="comment-text">${text}</p>
            `;

            commentsFeed.prepend(newComment);
            formComentari.reset();
            alert(msgSuccess);
        });
    }

    // --- 7. CONTACT FORM SUBMISSION ---
    const formContacte = document.getElementById('formContacte');
    if (formContacte) {
        formContacte.addEventListener('submit', (e) => {
            e.preventDefault();
            const msgContact = currentLang === 'es' ?
                '¡Gracias por contactar con Nòmades Del Món! Hemos recibido tu consulta y un asesor te responderá enseguida.' :
                'Gràcies per contactar amb Nòmades Del Món! Hem rebut la teva consulta i un assessor et respondrà de seguida.';
            alert(msgContact);
            formContacte.reset();
        });
    }

    // --- 8. COOKIES BANNER & CONFIGURATION ---
    const cookieBanner = document.getElementById('cookieBanner');
    const cookieAcceptBtn = document.getElementById('cookieAcceptBtn');
    const cookieConfigBtn = document.getElementById('cookieConfigBtn');
    const footerCookieConfig = document.getElementById('footerCookieConfig');

    if (!localStorage.getItem('cookiesAccepted')) {
        setTimeout(() => {
            if (cookieBanner) cookieBanner.classList.add('active');
        }, 1200);
    }

    if (cookieAcceptBtn) {
        cookieAcceptBtn.addEventListener('click', () => {
            localStorage.setItem('cookiesAccepted', 'true');
            if (cookieBanner) cookieBanner.classList.remove('active');
        });
    }

    if (cookieConfigBtn) {
        cookieConfigBtn.addEventListener('click', () => {
            const msgConfig = currentLang === 'es' ?
                'Configuración de Cookies: Todas las cookies esenciales y analíticas están activadas para el correcto funcionamiento de la web.' :
                'Configuració de Cookies: Totes les cookies essencials i analítiques estan activades per al correcte funcionament del web.';
            alert(msgConfig);
            localStorage.setItem('cookiesAccepted', 'true');
            if (cookieBanner) cookieBanner.classList.remove('active');
        });
    }

    if (footerCookieConfig) {
        footerCookieConfig.addEventListener('click', () => {
            const msgFooter = currentLang === 'es' ?
                'Configuración de Cookies de Nòmades Del Món:\nPuede gestionar el consentimiento de las cookies analíticas y de rendimiento.' :
                'Configuració de Cookies de Nòmades Del Món:\nPodeu gestionar el consentiment de les cookies analítiques i de rendiment.';
            alert(msgFooter);
        });
    }

    // --- 9. CUSTOM CURSOR ---
    const customCursor = document.getElementById('customCursor');
    const cursorDot = document.getElementById('cursorDot');
    
    if (customCursor && cursorDot && window.matchMedia('(min-width: 769px)').matches) {
        let mouseX = 0, mouseY = 0;
        let cursorX = 0, cursorY = 0;
        
        document.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
            cursorDot.style.left = mouseX + 'px';
            cursorDot.style.top = mouseY + 'px';
        });
        
        function animateCursor() {
            cursorX += (mouseX - cursorX) * 0.12;
            cursorY += (mouseY - cursorY) * 0.12;
            customCursor.style.left = cursorX + 'px';
            customCursor.style.top = cursorY + 'px';
            requestAnimationFrame(animateCursor);
        }
        animateCursor();
        
        // Hover effect on interactive elements
        const hoverTargets = document.querySelectorAll('a, button, .offer-card, .gallery-item, .filter-btn, input, textarea');
        hoverTargets.forEach(el => {
            el.addEventListener('mouseenter', () => customCursor.classList.add('cursor-hover'));
            el.addEventListener('mouseleave', () => customCursor.classList.remove('cursor-hover'));
        });
    }

    // --- 10. TEXT REVEAL & SCROLL REVEAL ANIMATIONS ---
    // Auto-wrap titles for the premium masking effect
    document.querySelectorAll('.section-title, .hero-title').forEach(title => {
        const content = title.innerHTML;
        title.innerHTML = `<span class="text-reveal-inner">${content}</span>`;
        title.classList.add('text-reveal');
    });

    const revealElements = document.querySelectorAll('.reveal');
    if (revealElements.length > 0) {
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: '0px 0px -50px 0px'
        });
        
        revealElements.forEach(el => revealObserver.observe(el));
    }

    // --- 11. SUBTLE PARALLAX ON SCROLL ---
    const parallaxCards = document.querySelectorAll('.hero-floating-card');
    if (parallaxCards.length > 0) {
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            parallaxCards.forEach(card => {
                if (card.closest('.hero-slide.active')) {
                    card.style.transform = `translateY(${scrollY * 0.08}px)`;
                }
            });
        }, { passive: true });
    }

    // --- 12. MAGNETIC BUTTON EFFECT ---
    const magneticBtns = document.querySelectorAll('.nav-cta-btn, .hero-actions .btn-gold');
    if (window.matchMedia('(min-width: 769px)').matches) {
        magneticBtns.forEach(btn => {
            btn.addEventListener('mousemove', (e) => {
                const rect = btn.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                btn.style.transform = `translate(${x * 0.15}px, ${y * 0.15}px)`;
            });
            btn.addEventListener('mouseleave', () => {
                btn.style.transform = '';
            });
        });
    }

    // --- 13. OFFER DETAILS (DYNAMIC SPA ROUTING) ---
    const btnViewOffers = document.querySelectorAll('.btn-view-offer');
    btnViewOffers.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const card = btn.closest('.offer-card');
            if (card) {
                const offerId = card.dataset.offerId;
                const data = (offerId && typeof offersData !== 'undefined') ? offersData[offerId] : null;

                if (data && typeof data === 'object') {
                    // Save to localStorage so refresh works
                    localStorage.setItem('lastOfferId', offerId);

                    // Pick content based on current language
                    const lang = currentLang || 'ca';
                    const d = (data[lang] && typeof data[lang] === 'object') ? data[lang] : data;

                    // UI labels per language
                    const lbl = {
                        gallery:    lang === 'es' ? "Galería de Imágenes"        : "Galeria d'Imatges",
                        itinerary:  lang === 'es' ? "Itinerario Día a Día"       : "Itinerari Dia a Dia",
                        included:   lang === 'es' ? "¿Qué Incluye Este Viaje?"   : "Què Inclou Aquest Viatge?",
                        sidebarInc: lang === 'es' ? [
                            "Vuelos ida y vuelta incluidos",
                            "Alojamientos con desayuno",
                            "Traslados o coche de alquiler",
                            "Seguro de cancelación y asistencia"
                        ] : [
                            "Vols anada i tornada inclosos",
                            "Allotjaments amb esmorzar",
                            "Trasllats o cotxe de lloguer",
                            "Assegurança d'anul·lació i assistència"
                        ],
                        ctaBtn:     lang === 'es' ? "Solicitar propuesta"         : "Sol·licitar proposta",
                        backBtn:    lang === 'es' ? "Volver a todas las ofertas"  : "Tornar a totes les ofertes",
                        priceFrom:  lang === 'es' ? "Precio Desde"               : "Preu Des de",
                        priceNote:  lang === 'es' ? "* Precio estimado por persona. Personalizable según tus fechas." : "* Preu estimat per persona. Personalitzable segons les teves dates.",
                        ctaAdvH:    lang === 'es' ? "Viaje 100% a tu medida"      : "Viatge 100% a la teva mida",
                        ctaAdvP:    lang === 'es' ? "¿Quieres añadir días, cambiar de hotel o adaptar el recorrido? Diseñamos el itinerario según tus gustos." : "Vols afegir dies, canviar d'hotel o adaptar el recorregut? Dissenyem l'itinerari segons els teus gustos.",
                        metaFlight: lang === 'es' ? "Vuelos desde Barcelona"      : "Vols des de Barcelona",
                        metaHotel:  lang === 'es' ? "Hoteles 4* & Boutique"       : "Hotels 4* & Boutique",
                        metaAssist: lang === 'es' ? "Asistencia 24/7"             : "Assistència 24/7",
                    };

                    // Update header fields
                    document.getElementById('detail-title').textContent = d.title;
                    document.getElementById('detail-subtitle').textContent = d.subtitle || '';
                    document.getElementById('detail-price').textContent = d.price;
                    document.getElementById('detail-duration').textContent = d.duration;

                    // Hero Background
                    if (d.heroImage) {
                        document.getElementById('detail-bg').style.backgroundImage = `url('${d.heroImage}')`;
                    }

                    // Tag Badge
                    const tagWrap = document.getElementById('detail-tag-wrap');
                    if (tagWrap) {
                        const iconClass = d.badgeIcon || 'fa-tag';
                        tagWrap.innerHTML = `<span class="offer-tag"><i class="fa-solid ${iconClass}"></i> ${d.tag}</span>`;
                    }

                    // Update meta items
                    const metaItems = document.querySelectorAll('.hero-detail-meta-item span');
                    if (metaItems[1]) metaItems[1].textContent = lbl.metaFlight;
                    if (metaItems[2]) metaItems[2].textContent = lbl.metaHotel;
                    if (metaItems[3]) metaItems[3].textContent = lbl.metaAssist;

                    // Update sidebar texts
                    const priceLabel = document.querySelector('#detail-cta-contact')?.closest('.glass-form-card')?.querySelector('.pill-badge');
                    if (priceLabel) priceLabel.innerHTML = `<i class="fa-solid fa-sparkles"></i> ${lbl.priceFrom}`;
                    const priceNote = document.querySelector('#detail-cta-contact')?.closest('.glass-form-card')?.querySelector('.form-subtext');
                    if (priceNote) priceNote.textContent = lbl.priceNote;
                    const sidebarList = document.querySelector('.sidebar-feature-list');
                    if (sidebarList) {
                        sidebarList.innerHTML = lbl.sidebarInc.map((t, i) => {
                            const icons = ['fa-plane-departure','fa-bed','fa-car','fa-shield-heart'];
                            return `<li><i class="fa-solid ${icons[i]}"></i> ${t}</li>`;
                        }).join('');
                    }
                    const advBox = document.querySelector('.sidebar-advice-box');
                    if (advBox) advBox.innerHTML = `
                        <i class="fa-solid fa-headset text-gold" style="font-size:1.2rem;margin-bottom:0.5rem;display:block;"></i>
                        <strong>${lbl.ctaAdvH}</strong>
                        <p style="margin:0.25rem 0 0 0;font-size:0.82rem;">${lbl.ctaAdvP}</p>`;
                    const ctaBtn = document.getElementById('detail-cta-contact');
                    if (ctaBtn) {
                        ctaBtn.innerHTML = `<span>${lbl.ctaBtn}</span> <i class="fa-solid fa-paper-plane btn-arrow-icon"></i>`;
                        ctaBtn.onclick = () => {
                            const msgInput = document.getElementById('contacte-missatge');
                            if (msgInput) {
                                msgInput.value = lang === 'es'
                                    ? `Hola, me interesa solicitar información sobre la oferta "${d.title}" (${d.duration}).`
                                    : `Hola, m'interessa sol·licitar informació sobre l'oferta "${d.title}" (${d.duration}).`;
                            }
                        };
                    }
                    const backBtn = document.querySelector('#view-oferta-detall .btn-outline[data-target="ofertes"]');
                    if (backBtn) backBtn.innerHTML = `<i class="fa-solid fa-arrow-left"></i> <span>${lbl.backBtn}</span>`;

                    // Build Rich Body Content
                    let html = '';

                    // 1. Highlight Banner
                    if (d.highlights) {
                        html += `
                            <div class="offer-highlight-banner">
                                <p><i class="fa-solid fa-quote-left text-gold" style="margin-right:0.5rem;opacity:0.6;"></i>${d.highlights}</p>
                            </div>`;
                    }

                    // 2. Photo Gallery
                    if (d.gallery && d.gallery.length > 0) {
                        html += `
                            <div class="offer-gallery-section">
                                <h3><i class="fa-solid fa-camera-retro text-gold"></i> ${lbl.gallery}</h3>
                                <div class="offer-gallery-grid">`;
                        d.gallery.forEach(imgUrl => {
                            html += `
                                <div class="offer-gallery-item" onclick="openLightbox('${imgUrl}', '${d.title.replace(/'/g, "\\'")}')">
                                    <img src="${imgUrl}" alt="${d.title}" loading="lazy">
                                </div>`;
                        });
                        html += `</div></div>`;
                    }

                    // 3. Day-by-Day Itinerary Timeline
                    if (d.itinerary && d.itinerary.length > 0) {
                        html += `
                            <div class="itinerary-section">
                                <h3><i class="fa-solid fa-map-location-dot text-gold"></i> ${lbl.itinerary}</h3>
                                <div class="itinerary-timeline">`;
                        d.itinerary.forEach(item => {
                            html += `
                                <div class="timeline-card">
                                    <span class="timeline-day-badge">${item.day}</span>
                                    <h4 class="timeline-card-title">${item.title}</h4>
                                    <p class="timeline-card-desc">${item.desc}</p>
                                </div>`;
                        });
                        html += `</div></div>`;
                    }

                    // 4. What's Included
                    if (d.included && d.included.length > 0) {
                        html += `
                            <div class="inclusions-card">
                                <h3><i class="fa-solid fa-circle-check text-gold"></i> ${lbl.included}</h3>
                                <ul class="inclusions-list">`;
                        d.included.forEach(inc => {
                            html += `<li><i class="fa-solid fa-check"></i><span>${inc}</span></li>`;
                        });
                        html += `</ul></div>`;
                    }

                    document.getElementById('detail-body').innerHTML = html;
                } else {
                    // Fallback if data object not found
                    const imgWrap = card.querySelector('.offer-image-wrap img');
                    if (imgWrap) document.getElementById('detail-bg').style.backgroundImage = `url('${imgWrap.src}')`;
                    const title = card.querySelector('.offer-title');
                    if (title) document.getElementById('detail-title').textContent = title.textContent;
                    const desc = card.querySelector('.offer-desc');
                    if (desc) document.getElementById('detail-body').innerHTML = '<p class="lead-text">' + desc.textContent + '</p>';
                }

                window.location.hash = 'oferta-detall';
                switchView('oferta-detall');
            }
        });
    });

});
