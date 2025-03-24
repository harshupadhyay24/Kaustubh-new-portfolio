from django.shortcuts import render
from .models import Resume

#create your views here.
from django.http import HttpResponse

def home(request):
     return render(request,'index.html')

from .models import Resume

def resume(request):
    resume = Resume.objects.first()  # Get the first resume
    return render(request, 'Resume.html', {'resume': resume})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Certificate

def certificate_list(request):
    certificates = Certificate.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        issued_by = request.POST.get('issued_by')  # Ensure correct field name
        issue_date = request.POST.get('issue_date')
        certificate_file = request.FILES.get('certificate_file')

        if title and issued_by and issue_date and certificate_file:
            Certificate.objects.create(
                title=title,
                issued_by=issued_by,
                issue_date=issue_date,
                certificate_file=certificate_file
            )
            return redirect('certificates')  # Refresh page after upload

    return render(request, 'certificates.html', {'certificates': certificates})

def delete_certificate(request, certificate_id):
    certificate = Certificate.objects.get(id=certificate_id)
    certificate.delete()
    return redirect('certificates')  # Refresh page after delete
    return redirect('certificates')


from django.shortcuts import render, redirect
from .models import ContactMessage

from django.shortcuts import render, redirect
from .models import ContactMessage

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            return redirect('contact')  # Refresh page after submission

    return render(request, 'contact.html')

