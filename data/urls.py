from django.urls import path

from . import views

app_name = 'data'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:DSN>/', views.detail, name="detail"),
    path('results/',views.results, name="results"),
    path('complaint/<file_no>/', views.complaint, name="complaint"),
    path('locations/', views.complaint_locations, name="complaint_locations")

]