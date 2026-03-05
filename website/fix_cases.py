import re
path = r'c:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\services_social_media.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Header
text = re.sub(r'Real results from <span[^>]*>organic growth</span>', 'Real results for real businesses', text, flags=re.IGNORECASE)
text = re.sub(r'See the measurable impact our social media strategies have delivered for businesses across various(\s*)industries\.', 'See how our paid advertising strategies have transformed businesses across industries into market leaders.', text, flags=re.IGNORECASE)

# Case 1
text = text.replace('Cell Phone Repair', 'Car Detailing')
text = text.replace('115+', '+650%')
text = text.replace('Monthly Phone Calls', 'Growth in Conversions')
text = text.replace('+650% Phone Calls Monthly from social media', 'From $100 to $22 Cost Per Conversion')
text = text.replace('115+ Phone Calls Monthly from social media', 'From $100 to $22 Cost Per Conversion')
text = text.replace('Local search visibility drives consistent inbound leads.', 'Car Detailer Gets +650% Increase in Bookings with Strategic Google Ads & Landing Page Optimization')
text = text.replace('FastCellRepair.ca', 'TME Mobile Detailing')

# Case 2 - checking actual names by printing if not matched
text = text.replace('Plumbing Services', 'Legal (Eviction Law)')
text = text.replace('+340%', '+181.8%')
text = text.replace('Increase in Organic Traffic', 'Conversion Increment')
text = text.replace('+181.8% Organic Traffic in 6 Months', '181.8% Conversion Increment in Google Ads')
text = text.replace('+340% Organic Traffic in 6 Months', '181.8% Conversion Increment in Google Ads')
text = text.replace('Technical social media and content strategy revived a penalized domain.', 'Eviction Lawyer Generates $600 Per Conversion with Targeted PPC & Landing Page Strategy')
text = text.replace('Technical SEO and content strategy revived a penalized domain.', 'Eviction Lawyer Generates $600 Per Conversion with Targeted PPC & Landing Page Strategy')
text = text.replace('RooterTeam.com', 'Evictions Done For You')

# Case 3
text = text.replace('E-Commerce / Retail', 'Real Estate (Cash Home Buyer)')
text = text.replace('2.8x', '+600%')
text = text.replace('Revenue Growth from social media', 'Increase in Serious Leads')
text = text.replace('+600% Revenue from Non-Branded Search', 'Home Buyer Gets +600% Increase in Serious Leads')
text = text.replace('2.8x Revenue from Non-Branded Search', 'Home Buyer Gets +600% Increase in Serious Leads')
text = text.replace('Category optimization captured high-intent shoppers.', 'Real Estate Investor Achieves Skyrocketing Growth with Targeted PPC Strategy')
text = text.replace('CozyHome.co', 'ASAP Outreach')

# Aggregate Stats
text = text.replace('Aggregate performance improvements across all social media clients', 'Aggregate performance improvements across all paid advertising clients')

text = re.sub(r'<div class="mt-2 text-2xl font-bold">285%</div>\s*<div class="text-xs text-white/70">Average.*?Increase</div>',
              '<div class="mt-2 text-2xl font-bold">400%</div>\n                                    <div class="text-xs text-white/70">Average ROI</div>', text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<div class="mt-2 text-2xl font-bold">-45%</div>\s*<div class="text-xs text-white/70">.*?CPA</div>',
              '<div class="mt-2 text-2xl font-bold">-45%</div>\n                                    <div class="text-xs text-white/70">Lower CPA</div>', text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<div class="mt-2 text-2xl font-bold">60%</div>\s*<div class="text-xs text-white/70">.*?</div>',
              '<div class="mt-2 text-2xl font-bold">-45%</div>\n                                    <div class="text-xs text-white/70">Lower CPA</div>', text, flags=re.IGNORECASE | re.DOTALL)

text = re.sub(r'<div class="mt-2 text-2xl font-bold">180%</div>\s*<div class="text-xs text-white/70">.*?Conversions</div>',
              '<div class="mt-2 text-2xl font-bold">+180%</div>\n                                    <div class="text-xs text-white/70">More Conversions</div>', text, flags=re.IGNORECASE | re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
    