from django.shortcuts import render
from job.models import Job,Category

def home_display(request):
        job = Job.objects.all()
       
        return render(request,'home.html',{'job': job})
