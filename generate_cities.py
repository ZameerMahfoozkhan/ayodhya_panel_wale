import re

def generate_city_page(city_name):
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace "Ayodhya & Faizabad" or "Ayodhya &amp; Faizabad"
    content = re.sub(r'Ayodhya\s*(?:&|&amp;)\s*Faizabad', city_name, content, flags=re.IGNORECASE)
    
    # 2. Replace "Ayodhya" with city_name, but NOT when followed by " Panel Wale" or in "ayodhya_panel_wale" or inside href links
    # To do this safely, we will replace specific known patterns
    
    replacements = [
        ('PVC Panel Installation Ayodhya', f'PVC Panel Installation {city_name}'),
        ('PVC Wall Panel Ayodhya', f'PVC Wall Panel {city_name}'),
        ('PVC Panel Price Ayodhya', f'PVC Panel Price {city_name}'),
        ('PVC Ceiling Panel Ayodhya', f'PVC Ceiling Panel {city_name}'),
        ('Ayodhya <span>PVC Panel</span>', f'{city_name} <span>PVC Panel</span>'),
        ('Services in Ayodhya', f'Services in {city_name}'),
        ('Panel Work Ayodhya', f'Panel Work {city_name}'),
        ('Installation Ayodhya', f'Installation {city_name}'),
        ('TV Unit Panel Ayodhya', f'TV Unit Panel {city_name}'),
        ('3D PVC Panel Ayodhya', f'3D PVC Panel {city_name}'),
        ('Kitchen Panel Ayodhya', f'Kitchen Panel {city_name}'),
        ('Bedroom Panel Ayodhya', f'Bedroom Panel {city_name}'),
        ('Office Panel Ayodhya', f'Office Panel {city_name}'),
        ('families across Ayodhya', f'families across {city_name}'),
        (', Ayodhya', f', {city_name}'), # for testimonials
        ('prices in Ayodhya', f'prices in {city_name}'),
        ('Service in Ayodhya', f'Service in {city_name}'),
        ('installation service in Ayodhya', f'installation service in {city_name}'),
        ('installation service in Ayodhya', f'installation service in {city_name}'),
        ('Ayodhya district', f'{city_name} district'),
        ('installation in Ayodhya.', f'installation in {city_name}.'),
        ('home in Ayodhya.', f'home in {city_name}.'),
        ('from Ayodhya,', f'from {city_name},'),
        ('across Ayodhya', f'across {city_name}'),
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    # Fix SEO meta description specifically
    content = content.replace(f'service in {city_name} &amp; Faizabad', f'service in {city_name}')
    
    filename = f'pvc-panels-{city_name.lower()}.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f'Created {filename}')

generate_city_page('Lucknow')
generate_city_page('Sultanpur')
generate_city_page('Gonda')
