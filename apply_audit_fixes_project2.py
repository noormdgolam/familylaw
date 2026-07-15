import os
import re

folder_path = r"e:\Adsense sites\1-10\2"

search_form_html = """
            <form action="/search" method="get" style="display:inline-block; margin-left: 20px;">
                <input type="search" name="q" placeholder="Search..." required style="padding: 5px; border: 1px solid #ccc; border-radius: 4px;">
                <button type="submit" style="padding: 5px 10px; background: var(--primary); color: white; border: none; border-radius: 4px; cursor: pointer;">Search</button>
            </form>
            </nav>"""

social_links_html = """<p>&copy; 2026 Family Law Attorney Guide. All rights reserved.</p>
            <div style="margin-top: 20px; display: flex; justify-content: center; gap: 15px;">
                <a href="https://twitter.com/familylawguide" target="_blank" rel="noopener noreferrer" style="color: var(--primary);">Twitter</a>
                <a href="https://facebook.com/familylawguide" target="_blank" rel="noopener noreferrer" style="color: var(--primary);">Facebook</a>
                <a href="https://linkedin.com/company/familylawguide" target="_blank" rel="noopener noreferrer" style="color: var(--primary);">LinkedIn</a>
            </div>"""

svg_banner_html = """<section class="content">
<div style="text-align: center; margin-bottom: 20px;"><svg width="728" height="90" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Family Law Attorney Guide Banner"><rect width="100%" height="100%" fill="#8b0000"/><text x="50%" y="50%" font-family="Arial, sans-serif" font-size="24" fill="#ffffff" dominant-baseline="middle" text-anchor="middle">Find a Top Family Law Attorney Today</text></svg></div>
"""

index_article = """<p style="font-size: 1.2rem; margin-top: 10px;">Explore our detailed family law attorney guide resources.</p>
<div style="margin-top: 30px; line-height: 1.8;">
    <h2>Navigating Family Law: A Comprehensive Guide</h2>
    <p>Family law is a multifaceted and deeply personal legal practice area that touches on the most fundamental aspects of our lives—our relationships, our children, and our futures. Whether you are facing a difficult divorce, seeking fair child custody arrangements, or dealing with spousal support disputes, understanding the nuances of family law is crucial to protecting your rights. This comprehensive guide serves as an essential resource for navigating these complex legal waters.</p>
    
    <h3>The Importance of a Specialized Family Law Attorney</h3>
    <p>When legal issues arise within a family unit, emotions often run high. A specialized family law attorney acts as both a legal advocate and an objective advisor. From filing the initial divorce petition to negotiating child support payments and dividing marital assets, an experienced lawyer can prevent costly mistakes. Family law varies significantly by state, meaning that a child custody strategy that works in Alabama might be entirely different in California or Texas. Local expertise is indispensable for achieving a favorable outcome.</p>
    
    <h3>Child Custody and Support</h3>
    <p>One of the most contentious areas in family law is child custody. Courts uniformly base their decisions on the "best interests of the child" standard. However, interpreting this standard involves evaluating numerous factors, including the child’s age, health, emotional ties with each parent, and the parents' ability to provide a stable environment. A skilled family law attorney will help you present a compelling case for sole, joint, legal, or physical custody. Furthermore, child support calculations, while often formulaic, can become complex when dealing with self-employed parents, hidden assets, or special needs children.</p>
    
    <h3>Divorce and Asset Division</h3>
    <p>Divorce proceedings range from simple, uncontested separations to highly litigated courtroom battles. A primary challenge is the division of assets and debts. States are generally divided into "community property" states (where marital assets are split 50/50) and "equitable distribution" states (where assets are divided fairly but not necessarily equally). Navigating the division of real estate, retirement accounts, business interests, and investments requires careful financial analysis and aggressive legal representation.</p>
    
    <h3>Taking the Next Step</h3>
    <p>If you are facing a family law matter, do not navigate the process alone. Use our state-by-state guides to find the resources, information, and legal representation you need to secure your family’s future and find peace of mind during turbulent times.</p>
</div>"""

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # 1. Search Bar
        if '<form action="/search"' not in content:
            content = content.replace('</nav>', search_form_html)
            
        # 2. Social Links
        if 'twitter.com/familylawguide' not in content:
            # We match the copyright paragraph
            content = re.sub(r'<p>&copy; 2026 Family Law Attorney Guide\. All rights reserved\.</p>', social_links_html, content)
            
        # 3. SVG Banner
        if 'aria-label="Family Law Attorney Guide Banner"' not in content:
            content = content.replace('<section class="content">', svg_banner_html)
            
        # 4. Thin content on index.html
        if os.path.basename(filepath) == 'index.html' and 'Navigating Family Law: A Comprehensive Guide' not in content:
            content = content.replace('<p style="font-size: 1.2rem; margin-top: 10px;">Explore our detailed family law attorney guide resources.</p>', index_article)
            
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")

count = 0
for root, dirs, files in os.walk(folder_path):
    if '.git' in dirs:
        dirs.remove('.git')
    for f in files:
        if f.endswith('.html'):
            process_file(os.path.join(root, f))
            count += 1

print(f"Processed {count} HTML files in {folder_path}")
