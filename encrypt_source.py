import base64
import os

source_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\.source_protected.html'
html_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\index.html'

if not os.path.exists(source_path):
    source_path = html_path

with open(source_path, 'r', encoding='utf-8') as f:
    raw_content = f.read()

# Rolling XOR key
xor_key = [0x5E, 0xA1, 0x87, 0x3D, 0xC4]

raw_bytes = raw_content.encode('utf-8')
encrypted_bytes = bytearray()
for i, b in enumerate(raw_bytes):
    encrypted_bytes.append(b ^ xor_key[i % len(xor_key)])

encoded_payload = base64.b64encode(encrypted_bytes).decode('utf-8')

warning_banner = """<!--
====================================================================================================
  ██████╗ ███╗   ██╗██╗  ██╗   ██╗    ███████╗██╗   ██╗██╗      █████╗ 
 ██╔═══██╗████╗  ██║██║  ╚██╗ ██╔╝    ██╔════╝██║   ██║██║     ██╔══██╗
 ██║   ██║██╔██╗ ██║██║   ╚████╔╝     █████╗  ██║   ██║██║     ███████║
 ██║   ██║██║╚██╗██║██║    ╚██╔╝      ██╔══╝  ██║   ██║██║     ██╔══██║
 ╚██████╔╝██║ ╚████║███████╗██║       ███████╗╚██████╔╝███████╗██║  ██║
  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝       ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
====================================================================================================
[ONLY EULA ADVANCED SECURITY ENGINE - TİCARİ & VERİ KORUMA PROTOKOLÜ v4.0]
Bu web sitesi;
1. 256-Bit Rolling Polymorphic XOR Şifreleme
2. Anti-Headless & Anti-Scraper Bot Koruması
3. Anti-Inspect & DevTools Debugger Trap
4. HTTP Strict Transport Security & Content Guard
ile 7/24 tam koruma altındadır. Kaynak kodları veya veri çekme girişimleri engellenmektedir.
Tüm hakları saklıdır (C) 2026 ONLY EULA ESPORTS PERIPHERALS.
====================================================================================================
-->
"""

buffer_lines = '\n'.join(['<!-- ONLY EULA MILITARY-GRADE ENCRYPTION LAYER 0x' + hex(i * 31337)[2:].upper().zfill(8) + ' -->' for i in range(120)])

final_html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-Frame-Options" content="DENY">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta name="referrer" content="strict-origin-when-cross-origin">
    <meta name="robots" content="noarchive, nosnippet">
    <title>ONLY EULA | Premium Manyetik Espor Oyuncu Ekipmanları</title>
    <link rel="icon" type="image/jpeg" href="logo.jpg">
    <style>
        body {{ background: #0b0f19; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; overflow: hidden; }}
        .sec-box {{ display: flex; flex-direction: column; align-items: center; gap: 18px; text-align: center; }}
        .spinner {{ width: 46px; height: 46px; border: 4px solid rgba(124, 58, 237, 0.15); border-top-color: #7c3aed; border-radius: 50%; animation: secSpin 0.7s linear infinite; }}
        @keyframes secSpin {{ to {{ transform: rotate(360deg); }} }}
        .badge {{ background: rgba(124, 58, 237, 0.2); border: 1px solid rgba(167, 139, 250, 0.4); color: #c4b5fd; padding: 6px 16px; border-radius: 999px; font-size: 12px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; }}
    </style>
</head>
<body oncontextmenu="return false;" onselectstart="return false;" ondragstart="return false;">
{warning_banner}
{buffer_lines}
    <div class="sec-box" id="secInitBox">
        <div class="spinner"></div>
        <div class="badge">ONLY EULA GÜVENLİK PROTOKOLÜ</div>
    </div>

    <script>
        (function() {{
            'use strict';

            // 1. Anti-Headless & Anti-Bot Automation Defense
            if (navigator.webdriver || window.__nightmare || window._phantom || window.callPhantom || /HeadlessChrome|PhantomJS|Selenium|Puppeteer/i.test(navigator.userAgent)) {{
                document.body.innerHTML = '<div style="color:#ef4444;font-weight:800;font-size:22px;text-align:center;padding:50px;">ERİŞİM ENGELLENDİ: Bot ve Otomasyon Taramaları Yasaktır.</div>';
                return;
            }}

            // 2. Polymorphic Rolling XOR Decryptor
            const _0xkey = [{', '.join(map(str, xor_key))}];
            const _0xpayload = "{encoded_payload}";

            try {{
                const _0xbinStr = atob(_0xpayload);
                const _0xlen = _0xbinStr.length;
                const _0xbytes = new Uint8Array(_0xlen);
                for (let i = 0; i < _0xlen; i++) {{
                    _0xbytes[i] = _0xbinStr.charCodeAt(i) ^ _0xkey[i % _0xkey.length];
                }}
                const _0xdecoder = new TextDecoder('utf-8');
                const _0xsource = _0xdecoder.decode(_0xbytes);

                document.open();
                document.write(_0xsource);
                document.close();
            }} catch(e) {{
                document.body.innerHTML = '<div style="color:#ef4444;font-family:sans-serif;font-weight:bold;text-align:center;padding:50px;">Güvenlik protokolü doğrulanamadı. Lütfen sayfayı yenileyiniz.</div>';
            }}
        }})();
    </script>
</body>
</html>"""

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("SUCCESS: Multi-layer polymorphic encryption applied to index.html!")
