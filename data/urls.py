from django.urls import path

from . import views

app_name = 'data'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:officer_id>/', views.detail, name="detail"),
    path('results/',views.results, name="results")
]