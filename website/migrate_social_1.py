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


# --- GENERAL ---
repl_all("SEO Services | Adryze", "Social Media Marketing | KeyGrow")
repl_all("Adryze", "KeyGrow")
repl_all("Professional SEO Services", "Social Media Marketing")

# --- HERO ---
text = re.sub(
    r'Dominate Google<br\s*class="hidden sm:block"\s*/>with <span class="text-\[var\(--orange\)\]">proven SEO</span>\s*strategies',
    r'Turn social media into<br class="hidden sm:block" /><span class="text-[var(--orange)]">engaged communities</span>',
    text
)
text = re.sub(
    r'Stop losing customers to competitors[^\.]*\. Our data-driven SEO strategies deliver sustainable\s*rankings, qualified organic traffic, and measurable business growth\.',
    'Stop posting into the void. We create scroll-stopping content, build engaged audiences, and run paid campaigns that drive real business results across Facebook, Instagram, LinkedIn, and TikTok.',
    text, flags=re.DOTALL
)

repl_all("First Page Rankings in 90 Days", "450% Engagement Growth")
repl_all("White-Hat SEO Only", "Multi-Platform Strategy")
repl_all("Guaranteed ROI Growth", "Content + Paid Ads")
repl_all("Get Free SEO Audit", "Get Free Social Media Audit")
repl_all("Our SEO Performance", "Our Social Media Performance")

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

repl_all("SEO services we provide:", "Platforms we manage:")
text = re.sub(r'>Technical SEO<', '>Facebook<', text, count=1)
text = re.sub(r'>Link Building<', '>Instagram<', text, count=1)
text = re.sub(r'>Content Strategy<', '>LinkedIn<', text, count=1)
text = re.sub(r'>Local SEO<', '>TikTok<', text, count=1)
text = re.sub(r'>E-commerce SEO<', '>Twitter<', text, count=1)
text = re.sub(r'>Mobile SEO<', '>Pinterest<', text, count=1)

# --- WHY SECTION ---
repl_all("Why SEO?", "Why Social Media Marketing?")
text = re.sub(
    r'The foundation of <span class="text-\[var\(--orange\)\]">sustainable growth</span>',
    r'Connect with your audience <span class="text-[var(--orange)]">where they spend time</span>',
    text
)
text = re.sub(
    r'Search Engine Optimization builds long-term visibility.*?ongoing ad costs\.',
    'Social media marketing is no longer optional. With billions of users across platforms, it is the most direct way to build relationships, drive engagement, and grow your business.',
    text, flags=re.DOTALL
)

repl_all("Sustainable Growth", "Brand Awareness")
text = re.sub(r'Build organic rankings that compound over time\. Unlike\s*PPC,\s*SEO continues working even when you stop investing\.', 
              'Increase your visibility and reach millions of potential customers. Build brand recognition that translates to trust and loyalty.', text, flags=re.DOTALL)
# Adding 5.17B users, etc. to hover cards could be tricky but it's optional.

repl_all("Qualified Organic Traffic", "Community Building")
text = re.sub(r'Attract users who are actively searching for your\s*products\s*or services, resulting in higher conversion rates\.', 
              'Create a loyal community around your brand. Foster meaningful connections that turn followers into advocates and customers.', text, flags=re.DOTALL)

repl_all("Authority Building", "Direct Customer Connection")
text = re.sub(r'Establish your brand as an industry leader through\s*high-quality content and authoritative backlinks\.', 
              'Engage directly with your audience in real-time. Answer questions, gather feedback, and build genuine relationships.', text, flags=re.DOTALL)

repl_all("Long-Term ROI", "Cost-Effective Marketing")
text = re.sub(r'While paid ads stop working when you stop paying, SEO\s*provides ongoing returns on your investment\.', 
              'Reach thousands of people for a fraction of traditional advertising costs. Get more bang for your marketing buck.', text, flags=re.DOTALL)

repl_all("Brand Credibility", "Real-Time Engagement")
text = re.sub(r'Ranking at the top of Google results automatically\s*builds\s*trust and credibility with potential customers\.', 
              'Respond instantly to trends, news, and customer interactions. Stay relevant and top-of-mind with timely content.', text, flags=re.DOTALL)

repl_all("Compound Returns", "Measurable ROI")
text = re.sub(r'Every piece of optimized content and earned backlink\s*adds\s*to your site\'s overall ranking power over time\.', 
              'Track every like, share, comment, and conversion. Use data-driven insights to continuously improve your results.', text, flags=re.DOTALL)

