import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<p class="promo-desc">Anodize camgöbeği alüminyum kasa üzerine ince işçilikle kazınmış lazer gravür detaylar. Tuşların üzerine yayılan özel yapım sanatsal tasarım ile güzelliğin ve 8000Hz performansın zirvesi.</p>',
    '<p class="promo-desc">Normal profil ince camgöbeği alüminyum kasa üzerine kazınmış lazer gravür detaylar. Tamamen Manyetik (Hall-Effect) switchler ve tuşlara yayılan özel yapım anime tasarımı ile %100 gerçekçi, 8000Hz performansın zirvesi.</p>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
