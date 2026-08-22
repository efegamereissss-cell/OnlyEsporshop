import re

source_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\.source_protected.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Checkout CSS
checkout_css = """
        /* ==================== CHECKOUT & PAYMENT STYLING ==================== */
        #checkoutView {
            display: none;
            max-width: 1200px;
            margin: 40px auto 80px auto;
            padding: 0 24px;
        }

        .checkout-steps {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 16px;
            margin-bottom: 36px;
        }
        .checkout-step-item {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 14px;
            font-weight: 600;
            color: var(--text-light);
        }
        .checkout-step-item.active {
            color: var(--primary);
        }
        .checkout-step-item.completed {
            color: #10b981;
        }
        .step-num-badge {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: #e2e8f0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: 700;
            color: var(--text-muted);
        }
        .checkout-step-item.active .step-num-badge {
            background: var(--primary);
            color: #fff;
            box-shadow: 0 0 12px rgba(124, 58, 237, 0.4);
        }
        .checkout-step-item.completed .step-num-badge {
            background: #10b981;
            color: #fff;
        }
        .step-divider {
            width: 40px;
            height: 2px;
            background: #e2e8f0;
        }

        .checkout-layout {
            display: grid;
            grid-template-columns: 1fr 420px;
            gap: 32px;
            align-items: start;
        }

        @media (max-width: 900px) {
            .checkout-layout {
                grid-template-columns: 1fr;
            }
        }

        .checkout-card {
            background: var(--bg-white);
            border-radius: 16px;
            border: 1px solid var(--border-color);
            padding: 28px;
            margin-bottom: 24px;
            box-shadow: var(--shadow-subtle);
        }

        .checkout-card-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
            padding-bottom: 14px;
            border-bottom: 1px solid #f1f5f9;
        }
        .checkout-card-title {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 17px;
            font-weight: 700;
            color: var(--text-dark);
        }
        .checkout-card-title svg {
            color: var(--primary);
        }

        .form-grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin-bottom: 16px;
        }
        .form-grid-3 {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 16px;
            margin-bottom: 16px;
        }
        .form-group {
            display: flex;
            flex-direction: column;
            gap: 6px;
            margin-bottom: 16px;
        }
        .form-group label {
            font-size: 13px;
            font-weight: 600;
            color: var(--text-muted);
        }
        .form-input {
            width: 100%;
            padding: 12px 14px;
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            font-size: 14px;
            color: var(--text-dark);
            outline: none;
            transition: var(--transition);
        }
        .form-input:focus {
            background: #fff;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.15);
        }

        /* Payment Tab Selection */
        .payment-method-selector {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 20px;
        }
        .payment-method-pill {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 14px 16px;
            border: 2px solid var(--border-color);
            border-radius: 12px;
            background: #f8fafc;
            cursor: pointer;
            font-weight: 600;
            font-size: 14px;
            color: var(--text-dark);
            transition: var(--transition);
        }
        .payment-method-pill.active {
            border-color: var(--primary);
            background: var(--primary-light);
            color: var(--primary);
        }

        /* Security Badges Grid */
        .trust-security-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            margin-top: 20px;
            padding-top: 18px;
            border-top: 1px solid #f1f5f9;
        }
        .trust-badge-item {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 10px 8px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
        }
        .trust-badge-item img, .trust-badge-item svg {
            height: 22px;
            width: auto;
        }
        .trust-badge-label {
            font-size: 10px;
            font-weight: 700;
            color: #475569;
            letter-spacing: 0.3px;
        }

        /* Order Summary Box */
        .checkout-summary-box {
            background: var(--bg-white);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            position: sticky;
            top: 90px;
            box-shadow: var(--shadow-card);
        }
        .summary-items-list {
            max-height: 260px;
            overflow-y: auto;
            margin-bottom: 20px;
            padding-right: 4px;
        }
        .summary-item-row {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 10px 0;
            border-bottom: 1px solid #f1f5f9;
        }
        .summary-item-row:last-child {
            border-bottom: none;
        }
        .summary-item-img {
            width: 48px;
            height: 48px;
            border-radius: 8px;
            object-fit: cover;
            background: #f1f5f9;
        }
        .summary-item-info {
            flex: 1;
        }
        .summary-item-name {
            font-size: 13px;
            font-weight: 700;
            color: var(--text-dark);
            line-height: 1.3;
        }
        .summary-item-variant {
            font-size: 11px;
            color: var(--text-muted);
            margin-top: 2px;
        }
        .summary-item-price {
            font-size: 13px;
            font-weight: 700;
            color: var(--primary);
        }

        .coupon-box {
            display: flex;
            gap: 8px;
            margin-bottom: 20px;
        }
        .coupon-input {
            flex: 1;
            padding: 10px 12px;
            background: #f8fafc;
            border: 1px dashed var(--border-color);
            border-radius: 8px;
            font-size: 13px;
            text-transform: uppercase;
            font-weight: 600;
            outline: none;
        }
        .coupon-btn {
            padding: 10px 16px;
            background: var(--text-dark);
            color: #fff;
            border: none;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
        }
        .coupon-btn:hover {
            background: var(--primary);
        }

        .summary-calc-row {
            display: flex;
            justify-content: space-between;
            font-size: 13px;
            color: var(--text-muted);
            margin-bottom: 8px;
        }
        .summary-calc-row.total {
            font-size: 18px;
            font-weight: 800;
            color: var(--text-dark);
            border-top: 2px solid #f1f5f9;
            padding-top: 14px;
            margin-top: 12px;
        }
        .summary-calc-row.total span:last-child {
            color: var(--primary);
        }

        .btn-complete-payment {
            width: 100%;
            padding: 16px;
            background: linear-gradient(135deg, #7c3aed, #6d28d9);
            color: #fff;
            border: none;
            border-radius: 12px;
            font-size: 15px;
            font-weight: 800;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            box-shadow: 0 10px 20px -5px rgba(124, 58, 237, 0.4);
            transition: var(--transition);
            margin-top: 20px;
        }
        .btn-complete-payment:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 28px -5px rgba(124, 58, 237, 0.5);
        }

        /* 3D Secure 2.0 Bank Simulation Modal */
        .three-ds-modal-overlay {
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(8px);
            z-index: 10000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .three-ds-modal-overlay.active {
            display: flex;
        }
        .three-ds-card {
            background: #ffffff;
            width: 100%;
            max-width: 440px;
            border-radius: 20px;
            box-shadow: 0 25px 50px -12px rgba(0,0,0,0.4);
            overflow: hidden;
            border: 1px solid #e2e8f0;
            animation: modalFadeUp 0.3s ease;
        }
        .three-ds-header {
            background: #0f172a;
            color: #fff;
            padding: 18px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .three-ds-logo-wrap {
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 800;
            font-size: 14px;
            color: #c4b5fd;
        }
        .three-ds-body {
            padding: 24px;
        }
        .bank-info-table {
            width: 100%;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 14px;
            margin-bottom: 20px;
            font-size: 13px;
        }
        .bank-info-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
            color: #64748b;
        }
        .bank-info-row:last-child {
            margin-bottom: 0;
            font-weight: 700;
            color: #0f172a;
        }
        .sms-input-wrap {
            text-align: center;
            margin-bottom: 20px;
        }
        .sms-code-input {
            width: 180px;
            height: 48px;
            text-align: center;
            font-size: 24px;
            font-weight: 800;
            letter-spacing: 6px;
            background: #f1f5f9;
            border: 2px solid var(--primary);
            border-radius: 12px;
            outline: none;
        }
        .three-ds-confirm-btn {
            width: 100%;
            padding: 14px;
            background: #10b981;
            color: #fff;
            border: none;
            border-radius: 12px;
            font-weight: 800;
            font-size: 15px;
            cursor: pointer;
            transition: var(--transition);
        }
        .three-ds-confirm-btn:hover {
            background: #059669;
        }

        /* Order Success Screen */
        .order-success-screen {
            display: none;
            max-width: 600px;
            margin: 60px auto 100px auto;
            background: #fff;
            border-radius: 24px;
            border: 1px solid #e2e8f0;
            padding: 48px 36px;
            text-align: center;
            box-shadow: var(--shadow-hover);
        }
        .success-checkmark-icon {
            width: 80px;
            height: 80px;
            background: #ecfdf5;
            color: #10b981;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px auto;
            border: 2px solid #a7f3d0;
        }
"""

