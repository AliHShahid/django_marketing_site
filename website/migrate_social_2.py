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


# --- PROCESS ---
repl_all("How we deliver SEO success", "How we deliver social media success")
text = re.sub(r'Our proven 5-step process ensures your website climbs the rankings.*?over time\.',
              'Our proven 5-step process ensures your social media presence drives real business results from day one and continues to grow over time.', text, flags=re.DOTALL)

repl_all("Discovery & Audit", "Discovery & Audit")
text = re.sub(r'We analyze your current rankings, website architecture, competitor strategies, and target audience to identify the biggest opportunities\.',
              'We analyze your current social media presence, competitor strategies, target audience, and business goals to understand your unique situation and opportunities.', text)

repl_all("Keyword & Content Strategy", "Strategy Development")
text = re.sub(r'We identify high-value search terms and create a comprehensive roadmap for content that will capture targeted organic traffic\.',
              'We create a comprehensive social media strategy including content pillars, posting schedule, engagement tactics, and growth objectives tailored to your brand.', text)
repl_all("Keyword research report", "Content strategy document")
repl_all("Content gap analysis", "Editorial calendar template")
repl_all("Topic cluster mapping", "Brand voice guidelines")
repl_all("ROI projections", "KPI framework")

repl_all("Technical & On-Page SEO", "Content Production")
text = re.sub(r'Our team fixes all technical issues, optimizes site speed, and ensures your pages are perfectly structured for search engines\.',
              'Our creative team produces high-quality content including graphics, videos, copy, and stories designed to engage your audience and drive results.', text)
repl_all("Technical fix implementation", "Custom graphics & videos")
repl_all("Meta tag optimization", "Engaging copy & captions")
repl_all("Schema markup", "Hashtag research")
repl_all("Internal linking", "Content library setup")

repl_all("Link Building & Authority", "Campaign Launch")
text = re.sub(r'We execute targeted outreach campaigns to acquire high-quality, relevant backlinks that boost your domain authority\.',
              'We launch your social media campaigns with strategic posting, community engagement, and paid advertising to maximize reach and impact from day one.', text)
repl_all("Outreach strategy", "Content posting schedule")
repl_all("Digital PR campaigns", "Community management")
repl_all("Guest post placements", "Paid ad campaigns")
repl_all("Authority tracking", "Performance monitoring")

repl_all("Monitor & Optimize", "Monitor & Optimize")
text = re.sub(r'We continuously track keyword movements, traffic quality, and conversion metrics to refine and scale your \.',
              'We continuously track performance, test new content, engage with your community, and optimize strategy to ensure consistent growth and results.', text) # Not an exact match for the original text just based on my memory, wait let's use broad replacements.
repl_all("We continuously track keyword movements, traffic quality, and conversion metrics to refine and scale your SEO strategy.",
         "We continuously track performance, test new content, engage with your community, and optimize strategy to ensure consistent growth and results.")

# Process small deliverable labels
repl_all("Ranking reports", "Weekly performance reviews")
repl_all("Traffic analysis", "Monthly strategy reports")
repl_all("Conversion tracking", "A/B testing insights")
repl_all("Next steps roadmap", "Growth recommendations")

repl_all("Response time", "Response time")
repl_all("Technical review", "Community engagement")

# --- PLATFORMS ---
repl_all("Our professional SEO tools", "Our professional social media tools")
repl_all("We leverage the most powerful enterprise SEO platforms to drive exceptional results for your brand.",
         "We leverage the most powerful social media platforms and management tools to drive exceptional results for your brand.")
repl_all("SEMrush", "Meta")
repl_all("Ahrefs", "Meta Business Suite")
repl_all("Screaming Frog", "Facebook Ads Manager")
repl_all("Google Search Console", "Instagram Creator Studio")
repl_all("Majestic", "LinkedIn Campaign Manager")
repl_all("Surfer SEO", "TikTok Ads Manager")


# --- ENGAGEMENT GROWTH ---
repl_all("Organic Results", "Engagement Growth")
repl_all("Skyrocket your organic traffic", "Skyrocket your social media engagement")
repl_all("Dominate the first page of Google to capture high-intent users and drive consistent, scalable revenue for your business.",
         "Turn passive followers into an active, engaged community that amplifies your brand and drives real business results.")

repl_all("Keyword Dominance", "Viral Content Strategy")
repl_all("Rank #1 for the most valuable search terms in your industry, capturing users at the exact moment they are ready to buy.",
         "Create content designed to resonate, engage, and spread organically across your target audience.")

repl_all("Conversion Optimization", "Engagement Optimization")
repl_all("We do not just drive traffic; we optimize your pages to turn those visitors into qualified leads and paying customers.",
         "Maximize likes, comments, and shares with scientifically-tested engagement tactics.")

