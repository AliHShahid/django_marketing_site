from django.shortcuts import render, redirect
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
            company=request.POST.get('company'),
            package=request.POST.get('package'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('home')   # important

    return render(request, 'index.html')


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
