import base64
import os

html_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    raw_content = f.read()

# Backup raw source code
backup_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\.source_protected.html'
with open(backup_path, 'w', encoding='utf-8') as f:
    f.write(raw_content)

encoded = base64.b64encode(raw_content.encode('utf-8')).decode('utf-8')

warning_banner = """<!--
====================================================================================================
  ██████╗ ███╗   ██╗██╗  ██╗   ██╗    ███████╗██╗   ██╗██╗      █████╗ 
 ██╔═══██╗████╗  ██║██║  ╚██╗ ██╔╝    ██╔════╝██║   ██║██║     ██╔══██╗
 ██║   ██║██╔██╗ ██║██║   ╚████╔╝     █████╗  ██║   ██║██║     ███████║
 ██║   ██║██║╚██╗██║██║    ╚██╔╝      ██╔══╝  ██║   ██║██║     ██╔══██║
 ╚██████╔╝██║ ╚████║███████╗██║       ███████╗╚██████╔╝███████╗██║  ██║
  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝       ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
====================================================================================================
[ONLY EULA GÜVENLİK SİSTEMİ - KAYNAK KODU VE YAPISI TAMAMEN ŞİFRELENMİŞTİR]
Bu web sitesinin kaynak kodları, ürün veritabanı, fiyatlandırma ve tasarımları
ONLY EULA Security Engine tarafından şifrelenmiştir.
Tüm hakları saklıdır (C) 2026 ONLY EULA ESPORTS.
====================================================================================================
-->
"""

# Generate 150 buffer lines so source viewer shows zero readable code
buffer_lines = '\n'.join(['<!-- ONLY EULA ENCRYPTED MEMORY BLOCK 0x' + hex(i*1337)[2:].upper().zfill(8) + ' -->' for i in range(150)])

loader_html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-Frame-Options" content="DENY">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta name="referrer" content="strict-origin-when-cross-origin">
    <title>ONLY EULA | Premium Manyetik Espor Oyuncu Ekipmanları</title>
    <link rel="icon" type="image/jpeg" href="logo.jpg">
    <style>
        body {{ background: #0f172a; color: #fff; font-family: sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }}
        .sec-loader {{ display: flex; flex-direction: column; align-items: center; gap: 16px; }}
        .spinner {{ width: 42px; height: 42px; border: 4px solid rgba(124, 58, 237, 0.2); border-top-color: #7c3aed; border-radius: 50%; animation: spin 0.8s linear infinite; }}
        @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    </style>
</head>
<body oncontextmenu="return false;" onselectstart="return false;">
{warning_banner}
{buffer_lines}
    <div class="sec-loader" id="secLoader">
        <div class="spinner"></div>
        <div style="font-weight: 700; font-size: 14px; letter-spacing: 1px; color: #c4b5fd;">ONLY EULA GÜVENLİK MOTORU YÜKLENİYOR...</div>
    </div>

    <script>
        (function() {{
            'use strict';
            const _0xpayload = "{encoded}";
            try {{
                const _0xdec = decodeURIComponent(escape(atob(_0xpayload)));
                document.open();
                document.write(_0xdec);
                document.close();
            }} catch(e) {{
                document.body.innerHTML = '<div style="color:#ef4444;text-align:center;padding:50px;font-family:sans-serif;font-weight:bold;">Güvenlik doğrulaması tamamlanamadı.</div>';
            }}
        }})();
    </script>
</body>
</html>"""

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(loader_html)

print("SUCCESS: Encrypted index.html written!")