repl_all("Content Authority", "Audience Growth")
repl_all("Establish your brand as the go-to resource in your space with comprehensive, expertly crafted content that Google loves.",
         "Strategic follower acquisition that brings real, engaged users interested in your brand.")

repl_all("Technical Excellence", "Hashtag Mastery")
repl_all("Build a perfectly optimized digital foundation that loads instantly and provides a flawless experience across all devices.",
         "Research and implement high-performing hashtags that expand your reach exponentially.")

repl_all("Link Profile Growth", "Community Building")
repl_all("Develop a powerful, natural backlink profile that signals authority to search engines and protects against algorithm updates.",
         "Foster authentic connections that turn followers into a loyal, engaged community.")


# Fake UI mock replacements
repl_all("organic traffic", "engagement")
repl_all("+385%", "+385%")

# --- REVIEWS ---
# I'll leave the reviews mostly untouched but change SEO to Social Media or PPC if mentioned, wait, the user prompt specifically had Paid Advertising Case Studies & PPC reviews for some reason.
repl_all("Google Ads campaigns", "Social Media campaigns")
repl_all("real estate PPC campaigns", "real estate social media campaigns")
repl_all("Google Ads PPC campaigns", "Social Media campaigns")
repl_all("google ads account", "social media accounts")

# --- INDUSTRIES ---
repl_all("SEO strategies for your industry", "Social media strategies for your industry")
repl_all("Search intent and algorithms vary by industry. Our specialized SEO strategies are designed to dominate your specific landscape.",
         "Every industry has unique social media needs. Our specialized strategies are designed to resonate with your specific audience.")

# E-commerce 
repl_all("Product category optimization, technical fixes for large catalogs, and revenue-focused targeting for online retailers.",
         "Product showcases, shoppable posts, influencer campaigns, and user-generated content strategies for online retailers.")
repl_all("Keyword cannibalization", "High competition")
repl_all("Faceted navigation", "Ad fatigue")
repl_all("Product churn", "Conversion tracking")
repl_all("Dynamic optimization", "Shopping posts")
repl_all("Schema implementation", "Influencer partnerships")
repl_all("Internal linking", "UGC campaigns")

# Home Services 
repl_all("Local map pack dominance, geo-targeted service pages, and reputation management for contractors and service providers.",
         "Before/after showcases, customer reviews, service highlights, and local community engagement for contractors and service providers.")
repl_all("Service area pages", "Project showcases")
repl_all("GBP optimization", "Location targeting")
repl_all("Local link building", "Story highlights")

# Healthcare
repl_all("YMYL compliance, authoritative medical content, and local clinic optimization for medical practices and wellness brands.",
         "Patient education, wellness tips, service highlights, and community building for medical practices and wellness brands.")
repl_all("YMYL compliance", "HIPAA compliance")
repl_all("Expert author bios", "Educational content")
repl_all("Service siloing", "Patient testimonials")
repl_all("Local clinic SEO", "Health tips")

# Real Estate 
repl_all("Neighborhood pages, MLS integration SEO, and high-value property term targeting for agents, brokers, and developers.",
         "Property showcases, virtual tours, market updates, and community spotlights for agents, brokers, and developers.")
repl_all("IDX integration", "Visual content needs")
repl_all("Property listings", "Property showcases")
repl_all("Neighborhood guides", "Video tours")
repl_all("Local link outreach", "Market insights")

# Legal 
repl_all("Practice area dominance, thought leadership content, and high-trust citations for law firms and attorneys.",
         "Thought leadership, case results, legal insights, and community engagement for law firms and attorneys.")
repl_all("Practice area silos", "Thought leadership")
repl_all("Attorney bios", "Case results")
repl_all("High-authority links", "LinkedIn focus")

# SaaS 
repl_all("Feature page optimization, alternative-to comparisons, and top-of-funnel resource hubs for software companies.",
         "Product updates, feature highlights, customer success stories, and industry thought leadership for software companies.")
repl_all("Comparison pages", "Product demos")
repl_all("Resource hubs", "Customer stories")
repl_all("Use-case targeting", "Educational content")

# --- FAQ ---
repl_all("Common SEO questions answered", "Common social media questions answered")
repl_all("Everything you need to know about our SEO services and search engine optimization in general.",
         "Everything you need to know about our social media marketing services.")

repl_all("What is SEO and how does it benefit my business?", "What is social media marketing and how does it benefit my business?")
text = re.sub(r'SEO stands for Search Engine Optimization.*?long-term visibility\.',
              "Social media marketing is the practice of using platforms like Facebook, Instagram, LinkedIn, and TikTok to connect with your audience, build brand awareness, drive website traffic, and generate leads. It benefits your business by providing direct access to billions of potential customers, enabling two-way communication, building brand loyalty, and delivering measurable ROI through both organic and paid strategies.", text, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Migration step 2 complete.")
