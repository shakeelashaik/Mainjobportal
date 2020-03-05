from django.db import models


class City(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city


class State(models.Model):
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.state


class Country(models.Model):
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country


class Languages(models.Model):
    lang = models.CharField(max_length=50)

    def __str__(self):
        return self.lang


class Experience(models.Model):
    experiance = models.CharField(max_length=50)

    def __str__(self):
        return self.experiance


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Designation(models.Model):
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.designation


class Industries(models.Model):
    industry = models.CharField(max_length=50)

    def __str__(self):
        return self.industry


class Functional_area(models.Model):
    fun_area = models.CharField(max_length=100)

    def __str__(self):
        return self.fun_area


class Package(models.Model):
    package = models.CharField(max_length=50)

    def __str__(self):
        return self.package


class Jobseeker(models.Model):
    user1 = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    fname1 = models.CharField(max_length=50)
    lname1 = models.CharField(max_length=50)
    email1 = models.EmailField()
    mobile1 = models.IntegerField()
    uploadresume = models.FileField(upload_to='resume')
    passport = models.CharField(max_length=50)
    address1 = models.CharField(max_length=200)
    location1 = models.ForeignKey(City, on_delete=models.CASCADE)
    fathername1 = models.CharField(max_length=50)
    dob1 = models.DateField()
    hobbies = models.CharField(max_length=200)
    languages_known = models.ForeignKey(Languages, on_delete=models.CASCADE)
    gender1 = models.CharField(max_length=50)
    maritual_status = models.CharField(max_length=50)
    career_objective = models.CharField(max_length=300)
    desire_job_title = models.CharField(max_length=50)
    desired_job_type = models.CharField(max_length=50)
    desired_designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    work_experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    expect_package = models.ForeignKey(Package, on_delete=models.CASCADE)
    desired_shipt = models.CharField(max_length=50)
    desire_location = models.CharField(max_length=50)
    desire_industry = models.ForeignKey(Industries, on_delete=models.CASCADE)
    availability_join = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    y_o_p = models.IntegerField()
    percentage = models.IntegerField()
    skills = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    job_description = models.CharField(max_length=100)
    facebook = models.URLField()
    google = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    pinterest = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return self.email1


class Createjob(models.Model):
    user2 = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    job_title = models.CharField(max_length=50)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    job_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industries, on_delete=models.CASCADE)
    fun_area = models.ForeignKey(Functional_area, on_delete=models.CASCADE)
    hiring_process = models.CharField(max_length=50)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    no_of_vacancies = models.IntegerField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    jobtype = models.CharField(max_length=50)
    job_location = models.ForeignKey(City, on_delete=models.CASCADE)
    key_skills = models.CharField(max_length=50)
    edu_qualification = models.CharField(max_length=50)
    yop = models.IntegerField()
    qualification_marks = models.CharField(max_length=50)
    language_known = models.CharField(max_length=50)
    eligible_for = models.CharField(max_length=50)
    comp_type = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    email = models.EmailField()
    contact_num = models.IntegerField()
    alt_num = models.IntegerField()
    website_link = models.URLField()
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    zipcode = models.IntegerField()
    company_logo = models.ImageField(upload_to='logo')
    interview_location = models.CharField(max_length=50)
    contact_prole = models.CharField(max_length=50)
    contact_pname = models.CharField(max_length=50)
    contactperson_mail = models.EmailField()
    job_summary = models.CharField(max_length=200)
    responsibilities_duties = models.CharField(max_length=200)
    req_experiance = models.CharField(max_length=200)
    benfits = models.CharField(max_length=100)
    company_description = models.CharField(max_length=200)
    facebook = models.URLField()
    google = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    pinterest = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return self.email


class Register(models.Model):
    user3 = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    your = models.CharField(max_length=50)

    def __str__(self):
        return self.your


class Bookmarks(models.Model):
    user4 = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    book = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)

    def __str__(self):
        return self.book


class Shortlisted_profile(models.Model):
    user5 = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    short_prof = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)

    def __str__(self):
        return self.short_prof


class Contacted_profile(models.Model):
    user6 = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    c_prof = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)

    def __str__(self):
        return self.c_prof


class Shortlisted_jobs(models.Model):
    user7 = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    short_job = models.ForeignKey(Createjob, on_delete=models.CASCADE)

    def __str__(self):
        return self.short_job


class Shortlisted_company(models.Model):
    user8 = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    short_compy = models.ForeignKey(Createjob, on_delete=models.CASCADE)

    def __str__(self):
        return self.short_compy


class Intrestedjobs(models.Model):
    user9 = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    int_job = models.ForeignKey(Createjob, on_delete=models.CASCADE)

    def __str__(self):
        return self.int_job


class Notintrestedjobs(models.Model):
    user10 = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    notint_job = models.ForeignKey(Createjob, on_delete=models.CASCADE)

    def __str__(self):
        return self.notint_job


class Appliedjobs(models.Model):
    user11 = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ap_job = models.ForeignKey(Createjob, on_delete=models.CASCADE)

    def __str__(self):
        return self.ap_job

