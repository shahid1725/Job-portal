from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import HireJob
from django.forms import ModelForm
from home.models import Application

class UserSignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class UserLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form_control"}))




class AddHireJobForm(ModelForm):
    class Meta:
        model= HireJob
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
