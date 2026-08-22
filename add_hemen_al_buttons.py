import re

source_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\.source_protected.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add direct buy styling
direct_buy_css = """
        .pdp-direct-buy-btn {
            flex: 1.2;
            height: 52px;
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            border-radius: var(--radius-full);
            font-size: 15px;
            font-weight: 800;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            transition: var(--transition);
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.35);
            cursor: pointer;
            border: none;
        }

        .pdp-direct-buy-btn:hover {
            background: linear-gradient(135deg, #059669 0%, #047857 100%);
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(16, 185, 129, 0.45);
        }

        .quick-buy-action-btn {
            background: linear-gradient(135deg, #10b981, #059669);
            color: white;
            padding: 8px 14px;
            border-radius: var(--radius-full);
            font-size: 12px;
            font-weight: 800;
            cursor: pointer;
            transition: var(--transition);
            border: none;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }

        .quick-buy-action-btn:hover {
            transform: scale(1.04);
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
        }
"""

content = content.replace('.pdp-add-cart-btn {', direct_buy_css + '\n        .pdp-add-cart-btn {')

# 2. Update PDP buy row HTML to have both "Sepete Ekle" and "Hemen Satın Al"
pdp_buy_row_html = """
                <!-- Quantity & Cart Row -->
                <div class="pdp-buy-row">
                    <div class="pdp-qty-stepper">
                        <button class="qty-btn" onclick="changeQuantity(-1)">-</button>
                        <div class="qty-val-display" id="pdpQtyVal">1</div>
                        <button class="qty-btn" onclick="changeQuantity(1)">+</button>
                    </div>
                    
                    <button class="pdp-add-cart-btn" onclick="addCurrentProductToCart()">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 002 1.61h9.72a2 2 0 002-1.61L23 6H6"></path></svg>
                        Sepete Ekle
                    </button>

                    <button class="pdp-direct-buy-btn" onclick="buyCurrentProductDirectly()">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
                        Hemen Satın Al (3D Secure)
                    </button>
                </div>
"""

# Replace in PDP
content = re.sub(r'<!-- Quantity & Cart Row -->[\s\S]*?<\/div>\s*<\/div>\s*<button class="pdp-back-link-btn"', pdp_buy_row_html + '\n                <button class="pdp-back-link-btn"', content)

# 3. Update Hero Promo Buttons
hero_promo_btns = """
                    <div class="promo-action-row">
                        <button class="promo-main-btn" onclick="openProduct(9)">
                            <span>Ürünü İncele</span>
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"></path></svg>
                        </button>
                        <button class="promo-main-btn" onclick="quickBuyProduct(9)" style="background: linear-gradient(90deg, #10b981, #059669); border: none;">
                            <span>⚡ Hemen Satın Al</span>
                        </button>
                        <div class="promo-price-tag">₺8,999</div>
                    </div>
"""

content = re.sub(r'<div class="promo-action-row">[\s\S]*?<\/div>\s*<\/div>\s*<div class="promo-visual-side">', hero_promo_btns + '\n                </div>\n                <div class="promo-visual-side">', content)

# 4. Update Product Cards Grid HTML in renderProducts
product_card_btn_pattern = """
                        <div style="display: flex; gap: 6px;">
                            <button class="quick-view-action-btn" onclick="event.stopPropagation(); openProduct(${p.id})">
                                İncele
                            </button>
                            <button class="quick-buy-action-btn" onclick="event.stopPropagation(); quickBuyProduct(${p.id})">
                                ⚡ Satın Al
                            </button>
                        </div>
"""

content = re.sub(r'<button class="quick-view-action-btn" onclick="event\.stopPropagation\(\); openProduct\(\$\{p\.id\}\)">\s*İncele\s*<\/button>', product_card_btn_pattern.strip(), content)

# 5. Add quickBuyProduct JS function
quick_buy_js = """
        function quickBuyProduct(id) {
            const p = productsDB.find(x => x.id === id);
            if (!p) return;
            currentProduct = p;
            currentQuantity = 1;
            selectedVariants.color = (p.variants && p.variants[0]) ? p.variants[0].name : "Standart";
            selectedVariants.layout = "Türkçe Q";
            selectedVariants.switch = "Hall Effect Linear (0.1-4.0mm)";
            addCurrentProductToCart();
            openCheckout();
        }

        function buyCurrentProductDirectly() {
            addCurrentProductToCart();
            openCheckout();
        }
"""

content = content.replace('function openCheckout() {', quick_buy_js + '\n        function openCheckout() {')

with open(source_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: 'Hemen Satın Al' buttons added to PDP, Hero Promo, and Product Cards!")
