import re

path_in = r'c:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\services_social_media.html.bak'
path_out = r'c:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\services_social_media.html'

with open(path_in, 'r', encoding='utf-8') as f:
    text = f.read()

def robust_replace(old, new, count=0):
    global text
    # Convert old string into a regex that tolerates any whitespace between words
    escaped = re.escape(old)
    # Replace escaped spaces with \s+ so it matches newlines or multiple spaces
    pattern = escaped.replace(r'\ ', r'\s+')
    
    matches = re.findall(pattern, text)
    if not matches:
        pass # print(f"WARNING: Not found: '{old}'")
    else:
        text = re.sub(pattern, new, text, count=count)

# --- General ---
robust_replace("SEO Services | Adryze", "Social Media Marketing | KeyGrow")
robust_replace("Adryze", "KeyGrow")
robust_replace("Professional SEO Services", "Social Media Marketing")

text = re.sub(
    r'Dominate Google<br[^>]*>with\s*<span[^>]*>proven SEO</span>\s*strategies',
    'Turn social media into<br class="hidden sm:block" /> <span class="text-[var(--orange)]">engaged communities</span>',
    text, flags=re.IGNORECASE | re.DOTALL
)

text = re.sub(
    r'Stop losing customers to competitors.*?business growth\.',
    'Stop posting into the void. We create scroll-stopping content, build engaged audiences, and run paid campaigns that drive real business results across Facebook, Instagram, LinkedIn, and TikTok.',
    text, flags=re.IGNORECASE | re.DOTALL
)

robust_replace("First Page Rankings in 90 Days", "450% Engagement Growth")
robust_replace("White-Hat SEO Only", "Multi-Platform Strategy")
robust_replace("Guaranteed ROI Growth", "Content + Paid Ads")
robust_replace("Our SEO Performance", "Our Social Media Performance")
robust_replace("Get Free SEO Audit →", "Get Free Social Media Audit →")


# Stats replacements (we regex the whole block or just the text)
text = re.sub(
    r'<div class="text-xl font-semibold count-num" data-target="500" data-suffix="\+">0\+</div>\s*<div class="text-xs text-white/60">Keywords Ranked #1</div>',
    '<div class="text-xl font-semibold">15M+</div>\n                                <div class="text-xs text-white/60">Total Reach</div>',
    text
)
text = re.sub(
    r'<div class="text-xl font-semibold count-num" data-target="285" data-suffix="%">0%</div>\s*<div class="text-xs text-white/60">Avg Traffic Increase</div>',
    '<div class="text-xl font-semibold count-num" data-target="450" data-suffix="%">0%</div>\n                                <div class="text-xs text-white/60">Avg. Engagement Growth</div>',
    text
)
text = re.sub(
    r'<div class="text-xl font-semibold">90 Days</div>\s*<div class="text-xs text-white/60">To First Page Results</div>',
    '<div class="text-xl font-semibold count-num" data-target="500" data-suffix="K+">0</div>\n                                <div class="text-xs text-white/60">Content Pieces Created</div>',
    text
)
text = re.sub(
    r'<div class="text-xl font-semibold count-num" data-target="150" data-suffix="\+">0\+</div>\s*<div class="text-xs text-white/60">Websites SEO Managed</div>',
    '<div class="text-xl font-semibold count-num" data-target="98" data-suffix="%">0%</div>\n                                <div class="text-xs text-white/60">Client Retention</div>',
    text
)

robust_replace("SEO services we provide:", "Platforms we manage:")
robust_replace(">Technical SEO<", ">Facebook<")
robust_replace(">Link Building<", ">Instagram<")
robust_replace(">Content Strategy<", ">LinkedIn<")
robust_replace(">Local SEO<", ">TikTok<")
robust_replace(">E-commerce SEO<", ">Twitter<")
robust_replace(">Mobile SEO<", ">Pinterest<")

# --- Why Section ---
robust_replace("Why SEO?", "Why Social Media Marketing?")
text = re.sub(
    r'The foundation of <span class="text-\[var\(--orange\)\]">sustainable growth</span>',
    'Connect with your audience <span class="text-[var(--orange)]">where they spend time</span>',
    text, flags=re.DOTALL
)
text = re.sub(
    r'Search Engine Optimization builds long-term visibility.*?ongoing ad costs\.',
    'Social media marketing is no longer optional. With billions of users across platforms, it is the most direct way to build relationships, drive engagement, and grow your business.',
    text, flags=re.DOTALL
)

