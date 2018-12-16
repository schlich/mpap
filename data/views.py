from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from django.http import HttpResponse
from django.conf import settings


from .models import Officer
from .models import Complaint

def index(request):
    officer_list = Officer.objects.all()
    complaints_list = Complaint.objects.all()
    context = {
        'officer_list': officer_list,
        'complaints_list': complaints_list,
        'api_key': settings.GOOGLE_API_KEY,
    }
    return render(request,'data/index.html',context)

def detail(request, DSN):
    officer = get_object_or_404(Officer, pk=DSN)
    complaints = officer.complaint_set.all()
    return render(request,'data/detail.html',{'officer':officer, 'complaints': complaints})

def results(request):
    searchterm = requaest.GET.get('searchterm','')
    officer_matches = Officer.objects.filter(last_name__istartswith=searchterm)
    return render(request,'data/results.html',{'officer_list': officer_matches})

def complaint(request, file_no):
    complaint = get_object_or_404(Complaint, pk=file_no)
    officer = complaint.officer
    return render(request, 'data/complaint.html',{'officer':officer,'complaint':complaint})

def complaint_locations(request):
    response = serialize('geojson', Complaint.objects.all())
    return HttpResponse(response)