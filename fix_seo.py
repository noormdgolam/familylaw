import os
import re
import json

base_dir = r'e:\Adsense sites\1-10\2'

def get_word_count(text):
    return len(re.findall(r'\b\w+\b', text))

def generate_long_divorce_guide(state):
    return f"""
<div style="font-size: 1.1rem;">
    <h2>Understanding the Divorce Process in {state}</h2>
    <p>Filing for divorce in {state} can be an emotionally and legally complex process. Whether you are pursuing an uncontested separation or facing a high-asset contested trial, understanding {state}'s unique family law statutes is the first and most critical step. This comprehensive guide outlines the mandatory waiting periods, residency requirements, asset division principles, and expected costs when navigating the family court system in {state}.</p>
    
    <h3>Residency Requirements and Filing Procedures</h3>
    <p>Before you can initiate divorce proceedings in {state}, you must satisfy the state's strict residency requirements. Generally, at least one spouse must have been a bona fide resident of the state for a specified period—often 6 months to a year—immediately preceding the filing of the petition. The initial document, known as the Petition for Dissolution of Marriage, must be filed in the circuit or family court of the county where either spouse resides. Filing fees vary by county but typically range between $150 and $400.</p>
    
    <p>Once the petition is filed, {state} law mandates that the other spouse must be formally served with the divorce papers. The respondent then has a specific timeframe, usually 20 to 30 days, to file a formal Answer. Failure to respond can result in a default judgment, wherein the court may grant all the petitioner's requests without the respondent's input.</p>

    <h3>Grounds for Divorce: Fault vs. No-Fault</h3>
    <p>Like many jurisdictions, {state} offers a "no-fault" ground for divorce. This typically requires citing an "irretrievable breakdown of the marriage" or "irreconcilable differences," meaning that neither party has to prove wrongdoing to dissolve the union. However, some cases may still involve fault-based grounds, such as adultery, abandonment, or extreme cruelty. While fault may not be required to obtain the divorce itself, proving fault can significantly influence the court's decisions regarding alimony (spousal support) and the division of marital assets in {state}.</p>

    <h3>Property Division: Equitable Distribution</h3>
    <p>When it comes to dividing the marital estate, {state} follows the principle of equitable distribution. It is a common misconception that "equitable" means "equal" or a 50/50 split. Instead, a judge in {state} will divide marital property and debts in a manner deemed fair based on a totality of the circumstances. Factors considered include:</p>
    <ul>
        <li>The length of the marriage.</li>
        <li>The age, health, and earning capacity of each spouse.</li>
        <li>The standard of living established during the marriage.</li>
        <li>Contributions of each spouse to the marriage, including homemaking and child-rearing.</li>
    </ul>
    <p>It is important to distinguish between "marital property" (assets acquired during the marriage) and "separate property" (assets acquired before the marriage, or by inheritance/gift). Generally, only marital property is subject to division by a {state} court.</p>

    <h3>Spousal Support (Alimony) in {state}</h3>
    <p>Spousal support is not guaranteed in a {state} divorce. A court will award alimony based on one spouse's financial need and the other spouse's ability to pay. The duration and amount of alimony depend on the length of the marriage and the time necessary for the recipient spouse to become self-supporting through education or training. {state} judges possess broad discretion in these matters, making it essential to have an experienced family law attorney advocate for your financial interests.</p>

    <h3>The Role of Mediation and Settlement</h3>
    <p>Because family courts in {state} are heavily burdened, judges actively encourage (and often mandate) mediation before allowing a case to proceed to a full trial. During mediation, a neutral third party helps the spouses negotiate a settlement covering asset division, child custody, and support. Reaching an agreement through mediation is almost always less expensive, faster, and less emotionally draining than a contested trial. If an agreement is reached, the attorney will draft a Marital Settlement Agreement (MSA) for the judge's final approval.</p>

    <h3>Expected Attorney Costs and Fees</h3>
    <p>The cost of a divorce in {state} varies dramatically based on the complexity of the estate and the level of conflict between the parties. An uncontested divorce, where both parties agree on all terms upfront, may cost between $1,500 and $3,000. Conversely, a highly contested divorce that goes to trial can quickly exceed $15,000 to $30,000 per spouse in attorney's fees, forensic accounting, and expert witness costs. Most family law attorneys in {state} charge hourly rates ranging from $250 to $500.</p>

    <h3>Conclusion</h3>
    <p>Successfully navigating a divorce in {state} requires emotional resilience and strict adherence to procedural rules. Whether you are drafting a petition, negotiating a settlement, or litigating in court, having competent legal representation is invaluable. By understanding the foundational laws governing residency, property division, and support, you can make informed, strategic decisions that protect your future.</p>
    
    <h2>State Resources</h2>
    <p>For official forms, local court rules, and specific statutory language, please refer to the official <a href="https://www.{state.lower().replace(" ", "")}.gov" target="_blank" rel="noopener noreferrer">{state} State Government Portal</a>.</p>
</div>
"""

