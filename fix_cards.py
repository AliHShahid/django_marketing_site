import re

path = r'c:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\services_social_media.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the h3s and their paragraphs in the "Why Social Media Marketing?" section
text = re.sub(r'<h3 class="text-lg font-semibold">Community Building</h3>\s*<p class="mt-2 text-sm.*?">.*?</p>', 
              '<h3 class="text-lg font-semibold">Community Building</h3>\n                        <p class="mt-2 text-sm text-black/70">Create a loyal community around your brand. Foster meaningful connections that turn followers into advocates and customers.</p>', 
              text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<h3 class="text-lg font-semibold">Direct Customer Connection</h3>\s*<p class="mt-2 text-sm.*?">.*?</p>', 
              '<h3 class="text-lg font-semibold">Direct Customer Connection</h3>\n                        <p class="mt-2 text-sm text-black/70">Engage directly with your audience in real-time. Answer questions, gather feedback, and build genuine relationships.</p>', 
              text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<h3 class="text-lg font-semibold">Cost-Effective Marketing</h3>\s*<p class="mt-2 text-sm.*?">.*?</p>', 
              '<h3 class="text-lg font-semibold">Cost-Effective Marketing</h3>\n                        <p class="mt-2 text-sm text-black/70">Reach thousands of people for a fraction of traditional advertising costs. Get more bang for your marketing buck.</p>', 
              text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<h3 class="text-lg font-semibold">Real-Time Engagement</h3>\s*<p class="mt-2 text-sm.*?">.*?</p>', 
              '<h3 class="text-lg font-semibold">Real-Time Engagement</h3>\n                        <p class="mt-2 text-sm text-black/70">Respond instantly to trends, news, and customer interactions. Stay relevant and top-of-mind with timely content.</p>', 
              text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<h3 class="text-lg font-semibold">Measurable ROI</h3>\s*<p class="mt-2 text-sm.*?">.*?</p>', 
              '<h3 class="text-lg font-semibold">Measurable ROI</h3>\n                        <p class="mt-2 text-sm text-black/70">Track every like, share, comment, and conversion. Use data-driven insights to continuously improve your results.</p>', 
              text, flags=re.IGNORECASE | re.DOTALL)

# Fix the Services section (which currently has 'Facebook', 'Instagram', etc as headers)
# We know the specific HTML structure from previous outputs
text = re.sub(r'<h3 class="text-xl font-bold">Facebook</h3>.*?<p class="mt-3 text-sm.*?">.*?</p>',
              '<h3 class="text-xl font-bold">Social Media Management</h3>\n                            <p class="mt-3 text-sm text-black/70">Full-service management of your social media accounts including content planning, posting, and daily monitoring across all platforms.</p>',
              text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<h3 class="text-xl font-bold">Content Creation & Strategy</h3>.*?<p class="mt-3 text-sm.*?">.*?</p>',
              '<h3 class="text-xl font-bold">Content Creation & Strategy</h3>\n                            <p class="mt-3 text-sm text-black/70">Professional content creation including graphics, videos, copy, and strategic planning to engage your target audience.</p>',
              text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<h3 class="text-xl font-bold">Instagram</h3>.*?<p class="mt-3 text-sm.*?">.*?</p>',
              '<h3 class="text-xl font-bold">Paid Social Advertising</h3>\n                            <p class="mt-3 text-sm text-black/70">Strategic paid advertising campaigns on Facebook, Instagram, LinkedIn, and TikTok to amplify your reach and drive conversions.</p>',
              text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<h3 class="text-xl font-bold">LinkedIn</h3>.*?<p class="mt-3 text-sm.*?">.*?</p>',
              '<h3 class="text-xl font-bold">Community Management</h3>\n                            <p class="mt-3 text-sm text-black/70">Active engagement with your audience through responding to comments, messages, and mentions to build strong relationships.</p>',
              text, flags=re.IGNORECASE | re.DOTALL) # originally Content strategy -> Social Media Analytics? Wait! In original SEO file: Technical SEO, On-Page SEO, Link Building, Content Strategy, Local SEO, E-commerce SEO... Oh boy... 

text = re.sub(r'<h3 class="text-xl font-bold">TikTok</h3>.*?<p class="mt-3 text-sm.*?">.*?</p>',
              '<h3 class="text-xl font-bold">Influencer Partnerships</h3>\n                            <p class="mt-3 text-sm text-black/70">Connect with relevant influencers and content creators to expand your reach and build authentic brand awareness.</p>',
              text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<h3 class="text-xl font-bold">Twitter</h3>.*?<p class="mt-3 text-sm.*?">.*?</p>',
              '<h3 class="text-xl font-bold">Social Media Analytics</h3>\n                            <p class="mt-3 text-sm text-black/70">Comprehensive tracking and reporting on all key metrics to measure performance and inform strategy decisions.</p>',
              text, flags=re.IGNORECASE | re.DOTALL)

# Bottom Ready to dominate...
text = re.sub(r'<h2[^>]*>Ready to dominate organic search\?</h2>\s*<p[^>]*>Our social media experts will optimize every aspect of your online\s*presence to drive sustainable organic growth\.</p>',
              '<h2 class="mt-6 text-3xl font-bold text-white md:text-4xl">Ready to transform your social media presence?</h2>\n                    <p class="mx-auto mt-4 max-w-2xl text-base text-white/80">Our social media experts will create a custom strategy to grow your following, boost engagement, and drive real business results.</p>',
              text, flags=re.IGNORECASE | re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
