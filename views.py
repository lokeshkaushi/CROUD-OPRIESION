from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from django.urls import reverse
from . models import Reg
from . models import Job
def register(request):
    return render(request,"ajax/register.html")
    

def regcode(request):
    print("data is",request.POST.get("uid"))
    print(request.POST.get("upass"))
    r=Reg(uname=request.POST.get("uid"),password=request.POST.get("upass"),emailid=request.POST.get("email"),mobileno=request.POST.get("mobileno"))
    r.save()
    return HttpResponse("data inserted successfully")

def load(request):
    return render(request,"ajax/search.html")
def data(request):
    r = request.GET["q"]
    
    result = Reg.objects.filter(uname__contains=r)
    return render(request,"ajax/data.html",{'res':result})

class JobCreate(CreateView):
    model = Job
    fields = ['jobtitle', 'jobdescription']
    def get_success_url(self):
        return reverse('login')

class jobList(ListView):
   
    # specify the model for list view
    model = Job  
    def get_queryset(self, *args, **kwargs):
        qs = super(jobList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs

class JobDetail(DetailView):
  fields = ['jobtitle','jobdescription']
  model = Job   # Job.objects.all()  

class JobUpdate(UpdateView):
    model = Job
    fields = ['jobtitle','jobdescription']
    success_url ='/ajax/joblist'


class JobDelete(DeleteView):
    model = Job
    success_url = '/ajax/joblist'