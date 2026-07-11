import os

output_dir = "educational"
os.makedirs(output_dir, exist_ok=True)

guides = [
    {
        "title": "The Divorce Filing Process Explained",
        "slug": "divorce-filing-process",
        "desc": "A step-by-step educational guide on how the divorce filing process works from petition to final decree."
    },
    {
        "title": "Child Custody Fundamentals",
        "slug": "child-custody-fundamentals",
        "desc": "Understand the difference between legal and physical custody, and how courts determine the best interests of the child."
    },
    {
        "title": "Navigating Alimony and Spousal Support",
        "slug": "alimony-spousal-support",
        "desc": "Learn how alimony is calculated, the different types of spousal support, and how long it typically lasts."
    },
    {
        "title": "Division of Marital Property",
        "slug": "division-of-marital-property",
        "desc": "An overview of equitable distribution vs. community property states, and how assets and debts are divided."
    },
    {
        "title": "Domestic Violence and Restraining Orders",
        "slug": "domestic-violence-restraining-orders",
        "desc": "Crucial information on obtaining protection orders and how domestic violence impacts family law cases."
    }
]

def generate_edu_html(guide):
    slug = guide["slug"]
    title = guide["title"]
    desc = guide["desc"]
    url = f"https://familylaw.bongshai.com/educational/{slug}/"
    
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
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Educational Explainer | familylaw.bongshai.com</title>
    <meta name="description" content="{title} | {desc} | familylaw.bongshai.com | Read Explainer">
    <link rel="canonical" href="{url}">
    <link rel="alternate" hreflang="en-us" href="{url}">
    <meta name="google-site-verification" content="YOUR_GSC_VERIFICATION_STRING" />
    
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-XXXXXXXXXX');
    </script>
    
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
    [
        {schema},
        {{
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://familylaw.bongshai.com/" }},
                {{ "@type": "ListItem", "position": 2, "name": "Educational Explainers", "item": "https://familylaw.bongshai.com/educational/" }},
                {{ "@type": "ListItem", "position": 3, "name": "{title}", "item": "{url}" }}
            ]
        }},
        {{
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {{
                    "@type": "Question",
                    "name": "Do I need a lawyer for this?",
                    "acceptedAnswer": {{
                        "@type": "Answer",
                        "text": "While you can represent yourself (Pro Se), it is highly advised to retain an attorney due to the complex nature of legal procedures and the long-term impact of court orders."
                    }}
                }}
            ]
        }}
    ]
    </script>
    
    <!-- Google AdSense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-YOUR_CLIENT_ID" crossorigin="anonymous"></script>

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
                    <li><a href="/states" class="nav-link">State Guides</a></li>
                    <li><a href="/educational" class="nav-link">Process Explainers</a></li>
                    <li><a href="/directory" class="nav-link">Find an Attorney</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="container mt-lg mb-xl">
        <article class="prose">
            <header class="mb-lg text-center">
                <span class="badge mb-sm">Educational Explainer</span>
                <h1>{title}</h1>
                <div class="author-bio" style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin-top: 1.5rem; text-align: left;">
                    <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=100&auto=format&fit=crop" alt="John Smith, Legal Analyst" style="width: 50px; height: 50px; border-radius: 50%;">
                    <div>
                        <p style="margin: 0; font-weight: 600; color: var(--primary);">Written by John Smith, Legal Analyst</p>
                        <p class="text-sm text-muted" style="margin: 0;">Last updated: July 2026</p>
                    </div>
                </div>
            </header>
            
            <div class="ad-placeholder">AdSense Leaderboard Space</div>
            
            <div class="content">
                <p class="lead"><strong>{desc}</strong></p>
                <p>Navigating the legal system can be incredibly overwhelming, especially when dealing with family-related matters. This guide serves to break down the complexities of <em>{title.lower()}</em> into manageable, understandable concepts.</p>
                
                <div class="toc" style="background: var(--surface); padding: 1.5rem; border-radius: 8px; margin-bottom: 2rem; border: 1px solid var(--border-color);">
                    <h3 style="margin-top:0;">Table of Contents</h3>
                    <ul style="margin-bottom:0;">
                        <li><a href="#understanding-basics">Understanding the Basics</a></li>
                        <li><a href="#general-process">The General Process</a></li>
                        <li><a href="#faqs">Frequently Asked Questions</a></li>
                    </ul>
                </div>
                
                <h2 id="understanding-basics">Understanding the Basics</h2>
                <p>Before diving into court proceedings, it is critical to understand the foundational principles of this legal area. Family law is designed to protect the rights of individuals and ensure the well-being of any children involved.</p>
                
                <div class="ad-placeholder">AdSense In-Article Space</div>
                
                <h2 id="general-process">The General Process</h2>
                <ol>
                    <li><strong>Initial Consultation:</strong> Always start by consulting with a licensed family law attorney.</li>
                    <li><strong>Filing the Petition:</strong> The formal legal document that initiates the process in the court system.</li>
                    <li><strong>Discovery Phase:</strong> Both parties exchange relevant information and documents.</li>
                    <li><strong>Mediation/Negotiation:</strong> Attempts to resolve the issues outside of a courtroom trial.</li>
                    <li><strong>Court Trial:</strong> If an agreement cannot be reached, a judge will make the final determination.</li>
                </ol>
                
                <h2 id="faqs">Frequently Asked Questions</h2>
                <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="margin-bottom: 1.5rem;">
                    <h3 itemprop="name" style="font-size: 1.2rem; margin-bottom: 0.5rem;">Do I need a lawyer for this?</h3>
                    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                        <div itemprop="text">
                            <p>While you can represent yourself (Pro Se), it is highly advised to retain an attorney due to the complex nature of legal procedures and the long-term impact of court orders.</p>
                        </div>
                    </div>
                </div>
                
                <blockquote class="ymyl-disclaimer mt-lg" style="background-color: #fff3cd; border-left-color: #ffc107;">
                    <strong>Disclaimer:</strong> The content on this website is for educational and informational purposes only and does not constitute professional legal advice. Please consult with a licensed attorney regarding your specific situation.
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

# Generate main educational index
index_html = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Educational Guides to Family Law Processes | familylaw.bongshai.com</title>
    <meta name="description" content="Educational Guides to Family Law Processes | Read our in-depth guides covering everything from divorce filing to child custody strategies. | familylaw.bongshai.com">
    <link rel="canonical" href="https://familylaw.bongshai.com/educational/">
    <link rel="alternate" hreflang="en-us" href="https://familylaw.bongshai.com/educational/">
    <meta name="google-site-verification" content="YOUR_GSC_VERIFICATION_STRING" />
    
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-XXXXXXXXXX');
    </script>
    
    <!-- Google AdSense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-YOUR_CLIENT_ID" crossorigin="anonymous"></script>

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
                    <li><a href="/states" class="nav-link">State Guides</a></li>
                    <li><a href="/educational" class="nav-link">Process Explainers</a></li>
                    <li><a href="/about" class="nav-link">About</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="container mt-lg mb-xl">
        <h1 class="text-center mb-lg">Educational Process Explainers</h1>
        <div class="grid-3">
            {''.join([f'''<div class="card">
                <h3>{g["title"]}</h3>
                <p class="text-muted mb-lg">{g["desc"]}</p>
                <a href="/educational/{g["slug"]}" class="btn-outline">Read Guide</a>
            </div>''' for g in guides])}
        </div>
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
with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)


for guide in guides:
    generate_edu_html(guide)

print(f"Generated {len(guides)} educational HTML guides successfully.")
