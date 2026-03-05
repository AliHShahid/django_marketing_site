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

# --- Why choose us ---
robust_replace("Why choose our SEO service?", "Why choose our social media service?")
text = re.sub(r'Partner with an agency that understands search engines inside and out(.*?)partner', 
              r'Partner with a team that understands social media inside and out\1partner', text, flags=re.DOTALL)
robust_replace("Partner with an agency that understands search engines inside and out, and is committed to delivering measurable results for your business.",
               "Partner with a team that understands social media inside and out, and is committed to delivering measurable results for your business.")
robust_replace("Data-driven SEO strategies", "Data-driven social media strategies")
robust_replace("Custom link building", "Consistent Execution")
robust_replace("Securing high-quality backlinks that move the needle", "Regular, high-quality content that keeps your audience engaged and your brand top-of-mind")
robust_replace("Technical Excellence", "Active Engagement")
robust_replace("We don't just build sites; we build sites that perform.", "We do not just post and ghost. We actively engage with your community to build relationships.")
robust_replace("Deep expertise in technical SEO to ensure your site is perfectly optimized", "We do not just post and ghost. We actively engage with your community to build relationships.") # adjust for correct replaced string from html
text = re.sub(r'Deep expertise in technical SEO to ensure your site is perfectly optimized', 'We do not just post and ghost. We actively engage with your community to build relationships.', text)
robust_replace("Content Expertise", "Platform Expertise")
robust_replace("Creating authoritative content that ranks well and converts visitors", "Deep knowledge of each platform algorithm, best practices, and emerging trends")
robust_replace("Analytics proficiency", "Creative Excellence")
robust_replace("Advanced tracking to measure every metric that matters", "Professional content creation that captures attention and drives action")
robust_replace("Clear dashboards indicating how our SEO efforts translate to ROI", "Clear metrics and insights so you always know how your social media is performing")

robust_replace("Consistent track record of delivering first page rankings and organic growth.",
               "Track record of growing followers, increasing engagement, and driving conversions.")

robust_replace("Organic Traffic Growth", "Social Media Performance Analytics")
robust_replace("Rankings & Organic Traffic Insights", "Meta Ads Dashboard - Social Media Performance Analytics")
robust_replace("Meta Ads Dashboard - Social Media Performance Analytics", "Meta Ads Dashboard - Social Media Performance Analytics") # careful not to duplicate

# Stats in blue dashboard:
robust_replace("Your competitors are stealing your customers on Google!", "Your competitors are stealing your customers on social media!")
robust_replace("While you are missing from the first page, your competitors are capturing free, high-intent traffic every single day.",
               "While you are posting inconsistently or not at all, your competitors are building communities, generating leads, and growing their brands on social media every single day.")

text = re.sub(r'>93%<', '>4.8B<', text)
robust_replace("Online experiences begin with a search engine", "People on social media")
text = re.sub(r'>75%<', '>2.5 hrs<', text)
robust_replace("Users never scroll past the first page of results", "Average daily usage")
text = re.sub(r'>5.6x<', '>76%<', text)
robust_replace("Better ROI compared to outbound marketing", "Research products on social")

robust_replace("Get A Free SEO Audit", "Get A Free Social Media Audit")
robust_replace("No credit card required • See your SEO score in 48 hours • Start growing today",
               "No credit card required • See your opportunities in 48 hours • Start growing today")

# --- Process ---
robust_replace("How we deliver SEO success", "How we deliver social media success")
text = re.sub(r'Our proven 5-step process ensures your website climbs the rankings.*?over time\.',
              "Our proven 5-step process ensures your social media presence drives real business results from day one and continues to grow over time.", text, flags=re.DOTALL)

robust_replace("Keyword & Content Strategy", "Strategy Development")
robust_replace("Technical & On-Page SEO", "Content Production")
robust_replace("Link Building & Authority", "Campaign Launch")

text = re.sub(r'We analyze your current rankings, website architecture, competitor strategies, and target audience to identify the biggest opportunities\.',
              "We analyze your current social media presence, competitor strategies, target audience, and business goals to understand your unique situation and opportunities.", text)

robust_replace("Keyword research report", "Social media audit report") # oops step 1 had "Social media audit report" in user text
robust_replace("Technical audit document", "Social media audit report") # Wait, "Social media audit report", "Competitor analysis", "Audience research", "Platform recommendations"
robust_replace("Platform recommendations", "Platform recommendations")

text = re.sub(r'We identify high-value search terms and create a comprehensive roadmap for content that will capture targeted organic traffic\.',
              "We create a comprehensive social media strategy including content pillars, posting schedule, engagement tactics, and growth objectives tailored to your brand.", text)
