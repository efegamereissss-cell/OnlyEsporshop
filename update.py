import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Animations
content = content.replace(
    '@keyframes kb1 { 0% { transform: scale(1) translate(0, 0); } 100% { transform: scale(1.15) translate(-2%, 2%); } }',
    '@keyframes kb1 { 0% { transform: scale(1) translate(0, 0); } 100% { transform: scale(1.25) translate(-4%, 4%); } }'
)
content = content.replace(
    '@keyframes kb2 { 0% { transform: scale(1.1) translate(2%, -2%); } 100% { transform: scale(1) translate(0, 0); } }',
    '@keyframes kb2 { 0% { transform: scale(1.2) translate(4%, -4%); } 100% { transform: scale(1) translate(0, 0); } }'
)
content = content.replace(
    '@keyframes kb3 { 0% { transform: scale(1) translate(0, 0); } 100% { transform: scale(1.1) translate(2%, 2%); } }',
    '@keyframes kb3 { 0% { transform: scale(1) translate(0, 0); } 100% { transform: scale(1.2) translate(4%, 4%); } }'
)
content = content.replace(
    '@keyframes kb4 { 0% { transform: scale(1.15) translate(-2%, -2%); } 100% { transform: scale(1) translate(0, 0); } }',
    '@keyframes kb4 { 0% { transform: scale(1.25) translate(-4%, -4%); } 100% { transform: scale(1) translate(0, 0); } }'
)
content = content.replace(
    '@keyframes kb5 { 0% { transform: scale(1.05) translate(1%, 0); } 100% { transform: scale(1.15) translate(-1%, -1%); } }',
    '@keyframes kb5 { 0% { transform: scale(1.05) translate(2%, 0); } 100% { transform: scale(1.25) translate(-2%, -2%); } }'
)

# Faster animations
content = content.replace('.anim-1 { animation: kb1 20s infinite alternate ease-in-out; }', '.anim-1 { animation: kb1 12s infinite alternate ease-in-out; }')
content = content.replace('.anim-2 { animation: kb2 18s infinite alternate ease-in-out; }', '.anim-2 { animation: kb2 10s infinite alternate ease-in-out; }')
content = content.replace('.anim-3 { animation: kb3 22s infinite alternate ease-in-out; }', '.anim-3 { animation: kb3 14s infinite alternate ease-in-out; }')
content = content.replace('.anim-4 { animation: kb4 15s infinite alternate ease-in-out; }', '.anim-4 { animation: kb4 9s infinite alternate ease-in-out; }')
content = content.replace('.anim-5 { animation: kb5 25s infinite alternate ease-in-out; }', '.anim-5 { animation: kb5 15s infinite alternate ease-in-out; }')

# More intense hover
content = content.replace(
    '.hero-card:hover .hero-img { transform: scale(1.08) !important; animation-play-state: paused; }',
    '.hero-card:hover .hero-img { transform: scale(1.15) !important; animation-play-state: paused; transition: transform 0.8s cubic-bezier(0.25, 1, 0.5, 1); }'
)

# 2. Add Dropdown CSS
css_dropdown = '''
        .nav-center .dropdown { position: relative; display: flex; align-items: center; cursor: pointer; height: 100%; }
        .dropdown-menu { 
            position: absolute; top: 40px; left: -16px; background: var(--white); 
            box-shadow: 0 10px 30px rgba(0,0,0,0.1); border-radius: 12px; padding: 12px;
            display: flex; flex-direction: column; min-width: 200px;
            opacity: 0; visibility: hidden; transform: translateY(10px); transition: all 0.3s ease;
            border: 1px solid var(--border); z-index: 100;
        }
        .nav-center .dropdown:hover .dropdown-menu { opacity: 1; visibility: visible; transform: translateY(0); }
        .dropdown-menu a { padding: 12px 16px; border-radius: 8px; font-weight: 500; display: block; color: var(--text-main); text-decoration: none; }
        .dropdown-menu a:hover { background: var(--bg); color: var(--primary); }
'''
content = content.replace('/* Hero Grid */', css_dropdown + '\n        /* Hero Grid */')

# 3. Add Dropdown HTML
html_dropdown_kategoriler = '''
            <div class="dropdown">
                <span>Kategoriler ▾</span>
                <div class="dropdown-menu">
                    <a href="#">Klavyeler</a>
                    <a href="#">Mousepadler</a>
                    <a href="#">Aksesuarlar</a>
                    <a href="#">Switches</a>
                </div>
            </div>
'''
content = re.sub(r'<a href="#">Kategoriler.*?</a>', html_dropdown_kategoriler, content)

html_dropdown_markalar = '''
            <div class="dropdown">
                <span>Markalar ▾</span>
                <div class="dropdown-menu">
                    <a href="#">ONLY EULA</a>
                    <a href="#">Wraith</a>
                    <a href="#">Gateron</a>
                </div>
            </div>
'''
content = re.sub(r'<a href="#">Markalar.*?</a>', html_dropdown_markalar, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