robust_replace("Sustainable Growth", "Brand Awareness")
text = re.sub(
    r'Build organic rankings that compound over time\. Unlike\s*PPC,\s*SEO continues working even when you stop investing\.',
    'Increase your visibility and reach millions of potential customers. Build brand recognition that translates to trust and loyalty.',
    text, flags=re.DOTALL
)

robust_replace("Qualified Organic Traffic", "Community Building")
text = re.sub(
    r'Attract users who are actively searching for your\s*products\s*or services, resulting in higher conversion rates\.',
    'Create a loyal community around your brand. Foster meaningful connections that turn followers into advocates and customers.',
    text, flags=re.DOTALL
)

robust_replace("Authority Building", "Direct Customer Connection")
text = re.sub(
    r'Establish your brand as an industry leader through\s*high-quality content and authoritative backlinks\.',
    'Engage directly with your audience in real-time. Answer questions, gather feedback, and build genuine relationships.',
    text, flags=re.DOTALL
)

robust_replace("Long-Term ROI", "Cost-Effective Marketing")
text = re.sub(
    r'While paid ads stop working when you stop paying, SEO\s*provides ongoing returns on your investment\.',
    'Reach thousands of people for a fraction of traditional advertising costs. Get more bang for your marketing buck.',
    text, flags=re.DOTALL
)

robust_replace("Brand Credibility", "Real-Time Engagement")
text = re.sub(
    r'Ranking at the top of Google results automatically\s*builds\s*trust and credibility with potential customers\.',
    'Respond instantly to trends, news, and customer interactions. Stay relevant and top-of-mind with timely content.',
    text, flags=re.DOTALL
)

robust_replace("Compound Returns", "Measurable ROI")
text = re.sub(
    r'Every piece of optimized content and earned backlink\s*adds\s*to your site\'s overall ranking power over time\.',
    'Track every like, share, comment, and conversion. Use data-driven insights to continuously improve your results.',
    text, flags=re.DOTALL
)

robust_replace("Ready to dominate search results?", "Ready to grow your social media presence?")
robust_replace("Get a free technical SEO audit and growth strategy session.", "Get a free social media audit and strategy session.")


# --- Middle stuff ---
robust_replace("How SEO Works", "How Social Media Marketing Works")
robust_replace("Step 1. Technical Audit", "Step 1. Strategy & Planning")
robust_replace("Comprehensive analysis of your website's technical health and performance.", "Define goals, target audience, platforms, and content pillars")

robust_replace("Step 2. Keyword Strategy", "Step 2. Content Creation")
robust_replace("Identify high-value keywords your target audience is searching for.", "Develop engaging posts, graphics, videos, and stories")

robust_replace("Step 3. On-Page Optimization", "Step 3. Community Management")
robust_replace("Optimize website structure, content, and meta tags for readability.", "Monitor, respond to comments, messages, and mentions")

robust_replace("Step 4. Content Creation", "Step 4. Paid Advertising")
robust_replace("Develop authoritative content that answers user queries and builds trust.", "Amplify reach with targeted ads and sponsored content")

robust_replace("Step 5. Link Building", "Step 5. Analytics & Optimization")
robust_replace("Acquire high-quality backlinks from respected industry domains.", "Track performance, refine strategy, and scale what works")

robust_replace("+280%<br />\n                                    <span class=\"block text-xs font-normal text-black/60 mt-1\">\n                                        Organic Traffic", 
               "+280%<br />\n                                    <span class=\"block text-xs font-normal text-black/60 mt-1\">\n                                        Engagement")
robust_replace("Organic Traffic", "Engagement")

robust_replace("+450%<br />\n                                    <span class=\"block text-xs font-normal text-black/60 mt-1\">\n                                        Lead Quality", 
               "+450%<br />\n                                    <span class=\"block text-xs font-normal text-black/60 mt-1\">\n                                        Followers")
robust_replace("Lead Quality", "Followers")

robust_replace("Overall ROI", "ROI")

