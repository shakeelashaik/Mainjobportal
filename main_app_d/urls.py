from django.urls import path
from main_app_d import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume/', views.create_resume, name='resume'),
    path('jsp/', views.jobseeker_profile, name='jsp'),
    path('job_details/', views.job_detail, name='job_details'),
    path('applied_jobs/', views.applied_jobs, name='applied_jobs'),
    path('browse_jobseeker/', views.browse_jobseeker, name='browse_jobseeker'),
    path('interested_jobs/', views.interested_jobs, name='interested_jobs'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('Contacted_com/', views.Contacted_com, name='Contacted_com'),
    path('shortlisted_com/', views.shortlisted_com, name='shortlisted_com'),
    path('shortlisted_jobs/', views.shortlisted_jobs, name='shortlisted_jobs'),
    path('applier_profile/', views.applier_profile, name='applier_profile'),
    path('company_details/', views.company_details, name='company_details'),
    path('edit/', views.edit, name='edit'),
    path('emp_index/', views.emp_index, name='emp_index'),
    path('create_job/', views.create_job, name='createjob'),
    path('browse_emp/', views.browse_employer, name='browseemp'),
    path('con_pro/', views.con_pro, name='conpro'),
    path('job_appliers/', views.job_appliers, name='jobappliers'),
    path('posted_jobs/', views.posted_jobs, name='postedjobs'),
    path('shortlisted_profiles/', views.shortlisted_pro, name='shortlistedprofiles'),
    path('empchange_password/', views.empchangepass, name='empchangepass'),
    path('emp_pro/', views.emp_pro, name='emppro'),
    path('emp_proedit/', views.emp_proedit, name='empproedit'),
    path('bookmark_pro/', views.bookmark_pro, name='bookmarkpro')
]
