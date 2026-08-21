import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Wrap Home View
# Replace from <!-- Hero Grid -->
content = content.replace('<!-- Hero Grid -->', '<div id="homeView">\\n    <!-- Hero Grid -->')
# End wrapper before Features Bar
content = content.replace('<!-- Features Bar -->', '</div>\\n    <!-- Features Bar -->')

# 2. Add Product View HTML
product_view_html = '''
    <!-- Product View -->
    <div id="productView" style="display: none; background: #f9f9f9; padding-bottom: 60px;">
        <div class="pv-container">
            <!-- Left: Gallery -->
            <div class="pv-gallery">
                <div class="pv-thumbnails">
                    <img src="" alt="thumb" class="pv-thumb active" id="pvImg1">
                    <img src="" alt="thumb" class="pv-thumb" id="pvImg2">
                    <img src="" alt="thumb" class="pv-thumb" id="pvImg3">
                </div>
                <div class="pv-main-image-container">
                    <img id="pvMainImg" src="" alt="Product">
                </div>
            </div>
            
            <!-- Right: Info -->
            <div class="pv-info">
                <div class="pv-brand" id="pvBrand">ONLY EULA</div>
                <h1 class="pv-title" id="pvTitle">KF90 HE PRO Always Edition</h1>
                
                <div class="pv-price-row">
                    <span class="pv-price" id="pvPrice">₺8,999</span>
                    <span class="pv-old-price" id="pvOldPrice"></span>
                    <span class="pv-discount-badge" id="pvDiscount">Kazancınız: ₺0</span>
                    <span class="pv-rating">5.0 ★</span>
                </div>
                
                <div class="pv-guarantee">
                    <h5>Only EULA Ürünlerinde 30 Gün Memnuniyet Garantisi!</h5>
                    <p>Only EULA markalı ürünlerde 30 gün içerisinde iade hakkı bulunur. Bu ürün grubunda iade koşulları ile ilgili bilgi almak için iade politikamıza göz atabilirsiniz.</p>
                </div>
                
                <div class="pv-guarantee" style="margin-top: 16px;">
                    <h5>Ürün Garantisi:</h5>
                    <p>Ürün 2 sene boyunca garanti kapsamındadır. Kullanıcı hatasından kaynaklanmayan kusur durumunda bire bir değişim veya teknik servis desteği sağlanır.</p>
                </div>
                
                <div class="pv-options">
                    <div class="pv-option-group">
                        <label>Renk: <span style="font-weight:700">Varsayılan</span></label>
                        <div class="pv-option-btns">
                            <button class="pv-opt-btn active">Varsayılan</button>
                            <button class="pv-opt-btn">Siyah</button>
                            <button class="pv-opt-btn">Beyaz</button>
                        </div>
                    </div>
                    
                    <div class="pv-option-group">
                        <label>Tuş Takımı: <span style="font-weight:700">Türkçe</span></label>
                        <div class="pv-option-btns">
                            <button class="pv-opt-btn active">Türkçe</button>
                            <button class="pv-opt-btn">İngilizce</button>
                        </div>
                    </div>
                    
                    <div class="pv-option-group">
                        <label>Miktar</label>
                        <div class="pv-qty-selector">
                            <button>-</button>
                            <span>1</span>
                            <button>+</button>
                        </div>
                    </div>
                </div>
                
                <button class="pv-add-btn">Sepete ekle</button>
                <button class="pv-back-btn" onclick="closeProduct()">← Ana Sayfaya Dön</button>
            </div>
        </div>
    </div>
'''

content = content.replace('<!-- Features Bar -->', product_view_html + '\\n    <!-- Features Bar -->')