content = content.replace('/* ==================== SECURITY & ANTI-TAMPER CSS ==================== */', checkout_css + '\n        /* ==================== SECURITY & ANTI-TAMPER CSS ==================== */')

# 2. Add Checkout View HTML before features-bar
checkout_html = """
    <!-- ==================== CHECKOUT VIEW ==================== -->
    <div id="checkoutView">
        <!-- Steps Header -->
        <div class="checkout-steps">
            <div class="checkout-step-item completed">
                <div class="step-num-badge">✓</div>
                <span>Sepet</span>
            </div>
            <div class="step-divider"></div>
            <div class="checkout-step-item active">
                <div class="step-num-badge">2</div>
                <span>Teslimat & Fatura</span>
            </div>
            <div class="step-divider"></div>
            <div class="checkout-step-item">
                <div class="step-num-badge">3</div>
                <span>3D Güvenli Ödeme</span>
            </div>
        </div>

        <div class="checkout-layout">
            <!-- Left Side: Forms & Payment -->
            <div class="checkout-form-column">
                
                <!-- Delivery Info Card -->
                <div class="checkout-card">
                    <div class="checkout-card-header">
                        <div class="checkout-card-title">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                            Teslimat ve İletişim Bilgileri
                        </div>
                    </div>
                    
                    <div class="form-grid-2">
                        <div class="form-group">
                            <label>Adınız *</label>
                            <input type="text" class="form-input" id="coName" placeholder="Adınız" value="Efe">
                        </div>
                        <div class="form-group">
                            <label>Soyadınız *</label>
                            <input type="text" class="form-input" id="coSurname" placeholder="Soyadınız" value="Yılmaz">
                        </div>
                    </div>

                    <div class="form-grid-2">
                        <div class="form-group">
                            <label>E-Posta Adresi (Fatura ve Takip) *</label>
                            <input type="email" class="form-input" id="coEmail" placeholder="ornek@domain.com" value="efegamer@gmail.com">
                        </div>
                        <div class="form-group">
                            <label>Telefon Numarası (Kargo SMS) *</label>
                            <input type="tel" class="form-input" id="coPhone" placeholder="05XX XXX XX XX" value="0532 123 45 67">
                        </div>
                    </div>

                    <div class="form-grid-2">
                        <div class="form-group">
                            <label>İl *</label>
                            <select class="form-input" id="coCity">
                                <option>İstanbul</option>
                                <option>Ankara</option>
                                <option>İzmir</option>
                                <option>Bursa</option>
                                <option>Antalya</option>
                                <option>Diğer</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label>İlçe *</label>
                            <input type="text" class="form-input" id="coDistrict" placeholder="İlçe" value="Kadıköy">
                        </div>
                    </div>

                    <div class="form-group">
                        <label>Açık Teslimat Adresi *</label>
                        <input type="text" class="form-input" id="coAddress" placeholder="Mahalle, Cadde, Sokak, Daire No" value="Bağdat Caddesi No:14 D:5">
                    </div>
                </div>

                <!-- Payment Info Card -->
                <div class="checkout-card">
                    <div class="checkout-card-header">
                        <div class="checkout-card-title">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg>
                            256-Bit Güvenli Ödeme Seçenekleri
                        </div>
                        <span style="font-size: 11px; color: #10b981; font-weight: 700; background: #ecfdf5; padding: 4px 10px; border-radius: 999px;">3D Secure 2.0 Aktif</span>
                    </div>

                    <!-- Payment Method Selector -->
                    <div class="payment-method-selector">
                        <div class="payment-method-pill active" onclick="selectPaymentMethod('card', this)">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg>
                            Kredi / Banka Kartı
                        </div>
                        <div class="payment-method-pill" onclick="selectPaymentMethod('eft', this)">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                            Havale / EFT (%3 İndirim)
                        </div>
                    </div>

                    <!-- Card Form -->
                    <div id="cardPaymentFields">
                        <div class="form-group">
                            <label>Kart Üzerindeki İsim ve Soyisim</label>
                            <input type="text" class="form-input" placeholder="AD SOYAD" value="EFE YILMAZ">
                        </div>

                        <div class="form-group">
                            <label>Kart Numarası</label>
                            <div style="position: relative;">
                                <input type="text" class="form-input" id="cardNumInput" placeholder="4543 •••• •••• ••••" value="5421 8934 1290 4812" style="letter-spacing: 2px;">
                                <div style="position: absolute; right: 12px; top: 50%; transform: translateY(-50%); font-weight: 800; font-size: 11px; color: #7c3aed; background: #ede9fe; padding: 2px 8px; border-radius: 4px;">
                                    Mastercard / Troy
                                </div>
                            </div>
                        </div>

                        <div class="form-grid-2">
                            <div class="form-group">
                                <label>Son Kullanma Tarihi (AA/YY)</label>
                                <input type="text" class="form-input" placeholder="12/28" value="10/29">
                            </div>
                            <div class="form-group">
                                <label>CVV / Güvenlik Kodu</label>
                                <input type="password" class="form-input" placeholder="•••" value="894" maxlength="3">
                            </div>
                        </div>

                        <div class="form-group">
                            <label>Taksit Seçenekleri</label>
                            <select class="form-input">
                                <option>Tek Çekim (Peşin Fiyatına)</option>
                                <option>Peşin Fiyatına 3 Taksit (Faizsiz)</option>
                                <option>Peşin Fiyatına 6 Taksit (Faizsiz)</option>
                                <option>12 Taksit (Vade Farklı)</option>
                            </select>
                        </div>
                    </div>

                    <!-- Trust Badges -->
                    <div class="trust-security-grid">
                        <div class="trust-badge-item">
                            <span style="font-weight: 900; color: #3b82f6; font-size: 14px;">iyzico</span>
                            <span class="trust-badge-label">Korumalı Alışveriş</span>
                        </div>
                        <div class="trust-badge-item">
                            <span style="font-weight: 900; color: #7c3aed; font-size: 14px;">param</span>
                            <span class="trust-badge-label">BDDK Lisanslı POS</span>
                        </div>
                        <div class="trust-badge-item">
                            <span style="font-weight: 900; color: #10b981; font-size: 14px;">3D SECURE</span>
                            <span class="trust-badge-label">2.0 SMS Doğrulama</span>
                        </div>
                        <div class="trust-badge-item">
                            <span style="font-weight: 900; color: #0f172a; font-size: 14px;">256-BIT</span>
                            <span class="trust-badge-label">SSL EV Şifreleme</span>
                        </div>
                    </div>

                </div>

            </div>

            <!-- Right Side: Order Summary -->
            <div class="checkout-summary-column">
                <div class="checkout-summary-box">
                    <h3 style="font-size: 16px; font-weight: 800; margin-bottom: 16px; color: var(--text-dark);">Sipariş Özeti</h3>
                    
                    <div class="summary-items-list" id="checkoutSummaryItems">
                        <!-- Injected via JS -->
                    </div>

                    <!-- Coupon Box -->
                    <div class="coupon-box">
                        <input type="text" class="coupon-input" id="couponCodeInput" placeholder="KUPON KODU (EULA10)">
                        <button class="coupon-btn" onclick="applyCouponCode()">Uygula</button>
                    </div>

                    <!-- Calculations -->
                    <div class="summary-calc-row">
                        <span>Ara Toplam:</span>
                        <span id="coSubtotal">₺0</span>
                    </div>
                    <div class="summary-calc-row">
                        <span>Kargo Ücreti:</span>
                        <span style="color: #10b981; font-weight: 700;">Ücretsiz (Aynı Gün)</span>
                    </div>
                    <div class="summary-calc-row" id="couponDiscountRow" style="display: none; color: #10b981; font-weight: 700;">
                        <span>Kupon İndirimi (%10):</span>
                        <span id="coDiscountAmount">-₺0</span>
                    </div>
                    <div class="summary-calc-row total">
                        <span>Ödenecek Tutar:</span>
                        <span id="coFinalTotal">₺0</span>
                    </div>

                    <button class="btn-complete-payment" onclick="trigger3DSecurePayment()">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                        <span id="btnPayText">3D Secure ile Güvenli Öde</span>
                    </button>

                    <div style="font-size: 11px; color: #94a3b8; text-align: center; margin-top: 14px; line-height: 1.4;">
                        "Öde" butonuna tıklayarak <a href="javascript:void(0)" style="color:#7c3aed;">Mesafeli Satış Sözleşmesi</a>'ni onaylamış olursunuz.
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- ==================== 3D SECURE 2.0 SIMULATION MODAL ==================== -->
    <div class="three-ds-modal-overlay" id="threeDSModal">
        <div class="three-ds-card">
            <div class="three-ds-header">
                <div class="three-ds-logo-wrap">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                    3D SECURE 2.0 DOĞRULAMA
                </div>
                <button onclick="close3DModal()" style="background:none; border:none; color:#fff; font-size:20px; cursor:pointer;">&times;</button>
            </div>
            <div class="three-ds-body">
                <div class="bank-info-table">
                    <div class="bank-info-row">
                        <span>İşyeri / Satıcı:</span>
                        <span>ONLY EULA ESPORTS / IYZICO</span>
                    </div>
                    <div class="bank-info-row">
                        <span>Kart Numarası:</span>
                        <span>•••• •••• •••• 4812</span>
                    </div>
                    <div class="bank-info-row">
                        <span>Doğrulama Süresi:</span>
                        <span id="smsCountdown" style="color: #ef4444; font-weight: 700;">180 sn</span>
                    </div>
                    <div class="bank-info-row">
                        <span>Ödenecek Tutar:</span>
                        <span id="threeDSTotalAmount" style="color: #7c3aed; font-size: 15px;">₺0</span>
                    </div>
                </div>

                <div class="sms-input-wrap">
                    <p style="font-size: 13px; color: #475569; margin-bottom: 10px;">Telefonunuza gönderilen 6 haneli SMS şifresini giriniz:</p>
                    <input type="text" class="sms-code-input" id="smsCodeInput" value="1923" maxlength="6">
                    <p style="font-size: 11px; color: #10b981; margin-top: 6px; font-weight: 600;">(Simülasyon SMS Onay Kodu: 1923)</p>
                </div>

                <button class="three-ds-confirm-btn" onclick="confirm3DPayment()">
                    ✓ Onayla ve Siparişi Tamamla
                </button>
            </div>
        </div>
    </div>

    <!-- ==================== ORDER SUCCESS SCREEN ==================== -->
    <div id="orderSuccessView" class="order-success-screen">
        <div class="success-checkmark-icon">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
        </div>
        <h2 style="font-size: 24px; font-weight: 900; color: #0f172a; margin-bottom: 10px;">Siparişiniz Başarıyla Alındı! 🎉</h2>
        <p style="color: #64748b; font-size: 14px; margin-bottom: 24px;">Ödemeniz 3D Secure 2.0 ile güvenle doğrulandı ve siparişiniz paketleme sırasına alındı.</p>
        
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 14px; padding: 18px; margin-bottom: 24px; text-align: left; font-size: 13px;">
            <div style="display:flex; justify-content:space-between; margin-bottom: 8px;">
                <span style="color:#64748b;">Sipariş Numarası:</span>
                <span style="font-weight:800; color:#7c3aed;" id="successOrderNo">#OE-849204</span>
            </div>
            <div style="display:flex; justify-content:space-between; margin-bottom: 8px;">
                <span style="color:#64748b;">Kargo Takip:</span>
                <span style="font-weight:700; color:#10b981;">Yurtiçi Kargo (Aynı Gün)</span>
            </div>
            <div style="display:flex; justify-content:space-between;">
                <span style="color:#64748b;">Tahmini Teslimat:</span>
                <span style="font-weight:700; color:#0f172a;">Yarın 11:00 - 15:00</span>
            </div>
        </div>

        <button class="cart-checkout-btn" onclick="showHomePage()" style="width: 100%;">
            Ana Sayfaya Dön ve Alışverişe Devam Et
        </button>
    </div>
"""

