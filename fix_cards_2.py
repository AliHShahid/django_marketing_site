import re

path = r'c:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\services_social_media.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the Services section
text = re.sub(r'<h3 class="text-lg font-semibold">\s*Facebook\s*</h3>.*?<p class="mt-2 text-sm.*?">.*?</p>',
              '<h3 class="text-lg font-semibold">Social Media Management</h3>\n                        <p class="mt-2 text-sm text-black/70">Full-service management of your social media accounts including content planning, posting, and daily monitoring across all platforms.</p>',
              text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<h3 class="text-lg font-semibold">\s*Content Creation & Strategy\s*</h3>.*?<p class="mt-2 text-sm.*?">.*?</p>',
              '<h3 class="text-lg font-semibold">Content Creation & Strategy</h3>\n                        <p class="mt-2 text-sm text-black/70">Professional content creation including graphics, videos, copy, and strategic planning to engage your target audience.</p>',
              text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<h3 class="text-lg font-semibold">\s*Instagram\s*</h3>.*?<p class="mt-2 text-sm.*?">.*?</p>',
              '<h3 class="text-lg font-semibold">Paid Social Advertising</h3>\n                        <p class="mt-2 text-sm text-black/70">Strategic paid advertising campaigns on Facebook, Instagram, LinkedIn, and TikTok to amplify your reach and drive conversions.</p>',
              text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<h3 class="text-lg font-semibold">\s*LinkedIn\s*</h3>.*?<p class="mt-2 text-sm.*?">.*?</p>',
              '<h3 class="text-lg font-semibold">Community Management</h3>\n                        <p class="mt-2 text-sm text-black/70">Active engagement with your audience through responding to comments, messages, and mentions to build strong relationships.</p>',
              text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<h3 class="text-lg font-semibold">\s*TikTok\s*</h3>.*?<p class="mt-2 text-sm.*?">.*?</p>',
              '<h3 class="text-lg font-semibold">Influencer Partnerships</h3>\n                        <p class="mt-2 text-sm text-black/70">Connect with relevant influencers and content creators to expand your reach and build authentic brand awareness.</p>',
              text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<h3 class="text-lg font-semibold">\s*Twitter\s*</h3>.*?<p class="mt-2 text-sm.*?">.*?</p>',
              '<h3 class="text-lg font-semibold">Social Media Analytics</h3>\n                        <p class="mt-2 text-sm text-black/70">Comprehensive tracking and reporting on all key metrics to measure performance and inform strategy decisions.</p>',
              text, flags=re.IGNORECASE | re.DOTALL)

# Also fix the "Ready to dominate organic search?" CTA block
text = re.sub(r'<h2 class="text-3xl font-bold">\s*Ready to dominate organic search\?\s*</h2>.*?<p class="mt-4 text-lg.*?">.*?</p>',
              '<h2 class="text-3xl font-bold">\n                    Ready to transform your social media presence?\n                </h2>\n                <p class="mt-4 text-lg text-black/70">\n                    Our social media experts will create a custom strategy to grow your following, boost engagement, and drive real business results.\n                </p>',
              text, flags=re.IGNORECASE | re.DOTALL)


with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
