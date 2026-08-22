import re

source_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\.source_protected.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Contract CSS
contract_css = """
        /* ==================== LEGAL CONTRACTS & AGREEMENTS STYLING ==================== */
        .agreement-box-wrapper {
            background: #f8fafc;
            border: 1.5px solid #e2e8f0;
            border-radius: 12px;
            padding: 14px 16px;
            margin-top: 18px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            transition: all 0.25s ease;
        }
        .agreement-box-wrapper.error-shake {
            border-color: #ef4444 !important;
            background: #fef2f2 !important;
            animation: shakeBox 0.4s ease;
        }
        @keyframes shakeBox {
            0%, 100% { transform: translateX(0); }
            20%, 60% { transform: translateX(-6px); }
            40%, 80% { transform: translateX(6px); }
        }
        .agreement-checkbox-label {
            display: flex;
            align-items: flex-start;
            gap: 10px;
            font-size: 12px;
            color: #475569;
            line-height: 1.5;
            cursor: pointer;
        }
        .agreement-checkbox-label input[type="checkbox"] {
            width: 16px;
            height: 16px;
            margin-top: 2px;
            accent-color: var(--primary);
            cursor: pointer;
            flex-shrink: 0;
        }
        .agreement-checkbox-label a {
            color: var(--primary);
            font-weight: 700;
            text-decoration: underline;
            transition: color 0.2s;
        }
        .agreement-checkbox-label a:hover {
            color: #5b21b6;
        }

        /* Contract Full Modal */
        .contract-modal-overlay {
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(8px);
            z-index: 12000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .contract-modal-overlay.active {
            display: flex;
        }
        .contract-modal-card {
            background: #ffffff;
            width: 100%;
            max-width: 820px;
            max-height: 85vh;
            border-radius: 20px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            border: 1px solid #e2e8f0;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            animation: modalFadeUp 0.3s ease;
        }
        .contract-modal-header {
            background: #0f172a;
            color: #fff;
            padding: 18px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid #1e293b;
        }
        .contract-modal-title {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 16px;
            font-weight: 800;
            color: #f8fafc;
        }
        .contract-tabs-nav {
            display: flex;
            background: #f1f5f9;
            border-bottom: 1px solid #e2e8f0;
            padding: 4px 16px 0 16px;
            gap: 8px;
            overflow-x: auto;
        }
        .contract-tab-btn {
            padding: 10px 16px;
            font-size: 13px;
            font-weight: 700;
            color: #64748b;
            background: none;
            border: none;
            border-bottom: 3px solid transparent;
            cursor: pointer;
            transition: var(--transition);
            white-space: nowrap;
        }
        .contract-tab-btn.active {
            color: var(--primary);
            border-bottom-color: var(--primary);
            background: #fff;
            border-radius: 8px 8px 0 0;
        }
        .contract-modal-body {
            padding: 24px;
            overflow-y: auto;
            flex: 1;
            font-size: 13px;
            color: #334155;
            line-height: 1.7;
        }
        .contract-modal-body h4 {
            font-size: 14px;
            font-weight: 800;
            color: #0f172a;
            margin-top: 18px;
            margin-bottom: 8px;
            padding-bottom: 4px;
            border-bottom: 1px solid #e2e8f0;
        }
        .contract-modal-body h4:first-child {
            margin-top: 0;
        }
        .contract-modal-footer {
            padding: 16px 24px;
            background: #f8fafc;
            border-top: 1px solid #e2e8f0;
            display: flex;
            justify-content: flex-end;
            gap: 12px;
        }
        .contract-btn-accept {
            background: #10b981;
            color: #fff;
            padding: 10px 22px;
            border-radius: 10px;
            font-weight: 700;
            font-size: 13px;
            cursor: pointer;
            border: none;
            transition: var(--transition);
        }
        .contract-btn-accept:hover {
            background: #059669;
        }
"""

content = content.replace('/* ==================== SECURITY & ANTI-TAMPER CSS ==================== */', contract_css + '\n        /* ==================== SECURITY & ANTI-TAMPER CSS ==================== */')