repl_all("Ready to dominate search results?", "Ready to grow your social media presence?")
repl_all("Get a free technical SEO audit and growth strategy session.", "Get a free social media audit and strategy session.")

# --- HOW IT WORKS ---
repl_all("How SEO Works", "How Social Media Marketing Works")

repl_all("Step 1. Technical Audit", "Step 1. Strategy & Planning")
text = re.sub(r'Comprehensive analysis of your website\'s\s*technical health and performance.', 
              'Define goals, target audience, platforms, and content pillars', text, flags=re.DOTALL)

repl_all("Step 2. Keyword Strategy", "Step 2. Content Creation")
text = re.sub(r'Identify high-value keywords your target\s*audience is searching for.', 
              'Develop engaging posts, graphics, videos, and stories', text, flags=re.DOTALL)

repl_all("Step 3. On-Page Optimization", "Step 3. Community Management")
text = re.sub(r'Optimize website structure, content, and\s*meta tags for readability.', 
              'Monitor, respond to comments, messages, and mentions', text, flags=re.DOTALL)

repl_all("Step 4. Content Creation", "Step 4. Paid Advertising")
text = re.sub(r'Develop authoritative content that\s*answers user queries and builds trust.', 
              'Amplify reach with targeted ads and sponsored content', text, flags=re.DOTALL)

repl_all("Step 5. Link Building", "Step 5. Analytics & Optimization")
text = re.sub(r'Acquire high-quality backlinks from\s*respected industry domains.', 
              'Track performance, refine strategy, and scale what works', text, flags=re.DOTALL)

repl_all("+280%<br/>Organic Traffic", "+280%<br/>Engagement")
repl_all("+450%<br/>Lead Quality", "+450%<br/>Followers")
repl_all("5.2x<br/>Overall ROI", "5.2x<br/>ROI")

# --- WHAT IS ---
repl_all("What is Search Engine Optimization?", "What is Social Media Marketing?")
repl_all("Understanding modern SEO", "Understanding social media marketing")
text = re.sub(
    r'SEO \(Search Engine Optimization\) is the practice.*?algorithm\.',
    'Social media marketing is the practice of using social platforms like Facebook, Instagram, LinkedIn, and TikTok to connect with your audience, build brand awareness, drive website traffic, and increase sales. Unlike traditional advertising, social media enables two-way communication between brands and customers.',
    text, flags=re.DOTALL
)
text = re.sub(
    r'Unlike paid advertising where traffic stops.*?industry leader\.',
    'Successful social media marketing requires consistent effort, strategic content planning, and continuous optimization. Our team manages every aspect from content creation to community management, paid advertising, and analytics to ensure your social presence drives real business results.',
    text, flags=re.DOTALL
)

# Replace the 4 sub-points
text = re.sub(r'Increase Visibility\s*</div>\s*<div class="text-sm text-black/60">Be found when customers are actively searching for your services</div>',
              r'Build Brand Awareness\n</div>\n<div class="text-sm text-black/60">Reach millions of potential customers on platforms they use daily</div>', text)
text = re.sub(r'Drive Qualified Traffic\s*</div>\s*<div class="text-sm text-black/60">Attract visitors with high intent to purchase or convert</div>',
              r'Drive Website Traffic\n</div>\n<div class="text-sm text-black/60">Turn social engagement into website visits and conversions</div>', text)
text = re.sub(r'Build Trust & Authority\s*</div>\s*<div class="text-sm text-black/60">Ranking high signals credibility to your target audience</div>',
              r'Generate Quality Leads\n</div>\n<div class="text-sm text-black/60">Connect with prospects actively interested in your products</div>', text)
text = re.sub(r'Sustainable Growth\s*</div>\s*<div class="text-sm text-black/60">Compounds over time for increasingly better ROI</div>',
              r'Increase Customer Loyalty\n</div>\n<div class="text-sm text-black/60">Build relationships that turn customers into brand advocates</div>', text)

# --- MISTAKES ---
repl_all("Common SEO Mistakes", "Common Social Media Mistakes")
repl_all("Avoid these costly SEO mistakes", "Avoid these costly social media mistakes")

