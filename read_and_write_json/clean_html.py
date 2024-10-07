import re
import html

def clean_html(raw_html):
    # Remove HTML tags using a regex
    clean_text = re.sub(r'<.*?>', '', raw_html)
    
    # Decode HTML entities (e.g. &amp;, &#x2019;)
    clean_text = html.unescape(clean_text)
    
    # Replace unnecessary symbols like \n, \t etc.
    clean_text = clean_text.replace('\n', '').replace('\t', '').strip()
    
    return clean_text