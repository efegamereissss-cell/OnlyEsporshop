import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure we add IDs to the thumbnails
content = content.replace(
    '<img src="" alt="thumb" class="pv-thumb active">\\n                    <img src="" alt="thumb" class="pv-thumb">\\n                    <img src="" alt="thumb" class="pv-thumb">',
    '<img src="" alt="thumb" class="pv-thumb active" id="pvImg1">\\n                    <img src="" alt="thumb" class="pv-thumb" id="pvImg2">\\n                    <img src="" alt="thumb" class="pv-thumb" id="pvImg3">'
)

js_new = '''
        // Page switching logic
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
            
            document.getElementById('homeView').style.display = 'none';
            document.getElementById('productView').style.display = 'block';
            window.scrollTo(0, 0);
        }
        
        function closeProduct() {
            document.getElementById('productView').style.display = 'none';
            document.getElementById('homeView').style.display = 'block';
            window.scrollTo(0, 0);
        }
'''

content = re.sub(r'// Modal Logic.*?document\.addEventListener\(\'keydown\', \(e\) => \{.*?\n\s*\}\);', js_new, content, flags=re.DOTALL)
content = re.sub(r'function closeModalOnOverlay\(e\).*?\}', '', content, flags=re.DOTALL)
content = re.sub(r'function closeModal\(\).*?\}', '', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