# What is SEO
robust_replace("What is Search Engine Optimization?", "What is Social Media Marketing?")
robust_replace("Understanding modern SEO", "Understanding social media marketing")
text = re.sub(
    r'SEO \(Search Engine Optimization\) is the practice.*?algorithm\.',
    'Social media marketing is the practice of using social platforms like Facebook, Instagram, LinkedIn, and TikTok to connect with your audience, build brand awareness, drive website traffic, and increase sales.\n<br><br>\nUnlike traditional advertising, social media enables two-way communication between brands and customers.',
    text, flags=re.DOTALL | re.IGNORECASE
)
text = re.sub(
    r'Unlike paid advertising where traffic stops.*?industry leader\.',
    'Successful social media marketing requires consistent effort, strategic content planning, and continuous optimization. Our team manages every aspect from content creation to community management, paid advertising, and analytics to ensure your social presence drives real business results.',
    text, flags=re.DOTALL | re.IGNORECASE
)

# 4 points
robust_replace("Increase Visibility", "Build Brand Awareness")
robust_replace("Be found when customers are actively searching for your services", "Reach millions of potential customers on platforms they use daily")
robust_replace("Drive Qualified Traffic", "Drive Website Traffic")
robust_replace("Attract visitors with high intent to purchase or convert", "Turn social engagement into website visits and conversions")
robust_replace("Build Trust & Authority", "Generate Quality Leads")
robust_replace("Ranking high signals credibility to your target audience", "Connect with prospects actively interested in your products")
robust_replace("Compounds over time for increasingly better ROI", "Build relationships that turn customers into brand advocates")
robust_replace("Sustainable Growth", "Increase Customer Loyalty")

# Mistakes
robust_replace("Common SEO Mistakes", "Common Social Media Mistakes")
robust_replace("Avoid these costly SEO mistakes", "Avoid these costly social media mistakes")
text = re.sub(
    r'Research shows that many businesses waste countless.*?technical foundations\.',
    'Research shows that businesses waste countless hours on social media without seeing results. Posting randomly without a strategy, ignoring your audience, or using the wrong platforms can kill engagement and damage your brand reputation.',
    text, flags=re.DOTALL | re.IGNORECASE
)
text = re.sub(
    r'One of the biggest mistakes is treating SEO.*?wasted budget\.',
    'One of the biggest mistakes is inconsistent posting. Studies show inconsistent brands lose up to 60% of their followers within months. Similarly, poor-quality visuals can reduce engagement by 65%, while ignoring comments can decrease reach by 50% as algorithms penalize inactive accounts.',
    text, flags=re.DOTALL | re.IGNORECASE
)
text = re.sub(
    r'Professional SEO management eliminates these risks.*?business results\.',
    'Professional social media management eliminates these risks through strategic planning, consistent execution, and active community engagement. Our team knows how to create content that resonates, engage meaningfully with your audience, and track what actually drives business results.',
    text, flags=re.DOTALL | re.IGNORECASE
)
robust_replace("Top 5 SEO Mistakes", "Top 5 Social Media Mistakes")

# Mistake 1
robust_replace("Poor Mobile Experience", "Inconsistent Posting")
robust_replace("-60%", "-60%")
robust_replace("Slow load times and bad mobile UX kill search rankings instantly", "Irregular posting schedule confuses followers and kills algorithm reach")
# Mistake 2
robust_replace("Thin Content", "No Strategy")
robust_replace("-55%", "-55%")
robust_replace("Creating superficial content that doesn't answer user intent", "Random posts without goals or planning waste time and resources")
# Mistake 3
robust_replace("Ignoring Technical SEO", "Ignoring Comments")
robust_replace("-50%", "-50%")
robust_replace("Broken links, poor site architecture, and indexation issues", "Not responding to followers reduces engagement and algorithm visibility")
# Mistake 4
robust_replace("Bad Link Building", "Wrong Platforms")
robust_replace("-45%", "-45%")
robust_replace("Buying cheap links that result in Google penalties", "Being on platforms where your audience is not active")
# Mistake 5
robust_replace("No Local Optimization", "Poor Visual Content")
robust_replace("-65%", "-65%")
robust_replace("Missing out on high-intent local customers", "Low-quality images and videos drastically reduce engagement")

