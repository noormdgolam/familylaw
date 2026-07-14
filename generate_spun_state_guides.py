import os
import random

output_dir = "states"
os.makedirs(output_dir, exist_ok=True)

states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", 
    "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", 
    "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", 
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", 
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", 
    "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", 
    "West Virginia", "Wisconsin", "Wyoming"
]

topics = [
    {
        "slug_suffix": "statute-of-limitations", 
        "title_suffix": "Statute of Limitations Guide", 
        "desc_suffix": "Comprehensive guide to the statute of limitations for family law cases in {state}. Learn about time limits for divorce, alimony, and child custody modifications.",
        "prompt_topic": "Family Law Statute of Limitations"
    },
    {
        "slug_suffix": "child-custody", 
        "title_suffix": "Child Custody Laws and Guidelines", 
        "desc_suffix": "Detailed overview of child custody laws in {state}. Understand how courts determine physical and legal custody, visitation schedules, and child support.",
        "prompt_topic": "Child Custody Laws and Guidelines"
    },
    {
        "slug_suffix": "divorce-process", 
        "title_suffix": "Divorce Filing Process and Requirements", 
        "desc_suffix": "Step-by-step guide to the divorce filing process in {state}. Learn about residency requirements, grounds for divorce, and division of property.",
        "prompt_topic": "Divorce Filing Process and Requirements"
    }
]

# Spintax components
intros = [
    "Navigating the legal landscape of {topic} in {state} can be a daunting and complex endeavor. Whether you are initiating proceedings or responding to a court order, understanding the precise statutory requirements is paramount. {state} operates under a unique set of family law codes that govern how these matters are handled, deeply impacting the lives and financial stability of the parties involved. In this comprehensive guide, we unpack the critical elements of {topic}, offering insights into court procedures, filing timelines, and the evidentiary standards expected by {state} judges. By familiarizing yourself with these foundational principles, you can better prepare for the legal journey ahead and make informed decisions that protect your rights.",
    "The domain of {topic} within {state} is governed by stringent legislative frameworks and nuanced judicial precedents. For individuals facing these family law challenges, achieving a favorable outcome relies heavily on a thorough comprehension of local regulations. This article serves as an extensive resource, detailing the essential mechanics of {topic} as applied in {state} courtrooms. From the initial petition to the final decree, the process is laden with mandatory waiting periods, disclosure requirements, and potential mediation phases. We will explore the historical context of {state}'s family law statutes and how contemporary rulings have shaped the current legal environment, ensuring you possess the knowledge required to navigate your case effectively.",
    "When dealing with {topic} in {state}, parties often find themselves overwhelmed by the sheer volume of legal jargon and procedural mandates. However, obtaining a clear grasp of these concepts is absolutely essential for anyone wishing to safeguard their legal interests. {state} family courts prioritize structured dispute resolution, placing a strong emphasis on statutory compliance and judicial discretion. This guide is designed to demystify {topic}, breaking down the complex legal doctrines into digestible, actionable information. We delve into the specific criteria {state} courts utilize when adjudicating these matters, the timeline of a typical case, and the strategic considerations that can significantly influence the final outcome of your family law dispute."
]

