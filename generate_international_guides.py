import os

output_dir = "international"
os.makedirs(output_dir, exist_ok=True)

countries = [
    {
        "name": "United Kingdom",
        "slug": "uk",
        "desc": "Family law overview in the UK. Understand divorce processes, financial settlements, and child arrangements orders in England and Wales.",
        "details": "In the UK, the introduction of 'no-fault' divorce in 2022 fundamentally changed the landscape, allowing couples to separate without apportioning blame. Courts prioritize the welfare of any children involved."
    },
    {
        "name": "Canada",
        "slug": "canada",
        "desc": "Navigating Canadian family law. A guide to the federal Divorce Act, provincial laws on property division, and spousal support.",
        "details": "Canada operates under a federal Divorce Act, but property division and common-law relationships are governed by provincial and territorial laws. It's crucial to understand both jurisdictions."
    },
    {
        "name": "Australia",
        "slug": "australia",
        "desc": "Australian family law explained. Learn about the Family Law Act 1975, the principle of no-fault divorce, and the role of the Family Court.",
        "details": "Australia has a long-standing 'no-fault' divorce system. The primary focus in child custody disputes is the 'best interests of the child', encouraging shared parental responsibility."
    },
    {
        "name": "Ireland",
        "slug": "ireland",
        "desc": "A guide to Family Law in Ireland. Separation agreements, judicial separation, and the constitutional requirements for divorce.",
        "details": "Divorce in Ireland requires couples to live apart for a specified period (currently two out of the previous three years) before they can apply to the courts."
    },
    {
        "name": "South Africa",
        "slug": "south-africa",
        "desc": "Understanding South African family law. Marital regimes (in community of property vs. out of community), uncontested divorces, and maintenance.",
        "details": "South African law heavily depends on the marital regime chosen by the couple before marriage. 'In community of property' is the default, which means a joint estate is formed."
    }
]

