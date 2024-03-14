import pdfkit
import io
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Profile

def forms(request):


    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        about = request.POST.get('about', "")
        degree = request.POST.get('degree', "")
        university = request.POST.get('university', "")
        work_experience = request.POST.get('work_experience', "")
        skills = request.POST.get('skills', "")

        profile = Profile(name=name,email=email,phone=phone,about=about,degree=degree,university=university,work_experience=work_experience,skills=skills)
        profile.save()

    return render(request, 'pdf/forms.html')

def cv(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/cv.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    # downloadable pdf
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "cv.pdf"

    return response

def list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/list.html', {'profiles':profiles})