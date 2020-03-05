from django import forms
from .models import Jobseeker, Createjob, Bookmarks, Intrestedjobs
from .data import PASSPORT, GEN, MARITAL_STATUS, DESIRED_SHIFT, DESIRE_JOBTYPE, QUALIFICATION, Hiring_Process, Eligible_for


class Jobseekers(forms.ModelForm):
    passport = forms.ChoiceField(choices=PASSPORT)
    gender = forms.ChoiceField(choices=GEN)
    maritual_status = forms.ChoiceField(choices=MARITAL_STATUS)
    job_type = forms.ChoiceField(choices=DESIRE_JOBTYPE)
    desired_shift = forms.ChoiceField(choices=DESIRED_SHIFT)
    qualification = forms.ChoiceField(choices=QUALIFICATION)

    class Meta:
        model = Jobseeker
        fields = '__all__'
        exclude = ('user',)


class Create_job(forms.ModelForm):
    hiring_process = forms.ChoiceField(choices=Hiring_Process)
    job_type = forms.ChoiceField(choices=DESIRE_JOBTYPE)
    education = forms.ChoiceField(choices=QUALIFICATION)
    flexible_for = forms.ChoiceField(choices=DESIRED_SHIFT)
    eligible_for = forms.ChoiceField(choices=Eligible_for)

    class Meta:
        model = Createjob
        fields = '__all__'
        exclude = ('user',)