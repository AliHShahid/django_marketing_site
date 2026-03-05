import sys, re
path = r'c:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\services_social_media.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'<h3 class="text-lg font-semibold">\s*Ready to dominate organic search\?\s*</h3>.*?<p class="mt-2 text-sm.*?">.*?</p>',
              '<h3 class="text-lg font-semibold">Ready to transform your social media presence?</h3>\n                        <p class="mt-2 text-sm text-black/70">Our social media experts will create a custom strategy to grow your following, boost engagement, and drive real business results.</p>',
              text, flags=re.IGNORECASE | re.DOTALL)
with open(path, 'w', encoding='utf-8') as f:
    f.write(text)