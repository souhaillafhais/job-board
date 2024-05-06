from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobs_list, name='jobs_list'),  
    path('', views.job_detail, name='job_detail'), 
]