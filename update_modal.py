import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_modal_css = '''
        .modal-overlay { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: var(--white); z-index: 9999; display: block; opacity: 0; pointer-events: none; transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.4s; padding: 0; transform: translateY(100%); overflow: hidden; }
        .modal-overlay.active { opacity: 1; pointer-events: auto; transform: translateY(0); }
        .modal-content { background: var(--white); width: 100%; height: 100%; border-radius: 0; display: flex; flex-direction: row; position: relative; transform: none; max-height: none; }
        .modal-close { position: absolute; top: 32px; right: 32px; background: rgba(0,0,0,0.05); width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 99999; transition: background 0.2s, transform 0.2s; border: none; color: var(--text-main); }
        .modal-close:hover { background: rgba(0,0,0,0.1); transform: rotate(90deg); }
        
        .modal-img-col { flex: 1.2; background: #f0f0f0; position: relative; height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; }
        .modal-img-col img { width: 100%; height: 100%; object-fit: cover; }
        .modal-info-col { flex: 0.8; padding: 80px 60px; display: flex; flex-direction: column; overflow-y: auto; height: 100vh; background: var(--white); }
        .m-brand { color: var(--primary); font-size: 16px; font-weight: 800; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 2px; }
        .m-title { font-size: 42px; font-weight: 900; margin-bottom: 24px; color: var(--text-main); line-height: 1.1; letter-spacing: -1px; }
        .m-desc { font-size: 18px; color: var(--text-light); margin-bottom: 32px; line-height: 1.6; }
        .m-specs { margin-bottom: 40px; display: flex; flex-direction: column; gap: 16px; }
        .m-spec-item { display: flex; align-items: center; gap: 16px; font-size: 16px; font-weight: 500; color: var(--text-main); }
        .m-spec-icon { color: #10b981; width: 24px; height: 24px; }
        .m-price-area { margin-top: auto; margin-bottom: 32px; display: flex; align-items: flex-end; gap: 16px; border-top: 1px solid var(--border); padding-top: 32px; }
        .m-price { font-size: 48px; font-weight: 900; color: var(--text-main); line-height: 1; letter-spacing: -2px; }
        .m-old-price { font-size: 24px; color: var(--text-light); text-decoration: line-through; margin-bottom: 8px; font-weight: 600; }
        .m-add-btn { background: var(--primary); color: white; border: none; border-radius: 12px; padding: 20px; font-size: 18px; font-weight: 800; width: 100%; display: flex; justify-content: center; align-items: center; gap: 12px; transition: all 0.3s; margin-bottom: 24px; cursor: pointer; box-shadow: 0 10px 20px rgba(124, 58, 237, 0.3); }
        .m-add-btn:hover { background: var(--primary-hover); transform: translateY(-2px); box-shadow: 0 15px 30px rgba(124, 58, 237, 0.4); }
        .m-meta { display: flex; flex-direction: column; gap: 12px; font-size: 14px; font-weight: 500; color: var(--text-light); }
        .m-meta span { display: flex; align-items: center; gap: 12px; }'''

# Using regex to replace the old block
pattern = re.compile(r'\.modal-overlay\s*\{.*\.m-meta span\s*\{[^\}]*\}', re.DOTALL)
content = pattern.sub(new_modal_css, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
