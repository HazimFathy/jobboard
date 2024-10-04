from django.shortcuts import render , redirect
from .models import job
from django.core.paginator import Paginator
from .form import applyform , addjob
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import jobFilter
# Create your views here.
def job_list(request):
    job_list= job.objects.all()
    
    #filter 
    myfilter =jobFilter(request.GET,queryset=job_list)
    job_list=myfilter.qs
    
    #paginator
    paginator = Paginator(job_list, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    
    context ={'jobs':page_obj,'myfilter':myfilter}
    return render(request,'job/job_list.html',context)




def job_detail ( request , slug ) :
    job_detail = job.objects.get( slug = slug  )
    
    if request.method=='POST':
        form= applyform(request.POST, request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job= job_detail
            myform.owner= request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form=applyform()
        
    context = {'job': job_detail,'form':form}
    return render(request,'job/job_detail.html',context)




#add job def
@login_required
def add_job(request):
    if request.method=='POST':
        form=addjob(request.POST,request.FILES)
        if form.is_valid():
            myform= form.save(commit=False)
            myform.owner= request.user
            myform.save()
        return redirect(reverse('jobs:job_list'))
    else:
        form = addjob()
        
        
    return render(request,'job/add_job.html',{'form':form})
    