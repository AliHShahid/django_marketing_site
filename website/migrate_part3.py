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

# Reviews:
robust_replace("SEO Case Studies", "Paid Advertising Case Studies")
robust_replace("See how our SEO strategies have transformed businesses across industries into market leaders.", "See how our paid advertising strategies have transformed businesses across industries into market leaders.")
robust_replace("Growth in Organic Traffic", "Growth in Conversions")
robust_replace("From 500 to 3,500 daily organic visitors", "From $100 to $22 Cost Per Conversion")
robust_replace("Car Detailer Gets +650% Increase in Traffic with Local SEO & GBP Optimization", "Car Detailer Gets +650% Increase in Bookings with Strategic Google Ads & Landing Page Optimization")
robust_replace("Organic Traffic Increment", "Conversion Increment")
robust_replace("Eviction Lawyer Generates 150+ Leads/mo with Targeted Content Strategy", "Eviction Lawyer Generates $600 Per Conversion with Targeted PPC & Landing Page Strategy")
robust_replace("Increase in Qualified Leads", "Increase in Serious Leads")
robust_replace("Real Estate Investor Achieves Skyrocketing Growth with Comprehensive SEO Strategy", "Real Estate Investor Achieves Skyrocketing Growth with Targeted PPC Strategy")
robust_replace("Aggregate performance improvements across all SEO clients", "Aggregate performance improvements across all paid advertising clients")

# Replace client reviews
text = re.sub(r'Partnering with Adryze for our SEO campaigns', 'partnering with KeyGrow for their Google Ads campaigns', text)
text = re.sub(r'They have a very good understanding of real estate SEO campaigns\.', 'They have a very good understanding of real estate PPC campaigns.', text)
text = re.sub(r'Adryze has been a great help in managing our SEO for two businesses that we own\.', 'KeyGrow has been a great help in managing our Google ads account for two businesses that we own.', text)
text = re.sub(r"Adryze's expertise and dedication in managing our SEO campaigns helped us achieve impressive organic rankings\.", "KeyGrow's expertise and dedication in managing our Google Ads PPC campaigns helped us achieve impressive ROI.", text)
text = re.sub(r"Adryze has been working on SEO for my website and he has done a fantastic job it has increased my organic traffic to roof\.", "KeyGrow has been working on google ads for my website and he has done a fantastic job it has increased my revenue to roof.", text)
text = re.sub(r"Adryze's communication and fresh ideas stood out\. Junaid is the best SEO expert we've worked with, boosting our business\.", "KeyGrow's communication and fresh ideas stood out. Junaid is the best Google Ads expert we've worked with, boosting our business.", text)
text = re.sub(r"Adryze fixed my technical SEO quickly and professionally\.", "KeyGrow fixed my Google Ads quickly and professionally.", text)


# Industry Expertise
robust_replace("SEO strategies for your industry", "Social media strategies for your industry")
robust_replace("Search intent and algorithms vary by industry. Our specialized SEO strategies are designed to dominate your specific landscape.",
               "Every industry has unique social media needs. Our specialized strategies are designed to resonate with your specific audience.")

robust_replace("Product category optimization, technical fixes for large catalogs, and revenue-focused targeting for online retailers.",
               "Product showcases, shoppable posts, influencer campaigns, and user-generated content strategies for online retailers.")
robust_replace("Keyword cannibalization", "High competition")
robust_replace("Faceted navigation", "Ad fatigue")
robust_replace("Product churn", "Conversion tracking")
robust_replace("Dynamic optimization", "Shopping posts")
robust_replace("Schema implementation", "Influencer partnerships")
robust_replace("Internal linking", "UGC campaigns")

robust_replace("Local map pack dominance, geo-targeted service pages, and reputation management for contractors and service providers.",
               "Before/after showcases, customer reviews, service highlights, and local community engagement for contractors and service providers.")
robust_replace("Service area pages", "Project showcases")
robust_replace("GBP optimization", "Location targeting")
robust_replace("Local link building", "Story highlights")

robust_replace("YMYL compliance, authoritative medical content, and local clinic optimization for medical practices and wellness brands.",
               "Patient education, wellness tips, service highlights, and community building for medical practices and wellness brands.")
text = re.sub(r'>YMYL compliance<', '>HIPAA compliance<', text)
robust_replace("Expert author bios", "Educational content")
robust_replace("Service siloing", "Patient testimonials")
robust_replace("Local clinic SEO", "Health tips")

