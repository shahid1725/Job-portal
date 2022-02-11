from django import forms
from django.forms import ModelForm

from home.models import Job,Application,HireApplication
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





class AddJobForm(ModelForm):
    class Meta:
        model= Job
        fields=["title","company","location","experience","eligibility","notice_period","description","posted_date","image"]

        widget={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "company": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "experience": forms.TextInput(attrs={"class": "form-control"}),
            "eligibility": forms.TextInput(attrs={"class": "form-control"}),
            "notice_period": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"})),
            "posted_date":forms.DateInput(attrs={"type":"date"}),

        }

        labels={
            "title":"Job Title",
            "company":"Company Name",
            "location":"Location",
            "experience":"Experience",
            "eligibility":"Eligibility",
            "notice_period":"Notice Period",
            "description":"Description",
            "posted_date":"Posted date",
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields=["first_name","last_name","email","phone","location","experience","qualification","skills","income"]

        labels={
            "first_name":"First Name",
            "last_name":"Last Name",
            "email":"Email",
            "phone":"Phone",
            "location":"Location",
            "experience":"Experience",
            "qualification":"Qualification",
            "skills":"Skills",
            "income":"Expecting Annual Income",
        }

        widget={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "experience": forms.TextInput(attrs={"class": "form-control"}),
            "qualification": forms.TextInput(attrs={"class": "form-control"}),
            "skills": forms.TextInput(attrs={"class": "form-control"}),
            "income": forms.NumberInput(attrs={"class": "form-control"}),
        }


class HireApplicationForm(forms.ModelForm):
    class Meta:
        model = HireApplication
        fields=["first_name","last_name","email","phone","location","experience","qualification","skills","income"]

        labels={
            "first_name":"First Name",
            "last_name":"Last Name",
            "email":"Email",
            "phone":"Phone",
            "location":"Location",
            "experience":"Experience",
            "qualification":"Qualification",
            "skills":"Skills",
            "income":"Expecting Annual Income",
        }

        widget={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "experience": forms.TextInput(attrs={"class": "form-control"}),
            "qualification": forms.TextInput(attrs={"class": "form-control"}),
            "skills": forms.TextInput(attrs={"class": "form-control"}),
            "income": forms.NumberInput(attrs={"class": "form-control"}),
        }

class AdminSignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class AdminLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form_control"}))