robust_replace("of SEO efforts", "of social media efforts")

# Services
robust_replace("Complete search engine optimization services", "Complete social media marketing services")
robust_replace("From audit to execution, we handle every aspect of your SEO strategy", "From strategy to execution, we handle every aspect of your social media presence")

robust_replace("Technical SEO", "Social Media Management") # 1st service title
text = re.sub(r'Comprehensive audits, site speed optimization, schema markup, and structural improvements to ensure search engines can easily crawl and index your site\.',
              'Full-service management of your social media accounts including content planning, posting, and daily monitoring across all platforms.', text)
robust_replace("Site speed optimization", "Content calendar planning")
robust_replace("Core Web Vitals", "Daily posting & scheduling")
robust_replace("Schema markup implementation", "Profile optimization")
robust_replace("Crawlability fixes", "Performance monitoring")

robust_replace("On-Page SEO", "Content Creation & Strategy")
text = re.sub(r'Strategic optimization of title tags, meta descriptions, headers, and content to align with search intent and target high-value keywords\.',
              'Professional content creation including graphics, videos, copy, and strategic planning to engage your target audience.', text)
robust_replace("Keyword research & mapping", "Custom graphics & videos")
robust_replace("Meta tag optimization", "Copywriting & captions")
robust_replace("Content gap analysis", "Content strategy development")
robust_replace("Internal linking strategy", "Brand voice consistency")

robust_replace("Link Building", "Paid Social Advertising") # Wait we already replaced Link Building -> Instagram at the top... ah! Let's be careful. Actually we used >Link Building< for the pill. Here it's <h3>Link Building</h3> or similar. Let's just do text replacement.
robust_replace("Acquiring high-authority backlinks through digital PR, guest posting, and broken link building to boost your domain authority.",
               "Strategic paid advertising campaigns on Facebook, Instagram, LinkedIn, and TikTok to amplify your reach and drive conversions.")
robust_replace("Digital PR campaigns", "Campaign strategy & setup")
robust_replace("Guest posting", "Audience targeting & research")
robust_replace("Broken link building", "Ad creative development")
robust_replace("Unlinked brand mentions", "Ongoing optimization")

robust_replace("<h3>Local SEO</h3>", "<h3>Community Management</h3>") # to avoid changing the button Local SEO
robust_replace("Optimization of Google Business Profile, local citations, and localized content to dominate search results in your specific geographic area.",
               "Active engagement with your audience through responding to comments, messages, and mentions to build strong relationships.")
robust_replace("Google Business optimization", "Comment & DM responses")
robust_replace("Local citation building", "Reputation monitoring")
robust_replace("Review management", "Crisis management")
robust_replace("Localized content strategy", "Engagement analytics")

robust_replace("<h3>E-commerce SEO</h3>", "<h3>Influencer Partnerships</h3>")
robust_replace("Specialized optimization for online stores, including category page SEO, product descriptions, and faceted navigation optimization.",
               "Connect with relevant influencers and content creators to expand your reach and build authentic brand awareness.")
robust_replace("Category optimization", "Influencer identification")
robust_replace("Product page SEO", "Partnership negotiation")
robust_replace("Faceted navigation fixes", "Campaign coordination")
robust_replace("Structured data for products", "Performance tracking")

robust_replace("Content Marketing", "Social Media Analytics")
robust_replace("Creating data-driven blog posts, guides, and resources that attract top-of-funnel traffic and establish your brand authority.",
               "Comprehensive tracking and reporting on all key metrics to measure performance and inform strategy decisions.")
robust_replace("Topic cluster strategy", "Custom dashboards")
robust_replace("Blog content creation", "Monthly performance reports")
robust_replace("Evergreen guides", "Competitor benchmarking")
robust_replace("Content refreshing", "ROI tracking")

robust_replace("Ready to dominate the search results?", "Ready to transform your social media presence?")
robust_replace("Our SEO experts will create a custom strategy to skyrocket", "Our social media experts will create a custom strategy to grow")
robust_replace("your organic traffic and grow your business.", "your following, boost engagement, and drive real business results.")


with open(path_out, 'w', encoding='utf-8') as f:
    f.write(text)

print("Pass 1 done")
