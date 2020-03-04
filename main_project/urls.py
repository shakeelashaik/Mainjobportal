"""main_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_app_d import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.emp_index,name='emp_index'),
    path('create_job',views.create_job,name='createjob'),
    path('browse_emp',views.browse_employer,name='browseemp'),
    path('con_pro',views.con_pro,name='conpro'),
    path('job_appliers',views.job_appliers,name='jobappliers'),
    path('posted_jobs',views.posted_jobs,name='postedjobs'),
    # path('shortlisted_jobs',views.shortlisted_jobs,name='shortlistedjobs'),
    path('shortlisted_profiles',views.shortlisted_pro,name='shortlistedprofiles'),
    path('empchange_password',views.empchangepass,name='empchangepass'),
    # path('sent_jobs',views.sent_jobs,name='sentjobs'),
    path('emp_pro',views.emp_pro,name='emppro'),
    path('emp_proedit',views.emp_proedit,name='empproedit'),
    path('bookmark_pro',views.bookmark_pro,name='bookmarkpro')
]