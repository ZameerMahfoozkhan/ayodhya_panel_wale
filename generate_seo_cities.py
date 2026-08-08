import re
import os

cities = ['Lucknow', 'Sultanpur', 'Gonda']

with open('index.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Replace Navigation in template for the localized pages
nav_original = """      <nav class="nav" id="mainNav">
        <a href="index.html" class="active">Home</a>
        <a href="pvc-panel-installation-ayodhya.html">Installation</a>
        <a href="pvc-wall-panel-ayodhya.html">Wall Panels</a>
        <a href="pvc-panel-price-ayodhya.html">Price</a>
        <a href="about.html">About</a>
        <a href="contact.html">Contact</a>
      </nav>"""
nav_new = """      <nav class="nav" id="mainNav">
        <a href="index.html">Home</a>
        <a href="#services">Services</a>
        <a href="#gallery">Gallery</a>
        <a href="about.html">About</a>
        <a href="contact.html">Contact</a>
      </nav>"""

footer_links_original = """          <h4>Quick Links</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="pvc-panel-installation-ayodhya.html">PVC Panel Installation</a></li>
            <li><a href="pvc-wall-panel-ayodhya.html">PVC Wall Panel</a></li>
            <li><a href="pvc-panel-price-ayodhya.html">PVC Panel Price</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>"""
footer_links_new = """          <h4>Quick Links</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#gallery">Gallery</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>"""

template = template.replace(nav_original, nav_new)
template = template.replace(footer_links_original, footer_links_new)

# Protect specific phrases from being replaced
protect_map = {
    'Ayodhya Panel Wale': '__BRAND__',
    'ayodhyapanelwale': '__EMAIL__',
    'Naka Bypass, Ayodhya': '__ADDRESS__',
    'Ayodhya, Faizabad, <a': '__FOOTER_AREAS__',
    'image/logo.png': '__LOGO__',
}

for city in cities:
    content = template
    
    # 1. Replace "Ayodhya & Faizabad" with the city name
    content = re.sub(r'Ayodhya\s*(?:&|&amp;)\s*Faizabad', city, content, flags=re.IGNORECASE)
    
    # 2. Protect specific brand terms
    for original, protected in protect_map.items():
        content = content.replace(original, protected)
        
    # 3. Replace all remaining "Ayodhya" with the new city
    content = content.replace('Ayodhya', city)
    content = content.replace('ayodhya', city.lower())
    
    # 4. Restore the protected terms
    for original, protected in protect_map.items():
        content = content.replace(protected, original)
        
    # 5. Make sure the title and meta are perfect
    content = content.replace(f'<title>PVC Panel Installation {city} | Ayodhya Panel Wale', 
                              f'<title>PVC Panel Installation {city} | Ayodhya Panel Wale')
    
    # If there are any stray "Faizabad" mentions, replace them if they aren't part of the footer service areas
    # Actually, we handled "Ayodhya & Faizabad". Let's do a quick regex for just Faizabad (except protected ones)
    content = content.replace('__FOOTER_AREAS__', 'Ayodhya, Faizabad, <a') # already restored but just in case
    
    filename = f'pvc-panels-{city.lower()}.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated {filename}")