content = content.replace('<!-- ============ FEATURES BAR ============ -->', checkout_html + '\n    <!-- ============ FEATURES BAR ============ -->')

# 3. Update PDP buy buttons to have "Hemen Satın Al" button calling openCheckout() directly
pdp_buy_row = """
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
                    <button class="pdp-add-cart-btn" onclick="buyCurrentProductDirectly()" style="background: linear-gradient(135deg, #10b981, #059669); border-color: #059669;">
                        ⚡ Hemen Satın Al
                    </button>
                </div>
"""

content = re.sub(r'<!-- Quantity & Cart Row -->[\s\S]*?<\/div>\s*<\/div>\s*<button class="pdp-back-link-btn"', pdp_buy_row + '\n                <button class="pdp-back-link-btn"', content)

# 4. Update cart drawer checkout button
content = content.replace('onclick="showToast(\'Ödeme adımı tamamlanmak üzere yönlendiriliyorsunuz!\')"', 'onclick="openCheckout()"')

# 5. Add Checkout & 3D Secure JavaScript Functions
checkout_js = """
        // Checkout System
        let activeDiscountRatio = 0;

        function openCheckout() {
            toggleCartDrawer(false);
            if (cartItems.length === 0 && currentProduct) {
                // If cart is empty but on PDP, add current product
                addCurrentProductToCart();
            } else if (cartItems.length === 0) {
                showToast('Lütfen önce sepete bir ürün ekleyin!');
                return;
            }

            // Hide other views
            document.getElementById('homeView').style.display = 'none';
            document.getElementById('productDetailView').style.display = 'none';
            document.getElementById('orderSuccessView').style.display = 'none';
            document.getElementById('checkoutView').style.display = 'block';

            renderCheckoutSummary();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function buyCurrentProductDirectly() {
            addCurrentProductToCart();
            openCheckout();
        }

        function renderCheckoutSummary() {
            const container = document.getElementById('checkoutSummaryItems');
            let subtotal = 0;
            let html = '';

            cartItems.forEach(ci => {
                const itemTotal = ci.product.price * ci.qty;
                subtotal += itemTotal;
                html += `
                <div class="summary-item-row">
                    <img src="${ci.product.img}" alt="${ci.product.name}" class="summary-item-img">
                    <div class="summary-item-info">
                        <div class="summary-item-name">${ci.product.name}</div>
                        <div class="summary-item-variant">${ci.color} · ${ci.qty} Adet</div>
                    </div>
                    <div class="summary-item-price">₺${itemTotal.toLocaleString('tr-TR')}</div>
                </div>`;
            });

            container.innerHTML = html;
            document.getElementById('coSubtotal').innerText = "₺" + subtotal.toLocaleString('tr-TR');

            const discount = Math.round(subtotal * activeDiscountRatio);
            const finalTotal = subtotal - discount;

            if (discount > 0) {
                document.getElementById('couponDiscountRow').style.display = 'flex';
                document.getElementById('coDiscountAmount').innerText = "-₺" + discount.toLocaleString('tr-TR');
            } else {
                document.getElementById('couponDiscountRow').style.display = 'none';
            }

            document.getElementById('coFinalTotal').innerText = "₺" + finalTotal.toLocaleString('tr-TR');
            document.getElementById('btnPayText').innerText = `3D Secure ile Güvenli Öde (₺${finalTotal.toLocaleString('tr-TR')})`;
            document.getElementById('threeDSTotalAmount').innerText = "₺" + finalTotal.toLocaleString('tr-TR');
        }

        function applyCouponCode() {
            const code = document.getElementById('couponCodeInput').value.trim().toUpperCase();
            if (code === 'EULA10' || code === 'KITSUNE' || code === 'RAPID') {
                activeDiscountRatio = 0.10;
                renderCheckoutSummary();
                showToast('🎉 Tebrikler! %10 İndirim Kuponu Başarıyla Uygulandı!');
            } else if (code) {
                showToast('Geçersiz veya süresi dolmuş kupon kodu.');
            }
        }

        function selectPaymentMethod(type, btnElement) {
            document.querySelectorAll('.payment-method-pill').forEach(p => p.classList.remove('active'));
            btnElement.classList.add('active');
            if (type === 'eft') {
                document.getElementById('cardPaymentFields').style.display = 'none';
                activeDiscountRatio = 0.03;
                showToast('Havale/EFT seçildi (%3 Ek İndirim yansıtıldı)');
            } else {
                document.getElementById('cardPaymentFields').style.display = 'block';
                activeDiscountRatio = 0;
            }
            renderCheckoutSummary();
        }

        let smsInterval;
        function trigger3DSecurePayment() {
            const modal = document.getElementById('threeDSModal');
            modal.classList.add('active');
            
            let seconds = 180;
            const cd = document.getElementById('smsCountdown');
            clearInterval(smsInterval);
            smsInterval = setInterval(() => {
                seconds--;
                cd.innerText = seconds + " sn";
                if (seconds <= 0) {
                    clearInterval(smsInterval);
                    close3DModal();
                }
            }, 1000);
        }

        function close3DModal() {
            document.getElementById('threeDSModal').classList.remove('active');
            clearInterval(smsInterval);
        }

        function confirm3DPayment() {
            close3DModal();
            document.getElementById('checkoutView').style.display = 'none';
            document.getElementById('orderSuccessView').style.display = 'block';
            
            // Random Order No
            const orderNo = "#OE-" + Math.floor(100000 + Math.random() * 900000);
            document.getElementById('successOrderNo').innerText = orderNo;

            // Clear Cart
            cartItems = [];
            updateCartUI();
            
            showToast('🎉 Siparişiniz Onaylandı! Faturanız e-postanıza iletildi.');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
"""

content = content.replace('// Initialize on Load', checkout_js + '\n        // Initialize on Load')

with open(source_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Checkout and 3D Secure 2.0 system integrated into .source_protected.html!")
