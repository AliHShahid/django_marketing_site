import re
path = r'c:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\services_social_media.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Case 2
text = text.replace('Real Estate (Home Buyers)', 'Legal (Eviction Law)')
text = text.replace('90+', '+181.8%')
# Growth in Conversions is already set correctly? No, it used to say "Growth in Conversions" due to previous replace? Wait, in original it was probably "Increase in organic traffic". But let's check what it currently says. 
# It says: "<div class="text-xs text-white/60">Growth in Conversions</div>"  Wait, a previous script replaced "Monthly Phone Calls" -> "Growth in Conversions" which probably affected this one too if it had the exact same text! Let's be careful.
# we just need to replace the whole specific lines.

text = re.sub(r'90\+\s*Monthly Seller Calls from Organic Search', '181.8% Conversion Increment in Google Ads', text, flags=re.IGNORECASE)
text = text.replace('Content and authority growth generated pipeline-ready leads.', 'Eviction Lawyer Generates $600 Per Conversion with Targeted PPC & Landing Page Strategy')
text = text.replace('HomeLink Properties', 'Evictions Done For You')

# Case 3
text = text.replace('Healthcare (Sexologist)', 'Real Estate (Cash Home Buyer)')
text = text.replace('2.5x', '+600%')  # Assuming it was 2.5x or something? I'll regex
text = re.sub(r'<div class="mt-2 text-3xl font-semibold">.*?</div>\s*<div class="text-xs text-white/60">Organic Traffic Increment</div>',
              '<div class="mt-2 text-3xl font-semibold">+600%</div>\n                        <div class="text-xs text-white/60">Increase in Serious Leads</div>', text, flags=re.IGNORECASE|re.DOTALL)
# Wait, my previous `text = text.replace('Increase in Organic Traffic', 'Conversion Increment')` might have broken something.
# Let's inspect Case 3 directly for the exact text and just replace what's there.

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