definitions = [
    "<h2>Core Definitions and Legal Concepts</h2><p>To effectively engage with {topic} in {state}, one must first master the terminology. The legal system utilizes specific terms that carry weighty implications. For instance, the burden of proof in these matters typically requires a 'preponderance of the evidence,' meaning that it is more likely than not that a claim is true. Furthermore, {state} distinguishes between procedural law (the rules of the court) and substantive law (the actual statutes governing the issue). Understanding this dichotomy is crucial, as failing to adhere to procedural rules—such as filing deadlines or proper service of process—can result in a case being dismissed regardless of its substantive merits.</p><p>Additionally, {state} courts frequently employ the concept of 'equitable resolution.' This does not necessarily mean an equal 50/50 split, but rather an outcome that the judge deems fair based on a totality of the circumstances. Factors such as the financial standing of each party, historical conduct, and future earning capacity are meticulously evaluated.</p>",
    "<h2>Fundamental Principles of {state} Family Law</h2><p>At the heart of {topic} in {state} lies a commitment to structured legal proceedings designed to yield equitable results. The terminology used in court filings is highly specific; terms like 'petitioner,' 'respondent,' 'affidavit,' and 'injunction' form the bedrock of legal communication. In {state}, the courts mandate strict adherence to civil procedure, meaning that every motion filed must be accompanied by the appropriate evidentiary support and legal citations. Ignorance of these procedural rules is rarely accepted as a valid excuse by sitting judges.</p><p>Moreover, the concept of 'jurisdiction' plays a pivotal role. Before a {state} court can hear a case concerning {topic}, it must establish both subject-matter jurisdiction and personal jurisdiction over the parties involved. This often involves analyzing residency requirements, the location where the marriage or separation occurred, and the current domicile of any children involved. These jurisdictional prerequisites ensure that the court has the legal authority to issue binding orders.</p>",
    "<h2>Deciphering the Legal Jargon</h2><p>A major hurdle in navigating {topic} in {state} is the dense legal vocabulary. To participate meaningfully in your case, you must understand the distinction between temporary orders (pendente lite) and final judgments. Temporary orders dictate the rules of engagement while the case is pending, addressing immediate needs such as temporary support or access. Conversely, a final judgment permanently resolves the issues, though it may be subject to future modifications under specific, stringent conditions.</p><p>In {state}, the courts also heavily rely on 'discovery'—the formal process of exchanging information. Through interrogatories, depositions, and requests for production of documents, both sides are compelled to reveal their evidence. This transparency is a cornerstone of {state} family law, designed to prevent trial by ambush and encourage pre-trial settlements. Failing to comply with discovery requests can lead to severe sanctions, including monetary fines or adverse inferences being drawn against the non-compliant party.</p>"
]

procedures = [
    "<h2>Step-by-Step Court Procedures</h2><p>The trajectory of a {topic} case in {state} generally follows a predictable, albeit lengthy, path. It commences with the filing of a formal Petition or Complaint in the appropriate county courthouse. This document outlines the relief being sought and the legal grounds justifying that relief. Following the filing, the petitioner must effectuate 'service of process' upon the opposing party, providing them with official notice of the lawsuit. The respondent is then granted a specific window—typically 20 to 30 days in {state}—to file a formal Answer.</p><p>Once the initial pleadings are established, the case enters the discovery phase, which can last several months. During this time, {state} courts often mandate alternative dispute resolution (ADR), such as mediation. Mediation brings both parties before a neutral third party in an attempt to forge a settlement without the need for a contentious trial. If mediation fails, the case proceeds to a pre-trial conference and ultimately a bench trial, where a judge will hear testimony, review evidence, and issue a binding ruling on {topic}.</p>",
    "<h2>Navigating the Legal Pathway in {state}</h2><p>Initiating an action related to {topic} in {state} requires meticulous preparation. The process is initiated when one party files the necessary initial pleadings with the family court clerk. These pleadings must strictly conform to {state}'s formatting and content rules. After the petition is filed and a filing fee is paid, the respondent must be legally served. In {state}, this is often accomplished via a county sheriff or a private process server. The respondent's Answer may also include counterclaims, expanding the scope of the litigation.</p><p>As the case progresses, {state} judges frequently issue scheduling orders that set strict deadlines for discovery completion, witness list exchanges, and mediation sessions. Mediation is heavily favored in {state} as a means to reduce court backlogs and allow parties to retain control over the outcome. Should the parties reach an impasse, the court will schedule an evidentiary hearing. Here, the rules of evidence are strictly enforced, and the judge acts as the sole trier of fact, delivering a final verdict based exclusively on the admissible evidence presented.</p>",
    "<h2>The Timeline of a {topic} Case</h2><p>Understanding the procedural timeline in {state} is vital for managing expectations. A case concerning {topic} begins with the drafting and filing of a Petition. This is not a mere formality; the Petition sets the jurisdictional basis and frames the issues for the court. Following proper service, the clock begins ticking for the respondent's reply. In many {state} jurisdictions, the filing of the petition automatically triggers mutual restraining orders, which prevent either party from dissipating assets or removing children from the state without court permission.</p><p>The bulk of the timeline is consumed by discovery and mandatory settlement conferences. {state} law highly encourages out-of-court settlements, often requiring parties to attend mandatory settlement conferences presided over by a seasoned attorney or retired judge. If these efforts prove unfruitful, the matter is set for trial. A trial concerning {topic} in {state} can last anywhere from a few hours to several weeks, depending on the complexity of the issues and the volume of evidentiary exhibits and expert testimonies involved.</p>"
]

