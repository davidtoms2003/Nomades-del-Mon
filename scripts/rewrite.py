import re
import os

filepath = r"C:\Users\david\Documents\Antigravity\Pagina Web\styles.css"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace Theme Blocks
dark_theme = """body.theme-dark {
    --bg-deep: #1A1612;
    --bg-surface: #231F1A;
    --bg-card: #2A2520;
    --bg-card-hover: #342E28;
    --bg-glass: rgba(26, 22, 18, 0.92);
    --bg-glass-border: rgba(199, 91, 57, 0.2);
    --accent: #C75B39;
    --accent-hover: #D96B49;
    --accent-dark: #A04428;
    --accent-glow: rgba(199, 91, 57, 0.2);
    --accent-tag-bg: rgba(199, 91, 57, 0.1);
    --accent-sand: #E8D5B7;
    --accent-olive: #6B7F5E;
    --accent-blue: #4A7FB5;
    --text-main: #E8E0D6;
    --text-heading: #F5EDE3;
    --text-muted: #9E9286;
    --text-dark: #1A1612;
    --top-bar-bg: #14110E;
    --footer-bg: #12100D;
    --footer-bottom-bg: #0D0B09;
    --shadow-soft: 0 16px 36px rgba(26, 22, 18, 0.5);
    --shadow-accent: 0 8px 25px rgba(199, 91, 57, 0.2);
    --border-subtle: rgba(255, 255, 255, 0.06);
    --border-glass: rgba(255, 255, 255, 0.1);
}"""

light_theme = """body.theme-light {
    --bg-deep: #FAF5EE;
    --bg-surface: #FFFFFF;
    --bg-card: #FFFFFF;
    --bg-card-hover: #F5EDE3;
    --bg-glass: rgba(250, 245, 238, 0.94);
    --bg-glass-border: rgba(180, 75, 45, 0.25);
    --accent: #B54E30;
    --accent-hover: #C75B39;
    --accent-dark: #8B3A20;
    --accent-glow: rgba(181, 78, 48, 0.15);
    --accent-tag-bg: rgba(181, 78, 48, 0.08);
    --accent-sand: #C4A882;
    --accent-olive: #4E6344;
    --accent-blue: #3B6A9A;
    --text-main: #3D3428;
    --text-heading: #1A1612;
    --text-muted: #7A6E62;
    --text-dark: #FFFFFF;
    --top-bar-bg: #F0E8DC;
    --footer-bg: #EBE3D5;
    --footer-bottom-bg: #DDD4C5;
    --shadow-soft: 0 14px 30px rgba(26, 22, 18, 0.08);
    --shadow-accent: 0 6px 20px rgba(181, 78, 48, 0.15);
    --border-subtle: rgba(0, 0, 0, 0.06);
    --border-glass: rgba(0, 0, 0, 0.08);
}"""

root_theme = """:root {
    --font-heading: 'DM Serif Display', Georgia, serif;
    --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    --transition-fast: 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    --transition-smooth: 0.45s cubic-bezier(0.16, 1, 0.3, 1);
    --radius-sm: 8px;
    --radius-md: 16px;
    --radius-lg: 24px;
    --radius-full: 9999px;
    --radius-editorial: 2px 20px 20px 20px;
}"""

content = re.sub(r'body\.theme-dark\s*\{[^}]*\}', dark_theme, content)
content = re.sub(r'body\.theme-light\s*\{[^}]*\}', light_theme, content)
content = re.sub(r':root\s*\{[^}]*\}', root_theme, content)

# 2. Variable renaming in usages
replacements = {
    'var(--bg-dark)': 'var(--bg-deep)',
    'var(--primary-gold)': 'var(--accent)',
    'var(--primary-gold-hover)': 'var(--accent-hover)',
    'var(--primary-gold-dark)': 'var(--accent-dark)',
    'var(--gold-glow)': 'var(--accent-glow)',
    'var(--gold-tag-bg)': 'var(--accent-tag-bg)',
    'var(--shadow-gold)': 'var(--shadow-accent)'
}
for old, new in replacements.items():
    content = content.replace(old, new)

# 3. Class specific editorial updates
# .pill-badge
content = re.sub(
    r'(\.pill-badge\s*\{.*?)(border-radius:\s*var\(--radius-full\);)(.*?\})',
    r'\1border-radius: var(--radius-editorial);\n    position: relative;\n    overflow: hidden;\n\3\n.pill-badge::before {\n    content: "";\n    position: absolute;\n    left: 0;\n    top: 0;\n    bottom: 0;\n    width: 3px;\n    background: var(--accent);\n}',
    content, flags=re.DOTALL
)

# .btn-gold, .btn-primary, .btn-outline
content = content.replace('border-radius: var(--radius-full);', 'border-radius: 4px 22px 22px 22px;') # Generic update for .btn
content = re.sub(r'(\.btn-pill\s*\{.*?)(border-radius:.*?;\n?)(.*?\})', r'\1border-radius: var(--radius-full);\n\3', content, flags=re.DOTALL) # Restore full for btn-pill

# .offer-card border radius and hover
content = re.sub(r'(\.offer-card\s*\{.*?)(border-radius:\s*var\(--radius-lg\);)(.*?\})', r'\1border-radius: var(--radius-editorial);\3', content, flags=re.DOTALL)
content = re.sub(r'(\.offer-card:hover\s*\{.*?)(transform:.*?;\n?)(.*?box-shadow:.*?;\n?)(.*?\})', r'\1transform: translateY(-8px) rotate(-0.5deg);\n    box-shadow: 0 20px 40px rgba(199, 91, 57, 0.12);\n\4', content, flags=re.DOTALL)

