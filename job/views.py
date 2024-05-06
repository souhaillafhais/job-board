from django.shortcuts import redirect, render
from .models import Job
from django.core.paginator import Paginator
#from .form import ApplyForm , JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#from .filters import JobFilter
# Create your views here.

def jobs_list(request):
    job_list = Job.objects.all()
    context = {'jobs':job_list}
    return render(request,'job/job_list.html',context)
    
    




 



def job_detail(request , slug):
    job_detail = Job.objects.get(slug=slug)

""""  if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            print('DOne')

    else:
        form = ApplyForm()"""


    #context = {'job' : job_detail , 'form1':form}
    #return render(request,'job/job_detail.html',context)