robust_replace("Keyword research report", "Content strategy document")
robust_replace("Content gap analysis", "Editorial calendar template")
robust_replace("Topic cluster mapping", "Brand voice guidelines")
robust_replace("ROI projections", "KPI framework")

text = re.sub(r'Our team fixes all technical issues, optimizes site speed, and ensures your pages are perfectly structured for search engines\.',
              "Our creative team produces high-quality content including graphics, videos, copy, and stories designed to engage your audience and drive results.", text)
robust_replace("Technical fix implementation", "Custom graphics & videos")
robust_replace("Meta tag optimization", "Engaging copy & captions")
robust_replace("Schema markup", "Hashtag research")
robust_replace("Internal linking", "Content library setup")

text = re.sub(r'We execute targeted outreach campaigns to acquire high-quality, relevant backlinks that boost your domain authority\.',
              "We launch your social media campaigns with strategic posting, community engagement, and paid advertising to maximize reach and impact from day one.", text)
robust_replace("Outreach strategy", "Content posting schedule")
robust_replace("Digital PR campaigns", "Community management")
robust_replace("Guest post placements", "Paid ad campaigns")
robust_replace("Authority tracking", "Performance monitoring")

text = re.sub(r'We continuously track keyword movements, traffic quality, and conversion metrics to refine and scale your SEO strategy\.',
              "We continuously track performance, test new content, engage with your community, and optimize strategy to ensure consistent growth and results.", text)
robust_replace("Ranking reports", "Weekly performance reviews")
robust_replace("Traffic analysis", "Monthly strategy reports")
robust_replace("Conversion tracking", "A/B testing insights")
robust_replace("Next steps roadmap", "Growth recommendations")

robust_replace("7 days\n                        </div>\n                        <div class=\"mt-1 text-sm text-black/70\">\n                            Technical review",
               "7 days\n                        </div>\n                        <div class=\"mt-1 text-sm text-black/70\">\n                            Strategy development")
robust_replace("Technical review", "Strategy development")

robust_replace("Daily\n                        </div>\n                        <div class=\"mt-1 text-sm text-black/70\">\n                            Rank tracking",
               "Daily\n                        </div>\n                        <div class=\"mt-1 text-sm text-black/70\">\n                            Community engagement")
robust_replace("Rank tracking", "Community engagement")


# --- Platform Expertise ---
robust_replace("Our professional SEO tools", "Our professional social media tools")
robust_replace("We leverage the most powerful enterprise SEO platforms to drive exceptional results for your brand.", "We leverage the most powerful social media platforms and management tools to drive exceptional results for your brand.")
robust_replace("SEMrush", "Meta")
robust_replace("Ahrefs", "Meta Business Suite")
robust_replace("Screaming Frog", "Facebook Ads Manager")
robust_replace("Google Search Console", "Instagram Creator Studio")
robust_replace("Majestic", "LinkedIn Campaign Manager")
robust_replace("Surfer SEO", "TikTok Ads Manager")


# --- Engagement Growth ---
robust_replace("Organic Results", "Engagement Growth")
robust_replace("Skyrocket your organic traffic", "Skyrocket your social media engagement")
text = re.sub(r'Dominate the first page of Google to capture high-intent users and drive consistent, scalable revenue for your business\.',
              "Turn passive followers into an active, engaged community that amplifies your brand and drives real business results.", text)

robust_replace("Keyword Dominance", "Viral Content Strategy")
text = re.sub(r'Rank #1 for the most valuable search terms in your industry, capturing users at the exact moment they are ready to buy\.',
              "Create content designed to resonate, engage, and spread organically across your target audience.", text)

robust_replace("Conversion Optimization", "Engagement Optimization")
text = re.sub(r'We do not just drive traffic; we optimize your pages to turn those visitors into qualified leads and paying customers\.',
              "Maximize likes, comments, and shares with scientifically-tested engagement tactics.", text)

robust_replace("Content Authority", "Audience Growth")
text = re.sub(r'Establish your brand as the go-to resource in your space with comprehensive, expertly crafted content that Google loves\.',
              "Strategic follower acquisition that brings real, engaged users interested in your brand.", text)

robust_replace("Technical Excellence", "Hashtag Mastery")
text = re.sub(r'Build a perfectly optimized digital foundation that loads instantly and provides a flawless experience across all devices\.',
              "Research and implement high-performing hashtags that expand your reach exponentially.", text)

robust_replace("Link Profile Growth", "Community Building")
text = re.sub(r'Develop a powerful, natural backlink profile that signals authority to search engines and protects against algorithm updates\.',
              "Foster authentic connections that turn followers into a loyal, engaged community.", text)

with open(path_out, 'w', encoding='utf-8') as f:
    f.write(text)

print("Pass 2 done")