tables = [
    """<h2>Comparison of Key Timeframes and Deadlines</h2>
    <table border="1" style="width: 100%; border-collapse: collapse; text-align: left;">
        <thead>
            <tr style="background-color: #f2f2f2;">
                <th style="padding: 0.5rem; border: 1px solid #ddd;">Action / Requirement</th>
                <th style="padding: 0.5rem; border: 1px solid #ddd;">Typical {state} Timeline</th>
                <th style="padding: 0.5rem; border: 1px solid #ddd;">Statutory Reference / Notes</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Filing of Answer/Response</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">20 - 30 Days after Service</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Mandatory deadline to prevent default judgment.</td>
            </tr>
            <tr>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Discovery Completion</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">60 - 120 Days</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Extensions require formal court approval.</td>
            </tr>
            <tr>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Mandatory Mediation</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Prior to Trial Setting</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Required in over 80% of contested cases.</td>
            </tr>
            <tr>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Appeal Window</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">30 Days from Final Decree</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Strict timeline; late filings are dismissed.</td>
            </tr>
        </tbody>
    </table>""",
    
    """<h2>Overview of Legal Requirements in {state}</h2>
    <table border="1" style="width: 100%; border-collapse: collapse; text-align: left;">
        <thead>
            <tr style="background-color: #f2f2f2;">
                <th style="padding: 0.5rem; border: 1px solid #ddd;">Phase of Litigation</th>
                <th style="padding: 0.5rem; border: 1px solid #ddd;">Standard {state} Requirement</th>
                <th style="padding: 0.5rem; border: 1px solid #ddd;">Consequence of Non-Compliance</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Initial Pleading</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Must cite correct jurisdictional statutes</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Dismissal of the case without prejudice.</td>
            </tr>
            <tr>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Financial Disclosure</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Comprehensive affidavit within 45 days</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Fines, sanctions, or imputation of income.</td>
            </tr>
            <tr>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Pre-Trial Conference</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Mandatory attendance by parties and counsel</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Striking of pleadings or entry of default.</td>
            </tr>
            <tr>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Final Hearing</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Adherence to {state} Rules of Evidence</td>
                <td style="padding: 0.5rem; border: 1px solid #ddd;">Exclusion of critical witness testimony or exhibits.</td>
            </tr>
        </tbody>
    </table>"""
]

faqs_pool = [
    ("How long does the entire process take in {state}?", "The duration of a case involving {topic} in {state} varies widely. An uncontested matter might be resolved in as little as 60 to 90 days, depending on court backlogs. However, heavily contested cases requiring extensive discovery and a full trial can easily stretch from one to two years."),
    ("Do I strictly need an attorney for {topic}?", "While {state} law allows individuals to represent themselves (pro se), it is highly discouraged in cases involving {topic}. The procedural rules are unforgiving, and a single mistake in a filing deadline or evidentiary submission can permanently damage your case."),
    ("Can a final court order be modified later?", "Yes, but only under specific circumstances. {state} courts generally require a showing of a 'substantial and material change in circumstances' that occurred after the original order was entered. Modifications are not granted simply because a party is unhappy with the original outcome."),
    ("Are court records regarding {topic} public in {state}?", "Generally, yes. Most family court filings in {state} are matters of public record. However, sensitive information such as social security numbers, bank account details, and psychological evaluations of minors are typically redacted or placed under seal by the judge."),
    ("What happens if the other party ignores the court order?", "If a party violates a valid court order concerning {topic}, you can file a Motion for Contempt in {state}. If the judge finds the party in willful contempt, penalties can include fines, payment of your attorney's fees, and even incarceration until compliance is achieved.")
]

