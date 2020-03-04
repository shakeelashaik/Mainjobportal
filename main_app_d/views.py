from django.shortcuts import render
def emp_index(request):
    return render(request,'index2.html')
def create_job(request):
    return render(request,'create_job.html')
def browse_employer(request):
    return render(request,'browse_employer.html')
def con_pro(request):
    return render(request,'contacted_pro.html')
def job_appliers(request):
    return render(request,'job_appliers.html')
def posted_jobs(request):
    return render(request,'posted_jobs.html')
# def shortlisted_jobs(request):
#     return render(request,'shortlisted_jobs.html')
def shortlisted_pro(request):
    return render(request,'shortlisted_profiles.html')
def empchangepass(request):
    return render(request,'empchangepass.html')
# def sent_jobs(request):
#     return render(request,'sent_jobs.html')
def emp_pro(request):
    return render(request,'emp_profile.html')
def emp_proedit(request):
    return render(request,'emp_pro_edit.html')
def bookmark_pro(request):
    return render(request,'bookmarks.html')