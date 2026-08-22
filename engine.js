(function() {
    'use strict';

    // 1. Inject Styles & DDoS Modal
    const style = document.createElement('style');
    style.textContent = `
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        body { background: #07090e; color: #f8fafc; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }
        .ddos-shield-wrap { background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(124, 58, 237, 0.3); border-radius: 20px; padding: 36px 44px; text-align: center; max-width: 460px; width: 90%; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5), 0 0 40px rgba(124, 58, 237, 0.15); display: flex; flex-direction: column; align-items: center; gap: 20px; }
        .shield-icon { width: 64px; height: 64px; background: rgba(124, 58, 237, 0.15); border: 1px solid rgba(124, 58, 237, 0.4); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #a78bfa; }
        .shield-title { font-size: 18px; font-weight: 800; color: #f8fafc; letter-spacing: -0.3px; }
        .shield-desc { font-size: 13px; color: #94a3b8; line-height: 1.5; }
        .shield-bar-bg { width: 100%; height: 6px; background: #1e293b; border-radius: 999px; overflow: hidden; position: relative; }
        .shield-bar-fill { height: 100%; width: 0%; background: linear-gradient(90deg, #38bdf8, #7c3aed); border-radius: 999px; transition: width 0.3s ease; }
        .shield-status { font-size: 11px; font-weight: 700; color: #a78bfa; letter-spacing: 1px; text-transform: uppercase; }
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
    const desc = document.getElementById('shieldDescText');

    // 2. Anti-Bot / Anti-Headless Filter
    const isBot = navigator.webdriver || window.__nightmare || window._phantom || window.callPhantom ||
        /HeadlessChrome|PhantomJS|Selenium|Puppeteer|aiohttp|python-requests|Go-http-client|curl|Wget|Scrapy/i.test(navigator.userAgent) ||
        (window.outerWidth === 0 && window.outerHeight === 0) ||
        (screen.width === 0 && screen.height === 0);

    if (isBot) {
        document.body.innerHTML = '<div style="background:#07090e;color:#ef4444;font-family:sans-serif;font-weight:900;font-size:24px;text-align:center;padding:80px;height:100vh;display:flex;align-items:center;justify-content:center;">🚨 ERİŞİM ENGELLENDİ: Bot / Scraper Tespit Edildi.</div>';
        return;
    }

    // 3. Layer 7 HTTP Flood Rate Limiting
    const now = Date.now();
    const storageKey = 'oe_sec_req_log';
    const lockoutKey = 'oe_sec_lockout';

    const lockoutUntil = parseInt(localStorage.getItem(lockoutKey) || '0', 10);
    if (lockoutUntil > now) {
        const remaining = Math.ceil((lockoutUntil - now) / 1000);
        desc.innerText = "🚨 Aşırı istek/Flood tespit edildi. Güvenliğiniz için geçici koruma devrede.";
        status.innerText = "KORUMA SÜRESİ: " + remaining + " SANİYE";
        status.style.color = "#ef4444";
        bar.style.width = "100%";
        bar.style.background = "#ef4444";
        setTimeout(() => { window.location.reload(); }, 3000);
        return;
    }

    let requestLog = [];
    try {
        requestLog = JSON.parse(localStorage.getItem(storageKey) || '[]');
    } catch(e) { requestLog = []; }

    requestLog = requestLog.filter(ts => now - ts < 5000);
    requestLog.push(now);
    localStorage.setItem(storageKey, JSON.stringify(requestLog));

    if (requestLog.length > 6) {
        localStorage.setItem(lockoutKey, (now + 15000).toString());
        desc.innerText = "🚨 Yüksek frekanslı istek algılandı. IP ve tarayıcınız 15 saniyeliğine korumaya alındı.";
        status.innerText = "DDoS KORUMASI AKTİF (15 SN)";
        status.style.color = "#ef4444";
        bar.style.width = "100%";
        bar.style.background = "#ef4444";
        return;
    }

    // 4. Challenge Solver
    function solveChallenge() {
        return new Promise((resolve) => {
            let progress = 0;
            const interval = setInterval(() => {
                progress += 35;
                if (bar) bar.style.width = Math.min(progress, 100) + '%';
                if (progress >= 100) {
                    clearInterval(interval);
                    resolve();
                }
            }, 40);
        });
    }

    // 5. Load Data and Decrypt
    const _0xkey = [94, 161, 135, 61, 196, 155, 18, 247];

    const dataScript = document.createElement('script');
    dataScript.src = 'core.dat.js';
    dataScript.onload = function() {
        solveChallenge().then(() => {
            try {
                const _0xpayload = window.__OE_CORE_DATA__ || "";
                const _0xbinStr = atob(_0xpayload);
                const _0xlen = _0xbinStr.length;
                const _0xbytes = new Uint8Array(_0xlen);
                for (let i = 0; i < _0xlen; i++) {
                    _0xbytes[i] = _0xbinStr.charCodeAt(i) ^ _0xkey[i % _0xkey.length];
                }
                const _0xdecoder = new TextDecoder('utf-8');
                const _0xsource = _0xdecoder.decode(_0xbytes);

                document.open();
                document.write(_0xsource);
                document.close();
            } catch(e) {
                document.body.innerHTML = '<div style="color:#ef4444;font-family:sans-serif;font-weight:bold;text-align:center;padding:50px;">Güvenlik doğrulaması tamamlanamadı.</div>';
            }
        });
    };
    document.head.appendChild(dataScript);

})();
