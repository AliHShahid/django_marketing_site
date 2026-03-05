import re
path = r'c:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\services_social_media.html.bak'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.findall(r'<h3[^>]*>(.*?)</h3>', text)
print(m)