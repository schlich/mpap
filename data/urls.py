from django.urls import path

from . import views

appname="data"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:officer_id>/', views.detail, name="detail")
]