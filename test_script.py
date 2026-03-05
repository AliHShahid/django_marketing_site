import re
path = r'c:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\services_social_media.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'<h3 class="text-lg font-semibold">(.*?)</h3>\s*<p class="mt-2 text-sm.*?">(.*?)</p>', text, re.IGNORECASE | re.DOTALL)
for m in matches:
    print(m.group(1), ':', m.group(2))
