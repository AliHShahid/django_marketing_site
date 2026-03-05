"""
URL configuration for my_startup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website.views import home, how_it_works, about, case_study, pricing, services, ecommerce_case_study, amazon_ppc_case_study, beauty_brand_case_study, saas, b2b, dtc, service_ppc, service_seo, service_web_development, service_landing_pages, service_aeo, service_social_media, contact, blog, real_estate, healthcare, home_services, automotive, legal, ecommerce, finance, construction, get_started, all_industries, industry_detail
# from website import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('how_it_works/', how_it_works, name='how_it_works'),
    path('about/', about, name='about'),
    path('case_study/', case_study, name='case_study'),
    path('pricing/', pricing, name='pricing'),
    path('services/', services, name='services'),
    path('ecommerce_case_study/', ecommerce_case_study, name = 'ecommerce_case_study'),
    path('amazon_ppc_case_study/', amazon_ppc_case_study, name = 'amazon_ppc_case_study'),
    path('beauty_brand_case_study/', beauty_brand_case_study, name = 'beauty_brand_case_study'),
    path('saas/', saas, name = 'saas'),
    path('b2b/', b2b, name = 'b2b'),
    path('dtc/', dtc, name = 'dtc'),
    path('services/ppc/', service_ppc, name='service_ppc'),
    path('services/seo/', service_seo, name='service_seo'),
    path('services/web-development/', service_web_development, name='service_web_development'),
    path('services/web-development/landing-pages/', service_landing_pages, name='service_landing_pages'),
    path('services/aeo/', service_aeo, name='service_aeo'),
    path('services/social-media/', service_social_media, name='service_social_media'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('real-estate/', real_estate, name='real_estate'),
    path('healthcare/', healthcare, name='healthcare'),
    path('home-services/', home_services, name='home_services'),
    path('automotive/', automotive, name='automotive'),
    path('legal/', legal, name='legal'),
    path('ecommerce/', ecommerce, name='ecommerce'),
    path('finance/', finance, name='finance'),
    path('construction/', construction, name='construction'),
    path('get-started/', get_started, name='get_started'),
    path('industries/', all_industries, name='all_industries'),
    path('industries/<slug:slug>/', industry_detail, name='industry_detail')
    

]