robust_replace("Neighborhood pages, MLS integration SEO, and high-value property term targeting for agents, brokers, and developers.",
               "Property showcases, virtual tours, market updates, and community spotlights for agents, brokers, and developers.")
robust_replace("IDX integration", "Visual content needs")
robust_replace("Property listings", "Property showcases")
robust_replace("Neighborhood guides", "Video tours")
robust_replace("Local link outreach", "Market insights")


robust_replace("Practice area dominance, thought leadership content, and high-trust citations for law firms and attorneys.",
               "Thought leadership, case results, legal insights, and community engagement for law firms and attorneys.")
robust_replace("Practice area silos", "Thought leadership")
robust_replace("Attorney bios", "Case results")
robust_replace("High-authority links", "LinkedIn focus")

robust_replace("Feature page optimization, alternative-to comparisons, and top-of-funnel resource hubs for software companies.",
               "Product updates, feature highlights, customer success stories, and industry thought leadership for software companies.")
robust_replace("Comparison pages", "Product demos")
robust_replace("Resource hubs", "Customer stories")
robust_replace("Use-case targeting", "Educational content")


# FAQs
robust_replace("Common SEO questions answered", "Common social media questions answered")
robust_replace("Everything you need to know about our SEO services and search engine optimization in general.", "Everything you need to know about our social media marketing services.")

robust_replace("What is SEO and how does it benefit my business?", "What is social media marketing and how does it benefit my business?")
text = re.sub(r'SEO stands for Search Engine Optimization.*?long-term visibility\.',
              "Social media marketing is the practice of using platforms like Facebook, Instagram, LinkedIn, and TikTok to connect with your audience, build brand awareness, drive website traffic, and generate leads. It benefits your business by providing direct access to billions of potential customers, enabling two-way communication, building brand loyalty, and delivering measurable ROI through both organic and paid strategies.", text, flags=re.DOTALL)

robust_replace("How long does it take to see results from SEO?", "Which social media platforms should my business be on?")
robust_replace("Why do you need ongoing SEO?", "How often should we post on social media?")
robust_replace("What is the difference between On-Page and Off-Page SEO?", "Do you create content or do we need to provide it?")
robust_replace("Do you guarantee #1 rankings on Google?", "How long does it take to see results from social media marketing?")
robust_replace("What is the difference between SEO and PPC?", "What is the difference between organic and paid social media?")
robust_replace("How do you measure SEO success and ROI?", "How do you measure social media success and ROI?")
robust_replace("Do you handle content creation for SEO?", "Will you respond to comments and messages?")
robust_replace("What happens if Google updates its algorithm?", "What if we get negative comments or a social media crisis?")
robust_replace("Can you fix a website that has been penalized by Google?", "Can you help with influencer partnerships?")
robust_replace("How do I know what my competitors are doing?", "What is your content approval process?")
robust_replace("Do you require long-term contracts for SEO services?", "Do you require long-term contracts?")

robust_replace("Still have questions about SEO?", "Still have questions?")
robust_replace("Explore our comprehensive guides and articles to learn more about how search engine optimization can transform your business.",
               "Explore content strategies to grow your audience and drive engagement across social platforms.")

robust_replace("Ready to Dominate Search Results?", "Ready to Grow Your Social Media?")
robust_replace("Turn organic traffic into your biggest growth driver. Start climbing the rankings today.",
               "Turn followers into customers. Start growing today.")
robust_replace("Get a free, comprehensive SEO audit that reveals your biggest opportunities and actionable strategies to outrank your competitors.",
               "Get a free, comprehensive social media audit that reveals your biggest opportunities and actionable strategies to boost engagement.")

robust_replace("Technical Audit", "Complete Audit")
robust_replace("Full analysis of your website's health", "Full analysis of your social presence")

robust_replace("Content Gap Analysis", "Growth Strategy")
robust_replace("Identified opportunities vs competitors", "Custom plan to boost engagement")

robust_replace("Keyword Strategy", "Content Ideas")
robust_replace("Roadmap of high-value search terms", "Proven content frameworks")

robust_replace(">Get Your Free SEO Audit<", ">Get Your Free Social Media Audit<")

# At the end, KeyGrow
robust_replace("© 2026 Adryze LLC", "© 2026 KeyGrow LLC")

with open(path_out, 'w', encoding='utf-8') as f:
    f.write(text)

print("Pass 3 done")
