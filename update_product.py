import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Modify right-bottom hero card
old_hero_card = '''<div class="hero-card right-bottom" onclick="openModal(1)">
                <img src="keyboard.jpg" alt="KF90 PRO" class="hero-img anim-5">
                <div class="hero-overlay"></div>
                <div class="hero-content">
                    <h3>KF90 HE PRO</h3>
                    <p>Ultimate Performans</p>
                </div>
            </div>'''
new_hero_card = '''<div class="hero-card right-bottom" onclick="openModal(9)">
                <img src="keyboard_always.jpg" alt="KF90 Always Edition" class="hero-img anim-5">
                <div class="hero-overlay"></div>
                <div class="hero-content">
                    <h3>KF90 Always Edition</h3>
                    <p>Limited Edition</p>
                </div>
            </div>'''
content = content.replace(old_hero_card, new_hero_card)

# Insert product 9 into JS
product_9_str = '''{
                id: 9, name: "KF90 HE PRO Always Edition", brand: "ONLY EULA", price: "₺8,999", oldPrice: null, 
                desc: "60% HE Klavye, özel üretim anime artwork keycaps tasarımı. 8000Hz, Rapid Trigger ve premium cyan alüminyum kasa.", 
                specs: ["Özel Üretim Anime Keycaps", "Cyan Alüminyum Kasa", "8000Hz Polling Rate", "Rapid Trigger (0.1mm - 4.0mm)", "Sınırlı Üretim"], 
                img: "keyboard_always.jpg", tag: "Limited"
            },
            '''
content = content.replace('const products = [\n', 'const products = [\n            ' + product_9_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
