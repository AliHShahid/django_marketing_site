import re
import sys

path = r'c:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\services_social_media.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

def repl_all(old, new):
    global text
    if old not in text:
        print(f"WARNING: Not found: '{old}'")
    else:
        text = text.replace(old, new)


repl_all("How long does it take to see results from SEO?", "Which social media platforms should my business be on?")
repl_all("Why do you need ongoing SEO?", "How often should we post on social media?")
repl_all("What is the difference between On-Page and Off-Page SEO?", "Do you create content or do we need to provide it?")
repl_all("Do you guarantee #1 rankings on Google?", "How long does it take to see results from social media marketing?")
repl_all("What is the difference between SEO and PPC?", "What is the difference between organic and paid social media?")
repl_all("How do you measure SEO success and ROI?", "How do you measure social media success and ROI?")
repl_all("Do you handle content creation for SEO?", "Will you respond to comments and messages?")
repl_all("What happens if Google updates its algorithm?", "What if we get negative comments or a social media crisis?")
repl_all("Can you fix a website that has been penalized by Google?", "Can you help with influencer partnerships?")
repl_all("How do I know what my competitors are doing?", "What is your content approval process?")
repl_all("Do you require long-term contracts for SEO services?", "Do you require long-term contracts?")

repl_all("Still have questions about SEO?", "Still have questions?")
repl_all("Explore our comprehensive guides and articles to learn more about how search engine optimization can transform your business.",
         "Explore content strategies to grow your audience and drive engagement across social platforms.")

repl_all("Ready to Dominate Search Results?", "Ready to Grow Your Social Media?")
repl_all("Turn organic traffic into your biggest growth driver. Start climbing the rankings today.",
         "Turn followers into customers. Start growing today.")
repl_all("Get a free, comprehensive SEO audit that reveals your biggest opportunities and actionable strategies to outrank your competitors.",
         "Get a free, comprehensive social media audit that reveals your biggest opportunities and actionable strategies to boost engagement.")


repl_all("Technical Audit", "Complete Audit")
repl_all("Full analysis of your website's health", "Full analysis of your social presence")

repl_all("Content Gap Analysis", "Growth Strategy")
repl_all("Identified opportunities vs competitors", "Custom plan to boost engagement")

repl_all("Keyword Strategy", "Content Ideas")
repl_all("Roadmap of high-value search terms", "Proven content frameworks")

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Migration step 3 complete.")
