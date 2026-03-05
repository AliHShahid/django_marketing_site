import re

path = r'c:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\services_social_media.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Case 1
text = text.replace('Mobile Detailing', 'TME Mobile Detailing')
text = text.replace('Detailing Company Gets +70% Lead Volume', 'Service Based Industry Gets +70% Increase in Conversions')
text = text.replace('Targeted social media increased quality appointments.', 'Car Detailer Increases Their Conversions & Appointment Bookings.')

# Case 2
text = text.replace('Real Estate (Home Buyers)', 'Legal (Eviction Law)')
text = re.sub(r'<div class="mt-2 text-3xl font-semibold">90\+</div>\s*<div class="text-xs text-white/60">Growth in Conversions</div>', 
              '<div class="mt-2 text-3xl font-semibold">+181.8%</div>\n                        <div class="text-xs text-white/60">Conversion Increment</div>', text, flags=re.IGNORECASE)
text = text.replace('90+ Monthly Seller Calls from Organic Search', '181.8% Conversion Increment in Google Ads')
text = text.replace('Content and authority growth generated pipeline-ready leads.', 'Eviction Lawyer Generates $600 Per Conversion with Targeted PPC & Landing Page Strategy')
text = text.replace('HomeLink Properties', 'Evictions Done For You')

# Case 3
text = text.replace('Healthcare (Sexologist)', 'Real Estate (Cash Home Buyer)')
text = re.sub(r'<div class="mt-2 text-3xl font-semibold">1,519%</div>\s*<div class="text-xs text-white/60">Engagement.*?</div>', 
              '<div class="mt-2 text-3xl font-semibold">+600%</div>\n                        <div class="text-xs text-white/60">Increase in Serious Leads</div>', text, flags=re.IGNORECASE | re.DOTALL)
text = text.replace('Doctor Becomes Best in Dubai with social media', 'Home Buyer Gets +600% Increase in Serious Leads')
text = text.replace('A 1,519% surge in organic traffic and monthly calls.', 'Real Estate Investor Achieves Skyrocketing Growth with Targeted PPC Strategy')
text = text.replace('Dr. Intissz', 'ASAP Outreach')

# Aggregates
text = re.sub(r'data-target="285"([^>]*>)\s*0%[\n\r\s]*</div>\s*<div class="mt-1 text-xs text-white/70">Average.*?</div', 
              r'data-target="400"\g<1>0%</div>\n                            <div class="mt-1 text-xs text-white/70">Average ROI</div', text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'data-target="60"([^>]*>)\s*0%[\n\r\s]*</div>\s*<div class="mt-1 text-xs text-white/70">Lower.*?</div', 
              r'data-target="-45"\g<1>0%</div>\n                            <div class="mt-1 text-xs text-white/70">Lower CPA</div', text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'data-target="180"([^>]*>)\s*0%[\n\r\s]*</div>\s*<div class="mt-1 text-xs text-white/70">More.*?</div', 
              r'data-target="180"\g<1>0%</div>\n                            <div class="mt-1 text-xs text-white/70">More Conversions</div', text, flags=re.IGNORECASE | re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated Case Studies successfully!")