def generate_html(state, topic):
    intro = random.choice(intros).format(state=state, topic=topic['prompt_topic'].lower())
    definition = random.choice(definitions).format(state=state, topic=topic['prompt_topic'].lower())
    procedure = random.choice(procedures).format(state=state, topic=topic['prompt_topic'].lower())
    table = random.choice(tables).format(state=state)
    
    selected_faqs = random.sample(faqs_pool, 4)
    faq_html = "<h2 style='margin-top:2rem;'>Frequently Asked Questions</h2>"
    for q, a in selected_faqs:
        faq_html += f"""
        <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="margin-bottom: 1.5rem; border-bottom: 1px solid #eee; padding-bottom: 1rem;">
            <h3 itemprop="name" style="font-size: 1.2rem; margin-bottom: 0.5rem; color: #2c3e50;">{q.format(state=state, topic=topic['prompt_topic'].lower())}</h3>
            <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                <div itemprop="text">
                    <p style="color: #4a5568;">{a.format(state=state, topic=topic['prompt_topic'].lower())}</p>
                </div>
            </div>
        </div>"""
        
    content = f"<p class='lead'>{intro}</p>{definition}{procedure}{table}{faq_html}"
    
    state_slug = state.lower().replace(" ", "-")
    slug = f"{state_slug}-{topic['slug_suffix']}"
    title = f"{state} {topic['title_suffix']}"
    desc = topic['desc_suffix'].format(state=state)
    url = f"https://familylaw.bongshai.com/states/{slug}/"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | familylaw.bongshai.com</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{url}">
    <link rel="alternate" hreflang="en-us" href="{url}">
    
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
                    <li><a href="/directory" class="nav-link">Find an Attorney</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="container mt-lg mb-xl">
        <article class="prose">
            <header class="mb-lg text-center">
                <span class="badge mb-sm">State Guide</span>
                <h1 style="margin-top: 1rem; color: #1a202c;">{title}</h1>
                <p style="color: #718096; font-size: 1.1rem; max-width: 800px; margin: 1rem auto;">{desc}</p>
            </header>
            
            <div class="ad-placeholder">AdSense Leaderboard Space</div>
            
            <div class="content" style="line-height: 1.8; color: #2d3748; font-size: 1.05rem;">
                {content}
                
                <div class="ad-placeholder">AdSense End-of-Article Space</div>
                
                <blockquote class="ymyl-disclaimer mt-lg" style="background-color: #fff3cd; border-left-color: #ffc107; padding: 1.5rem; border-radius: 4px;">
                    <strong>Disclaimer:</strong> The content on this website is for educational and informational purposes only and does not constitute professional legal advice. Laws in {state} are subject to change. Please consult with a licensed family law attorney in {state} regarding your specific situation.
                </blockquote>
            </div>
        </article>
    </main>
    <footer class="site-footer">
        <div class="container text-center">
            <p class="text-sm text-muted">&copy; 2026 Family Law Guides. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>"""
    
    dir_path = os.path.join(output_dir, slug)
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)

def build_index_page(generated_pages):
    index_html = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>State Family Law Guides | familylaw.bongshai.com</title>
    <meta name="description" content="State-by-state family law guides covering divorce, child custody, and statutes of limitations.">
    <link rel="stylesheet" href="/assets/css/index.css">
    <style>
        .states-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1rem; }}
        .state-link {{ display: block; padding: 1rem; background: var(--surface); border: 1px solid var(--border-color); border-radius: 8px; text-align: center; font-weight: 500; text-decoration: none; }}
    </style>
</head>
<body>
    <header class="site-header">
        <div class="container flex justify-between items-center">
            <a href="/" class="logo">Family Law <span>Guides</span></a>
        </div>
    </header>
    <main class="container mt-lg mb-xl">
        <h1 class="text-center">Select Your State Guide</h1>
        <div class="states-grid">
            {''.join([f'<a href="/states/{p["slug"]}" class="state-link">{p["title"]}</a>' for p in generated_pages])}
        </div>
    </main>
</body>
</html>"""
    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

generated_pages = []
for state in states:
    for topic in topics:
        generate_html(state, topic)
        state_slug = state.lower().replace(" ", "-")
        generated_pages.append({"slug": f"{state_slug}-{topic['slug_suffix']}", "title": f"{state} {topic['title_suffix']}"})

build_index_page(generated_pages)
print(f"Generated {len(generated_pages)} spintax HTML guides successfully.")
