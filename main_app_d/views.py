from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def create_resume(request):
    return render(request, 'create_resume.html')


def jobseeker_profile(request):
    return render(request, 'jobseeker_profile.html')


def job_detail(request):
    return render(request, 'job_detail.html')


def edit(request):
    return render(request, 'edit.html')


def applied_jobs(request):
    return render(request, 'applied_jobs.html')


def browse_jobseeker(request):
    return render(request, 'browse_jobseeker.html')


def interested_jobs(request):
    return render(request, 'interested_jobs.html')


def job_appliers(request):
    return render(request, 'job_appliers.html')


def changepassword(request):
    return render(request, 'changepassword.html')


def Contacted_com(request):
    return render(request, 'Contacted_com.html')


def shortlisted_com(request):
    return render(request, 'shortlisted_com.html')


def shortlisted_jobs(request):
    return render(request, 'shortlisted_jobs.html')


def applier_profile(request):
    return render(request, 'applier_profile.html')


def company_details(request):
    return render(request, 'company_details.html')

