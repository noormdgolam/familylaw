import os
from datetime import datetime

base_url = "https://familylaw.bongshai.com"
urls = []

# Top level pages
top_level = ["", "/states", "/educational", "/directory", "/international", "/privacy-policy", "/terms-of-service", "/about", "/contact", "/disclaimer"]
for path in top_level:
    urls.append({"loc": f"{base_url}{path}", "changefreq": "weekly", "priority": "1.0" if path == "" else "0.8"})

# Add subdirectories
for directory in ["states", "educational", "international"]:
    if os.path.exists(directory):
        for slug in os.listdir(directory):
            if os.path.isdir(os.path.join(directory, slug)):
                urls.append({"loc": f"{base_url}/{directory}/{slug}/", "changefreq": "monthly", "priority": "0.6"})

xml_content = '<?xml version="1.0" encoding="UTF-8"?>\\n'
xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n'

today = datetime.now().strftime("%Y-%m-%d")

for url in urls:
    xml_content += f"""  <url>
    <loc>{url["loc"]}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{url["changefreq"]}</changefreq>
    <priority>{url["priority"]}</priority>
  </url>\\n"""

xml_content += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(xml_content)

print(f"Generated sitemap with {len(urls)} URLs.")
