import re
import os

def apply_aos_manually(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for static inline transitions with variations
    pattern = r'style="opacity:\s*[01];\s*transform:\s*(?:none|translateY\(16px\)|translateX\(-?16px\)|translateX\(16px\)|scale\(0\.97\));\s*transition-property:\s*opacity,\s*transform;\s*transition-duration:\s*\d+ms;\s*transition-timing-function:\s*ease-out;\s*transition-delay:\s*(\d+)ms;?"'
    
    def replace_with_aos(match):
        delay = match.group(1)
        return f'data-aos="fade-up" data-aos-delay="{delay}"'

    new_content = re.sub(pattern, replace_with_aos, content)
    
    # 2. Add AOS library if missing
    if 'unpkg.com/aos@next/dist/aos.css' not in new_content:
        new_content = new_content.replace('</head>', '    <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />\n</head>', 1)
    
    if 'AOS.init()' not in new_content:
        # Append before closing body if exists, else at end
        script = '\n    <script src="https://unpkg.com/aos@next/dist/aos.js"></script>\n    <script>\n      AOS.init({ duration: 800, once: true, offset: 50 });\n    </script>\n'
        if '</body>' in new_content:
            new_content = new_content.replace('</body>', script + '</body>', 1)
        else:
            new_content += script

    # 3. Add hover effects for more dynamic feel
    # Enhance cards with shadow and scaling
    new_content = new_content.replace('hover:shadow-md', 'hover:shadow-2xl hover:scale-[1.03] transition-all duration-300')
    new_content = new_content.replace('hover:shadow-lg', 'hover:shadow-2xl hover:scale-[1.03] transition-all duration-300')
    
    # Update buttons
    new_content = new_content.replace('hover:bg-gray-100 transition-all', 'hover:bg-gray-100 transition-all hover:-translate-y-1 hover:shadow-xl')
    new_content = new_content.replace('hover:bg-white/90 active:scale-[0.97] transition-all duration-200', 'hover:bg-white/90 active:scale-[0.97] transition-all duration-300 hover:-translate-y-1 hover:shadow-xl')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    target = r"C:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\chiropractors.html"
    apply_aos_manually(target)
    print("DONE: Applied AOS and hover effects.")
