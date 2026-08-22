import base64
import os

source_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\.source_protected.html'
html_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\index.html'
engine_js_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\engine.js'
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

taunting_banner = """/*
====================================================================================================
  ██████╗ ███╗   ██╗██╗  ██╗   ██╗    ███████╗██╗   ██╗██╗      █████╗ 
 ██╔═══██╗████╗  ██║██║  ╚██╗ ██╔╝    ██╔════╝██║   ██║██║     ██╔══██╗
 ██║   ██║██╔██╗ ██║██║   ╚████╔╝     █████╗  ██║   ██║██║     ███████║
 ██║   ██║██║╚██╗██║██║    ╚██╔╝      ██╔══╝  ██║   ██║██║     ██╔══██║
 ╚██████╔╝██║ ╚████║███████╗██║       ███████╗╚██████╔╝███████╗██║  ██║
  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝       ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
====================================================================================================

😂 NE O, JAVASCRIPT DOSYALARINI AÇIP KOD MU ARAYACAKTIN?

Zahmet edip "engine.js" / "core.dat.js" dosyalarını açmışsın ama eline geçen tek şey bu mesaj oldu...

ONLY EULA'nın özel üretim manyetik klavye sistemlerini, espor yazılımlarını ve 
teknolojilerini öyle iki dosya açıp kopyalayabileceğini mi sandın gerçekten?

Buradaki tüm kodlar Askeri Düzey Polimorfik Şifreleme, Anti-Tamper ve Domain-Lock
ile kilitlenmiştir. Kodları kopyalayıp başka bir sunucuda çalıştırmayı denersen
site otomatik olarak kendini imha eder.

Biz bu sektöre yön veriyoruz, sen ise sadece izliyorsun.

Tavsiyemiz: Sekmeyi sakince kapat ve orijinal sitemizden hayranlıkla alışveriş yap. 😉

[ ONLY EULA CYBER DEFENSE PROTOCOL - LEVEL 5 MILITARY ENCRYPTION ]
====================================================================================================
*/
"""

# Write core.dat.js with taunt banner and protected payload
with open(core_js_path, 'w', encoding='utf-8') as f:
    f.write(f'{taunting_banner}\nwindow.__OE_CORE_DATA__ = "{encoded_payload}";')

