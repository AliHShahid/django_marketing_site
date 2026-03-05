import re

path_out = r'c:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\services_social_media.html'

with open(path_out, 'r', encoding='utf-8') as f:
    text = f.read()

def robust_replace(old, new, count=0):
    global text
    escaped = re.escape(old)
    pattern = escaped.replace(r'\ ', r'\s+')
    matches = re.findall(pattern, text)
    if not matches:
        pass
    else:
        text = re.sub(pattern, new, text, count=count)

# Cleanups
text = re.sub(r'\bSEO\b', 'social media', text)
text = re.sub(r'\bSearch Engine Optimization\b', 'Social Media Marketing', text, flags=re.IGNORECASE)
robust_replace("social media audit and discover untapped", "social media audit to uncover opportunities")
robust_replace("social media audit to uncover issues", "social media audit to uncover opportunities")
text = re.sub(r'Get a free social media audit and discover.*?</p>', 'Get a free social media audit and strategy session.</p>', text, flags=re.DOTALL)

with open(path_out, 'w', encoding='utf-8') as f:
    f.write(text)

print("Cleanup pass done")
