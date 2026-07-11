import os

pages = {
    "privacy-policy": {
        "title": "Privacy Policy",
        "desc": "Privacy policy and data collection practices for Family Law Guides.",
        "content": """<h2>1. Information We Collect</h2>
<p>We collect information you provide directly to us, such as when you create or modify your account, request on-demand services, contact customer support, or otherwise communicate with us. This information may include: name, email, phone number, postal address, profile picture, payment method, and other information you choose to provide.</p>
<h2>2. Use of Information</h2>
<p>We may use the information we collect about you to Provide, maintain, and improve our Services, including, for example, to facilitate payments, send receipts, provide products and services you request (and send related information), develop new features, provide customer support to Users and Drivers, develop safety features, authenticate users, and send product updates and administrative messages.</p>
<h2>3. Google AdSense & DoubleClick Cookie</h2>
<p>Google, as a third party vendor, uses cookies to serve ads on our Service. Google's use of the DoubleClick cookie enables it and its partners to serve ads to our users based on their visit to our Service or other websites on the Internet.</p>"""
    },
    "terms-of-service": {
        "title": "Terms of Service",
        "desc": "Terms of service and usage rules for Family Law Guides.",
        "content": """<h2>1. Terms</h2>
<p>By accessing this Website, accessible from familylaw.bongshai.com, you are agreeing to be bound by these Website Terms and Conditions of Use and agree that you are responsible for the agreement with any applicable local laws.</p>
<h2>2. Use License</h2>
<p>Permission is granted to temporarily download one copy of the materials (information or software) on Family Law Guides's Website for personal, non-commercial transitory viewing only.</p>
<h2>3. Disclaimer</h2>
<p>All the materials on Family Law Guides’s Website are provided "as is". Family Law Guides makes no warranties, may it be expressed or implied, therefore negates all other warranties. Furthermore, Family Law Guides does not make any representations concerning the accuracy or reliability of the use of the materials on its Website.</p>"""
    },
    "disclaimer": {
        "title": "Legal Disclaimer",
        "desc": "Legal and medical disclaimer for Family Law Guides.",
        "content": """<h2>Not Legal Advice</h2>
<p>The information provided on Family Law Guides does not, and is not intended to, constitute legal advice; instead, all information, content, and materials available on this site are for general informational purposes only. Information on this website may not constitute the most up-to-date legal or other information.</p>
<p>Readers of this website should contact their attorney to obtain advice with respect to any particular legal matter. No reader, user, or browser of this site should act or refrain from acting on the basis of information on this site without first seeking legal advice from counsel in the relevant jurisdiction.</p>"""
    },
    "about": {
        "title": "About Us",
        "desc": "Learn about the mission and team behind Family Law Guides.",
        "content": """<h2>Our Mission</h2>
<p>Family Law Guides was founded with a simple mission: to demystify the complex world of family law. Navigating divorce, child custody, and alimony can be the most stressful period of a person's life. We aim to provide clear, actionable, and state-specific educational resources to help you understand your rights and the legal processes.</p>
<h2>Our Team</h2>
<p>Our content is researched and written by a team of legal researchers and writers dedicated to making the law accessible to everyone.</p>"""
    },
    "contact": {
        "title": "Contact Us",
        "desc": "Get in touch with the Family Law Guides team.",
        "content": """<h2>Reach Out</h2>
<p>If you have any questions, suggestions, or concerns regarding our content, please feel free to reach out to us. Note: We cannot provide specific legal advice or answer specific legal questions about your case.</p>
<p><strong>Email:</strong> contact@familylaw.bongshai.com</p>
<p><strong>Address:</strong> 123 Legal Way, Suite 400, Austin, TX 78701</p>"""
    }
}

base_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Family Law Guides | familylaw.bongshai.com</title>
    <meta name="description" content="{title} | {desc} | familylaw.bongshai.com | Read More">
    
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
                <h1>{title}</h1>
            </header>
            <div class="content">
                {content}
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

for slug, data in pages.items():
    os.makedirs(slug, exist_ok=True)
    with open(os.path.join(slug, "index.html"), "w", encoding="utf-8") as f:
        f.write(base_html.format(**data))

print("Generated mandatory legal pages.")