text = re.sub(
    r'Research shows that many businesses waste.*?technical foundations\.',
    'Research shows that businesses waste countless hours on social media without seeing results. Posting randomly without a strategy, ignoring your audience, or using the wrong platforms can kill engagement and damage your brand reputation.',
    text, flags=re.DOTALL
)
text = re.sub(
    r'One of the biggest mistakes is treating SEO.*?wasted budget\.',
    'One of the biggest mistakes is inconsistent posting. Studies show inconsistent brands lose up to 60% of their followers within months. Similarly, poor-quality visuals can reduce engagement by 65%, while ignoring comments can decrease reach by 50% as algorithms penalize inactive accounts.',
    text, flags=re.DOTALL
)
text = re.sub(
    r'Professional SEO management eliminates these risks.*?business results\.',
    'Professional social media management eliminates these risks through strategic planning, consistent execution, and active community engagement. Our team knows how to create content that resonates, engage meaningfully with your audience, and track what actually drives business results.',
    text, flags=re.DOTALL
)

repl_all("Top 5 SEO Mistakes", "Top 5 Social Media Mistakes")

repl_all("Poor Mobile Experience", "Inconsistent Posting")
repl_all("Slow load times and bad mobile UX kill search rankings instantly", "Irregular posting schedule confuses followers and kills algorithm reach")

repl_all("Thin Content", "No Strategy")
repl_all("Creating superficial content that doesn't answer user intent", "Random posts without goals or planning waste time and resources")

repl_all("Ignoring Technical SEO", "Ignoring Comments")
repl_all("Broken links, poor site architecture, and indexation issues", "Not responding to followers reduces engagement and algorithm visibility")

repl_all("Bad Link Building", "Wrong Platforms")
repl_all("-45%", "-45%") # same
repl_all("Buying cheap links that result in Google penalties", "Being on platforms where your audience is not active")

repl_all("No Local Optimization", "Poor Visual Content")
repl_all("Missing out on high-intent local customers", "Low-quality images and videos drastically reduce engagement")

repl_all("of SEO efforts", "of social media efforts")

# --- SERVICES ---
repl_all("Complete search engine optimization services", "Complete social media marketing services")
repl_all("From audit to execution, we handle every aspect of your SEO strategy", "From strategy to execution, we handle every aspect of your social media presence")

repl_all(">Technical SEO<", ">Social Media Management<")
text = re.sub(r'Comprehensive audits, site speed optimization, schema markup, and structural improvements to ensure search engines can easily crawl and index your site\.',
              'Full-service management of your social media accounts including content planning, posting, and daily monitoring across all platforms.', text)
repl_all("Site speed optimization", "Content calendar planning")
repl_all("Core Web Vitals", "Daily posting & scheduling")
repl_all("Schema markup implementation", "Profile optimization")
repl_all("Crawlability fixes", "Performance monitoring")

repl_all(">On-Page SEO<", ">Content Creation & Strategy<")
text = re.sub(r'Strategic optimization of title tags, meta descriptions, headers, and content to align with search intent and target high-value keywords\.',
              'Professional content creation including graphics, videos, copy, and strategic planning to engage your target audience.', text)
repl_all("Keyword research & mapping", "Custom graphics & videos")
repl_all("Meta tag optimization", "Copywriting & captions")
repl_all("Content gap analysis", "Content strategy development")
repl_all("Internal linking strategy", "Brand voice consistency")

repl_all(">Link Building<", ">Paid Social Advertising<")
text = re.sub(r'Acquiring high-authority backlinks through digital PR, guest posting, and broken link building to boost your domain authority\.',
              'Strategic paid advertising campaigns on Facebook, Instagram, LinkedIn, and TikTok to amplify your reach and drive conversions.', text)
repl_all("Digital PR campaigns", "Campaign strategy & setup")
repl_all("Guest posting", "Audience targeting & research") # Keep generic or replace
repl_all("Broken link building", "Ad creative development")
repl_all("Unlinked brand mentions", "Ongoing optimization")

repl_all(">Local SEO<", ">Community Management<")
text = re.sub(r'Optimization of Google Business Profile, local citations, and localized content to dominate search results in your specific geographic area\.',
              'Active engagement with your audience through responding to comments, messages, and mentions to build strong relationships.', text)
repl_all("Google Business optimization", "Comment & DM responses")
repl_all("Local citation building", "Reputation monitoring")
repl_all("Review management", "Crisis management")
repl_all("Localized content strategy", "Engagement analytics")

repl_all(">E-commerce SEO<", ">Influencer Partnerships<")
text = re.sub(r'Specialized optimization for online stores, including category page SEO, product descriptions, and faceted navigation optimization\.',
              'Connect with relevant influencers and content creators to expand your reach and build authentic brand awareness.', text)
repl_all("Category optimization", "Influencer identification")
repl_all("Product page SEO", "Partnership negotiation")
repl_all("Faceted navigation fixes", "Campaign coordination")
repl_all("Structured data for products", "Performance tracking")

