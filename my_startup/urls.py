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
from website.views import home, how_it_works, about, case_study, pricing, services, ecommerce_case_study, amazon_ppc_case_study, beauty_brand_case_study
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
    path('beauty_brand_case_study/', beauty_brand_case_study, name = 'beauty_brand_case_study')

]