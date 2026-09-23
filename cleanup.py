import re

file_path = r'c:\Users\pratu\OneDrive\Desktop\Coding\kumars-landing-page\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove floating graphics CSS
content = re.sub(r'/\* ========================================\s*FLOATING DECORATIVE GRAPHICS\s*======================================== \*/.*?/\* ========================================\s*SECTION SHARED', r'/* ========================================\n       SECTION SHARED', content, flags=re.DOTALL)

# 2. Remove all <div class="floater...">...</div>
content = re.sub(r'<div class="floater.*?</svg>\s*</div>', '', content, flags=re.DOTALL)

# 3. Remove specialty icons HTML
content = re.sub(r'<div class="specialty-icon-wrapper">.*?</div>', '', content, flags=re.DOTALL)

# 4. Remove specialty icon CSS
content = re.sub(r'\.specialty-icon-wrapper \{.*?\}', '', content, flags=re.DOTALL)
content = re.sub(r'\.specialty-item:hover \.specialty-icon-wrapper \{.*?\}', '', content, flags=re.DOTALL)
content = re.sub(r'\.specialty-icon \{.*?\}', '', content, flags=re.DOTALL)

# 5. Remove SVGs from buttons (Hero CTA, Store Maps, Catering CTA, Footer Links, Phone Links)
# Find SVG inside hero-cta
content = re.sub(r'<a href="#stores" class="hero-cta fade-in".*?>\s*<svg.*?</svg>\s*(.*?)\s*</a>', r'<a href="#stores" class="hero-cta fade-in" aria-label="Scroll to store locations">\n      \1\n    </a>', content, flags=re.DOTALL)

content = re.sub(r'<a href="#stores" class="catering-cta fade-in".*?>\s*<svg.*?</svg>\s*(.*?)\s*</a>', r'<a href="#stores" class="catering-cta fade-in" aria-label="Visit a store to order catering">\n      \1\n    </a>', content, flags=re.DOTALL)

# Footer stores link
content = re.sub(r'<a href="#stores" class="footer-stores-link fade-in".*?>\s*(.*?)\s*<svg.*?</svg>\s*</a>', r'<a href="#stores" class="footer-stores-link fade-in" aria-label="Scroll to store locations">\n      \1\n    </a>', content, flags=re.DOTALL)

# Store maps btn
content = re.sub(r'class="store-maps-btn"(.*?)>\s*(.*?)\s*<svg.*?</svg>\s*</a>', r'class="store-maps-btn"\1>\n          \2\n        </a>', content, flags=re.DOTALL)

# Footer phone link
content = re.sub(r'class="footer-phone-link"(.*?)>\s*<svg.*?</svg>\s*(.*?)\s*</a>', r'class="footer-phone-link"\1>\n          \2\n        </a>', content, flags=re.DOTALL)

# Footer instagram link
content = re.sub(r'class="footer-instagram-link"(.*?)>\s*<svg.*?</svg>\s*(.*?)\s*</a>', r'class="footer-instagram-link"\1>\n        \2\n      </a>', content, flags=re.DOTALL)

# Also remove z-index from sections that we don't need anymore since floaters are gone
content = re.sub(r'\.hero > \*:not\(\.floater\):not\(\.hero-bottom-border\).*?z-index: 1;\s*\}', '', content, flags=re.DOTALL)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleanup complete.")
