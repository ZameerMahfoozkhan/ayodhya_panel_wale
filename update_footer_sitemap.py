import glob
import re
from datetime import datetime

# 1. Update all HTML files
html_files = glob.glob('*.html')
target_str = '<p style="margin-top:10px"><strong>Service Areas:</strong> Ayodhya, Faizabad</p>'
replace_str = '<p style="margin-top:10px"><strong>Service Areas:</strong> Ayodhya, Faizabad, <a href="pvc-panels-lucknow.html">Lucknow</a>, <a href="pvc-panels-sultanpur.html">Sultanpur</a>, <a href="pvc-panels-gonda.html">Gonda</a></p>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_str in content:
        content = content.replace(target_str, replace_str)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated footer in {file}")

# 2. Update sitemap.xml
sitemap_urls = """  <url>
    <loc>https://ayodhya-panel-wale.vercel.app/pvc-panels-lucknow.html</loc>
    <lastmod>2026-08-08</lastmod>
    <priority>0.80</priority>
  </url>
  <url>
    <loc>https://ayodhya-panel-wale.vercel.app/pvc-panels-sultanpur.html</loc>
    <lastmod>2026-08-08</lastmod>
    <priority>0.80</priority>
  </url>
  <url>
    <loc>https://ayodhya-panel-wale.vercel.app/pvc-panels-gonda.html</loc>
    <lastmod>2026-08-08</lastmod>
    <priority>0.80</priority>
  </url>
</urlset>"""

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

if "pvc-panels-lucknow" not in sitemap:
    sitemap = sitemap.replace('</urlset>', sitemap_urls)
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("Updated sitemap.xml")

