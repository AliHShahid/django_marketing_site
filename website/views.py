from django.shortcuts import render, redirect
from django.http import Http404
from .models import Lead
from django.contrib import messages


# def home(request):
#     success = False
#     if request.method == 'POST':
#         # Get data from the form
#         Lead.objects.create(
#             name=request.POST.get('name'),
#             email=request.POST.get('email'),
#             company=request.POST.get('company'),
#             package=request.POST.get("package"),  # MUST MATCH name=""
#             phone = request.POST.get("phone") ,
#             message=request.POST.get('message')
#         )
#         success = True

#     return render(request, 'index.html', {'success': success})
def home(request):
    if request.method == 'POST':
        Lead.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            date=request.POST.get('date'),
            package=request.POST.get('package'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('home')   # important

    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        Lead.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            date=request.POST.get('date') or None,
            package=request.POST.get('package'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message', '')
        )
        messages.success(request, "Thanks! Your details were submitted successfully.")
        return redirect('contact')

    return render(request, 'contact.html')


def how_it_works(request):
    return render(request, 'how_it_works.html')

def about(request):
    return render(request, 'about.html')

def case_study(request):
    return render(request, 'case_study.html')

def pricing(request):
    return render(request, 'pricing.html')

def services(request):
    return render(request, 'services.html')

def ecommerce_case_study(request):
    return render(request, 'ecommerce_case_study.html')

def amazon_ppc_case_study(request):
    return render(request, 'amazon_ppc_case_study.html')

def beauty_brand_case_study(request):
    return render(request, 'beauty_brand_case_study.html')

def saas(request):
    return render(request, 'saas.html')

def b2b(request):
    return render(request, 'b2b.html')

def dtc(request):
    return render(request, 'dtc.html')


def service_ppc(request):
    return render(request, 'services_ppc.html')


def service_seo(request):
    return render(request, 'services_seo.html')


def service_web_development(request):
    return render(request, 'services_web_development.html')


def service_landing_pages(request):
    return render(request, 'services_landing_pages.html')


def service_aeo(request):
    return render(request, 'services_aeo.html')


def service_social_media(request):
    return render(request, 'services_social_media.html')


def blog(request):
    return render(request, 'blog.html')


def real_estate(request):
    return render(request, 'real_estate.html')


def healthcare(request):
    return render(request, 'healthcare.html')


def home_services(request):
    return render(request, 'home_services.html')


def automotive(request):
    return render(request, 'automotive.html')


def legal(request):
    return render(request, 'legal.html')


def ecommerce(request):
    return render(request, 'ecommerce.html')


def finance(request):
    return render(request, 'finance.html')


def construction(request):
    return render(request, 'construction.html')


def get_started(request):
    return render(request, 'get_started.html')


def all_industries(request):
    return render(request, 'all_industries.html')


SUB_INDUSTRY_PAGES = {
    'real-estate-agents': 'Real Estate Agents',
    'real-estate-investors': 'Real Estate Investors',
    'real-estate-brokers': 'Real Estate Brokers',
    'property-management': 'Property Management',
    'dentists': 'Dentists',
    'chiropractors': 'Chiropractors',
    'med-spas': 'Med Spas',
    'plastic-surgeons': 'Plastic Surgeons',
    'hvac-companies': 'HVAC Companies',
    'plumbers': 'Plumbers',
    'electricians': 'Electricians',
    'roofing-companies': 'Roofing Companies',
    'car-detailers': 'Car Detailers',
    'auto-repair-shops': 'Auto Repair Shops',
    'car-dealerships': 'Car Dealerships',
    'personal-injury-lawyers': 'Personal Injury Lawyers',
    'family-law-attorneys': 'Family Law Attorneys',
    'criminal-defense-lawyers': 'Criminal Defense Lawyers',
    'estate-planning-attorneys': 'Estate Planning Attorneys',
    'fashion-apparel': 'Fashion & Apparel',
    'beauty-cosmetics': 'Beauty & Cosmetics',
    'health-supplements': 'Health & Supplements',
    'financial-advisors': 'Financial Advisors',
    'wealth-management': 'Wealth Management',
    'accounting-firms': 'Accounting Firms',
    'home-remodelers': 'Home Remodelers',
    'custom-home-builders': 'Custom Home Builders',
    'commercial-contractors': 'Commercial Contractors',
    'pool-builders': 'Pool Builders',
}

SUB_INDUSTRY_TEMPLATES = {
    'dentists': 'dentists.html',
    'chiropractors': 'chiropractors.html',
    'med-spas': 'med_spas.html',
    'plastic-surgeons': 'plastic_surgeons.html',
}


def industry_detail(request, slug):
    industry_name = SUB_INDUSTRY_PAGES.get(slug)
    if not industry_name:
        raise Http404('Industry page not found')
    
    template_name = SUB_INDUSTRY_TEMPLATES.get(slug, 'industry_detail.html')
    return render(request, template_name, {'name': industry_name})

def custom_404(request, exception):
    return render(request, '404.html', status=404)

    dedicated_template = SUB_INDUSTRY_TEMPLATES.get(slug)
    if dedicated_template:
        return render(request, dedicated_template, {
            'industry_name': industry_name,
            'slug': slug,
        })

    return render(request, 'industry_detail.html', {
        'industry_name': industry_name,
        'slug': slug,
    })