# .hero-floating-card
content = re.sub(r'(\.hero-floating-card\s*\{.*?)(border-radius:\s*var\(--radius-lg\);)(.*?\})', r'\1border-radius: 4px 24px 24px 24px;\3', content, flags=re.DOTALL)
content = re.sub(r'(\.hero-floating-card:hover\s*\{.*?)(box-shadow:.*?;\n?)(.*?\})', r'\1box-shadow: 0 20px 40px rgba(199, 91, 57, 0.12);\n\3', content, flags=re.DOTALL)

# .glass-card-over, .glass-form-card, .comment-card
for cls in ['glass-card-over', 'glass-form-card', 'comment-card']:
    content = re.sub(rf'(\.{cls}\s*\{{.*?)(border-radius:\s*var\(--radius-[a-z]+\);)(.*?\}})', rf'\1border-radius: var(--radius-editorial);\3', content, flags=re.DOTALL)

# .offer-tag
content = re.sub(r'(\.offer-tag\s*\{.*?)(border-radius:\s*var\(--radius-full\);)(.*?\})', r'\1border-radius: 2px 14px 14px 14px;\3', content, flags=re.DOTALL)

# .text-gold
content = re.sub(r'\.text-gold\s*\{\s*color:.*?\s*\}', r'.text-gold { color: var(--accent) !important; }', content)

# .badge-gold
content = re.sub(r'\.badge-gold\s*\{\s*background:.*?\s*\}', r'.badge-gold { background: linear-gradient(135deg, var(--accent), var(--accent-dark)) !important; color: #000 !important; font-weight: 700; }', content)

# section-title after
content = re.sub(r'(\.section-title\s*\{.*?\})', r'\1\n.section-title::after {\n    content: "";\n    display: block;\n    width: 40px;\n    height: 3px;\n    background: var(--accent);\n    margin-top: 0.8rem;\n}', content, flags=re.DOTALL)

# section-offers before
# Assuming there's a .section-offers somewhere, if not we add the rule
new_css = """
/* --------------------------------------------------------------------------
   NEW EDITORIAL & DYNAMIC ELEMENTS
   -------------------------------------------------------------------------- */
.noise-overlay {
  position: fixed;
  inset: 0;
  z-index: 9999;
  pointer-events: none;
  opacity: 0.035;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-repeat: repeat;
  mix-blend-mode: overlay;
}

.custom-cursor {
  width: 40px;
  height: 40px;
  border: 1.5px solid var(--accent);
  border-radius: 50%;
  position: fixed;
  pointer-events: none;
  z-index: 10000;
  transition: transform 0.15s ease-out, width 0.3s, height 0.3s, border-color 0.3s;
  transform: translate(-50%, -50%);
  mix-blend-mode: difference;
}
.cursor-dot {
  width: 6px;
  height: 6px;
  background: var(--accent);
  border-radius: 50%;
  position: fixed;
  pointer-events: none;
  z-index: 10001;
  transform: translate(-50%, -50%);
  transition: transform 0.08s ease-out;
}
.custom-cursor.cursor-hover {
  width: 60px;
  height: 60px;
  border-color: var(--accent-sand);
}

@media (min-width: 769px) {
  body { cursor: none; }
  a, button, [role='button'], input, textarea, select { cursor: none; }
}

@media (max-width: 768px) {
  .custom-cursor, .cursor-dot { display: none; }
}

::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--bg-deep); }
::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent-hover); }

.marquee-wrapper {
  position: absolute;
  bottom: 5rem;
  left: 0;
  width: 100%;
  overflow: hidden;
  z-index: 5;
  opacity: 0.12;
  pointer-events: none;
}
.marquee-track {
  display: flex;
  gap: 2.5rem;
  animation: marquee-scroll 30s linear infinite;
  width: max-content;
  font-family: var(--font-heading);
  font-size: clamp(3rem, 8vw, 6rem);
  color: #FFFFFF;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  white-space: nowrap;
}
.marquee-dot {
  color: var(--accent);
  font-size: 0.6em;
  vertical-align: middle;
}
@keyframes marquee-scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

.reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}
.reveal.revealed {
  opacity: 1;
  transform: translateY(0);
}
.reveal.stagger-1 { transition-delay: 0.1s; }
.reveal.stagger-2 { transition-delay: 0.2s; }
.reveal.stagger-3 { transition-delay: 0.3s; }
.reveal.stagger-4 { transition-delay: 0.4s; }

.section-offers::before {
  content: "";
  display: block;
  width: 100%;
  height: 40px;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 120' preserveAspectRatio='none'%3E%3Cpath d='M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z' fill='%23C75B39' opacity='0.1'/%3E%3C/svg%3E");
  background-size: cover;
  background-repeat: no-repeat;
  margin-bottom: 2rem;
}

.social-links a[href*="facebook"]:hover, .social-links a:has(i.fa-facebook):hover { background: #4267B2; color: #fff; }
.social-links a[href*="twitter"]:hover, .social-links a:has(i.fa-twitter):hover, .social-links a:has(i.fa-x-twitter):hover { background: var(--text-heading); color: var(--bg-deep); }
.social-links a[href*="instagram"]:hover, .social-links a:has(i.fa-instagram):hover { background: #E1306C; color: #fff; }

"""

# Insert new_css right before media queries
parts = content.split('/* --------------------------------------------------------------------------\n   21. RESPONSIVE MEDIA QUERIES (MOBILE UI OPTIMIZATIONS)\n   -------------------------------------------------------------------------- */')
if len(parts) == 2:
    content = parts[0] + new_css + '/* --------------------------------------------------------------------------\n   21. RESPONSIVE MEDIA QUERIES (MOBILE UI OPTIMIZATIONS)\n   -------------------------------------------------------------------------- */' + parts[1]
else:
    content += new_css

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