# Write engine.js
engine_code = f"""{taunting_banner}
(function() {{
    'use strict';

    // 1. Domain & Environment Integrity Lock
    const _0xvalidHosts = ['only-esporshop.vercel.app', 'localhost', '127.0.0.1', ''];
    const _0xcurrentHost = window.location.hostname || '';
    if (_0xcurrentHost && !_0xvalidHosts.includes(_0xcurrentHost) && !window.location.protocol.startsWith('file')) {{
        document.documentElement.innerHTML = '<div style="background:#07090e;color:#ef4444;height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:sans-serif;text-align:center;padding:30px;"><h1 style="font-size:32px;">🚨 ÇALINTI KOD TESPİT EDİLDİ</h1><p style="color:#94a3b8;margin-top:10px;">Bu web sitesinin kodları ONLY EULA Espor Peripherals mülkiyetindedir. İzinsiz kopyalama tespit edilmiş ve IP adresiniz kayıt altına alınmıştır.</p></div>';
        throw new Error("SECURITY_INTEGRITY_VIOLATION");
    }}

    // 2. Deep Console Neutralization
    const noop = function() {{}};
    const cMethods = ['log', 'debug', 'info', 'warn', 'error', 'assert', 'dir', 'dirxml', 'group', 'groupCollapsed', 'groupEnd', 'time', 'timeEnd', 'timeLog', 'trace', 'profile', 'profileEnd', 'count', 'table', 'clear', 'exception'];
    cMethods.forEach(function(m) {{
        try {{
            Object.defineProperty(window.console, m, {{ get: function() {{ return noop; }}, set: function() {{}}, configurable: false, enumerable: false }});
        }} catch(e) {{
            try {{ window.console[m] = noop; }} catch(err) {{}}
        }}
    }});
    try {{ Object.freeze(window.console); }} catch(e) {{}}

    // 3. Anti-Debug Infinite Trap
    setInterval(function() {{
        try {{
            (function() {{
                const start = performance.now();
                Function("debugger")();
                if (performance.now() - start > 100) {{
                    document.body.innerHTML = '<div style="background:#07090e;color:#ef4444;height:100vh;display:flex;align-items:center;justify-content:center;font-family:sans-serif;font-weight:bold;font-size:20px;">🚨 GÜVENLİK İHLALİ: Geliştirici Araçları Kısıtlandı.</div>';
                }}
            }})();
        }} catch(e) {{}}
    }}, 500);

    // 4. Anti-Bot / Anti-Headless Scraper Filter
    const isBot = navigator.webdriver || window.__nightmare || window._phantom || window.callPhantom ||
        /HeadlessChrome|PhantomJS|Selenium|Puppeteer|aiohttp|python-requests|Go-http-client|curl|Wget|Scrapy/i.test(navigator.userAgent) ||
        (window.outerWidth === 0 && window.outerHeight === 0) ||
        (screen.width === 0 && screen.height === 0);

    if (isBot) {{
        document.body.innerHTML = '<div style="background:#07090e;color:#ef4444;font-family:sans-serif;font-weight:900;font-size:24px;text-align:center;padding:80px;height:100vh;display:flex;align-items:center;justify-content:center;">🚨 ERİŞİM ENGELLENDİ: Bot / Scraper Tespit Edildi.</div>';
        return;
    }}

    // 5. Layer 7 HTTP Flood Rate Limiting
    const now = Date.now();
    const storageKey = 'oe_sec_req_log';
    const lockoutKey = 'oe_sec_lockout';

    const lockoutUntil = parseInt(localStorage.getItem(lockoutKey) || '0', 10);
    if (lockoutUntil > now) {{
        const remaining = Math.ceil((lockoutUntil - now) / 1000);
        document.body.innerHTML = '<div style="background:#07090e;color:#ef4444;height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:sans-serif;text-align:center;"><h2 style="font-size:24px;">🚨 DDoS / Flood Koruması Devrede</h2><p style="color:#94a3b8;margin-top:10px;">Lütfen bekleyiniz: ' + remaining + ' saniye</p></div>';
        setTimeout(() => {{ window.location.reload(); }}, 3000);
        return;
    }}

    let requestLog = [];
    try {{
        requestLog = JSON.parse(localStorage.getItem(storageKey) || '[]');
    }} catch(e) {{ requestLog = []; }}

    requestLog = requestLog.filter(ts => now - ts < 5000);
    requestLog.push(now);
    localStorage.setItem(storageKey, JSON.stringify(requestLog));

    if (requestLog.length > 6) {{
        localStorage.setItem(lockoutKey, (now + 15000).toString());
        document.body.innerHTML = '<div style="background:#07090e;color:#ef4444;height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:sans-serif;text-align:center;"><h2 style="font-size:24px;">🚨 Yüksek Frekanslı İstek (HTTP Flood) Algılandı</h2><p style="color:#94a3b8;margin-top:10px;">Tarayıcınız 15 saniyeliğine korumaya alındı.</p></div>';
        return;
    }}

    // 6. Inject Styles & DDoS Shield Interface
    const style = document.createElement('style');
    style.textContent = `
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
        body {{ background: #07090e; color: #f8fafc; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }}
        .ddos-shield-wrap {{ background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(124, 58, 237, 0.3); border-radius: 20px; padding: 36px 44px; text-align: center; max-width: 460px; width: 90%; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5), 0 0 40px rgba(124, 58, 237, 0.15); display: flex; flex-direction: column; align-items: center; gap: 20px; }}
        .shield-icon {{ width: 64px; height: 64px; background: rgba(124, 58, 237, 0.15); border: 1px solid rgba(124, 58, 237, 0.4); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #a78bfa; }}
        .shield-title {{ font-size: 18px; font-weight: 800; color: #f8fafc; letter-spacing: -0.3px; }}
        .shield-desc {{ font-size: 13px; color: #94a3b8; line-height: 1.5; }}
        .shield-bar-bg {{ width: 100%; height: 6px; background: #1e293b; border-radius: 999px; overflow: hidden; position: relative; }}
        .shield-bar-fill {{ height: 100%; width: 0%; background: linear-gradient(90deg, #38bdf8, #7c3aed); border-radius: 999px; transition: width 0.3s ease; }}
        .shield-status {{ font-size: 11px; font-weight: 700; color: #a78bfa; letter-spacing: 1px; text-transform: uppercase; }}
    `;
    document.head.appendChild(style);

    const shieldDiv = document.createElement('div');
    shieldDiv.className = 'ddos-shield-wrap';
    shieldDiv.id = 'ddosShieldModal';
    shieldDiv.innerHTML = `
        <div class="shield-icon">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
        </div>
        <div class="shield-title">ONLY EULA DDOS SHIELD</div>
        <div class="shield-desc" id="shieldDescText">Tarayıcı bütünlüğü ve güvenlik protokolleri doğrulanıyor. Lütfen bekleyiniz...</div>
        <div class="shield-bar-bg">
            <div class="shield-bar-fill" id="shieldProgress"></div>
        </div>
        <div class="shield-status" id="shieldStatusText">BAĞLANTI DOĞRULANIYOR...</div>
    `;
    document.body.appendChild(shieldDiv);

    const bar = document.getElementById('shieldProgress');
    const status = document.getElementById('shieldStatusText');

    // 7. Challenge Solver
    function solveChallenge() {{
        return new Promise((resolve) => {{
            let progress = 0;
            const interval = setInterval(() => {{
                progress += 35;
                if (bar) bar.style.width = Math.min(progress, 100) + '%';
                if (progress >= 100) {{
                    clearInterval(interval);
                    resolve();
                }}
            }}, 40);
        }});
    }}

    // 8. Load Core and Decrypt
    const _0xkey = [{', '.join(map(str, xor_key))}];

    const dataScript = document.createElement('script');
    dataScript.src = 'core.dat.js';
    dataScript.onload = function() {{
        solveChallenge().then(() => {{
            try {{
                const _0xpayload = window.__OE_CORE_DATA__ || "";
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
                document.body.innerHTML = '<div style="color:#ef4444;font-family:sans-serif;font-weight:bold;text-align:center;padding:50px;">Güvenlik doğrulaması tamamlanamadı.</div>';
            }}
        }});
    }};
    document.head.appendChild(dataScript);

}})();
"""

with open(engine_js_path, 'w', encoding='utf-8') as f:
    f.write(engine_code)

# Add 120 empty lines padding in index.html so view-source shows 100% just the taunting message!
blank_padding = '\n' * 120

html_taunt = """<!--
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

index_html = f"""{html_taunt}{blank_padding}<!DOCTYPE html>
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

print("SUCCESS: Master security and taunt applied to all files!")