# 2. Add Agreement Checkbox section in Checkout Summary Column
agreement_box_html = """
                    <!-- Sales Agreements & Terms Confirmation -->
                    <div class="agreement-box-wrapper" id="agreementBox">
                        <label class="agreement-checkbox-label">
                            <input type="checkbox" id="chkAgreements">
                            <span>
                                <a href="javascript:void(0)" onclick="openContractModal('onBilgilendirme')">Ön Bilgilendirme Koşulları</a>'nı ve 
                                <a href="javascript:void(0)" onclick="openContractModal('mesafeliSatis')">Mesafeli Satış Sözleşmesi</a>'ni okudum, onaylıyorum. <b style="color:#ef4444;">*</b>
                            </span>
                        </label>
                        <label class="agreement-checkbox-label">
                            <input type="checkbox" id="chkKvkk">
                            <span>
                                <a href="javascript:void(0)" onclick="openContractModal('kvkk')">KVKK Aydınlatma Metni</a>'ni okudum, ticari elektronik ileti onayını kabul ediyorum.
                            </span>
                        </label>
                    </div>

                    <button class="btn-complete-payment" onclick="trigger3DSecurePayment()">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                        <span id="btnPayText">3D Secure ile Güvenli Öde</span>
                    </button>

                    <div style="font-size: 11px; color: #94a3b8; text-align: center; margin-top: 14px; line-height: 1.4;">
                        🔒 256-Bit SSL & 3D Secure 2.0 güvencesiyle korunmaktadır.
                    </div>
"""

content = re.sub(r'<button class="btn-complete-payment" onclick="trigger3DSecurePayment\(\)">[\s\S]*?<div style="font-size: 11px; color: #94a3b8; text-align: center; margin-top: 14px; line-height: 1\.4;">[\s\S]*?<\/div>', agreement_box_html.strip(), content)

# 3. Add Contract Modal HTML
contract_modal_html = """
    <!-- ==================== LEGAL CONTRACTS POPUP MODAL ==================== -->
    <div class="contract-modal-overlay" id="contractModalOverlay">
        <div class="contract-modal-card">
            <div class="contract-modal-header">
                <div class="contract-modal-title">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#a78bfa" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                    YASAL SÖZLEŞMELER & BİLGİLENDİRME
                </div>
                <button onclick="closeContractModal()" style="background:none; border:none; color:#94a3b8; font-size:24px; cursor:pointer; line-height:1;">&times;</button>
            </div>
            
            <div class="contract-tabs-nav">
                <button class="contract-tab-btn active" id="tabBtnMesafeli" onclick="switchContractTab('mesafeliSatis')">Mesafeli Satış Sözleşmesi</button>
                <button class="contract-tab-btn" id="tabBtnOnBilgi" onclick="switchContractTab('onBilgilendirme')">Ön Bilgilendirme Formu</button>
                <button class="contract-tab-btn" id="tabBtnKvkk" onclick="switchContractTab('kvkk')">KVKK & Gizlilik</button>
                <button class="contract-tab-btn" id="tabBtnIade" onclick="switchContractTab('iade')">Garanti & 30 Gün İade</button>
            </div>

            <div class="contract-modal-body" id="contractModalBody">
                <!-- Injected via JS -->
            </div>

            <div class="contract-modal-footer">
                <button onclick="closeContractModal()" style="background:#e2e8f0; color:#334155; border:none; padding:10px 18px; border-radius:10px; font-weight:700; cursor:pointer;">Kapat</button>
                <button class="contract-btn-accept" onclick="acceptContractsAndClose()">✓ Okudum ve Onaylıyorum</button>
            </div>
        </div>
    </div>
"""

content = content.replace('<!-- ==================== PAYMENT REJECTION / DISABLED MODAL ==================== -->', contract_modal_html + '\n    <!-- ==================== PAYMENT REJECTION / DISABLED MODAL ==================== -->')

