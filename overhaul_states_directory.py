import os
import re
import sys
import time
from groq import Groq
from bs4 import BeautifulSoup

client = Groq(api_key=os.environ.get("GROQ_API_KEY", "YOUR_API_KEY_HERE"))
base_dir = r'e:\Adsense sites\1-10\2\states'

def get_word_count(text):
    return len(re.findall(r'\b\w+\b', text))

def expand_content(state_name, attempt=0):
    prompt = f"""You are a highly experienced Family Law attorney and legal consultant. Write an extremely comprehensive, 1000+ word article about Family Law, Divorce, and Child Custody specifically in {state_name}. 
Your response MUST strictly contain ONLY raw, valid HTML (start with <p> tags, use <h2>, <h3>, <table>, <ul>, etc.). 
Do not include ```html markdown formatting, doctypes, body tags, or an <h1> tag. 
Cover state-specific statutes for {state_name}, common legal proceedings, expected attorney costs, step-by-step guidance, and FAQs. 
Write in a highly authoritative, YMYL-compliant professional tone. Make it very long, structured, and detailed."""
    
    model = "llama-3.1-8b-instant"
    
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=model,
            temperature=0.7,
        )
        content = response.choices[0].message.content
        return content.replace('```html', '').replace('```', '').strip(), True
    except Exception as e:
        err_msg = str(e)
        if "rate_limit_exceeded" in err_msg or "429" in err_msg:
            print(f"Rate limit hit on 8B model. Waiting 10 seconds...")
            time.sleep(10)
            return expand_content(state_name, attempt=attempt+1)
        print(f"Error calling Groq: {e}")
        return None, False

count = 0

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('index.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                html = file.read()
                
            # Fix AdSense Client ID
            if 'ca-pub-YOUR_CLIENT_ID' in html:
                html = html.replace('ca-pub-YOUR_CLIENT_ID', 'ca-pub-0000000000000000')
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(html)
                    
            soup = BeautifulSoup(html, 'html.parser')
            content_div = soup.find('div', class_='content')
            
            if content_div:
                words = get_word_count(content_div.get_text())
                if words < 800 or "Navigating family law in" in content_div.get_text(): # Detect spun content
                    state_name = os.path.basename(root).replace('-', ' ').title()
                    
                    print(f"Expanding: {state_name} ({words} words currently)", flush=True)
                    new_inner_html, success = expand_content(state_name)
                    
                    if new_inner_html:
                        # Replace everything inside <div class="content"> ... </div>
                        # We use regex to be safe about the replacement
                        div_pattern = re.compile(r'(<div class="content">)(.*?)(</div>\s*</article>)', re.DOTALL)
                        if div_pattern.search(html):
                            html = div_pattern.sub(rf'\1\n{new_inner_html}\n\3', html)
                            count += 1
                            with open(filepath, 'w', encoding='utf-8') as file:
                                file.write(html)
                            time.sleep(2) # pacing
                        else:
                            print(f"Could not match regex to inject HTML for {state_name}")

print(f"Overhaul complete. Expanded {count} state pages.", flush=True)