pv_css = '''
        /* PRODUCT VIEW (WRAITH STYLE) */
        .pv-container {
            max-width: 1400px; margin: 40px auto; padding: 0 5%;
            display: grid; grid-template-columns: 1.2fr 1fr; gap: 60px;
        }
        .pv-gallery { display: flex; gap: 20px; }
        .pv-thumbnails { display: flex; flex-direction: column; gap: 12px; }
        .pv-thumb { width: 64px; height: 64px; object-fit: contain; background: white; border-radius: 8px; border: 2px solid transparent; cursor: pointer; padding: 4px; transition: border-color 0.2s; }
        .pv-thumb:hover { border-color: #ddd; }
        .pv-thumb.active { border-color: var(--primary); }
        .pv-main-image-container { flex: 1; background: white; border-radius: 16px; display: flex; align-items: center; justify-content: center; padding: 40px; aspect-ratio: 1; box-shadow: 0 4px 20px rgba(0,0,0,0.02); }
        .pv-main-image-container img { width: 100%; height: 100%; object-fit: contain; }
        
        .pv-info { display: flex; flex-direction: column; padding-top: 12px; }
        .pv-brand { color: var(--text-light); font-size: 14px; font-weight: 500; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 1px; }
        .pv-title { font-size: 32px; font-weight: 800; color: var(--text-main); line-height: 1.2; margin-bottom: 24px; letter-spacing: -0.5px; }
        
        .pv-price-row { display: flex; align-items: center; gap: 16px; margin-bottom: 32px; flex-wrap: wrap; }
        .pv-price { font-size: 24px; font-weight: 800; color: var(--primary); }
        .pv-old-price { font-size: 16px; color: var(--text-light); text-decoration: line-through; font-weight: 500; display: none; }
        .pv-discount-badge { background: var(--primary); color: white; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 700; display: none; }
        .pv-rating { margin-left: auto; font-size: 14px; font-weight: 700; color: var(--text-main); }
        
        .pv-guarantee { background: transparent; padding: 0; margin-bottom: 24px; }
        .pv-guarantee h5 { color: #00bcd4; font-size: 13px; font-weight: 700; margin-bottom: 8px; }
        .pv-guarantee p { font-size: 13px; color: var(--text-main); line-height: 1.6; font-weight: 500; }
        
        .pv-options { margin-bottom: 32px; }
        .pv-option-group { margin-bottom: 24px; }
        .pv-option-group label { display: block; font-size: 13px; color: var(--text-light); margin-bottom: 12px; font-weight: 500; }
        .pv-option-btns { display: flex; gap: 12px; flex-wrap: wrap; }
        .pv-opt-btn { background: transparent; border: 1px solid var(--border); padding: 10px 20px; border-radius: 30px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s; color: var(--text-main); }
        .pv-opt-btn:hover { border-color: var(--text-main); }
        .pv-opt-btn.active { border-color: var(--text-main); background: transparent; }
        
        .pv-qty-selector { display: inline-flex; align-items: center; border: 1px solid var(--border); border-radius: 30px; overflow: hidden; }
        .pv-qty-selector button { background: transparent; border: none; width: 40px; height: 40px; font-size: 18px; cursor: pointer; transition: background 0.2s; }
        .pv-qty-selector button:hover { background: #f0f0f0; }
        .pv-qty-selector span { width: 40px; text-align: center; font-size: 14px; font-weight: 600; line-height: 40px; display: inline-block; }
        
        .pv-add-btn { background: var(--primary); color: white; border: none; padding: 18px; border-radius: 30px; font-size: 16px; font-weight: 700; cursor: pointer; transition: all 0.3s; margin-bottom: 16px; text-transform: lowercase; }
        .pv-add-btn:hover { background: var(--primary-hover); transform: translateY(-2px); box-shadow: 0 10px 20px rgba(124,58,237,0.2); }
        
        .pv-back-btn { background: transparent; border: none; color: var(--text-light); font-size: 14px; font-weight: 600; cursor: pointer; text-align: left; padding: 8px 0; display: inline-block; width: fit-content; }
        .pv-back-btn:hover { color: var(--text-main); text-decoration: underline; }
        
        @media (max-width: 992px) {
            .pv-container { grid-template-columns: 1fr; gap: 32px; }
            .pv-gallery { flex-direction: column-reverse; }
            .pv-thumbnails { flex-direction: row; justify-content: center; }
        }
'''
content = content.replace('/* Features Bar */', pv_css + '\\n        /* Features Bar */')

js_new = '''
        // Page switching logic (Wraith-style Product View)
        function openModal(id) {
            const p = products.find(x => x.id === id);
            if(!p) return;
            
            document.getElementById('pvImg1').src = p.img;
            document.getElementById('pvImg2').src = p.img;
            document.getElementById('pvImg3').src = p.img;
            document.getElementById('pvMainImg').src = p.img;
            
            document.getElementById('pvBrand').innerText = p.brand;
            document.getElementById('pvTitle').innerText = p.name;
            document.getElementById('pvPrice').innerText = p.price;
            
            const oldP = document.getElementById('pvOldPrice');
            const disc = document.getElementById('pvDiscount');
            if(p.oldPrice) {
                oldP.innerText = p.oldPrice;
                oldP.style.display = 'inline';
                disc.style.display = 'inline-block';
            } else {
                oldP.style.display = 'none';
                disc.style.display = 'none';
            }
            
            const hv = document.getElementById('homeView');
            if (hv) hv.style.display = 'none';
            document.getElementById('productView').style.display = 'block';
            window.scrollTo(0, 0);
        }
        
        function closeProduct() {
            document.getElementById('productView').style.display = 'none';
            const hv = document.getElementById('homeView');
            if (hv) hv.style.display = 'block';
            window.scrollTo(0, 0);
        }
'''

# We will remove the old openModal and closeModal completely and insert this
content = re.sub(r'function openModal\(id\).*?\}', js_new, content, flags=re.DOTALL)
content = re.sub(r'function closeProduct\(\).*?\}', '', content, flags=re.DOTALL) # remove duplicate if it exists

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