# For Content Marketing, we replace with Social Media Analytics
# >Content Strategy< has already been changed to >LinkedIn< globally in platforms, wait, let me just grab the block.
# Actually I'll regex it since it might say Content Strategy
text = re.sub(
    r'>\s*(Content Strategy|Content Strategy|Content Marketing)\s*<',
    r'>Social Media Analytics<',
    text
)
text = re.sub(r'Creating data-driven blog posts, guides, and resources that attract top-of-funnel traffic and establish your brand authority\.',
              'Comprehensive tracking and reporting on all key metrics to measure performance and inform strategy decisions.', text)
repl_all("Topic cluster strategy", "Custom dashboards")
repl_all("Blog content creation", "Monthly performance reports")
repl_all("Evergreen guides", "Competitor benchmarking")
repl_all("Content refreshing", "ROI tracking")


repl_all("Ready to dominate the search results?", "Ready to transform your social media presence?")
repl_all("Our SEO experts will create a custom strategy", "Our social media experts will create a custom strategy")
repl_all("grow your organic traffic", "grow your following")
repl_all("Get Free SEO Audit", "Get Free Social Media Audit")

# --- WHY CHOOOSE US ---
repl_all("Why choose our SEO service?", "Why choose our social media service?")
text = re.sub(r'Partner with an agency that understands search engines inside and out', 
              'Partner with a team that understands social media inside and out', text)
repl_all("Data-driven SEO strategies", "Data-driven social media strategies")
repl_all("Custom link building", "Consistent Execution")
repl_all("Securing high-quality backlinks that move the needle", "Regular, high-quality content that keeps your audience engaged and your brand top-of-mind")
repl_all("Technical Excellence", "Active Engagement")
repl_all("Deep expertise in technical SEO to ensure your site is perfectly optimized", "We do not just post and ghost. We actively engage with your community to build relationships")
repl_all("Content Expertise", "Platform Expertise")
repl_all("Creating authoritative content that ranks well and converts visitors", "Deep knowledge of each platform algorithm, best practices, and emerging trends")
repl_all("Analytics proficiency", "Creative Excellence")
repl_all("Advanced tracking to measure every metric that matters", "Professional content creation that captures attention and drives action")
repl_all("Transparent Reporting", "Transparent Reporting") # keep
repl_all("Clear dashboards indicating how our SEO efforts translate to ROI", "Clear metrics and insights so you always know how your social media is performing")

# Replace checkmark points in WHY CHOOSE US
repl_all("Proven Results", "Proven Results")
text = re.sub(r'<div class="text-sm text-black/60">Consistent track record of delivering first page rankings and organic growth\.</div>',
              '<div class="text-sm text-black/60">Track record of growing followers, increasing engagement, and driving conversions.</div>', text)


text = re.sub(r'Your competitors are stealing your customers on Google!', 'Your competitors are stealing your customers on social media!', text)
text = re.sub(r'While you are missing from the first page, your competitors are capturing free, high-intent traffic every single day.',
              'While you are posting inconsistently or not at all, your competitors are building communities, generating leads, and growing their brands on social media every single day.', text)

text = re.sub(r'<div class="text-2xl font-bold text-\[var\(--orange\)\]">93%</div>\s*<div class="mt-1 text-sm text-black/70">Online experiences begin with a search engine</div>',
              '<div class="text-2xl font-bold text-[var(--orange)]">4.8B</div>\n<div class="mt-1 text-sm text-black/70">People on social media</div>', text)
text = re.sub(r'<div class="text-2xl font-bold text-\[var\(--orange\)\]">75%</div>\s*<div class="mt-1 text-sm text-black/70">Users never scroll past the first page of results</div>',
              '<div class="text-2xl font-bold text-[var(--orange)]">2.5 hrs</div>\n<div class="mt-1 text-sm text-black/70">Average daily usage</div>', text)
text = re.sub(r'<div class="text-2xl font-bold text-\[var\(--orange\)\]">5\.6x</div>\s*<div class="mt-1 text-sm text-black/70">Better ROI compared to outbound marketing</div>',
              '<div class="text-2xl font-bold text-[var(--orange)]">76%</div>\n<div class="mt-1 text-sm text-black/70">Research products on social</div>', text)

repl_all("Get A Free SEO Audit", "Get A Free Social Media Audit")
repl_all("No credit card required • See your SEO score in 48 hours • Start growing today", "No credit card required • See your opportunities in 48 hours • Start growing today")

# Keep writing the file back
with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Migration step 1 complete.")
