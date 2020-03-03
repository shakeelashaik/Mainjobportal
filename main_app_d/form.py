from django import forms
from .models import Jobseeker,Createjob,Bookmarks,Intrestedjobs


GEN = (
        ('', 'Select...'),
        ('M', 'Male'),
        ('FM', 'Female'),
        ('OT', 'Others')
    )
CITY = (
        ('', 'Choose...'),
        ('', 'Choose...'),
        ('hyd', 'hyderabad'),
        ('ban', 'banglore'),
        ('ch', 'chennai')
    )
PASSPORT=(
        ('', 'Select...'),
        ('Y', 'Yes'),
        ('N','No')
    )
MARITAL_STATUS=(
    ('', 'Select...'),
    ('M', 'Married'),
    ('UM', 'Unmarried')
    )
DESIRE_JOBTYPE=(
    ('', 'Select...'),
    ('WH', 'Work from Home'),
    ('In', 'Internship'),
    ('PT', 'PartTime'),
    ('FT', 'FullTime'),
    ('Govt' 'Governmentjob')
)
DESIRED_DESIGNATION=(
    ('', 'Select...'),
    ('PythonDev', 'PythonDeveloper'),
    ('PHPDev', 'PhpDeveloper')



)
TOTALWORK_EXPERIANCE=(





)
EXPECT_PACKAGE=(




)
DESIRED_SHIFT=(




)
DESIRED_INDUSTRY=(



)
AVAIL_JOIN=(




)
QUALIFICATION=(





)
EXPERIANCE=(






)