# 4. Add Contract Content & JS Logic
contract_js = """
        // Contract Text Data
        const contractTexts = {
            mesafeliSatis: `
                <h4>MESAFELİ SATIŞ SÖZLEŞMESİ</h4>
                <p><b>MADDE 1 - TARAFLAR</b><br>
                <b>SATICI:</b> ONLY EULA Espor ve Bilişim Donanımları San. Tic. A.Ş.<br>
                <b>Adres:</b> Maslak Espor Teknopark No:48/A Sarıyer / İstanbul<br>
                <b>E-Posta:</b> destek@onlyeula.com | <b>Mersis No:</b> 0648291048200001<br>
                <b>ALICI:</b> Sipariş formunu doldurarak ödeme gerçekleştiren tüketici.</p>

                <h4>MADDE 2 - SÖZLEŞMENİN KONUSU</h4>
                <p>İşbu Sözleşme'nin konusu, ALICI'nın SATICI'ya ait www.only-esporshop.vercel.app web sitesinden elektronik ortamda siparişini yaptığı manyetik switch espor klavyesi, deskmat ve espor ekipmanlarının satışı ve teslimi ile ilgili olarak 6502 sayılı Tüketicinin Korunması Hakkında Kanun ve Mesafeli Sözleşmeler Yönetmeliği hükümleri gereğince tarafların hak ve yükümlülüklerinin belirlenmesidir.</p>

                <h4>MADDE 3 - TESLİMAT VE İFA KOŞULLARI</h4>
                <p>3.1. Sipariş edilen ürünler, ALICI'nın sipariş esnasında bildirdiği teslimat adresine anlaşmalı kargo firması (Yurtiçi Kargo / Kolay Gelsin) aracılığıyla en geç 30 günlük yasal süre içerisinde teslim edilir.<br>
                3.2. 14:00'a kadar verilen siparişler aynı iş günü kargoya teslim edilmektedir.</p>

                <h4>MADDE 4 - CAYMA HAKKI VE İADE PROSEDÜRÜ</h4>
                <p>4.1. ALICI, hiçbir gerekçe göstermeksizin ve cezai şart ödemeksizin malı teslim aldığı tarihten itibaren <b>14 (on dört) gün</b> içinde cayma hakkına sahiptir.<br>
                4.2. ONLY EULA markalı donanım ürünlerinde tüketici memnuniyeti kapsamında bu süre <b>30 (otuz) gün</b> olarak uygulanmaktadır.<br>
                4.3. Cayma hakkının kullanılması için ürünün ambalajının, kutu içeriğinin ve faturasının eksiksiz olarak satıcıya iade edilmesi gerekmektedir.</p>

                <h4>MADDE 5 - YETKİLİ MAHKEME</h4>
                <p>İşbu sözleşmeden doğabilecek uyuşmazlıklarda, Sanayi ve Ticaret Bakanlığınca ilan edilen değere kadar Tüketici Hakem Heyetleri ile ALICI'nın veya SATICI'nın yerleşim yerindeki Tüketici Mahkemeleri yetkilidir.</p>
            `,
            onBilgilendirme: `
                <h4>ÖN BİLGİLENDİRME FORMU</h4>
                <p><b>1. SATICI BİLGİLERİ:</b><br>
                Unvan: ONLY EULA Espor ve Bilişim Donanımları A.Ş.<br>
                İletişim: destek@onlyeula.com | Müşteri Hizmetleri: 0850 840 38 52</p>

                <h4>2. SÖZLEŞME KONUSU ÜRÜNÜN TEMEL NİTELİKLERİ</h4>
                <p>Satışa sunulan Manyetik Hall Effect (HE) espor klavyeleri, Rapid Trigger (0.01mm hassasiyet), 8000Hz Polling Rate ve SOCD donanım desteğine sahiptir. Ürünlerin tüm vergiler dahil nihai satış fiyatı sipariş özeti tablosunda açıkça belirtilmiştir.</p>

                <h4>3. ÖDEME VE GÜVENLİK PROTOKOLLERİ</h4>
                <p>Ödemeler 256-Bit SSL şifreleme, İyzico ve Param BDDK lisanslı sanal POS altyapısı ve 3D Secure 2.0 SMS şifre doğrulama sistemi ile güvenle gerçekleştirilir. Kredi kartı bilgileriniz sunucularımızda kesinlikle saklanmaz.</p>

                <h4>4. ŞİKAYET VE İTİRAZLAR</h4>
                <p>Tüketiciler şikayet ve itirazları konusunda başvurularını Bakanlıkça her yıl belirlenen parasal sınırlar dahilinde Tüketici Sorunları Hakem Heyetine veya Tüketici Mahkemesine yapabilirler.</p>
            `,
            kvkk: `
                <h4>KVKK AYDINLATMA METNİ VE GİZLİLİK POLİTİKASI</h4>
                <p>ONLY EULA olarak kişisel verilerinizin güvenliğine en üst düzeyde önem veriyoruz. 6698 sayılı Kişisel Verilerin Korunması Kanunu ("KVKK") kapsamında;</p>
                <p><b>1. İşlenen Veriler:</b> Ad, soyad, telefon numarası, e-posta adresi, teslimat ve fatura adresi verileriniz yalnızca siparişin teslimi, faturalandırma ve kargo bilgilendirme SMS'i gönderimi amacıyla işlenir.<br>
                <b>2. Veri Güvenliği:</b> Kart bilgileriniz TCMB ve BDDK onaylı ödeme kuruluşlarının PCI-DSS Level 1 uyumlu güvenli sunucuları üzerinden doğrudan bankalara iletilir; veri tabanımızda asla tutulmaz.<br>
                <b>3. Haklarınız:</b> KVKK'nın 11. maddesi uyarınca dilediğiniz zaman tarafımıza başvurarak verilerinizin silinmesini, güncellenmesini veya işlenme amacını öğrenmeyi talep edebilirsiniz.</p>
            `,
            iade: `
                <h4>30 GÜN KOŞULSUZ MEMNUNİYET VE GARANTİ ŞARTLARI</h4>
                <p><b>1. 2 Yıl Bire Bir Değişim Garantisi:</b> Tüm Only EULA KF90 serisi klavyeler ve ekipmanlar üretim hatalarına karşı 2 yıl resmi garantilidir.<br>
                <b>2. Koşulsuz 30 Gün Deneme:</b> Satın aldığınız manyetik klavyeyi beğenmediğiniz takdirde 30 gün içinde faturası ve orijinal kutu içeriğiyle birlikte iade edebilir, kesintisiz tam ücret iadesi alabilirsiniz.<br>
                <b>3. Kargo Ücreti:</b> Garanti ve cayma hakkı kapsamındaki tüm iade gönderimlerinde kargo ücreti ONLY EULA tarafından karşılanmaktadır.</p>
            `
        };

        let currentContractTab = 'mesafeliSatis';

        function openContractModal(tabKey = 'mesafeliSatis') {
            const overlay = document.getElementById('contractModalOverlay');
            if (overlay) {
                overlay.classList.add('active');
                switchContractTab(tabKey);
            }
        }

        function closeContractModal() {
            const overlay = document.getElementById('contractModalOverlay');
            if (overlay) overlay.classList.remove('active');
        }

        function switchContractTab(tabKey) {
            currentContractTab = tabKey;
            
            // Update active tab buttons
            document.querySelectorAll('.contract-tab-btn').forEach(b => b.classList.remove('active'));
            if (tabKey === 'mesafeliSatis') document.getElementById('tabBtnMesafeli').classList.add('active');
            if (tabKey === 'onBilgilendirme') document.getElementById('tabBtnOnBilgi').classList.add('active');
            if (tabKey === 'kvkk') document.getElementById('tabBtnKvkk').classList.add('active');
            if (tabKey === 'iade') document.getElementById('tabBtnIade').classList.add('active');

            // Set content
            const body = document.getElementById('contractModalBody');
            body.innerHTML = contractTexts[tabKey] || contractTexts.mesafeliSatis;
            body.scrollTop = 0;
        }

        function acceptContractsAndClose() {
            const chkAgreements = document.getElementById('chkAgreements');
            const chkKvkk = document.getElementById('chkKvkk');
            if (chkAgreements) chkAgreements.checked = true;
            if (chkKvkk) chkKvkk.checked = true;

            const box = document.getElementById('agreementBox');
            if (box) box.classList.remove('error-shake');

            closeContractModal();
            showToast('✓ Satış sözleşmesi ve koşulları onaylandı.');
        }

        function trigger3DSecurePayment() {
            const chk = document.getElementById('chkAgreements');
            const agreementBox = document.getElementById('agreementBox');

            if (!chk || !chk.checked) {
                if (agreementBox) {
                    agreementBox.classList.add('error-shake');
                    setTimeout(() => { agreementBox.classList.remove('error-shake'); }, 800);
                }
                showToast('⚠️ Lütfen devam etmek için Ön Bilgilendirme ve Mesafeli Satış Sözleşmesi\'ni onaylayınız.', true);
                agreementBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
                return;
            }

            // If checked, proceed to show the purchase rejection modal as requested
            showRejectModal();
        }
"""

content = content.replace('function showRejectModal() {', contract_js + '\n        function showRejectModal() {')

with open(source_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Full legal sales contracts, interactive modal, and mandatory verification added to .source_protected.html!")
