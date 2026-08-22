import base64
import os

source_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\.source_protected.html'
html_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\index.html'
core_js_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\core.dat.js'

with open(source_path, 'r', encoding='utf-8') as f:
    raw_content = f.read()

# 256-bit Rolling XOR key
xor_key = [0x5E, 0xA1, 0x87, 0x3D, 0xC4, 0x9B, 0x12, 0xF7]

raw_bytes = raw_content.encode('utf-8')
encrypted_bytes = bytearray()
for i, b in enumerate(raw_bytes):
    encrypted_bytes.append(b ^ xor_key[i % len(xor_key)])

encoded_payload = base64.b64encode(encrypted_bytes).decode('utf-8')

# Write the encrypted payload to core.dat.js
with open(core_js_path, 'w', encoding='utf-8') as f:
    f.write(f'window.__OE_CORE_DATA__ = "{encoded_payload}";')

taunting_banner = """<!--
====================================================================================================
  ██████╗ ███╗   ██╗██╗  ██╗   ██╗    ███████╗██╗   ██╗██╗      █████╗ 
 ██╔═══██╗████╗  ██║██║  ╚██╗ ██╔╝    ██╔════╝██║   ██║██║     ██╔══██╗
 ██║   ██║██╔██╗ ██║██║   ╚████╔╝     █████╗  ██║   ██║██║     ███████║
 ██║   ██║██║╚██╗██║██║    ╚██╔╝      ██╔══╝  ██║   ██║██║     ██╔══██║
 ╚██████╔╝██║ ╚████║███████╗██║       ███████╗╚██████╔╝███████╗██║  ██║
  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝       ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
====================================================================================================

😂 NE O, KAYNAK KODU MU ÇALACAKTIN?

Zahmet edip adres çubuğuna "view-source:" yazmışsın ama eline geçen tek şey bu mesaj oldu...

ONLY EULA'nın özel üretim manyetik klavye sistemlerini, ürün veritabanını, fiyatlarını ve 
özgün tasarımlarını öyle iki tıkla kopyalayıp çalabileceğini mi sandın gerçekten?

Burada sana göre hiçbir kod veya veri yok acemi dostum. Kodlarımız askeri düzeyde
şifreli ve senin erişim seviyenin fersah fersah üstünde.

Biz bu işe yıllarımızı verdik, sen 5 saniyede CTRL+U yapıp kopyalayamazsın.

Tavsiyemiz: O sekmeyi sakince kapat ve sektöre yön veren espor donanımlarımızı 
orijinal sitemizden hayranlıkla incelemeye devam et. 😉

[ ONLY EULA CYBER DEFENSE PROTOCOL - ACCESS PERMANENTLY DENIED ]
====================================================================================================
-->
"""

index_html = f"""{taunting_banner}<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ONLY EULA | Premium Manyetik Espor Oyuncu Ekipmanları</title>
    <link rel="icon" type="image/jpeg" href="logo.jpg">
</head>
<body oncontextmenu="return false;" onselectstart="return false;" ondragstart="return false;">
    <script src="engine.js"></script>
</body>
</html>"""

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(index_html)

print("SUCCESS: Ultra clean taunting index.html and core.dat.js generated!")
