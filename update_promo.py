import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update hero card image for Always Edition to the new ultra one
content = content.replace('keyboard_always.jpg', 'always_promo_1.jpg')

# 2. Inject CSS for the promo section
promo_css = '''
        /* ALWAYS EDITION PROMO SECTION */
        .promo-section {
            width: 100%;
            height: 80vh;
            min-height: 600px;
            background: #000;
            position: relative;
            overflow: hidden;
            margin: 40px 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .promo-slider {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            z-index: 1;
        }
        
        .promo-slide {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            object-fit: cover;
            opacity: 0;
            animation: promoCrossfade 15s infinite;
        }
        
        .promo-slide:nth-child(1) { animation-delay: 0s; }
        .promo-slide:nth-child(2) { animation-delay: 5s; }
        .promo-slide:nth-child(3) { animation-delay: 10s; }
        
        @keyframes promoCrossfade {
            0% { opacity: 0; transform: scale(1.05); }
            10% { opacity: 1; transform: scale(1.03); }
            33% { opacity: 1; transform: scale(1); }
            43% { opacity: 0; transform: scale(0.98); }
            100% { opacity: 0; transform: scale(0.98); }
        }
        
        .promo-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.8) 100%);
            z-index: 2;
        }
        
        .promo-content {
            position: relative;
            z-index: 3;
            text-align: center;
            color: #fff;
            max-width: 800px;
            padding: 40px;
        }
        
        .promo-badge {
            display: inline-block;
            background: rgba(124, 58, 237, 0.2);
            border: 1px solid var(--primary);
            color: var(--primary);
            padding: 8px 16px;
            border-radius: 30px;
            font-size: 14px;
            font-weight: 700;
            letter-spacing: 2px;
            margin-bottom: 24px;
            text-transform: uppercase;
        }
        
        .promo-title {
            font-size: 56px;
            font-weight: 900;
            letter-spacing: -1.5px;
            margin-bottom: 16px;
            line-height: 1.1;
            text-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }
        
        .promo-title span {
            color: #00d2ff;
            background: -webkit-linear-gradient(45deg, #00d2ff, #7c3aed);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .promo-desc {
            font-size: 18px;
            opacity: 0.9;
            margin-bottom: 32px;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }
        
        .promo-btn {
            background: #00d2ff;
            color: #000;
            border: none;
            padding: 16px 40px;
            font-size: 16px;
            font-weight: 800;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 0 20px rgba(0, 210, 255, 0.4);
        }
        
        .promo-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 0 30px rgba(0, 210, 255, 0.6);
            background: #fff;
        }
'''
content = content.replace('/* Product Section */', promo_css + '\n        /* Product Section */')

# 3. Inject HTML for promo section
promo_html = '''
    <!-- ALWAYS EDITION PROMO -->
    <section class="promo-section">
        <div class="promo-slider">
            <img src="always_promo_1.jpg" alt="Promo 1" class="promo-slide">
            <img src="always_promo_2.jpg" alt="Promo 2" class="promo-slide">
            <img src="always_promo_3.jpg" alt="Promo 3" class="promo-slide">
        </div>
        <div class="promo-overlay"></div>
        <div class="promo-content">
            <div class="promo-badge">LİMİTED EDİTİON</div>
            <h2 class="promo-title">KF90 <span>ALWAYS EDITION</span></h2>
            <p class="promo-desc">Anodize camgöbeği alüminyum kasa üzerine ince işçilikle kazınmış lazer gravür detaylar. Tuşların üzerine yayılan özel yapım sanatsal tasarım ile güzelliğin ve 8000Hz performansın zirvesi.</p>
            <button class="promo-btn" onclick="openModal(9)">Hemen İncele</button>
        </div>
    </section>
'''

content = content.replace('</section>\n\n    <!-- Product Grid -->', '</section>\n' + promo_html + '\n    <!-- Product Grid -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
