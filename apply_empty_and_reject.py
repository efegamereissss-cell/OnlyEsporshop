import re

source_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\.source_protected.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clear all default values from checkout form inputs
content = content.replace('value="Efe"', 'value=""')
content = content.replace('value="Yılmaz"', 'value=""')
content = content.replace('value="efegamer@gmail.com"', 'value=""')
content = content.replace('value="0532 123 45 67"', 'value=""')
content = content.replace('value="Kadıköy"', 'value=""')
content = content.replace('value="Bağdat Caddesi No:14 D:5"', 'value=""')
content = content.replace('value="EFE YILMAZ"', 'value=""')
content = content.replace('value="5421 8934 1290 4812"', 'value=""')
content = content.replace('value="10/29"', 'value=""')
content = content.replace('value="894"', 'value=""')
content = content.replace('value="1923"', 'value=""')

# Fix city dropdown to have disabled default placeholder
old_city_select = """                            <select class="form-input" id="coCity">
                                <option>İstanbul</option>
                                <option>Ankara</option>
                                <option>İzmir</option>
                                <option>Bursa</option>
                                <option>Antalya</option>
                                <option>Diğer</option>
                            </select>"""

new_city_select = """                            <select class="form-input" id="coCity">
                                <option value="" disabled selected>İl Seçiniz</option>
                                <option>İstanbul</option>
                                <option>Ankara</option>
                                <option>İzmir</option>
                                <option>Bursa</option>
                                <option>Antalya</option>
                                <option>Diğer</option>
                            </select>"""

content = content.replace(old_city_select, new_city_select)

# Remove (Simülasyon SMS Onay Kodu: 1923) hint
content = content.replace('<p style="font-size: 11px; color: #10b981; margin-top: 6px; font-weight: 600;">(Simülasyon SMS Onay Kodu: 1923)</p>', '<p style="font-size: 11px; color: #64748b; margin-top: 6px;">Bankanızdan gelen tek kullanımlık SMS şifresi</p>')

# 2. Add Payment Rejection Modal CSS & HTML
rejection_modal_css = """
        /* Payment Disabled / Rejection Modal */
        .payment-reject-modal-overlay {
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(10px);
            z-index: 11000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .payment-reject-modal-overlay.active {
            display: flex;
        }
        .payment-reject-card {
            background: #ffffff;
            width: 100%;
            max-width: 460px;
            border-radius: 20px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            border: 1px solid #fee2e2;
            text-align: center;
            padding: 36px 30px;
            animation: modalFadeUp 0.3s ease;
        }
        .reject-icon-circle {
            width: 72px;
            height: 72px;
            background: #fef2f2;
            border: 2px solid #fca5a5;
            color: #ef4444;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px auto;
        }
        .payment-reject-card h3 {
            font-size: 20px;
            font-weight: 900;
            color: #991b1b;
            margin-bottom: 12px;
        }
        .payment-reject-card p {
            font-size: 14px;
            color: #64748b;
            line-height: 1.6;
            margin-bottom: 24px;
        }
        .reject-btn-close {
            width: 100%;
            padding: 14px;
            background: #0f172a;
            color: #ffffff;
            border: none;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 800;
            cursor: pointer;
            transition: var(--transition);
        }
        .reject-btn-close:hover {
            background: #1e293b;
        }
"""

content = content.replace('/* ==================== SECURITY & ANTI-TAMPER CSS ==================== */', rejection_modal_css + '\n        /* ==================== SECURITY & ANTI-TAMPER CSS ==================== */')

# Rejection Modal HTML
rejection_modal_html = """
    <!-- ==================== PAYMENT REJECTION / DISABLED MODAL ==================== -->
    <div class="payment-reject-modal-overlay" id="paymentRejectModal">
        <div class="payment-reject-card">
            <div class="reject-icon-circle">
                <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg>
            </div>
            <h3>Satın Alımlar Kısa Süreliğine Kapalıdır</h3>
            <p>Yeni sezon sınırlı üretim ürün lansmanı ve stok entegrasyonu nedeniyle online ödeme ve sipariş alımı geçici olarak durdurulmuştur. Kartınızdan herhangi bir ücret tahsil edilmemiştir.</p>
            <button class="reject-btn-close" onclick="closeRejectModal()">
                Anladım
            </button>
        </div>
    </div>
"""

content = content.replace('<!-- ============ FEATURES BAR ============ -->', rejection_modal_html + '\n    <!-- ============ FEATURES BAR ============ -->')

# 3. Update payment functions to reject payment
payment_logic_replace = """
        function trigger3DSecurePayment() {
            // When user tries to pay, directly show the rejection notification & modal
            showRejectModal();
        }

        function showRejectModal() {
            const modal = document.getElementById('paymentRejectModal');
            if (modal) modal.classList.add('active');
            showToast('⚠️ Satın Alımlar Kısa Süreliğine Kapalıdır.', true);
        }

        function closeRejectModal() {
            const modal = document.getElementById('paymentRejectModal');
            if (modal) modal.classList.remove('active');
        }

        function confirm3DPayment() {
            close3DModal();
            showRejectModal();
        }
"""

# Replace trigger3DSecurePayment and confirm3DPayment in JS
content = re.sub(r'let smsInterval;[\s\S]*?function confirm3DPayment\(\) \{[\s\S]*?window\.scrollTo\(\{ top: 0, behavior: \'smooth\' \}\);\s*\}', payment_logic_replace.strip(), content)

with open(source_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Input fields emptied and purchase rejection logic applied!")
