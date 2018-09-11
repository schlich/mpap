from django.contrib import admin

# Register your models here.
from .models import Officer
from .models import Complaint
admin.site.register(Officer)
admin.site.register(Complaint)