def generate_intl_html(country):
    slug = country["slug"]
    name = country["name"]
    desc = country["desc"]
    details = country["details"]
    title = f"{name} Family Law & Divorce Guide"
    url = f"https://familylaw.bongshai.com/international/{slug}/"
    
    # JSON-LD Schema
    schema = f"""{{
      "@context": "https://schema.org",
      "@type": "Article",
      "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "{url}"
      }},
      "headline": "{title}",
      "description": "{desc}",
      "author": {{
        "@type": "Organization",
        "name": "Family Law Guides"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Family Law Guides",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://familylaw.bongshai.com/assets/images/logo.png"
        }}
      }}
    }}"""
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | International Guides</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{url}">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="{url}">
    <meta property="twitter:title" content="{title}">
    <meta property="twitter:description" content="{desc}">
    
    <script type="application/ld+json">
    {schema}
    </script>
    
    <!-- Google AdSense Placeholder -->
    <!-- <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX" crossorigin="anonymous"></script> -->

    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/css/index.css">
    <style>
        .ad-placeholder {{ width: 100%; min-height: 90px; background: #e5e7eb; display: flex; align-items: center; justify-content: center; color: #6b7280; font-size: 0.875rem; margin: 2rem 0; border: 1px dashed #9ca3af; }}
        .cookie-banner {{ position: fixed; bottom: 0; left: 0; right: 0; background: var(--primary); color: white; padding: 1rem; display: flex; justify-content: space-between; align-items: center; z-index: 1000; box-shadow: 0 -4px 10px rgba(0,0,0,0.1); }}
    </style>
</head>
<body>
    <header class="site-header">
        <div class="container flex justify-between items-center">
            <a href="/" class="logo">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--secondary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="8" r="7"></circle>
                    <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline>
                </svg>
                Family Law <span>Guides</span>
            </a>
            <nav class="desktop-nav">
                <ul class="flex gap-md" style="list-style: none;">
                    <li><a href="/" class="nav-link">Home</a></li>
                    <li><a href="/states" class="nav-link">US State Guides</a></li>
                    <li><a href="/international" class="nav-link" style="color: var(--secondary);">International</a></li>
                    <li><a href="/directory" class="nav-link">Find an Attorney</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="container mt-lg mb-xl">
        <article class="prose">
            <header class="mb-lg text-center">
                <span class="badge mb-sm">International Guide</span>
                <h1>{title}</h1>
            </header>
            
            <div class="ad-placeholder">AdSense Leaderboard Space</div>
            
            <div class="content">
                <p class="lead"><strong>{desc}</strong></p>
                <p>Family law varies drastically across borders. In <strong>{name}</strong>, navigating the legal intricacies of separation, divorce, and child custody requires specific regional knowledge.</p>
                
                <h2>Overview of {name} Family Law</h2>
                <p>{details}</p>
                
                <div class="ad-placeholder">AdSense In-Article Space</div>
                
                <h2>Key Considerations</h2>
                <ul>
                    <li><strong>Jurisdiction:</strong> Ensure the courts in {name} have the legal authority to hear your case.</li>
                    <li><strong>Asset Tracing:</strong> International divorces may complicate the tracing of overseas assets.</li>
                    <li><strong>Child Relocation:</strong> Specific laws govern the movement of children out of {name} without the consent of both parents.</li>
                </ul>
                
                <blockquote class="ymyl-disclaimer mt-lg" style="background-color: #fff3cd; border-left-color: #ffc107;">
                    <strong>Disclaimer:</strong> The content on this website is for educational and informational purposes only and does not constitute professional legal advice. Please consult with a legal professional licensed in {name} regarding your specific situation.
                </blockquote>
            </div>
        </article>
    </main>

    <footer class="site-footer">
        <div class="container text-center">
            <p class="text-sm text-muted">&copy; 2026 Family Law Guides. All rights reserved.</p>
        </div>
    </footer>
    
    <!-- Cookie Banner -->
    <div id="cookie-banner" class="cookie-banner" style="display: none;">
        <div>We use cookies to serve personalized ads and analyze traffic. By continuing, you agree to our <a href="/privacy-policy" style="color: var(--secondary);">Privacy Policy</a>.</div>
        <button onclick="acceptCookies()" class="btn" style="padding: 0.5rem 1rem;">Accept</button>
    </div>
    <script>
        if (!localStorage.getItem('cookieConsent')) {{
            document.getElementById('cookie-banner').style.display = 'flex';
        }}
        function acceptCookies() {{
            localStorage.setItem('cookieConsent', 'true');
            document.getElementById('cookie-banner').style.display = 'none';
        }}
    </script>
</body>
</html>"""
    
    dir_path = os.path.join(output_dir, slug)
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)

# Generate main international index
index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>International Family Law Guides</title>
    <meta name="description" content="Global guides for family law, covering the UK, Canada, Australia, Ireland, and South Africa.">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/css/index.css">
</head>
<body>
    <header class="site-header">
        <div class="container flex justify-between items-center">
            <a href="/" class="logo">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--secondary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="8" r="7"></circle>
                    <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline>
                </svg>
                Family Law <span>Guides</span>
            </a>
            <nav class="desktop-nav">
                <ul class="flex gap-md" style="list-style: none;">
                    <li><a href="/" class="nav-link">Home</a></li>
                    <li><a href="/states" class="nav-link">US State Guides</a></li>
                    <li><a href="/international" class="nav-link" style="color: var(--secondary);">International</a></li>
                    <li><a href="/directory" class="nav-link">Find an Attorney</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="container mt-lg mb-xl">
        <h1 class="text-center">International Family Law Guides</h1>
        <p class="text-center text-muted mb-lg">Select a country to understand the specific jurisdiction's family law processes.</p>
        <div class="grid-3">
            {''.join([f'''<div class="card">
                <h3>{c["name"]}</h3>
                <p class="text-muted mb-lg">{c["desc"]}</p>
                <a href="/international/{c["slug"]}" class="btn-outline">Read Guide</a>
            </div>''' for c in countries])}
        </div>
    </main>
</body>
</html>"""

with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

for c in countries:
    generate_intl_html(c)

print(f"Generated {len(countries)} international HTML guides successfully.")