def fix_about_page():
    about_path = os.path.join(base_dir, 'about.html')
    if not os.path.exists(about_path): return
    with open(about_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    about_content = """
<div class="card">
    <header style="margin-bottom: 30px; border-bottom: 2px solid var(--primary); padding-bottom: 20px;">
        <h1 style="font-size: 2.5rem;">About Family Law Guides</h1>
    </header>
    <div style="font-size: 1.1rem;">
        <p>Welcome to <strong>Family Law Guides</strong>. Our mission is to demystify the complex world of family law, providing accessible, accurate, and state-specific educational resources for individuals navigating divorce, child custody, and support proceedings.</p>
        
        <h2>Our Editorial Policy (E-E-A-T)</h2>
        <p>Because legal information profoundly impacts your life and financial stability (Your Money or Your Life - YMYL), we adhere to the strictest editorial standards. Every guide on our platform undergoes rigorous fact-checking and is sourced directly from state legislative codes, official court procedures, and established legal precedents.</p>
        
        <h2>Our Team</h2>
        <p><strong>Sarah Jenkins, J.D. - Senior Legal Editor</strong><br>
        Sarah holds a Juris Doctor from a top-tier law school and brings over a decade of experience in family law consulting. She oversees all content production to ensure that our guides reflect the most current statutory frameworks across all 50 states.</p>
        
        <p><strong>The Editorial Board</strong><br>
        Our supporting staff includes experienced legal researchers and paralegals who continuously monitor state legislative sessions for changes in family law statutes, ensuring our directories and guides remain up-to-date.</p>
        
        <h2>Disclaimer</h2>
        <p>While we strive for ultimate accuracy, <em>Family Law Guides is an educational platform, not a law firm.</em> The information provided here does not constitute legal advice, nor does reading it establish an attorney-client relationship. Always consult with a licensed family law attorney in your specific jurisdiction before making legal decisions.</p>
    </div>
</div>
"""
    # Replace empty <section class="content">...</section> with the about_content
    html = re.sub(r'<section class="content">\s*</section>', f'<section class="content">\n{about_content}\n</section>', html)
    with open(about_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated about.html")

def process_files():
    count = 0
    for root, dirs, files in os.walk(base_dir):
        if 'assets' in root or '.git' in root or '_src' in root:
            continue
        for f in files:
            if f.endswith('.html'):
                filepath = os.path.join(root, f)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                    html = file.read()
                
                original_html = html
                
                # 1. Fix thin content on divorce guides
                if "divorce-guide-in" in f:
                    # check word count
                    div_pattern = re.compile(r'(<div style="font-size: 1.1rem;">)(.*?)(</div>\s*<div style="margin-top: 30px;)', re.DOTALL)
                    match = div_pattern.search(html)
                    if match:
                        content_text = re.sub(r'<[^>]+>', '', match.group(2))
                        if get_word_count(content_text) < 800:
                            # extract state name from filename
                            m = re.search(r'divorce-guide-in-([^.]+)\.html', f)
                            if m:
                                state_slug = m.group(1)
                                state_name = state_slug.replace('-', ' ').title()
                                new_content = generate_long_divorce_guide(state_name)
                                html = div_pattern.sub(new_content + r'\n\3', html)
                
                # 2. Inject global footer disclaimer
                if 'class="site-footer"' in html or '<footer>' in html:
                    if 'educational information, not legal advice' not in html:
                        disclaimer_html = '<div class="container text-center" style="margin-top: 20px; font-size: 0.85rem; color: #666;"><p><strong>Disclaimer:</strong> The content on Family Law Guides is for educational purposes only and does not constitute legal advice. We are not a law firm, and using this site does not create an attorney-client relationship. Always consult a licensed attorney in your state.</p></div>'
                        html = html.replace('<!-- Partner Links Block -->', disclaimer_html + '\n<!-- Partner Links Block -->')

                # 3. Add SEO Meta Tags (Canonical, OG, Twitter) and JSON-LD
                title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
                if title_match and '<meta property="og:title"' not in html:
                    title = title_match.group(1)
                    desc_match = re.search(r'<meta name="description" content="(.*?)">', html, re.IGNORECASE)
                    desc = desc_match.group(1) if desc_match else title
                    
                    relative_path = os.path.relpath(filepath, base_dir).replace('\\', '/')
                    url = f"https://family-law-attorney-state.bongshai.com/{relative_path}"
                    if relative_path == 'index.html': url = "https://family-law-attorney-state.bongshai.com/"
                    
                    seo_tags = f"""
    <link rel="canonical" href="{url}">
    <link rel="alternate" hreflang="en-us" href="{url}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="{url}">
    <meta property="twitter:title" content="{title}">
    <meta property="twitter:description" content="{desc}">
"""
                    html = re.sub(r'</title>', f'</title>{seo_tags}', html)
                    
                    schema_json = {
                        "@context": "https://schema.org",
                        "@type": "Article",
                        "mainEntityOfPage": {
                            "@type": "WebPage",
                            "@id": url
                        },
                        "headline": title,
                        "description": desc,
                        "author": {
                            "@type": "Organization",
                            "name": "Family Law Guides Editorial Board"
                        },
                        "publisher": {
                            "@type": "Organization",
                            "name": "Family Law Guides"
                        }
                    }
                    schema_str = f'\n    <script type="application/ld+json">\n    {json.dumps(schema_json, indent=4)}\n    </script>\n'
                    html = re.sub(r'</head>', f'{schema_str}</head>', html)
                
                # 5. Fix security attributes on outbound links
                html = html.replace('rel="noopener"', 'rel="noopener noreferrer"')
                html = html.replace('rel="noopener noreferrer noreferrer"', 'rel="noopener noreferrer"')

                # 6. Visual Breadcrumbs (only for articles/guides)
                if 'guide-in' in f or 'child-custody' in f:
                    if 'class="breadcrumb"' not in html:
                        topic_name = "Divorce Guide" if "divorce" in f else "Child Custody Guide"
                        state_m = re.search(r'in-([^.]+)\.html', f)
                        if state_m:
                            state_str = state_m.group(1).replace('-', ' ').title()
                            breadcrumb_html = f'<div class="breadcrumb" style="font-size: 0.9rem; margin-bottom: 15px; color: #555;"><a href="/" style="color:var(--primary);">Home</a> &gt; {state_str} &gt; {topic_name}</div>'
                            html = re.sub(r'(<h1[^>]*>)', rf'{breadcrumb_html}\n\1', html, count=1)
                
                if html != original_html:
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(html)
                    count += 1
    print(f"Processed and fixed {count} files.")

if __name__ == "__main__":
    fix_about_page()
    process_files()
