from django.shortcuts import render, get_object_or_404

from .models import Officer
from .models import Complaint

def index(request):
    officer_list = Officer.objects.all()
    complaints_list = Complaint.objects.all()
    context = {
        'officer_list': officer_list,
        'complaints_list': complaints_list,
    }
    return render(request,'data/index.html',context)

def detail(request, officer_id):
    officer = get_object_or_404(Officer, pk=officer_id)
    complaints = officer.complaint_set.all()
    return render(request,'data/detail.html',{'officer':officer, 'complaints': complaints})

def results(request):
    searchterm = request.GET.get('searchterm','')
    officer_list = Officer.objects.filter(last_name__startswith=searchterm)
    return render(request,'data/results.html',{'officer_list': officer_list})