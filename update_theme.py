import re
import os

def update_chiropractors_theme(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Dark Backgrounds
    content = content.replace('bg-gradient-to-br from-black via-gray-900 to-black', 'bg-[#0B0B0F]')
    content = content.replace('bg-gradient-to-br from-black via-gray-950 to-black', 'bg-[#0B0B0F]')
    
    # 2. Text/Icon Gradients
    content = content.replace('from-purple-400 via-purple-400 to-[#EE3923]', 'from-[#FF4801] to-[#EE3923]')
    content = content.replace('from-purple-600 to-blue-600', 'from-[#FF4801] to-[#EE3923]')
    content = content.replace('from-purple-200 via-purple-400 to-blue-500', 'from-[#FF4801] via-[#EE3923] to-[#FF4801]')
    
    # 3. Accents
    # Purple to Orange
    content = content.replace('text-purple-600', 'text-[#EE3923]')
    content = content.replace('bg-purple-100', 'bg-[#EE3923]/10')
    content = content.replace('border-purple-100', 'border-[#EE3923]/20')
    content = re.sub(r'bg-purple-(\d+)', r'bg-orange-\1', content)
    content = re.sub(r'text-purple-(\d+)', r'text-orange-\1', content)
    
    # Blue to Secondary Orange
    content = content.replace('text-blue-600', 'text-[#FF4801]')
    content = content.replace('bg-blue-100', 'bg-[#FF4801]/10')
    content = content.replace('border-blue-200', 'border-[#FF4801]/20')
    
    # 4. Neutral Updates
    content = content.replace('bg-gradient-to-br from-purple-50 to-white', 'bg-gradient-to-br from-zinc-50 to-white')
    content = content.replace('bg-gradient-to-br from-white to-purple-50', 'bg-gradient-to-br from-white to-zinc-50')
    content = content.replace('bg-gradient-to-r from-purple-100 to-blue-100', 'bg-white/10')
    
    # 5. Fix remaining hero glow circles if they reference old purples
    content = content.replace('bg-purple-950/40', 'bg-[#EE3923]/20')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    target = r"C:\Users\Dell\Desktop\adryze site main\stratup site django\my_startup\website\templates\chiropractors.html"
    update_chiropractors_theme(target)
    print("DONE: Updated theme colors to brand standards.")
