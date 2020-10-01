from django import forms
from django.contrib.auth.models import User
from mmp_app.models import Faculty,Student,UploadFile
from django.forms import ClearableFileInput

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model=User
		fields=('username','email','password')


class StudentProfileInfoForm(forms.ModelForm):
	
	class Meta():
		model=Student
		fields=('student_name','student_branch','courses')


class FacultyProfileInfoForm(forms.ModelForm):
	
	class Meta():
		model=Faculty
		fields=('faculty_name','faculty_dept','courses')


class FileUploadForm(forms.ModelForm):

    class Meta():
        model = UploadFile
        fields = ['files']
        widgets = {
            'files': ClearableFileInput(attrs={'multiple': True}),
        }