import re
path = r'c:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\services_social_media.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('What is social media?', 'What is Social Media Marketing?')
text = text.replace('Social Media Marketing (social media) is the practice', 'Social media marketing is the practice')
text = text.replace('social media focuses on earning organic', 'social media enables two-way communication')
text = text.replace('When executed properly, social media delivers', 'Our team manages every aspect from content creation to community management, paid advertising, and analytics to ensure your social presence drives')
text = text.replace('<!-- social media Mistakes -->', '<!-- Social Media Mistakes -->')
text = text.replace('social media Mistakes', 'Social Media Mistakes')
text = text.replace('social media Services', 'Social Media Services')
text = text.replace('Complete social media <span', 'Complete social media marketing <span')
text = text.replace('social media delivers the best ROI of any', 'social media offers one of the best ROIs of any')
text = text.replace('social media improvements stack over time.', 'social media efforts compound over time.')
text = text.replace('social media <span class="text-[var(--orange)]">mistakes</span>', 'social media mistakes')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
