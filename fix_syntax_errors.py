source_path = r'C:\Users\eserh\Desktop\OnlyEULA-KF90-HE\.source_protected.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix duplicate trigger3DSecurePayment definition
old_dup_trigger = """        function trigger3DSecurePayment() {
            // When user tries to pay, directly show the rejection notification & modal
            showRejectModal();
        }"""

content = content.replace(old_dup_trigger, "")

# Fix unescaped apostrophe in showToast
bad_toast = "showToast('⚠️ Lütfen devam etmek için Ön Bilgilendirme ve Mesafeli Satış Sözleşmesi'ni onaylayınız.', true);"
good_toast = 'showToast("⚠️ Lütfen devam etmek için Ön Bilgilendirme ve Mesafeli Satış Sözleşmesi\'ni onaylayınız.", true);'

content = content.replace(bad_toast, good_toast)

with open(source_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Fixed JS syntax errors in .source_protected.html!")
