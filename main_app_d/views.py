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

def emp_index(request):
    return render(request, 'index2.html')


def create_job(request):
    return render(request, 'create_job.html')


def browse_employer(request):
    return render(request, 'browse_employer.html')


def con_pro(request):
    return render(request, 'contacted_pro.html')


def job_appliers(request):
    return render(request, 'job_appliers.html')


def posted_jobs(request):
    return render(request, 'posted_jobs.html')


def shortlisted_pro(request):
    return render(request, 'shortlisted_profiles.html')


def empchangepass(request):
    return render(request, 'empchangepass.html')



def emp_pro(request):
    return render(request, 'emp_profile.html')


def emp_proedit(request):
    return render(request, 'emp_pro_edit.html')


def bookmark_pro(request):
    return render(request, 'bookmarks.html')