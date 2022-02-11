from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from .forms import AddJobForm,AdminLoginForm,AdminSignupForm
from .models import Job,Application


from django.contrib.auth.models import User
# Create your views here.




class AdminSignupView(TemplateView):

    def get(self, request, *args, **kwargs):
        form=AdminSignupForm()
        context={}
        context["form"]=form
        return render(request,"admin_signup.html",context)

    def post(self,request):
        context={}
        form=AdminSignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("Admin registration success")
            return redirect("signin")
        else:
            context["form"]=form
            return render(request,"admin_signup.html",context)



class AdminLoginView(TemplateView):
    def get(self, request, *args, **kwargs):
        form=AdminLoginForm()
        context={"form":form}
        return render(request,"admin_login.html",context)

    def post(self,request):
        form=AdminLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user = authenticate(request,username=username,password=password)
            if(user):
                login(request,user)
                return redirect("home")

            else:
                return render(request,"login.html",{"form":form})


def Signout(request):
    logout(request)
    return redirect("login")


class Fun(TemplateView):
    template_name = "dashboard.html"



class AddJobView(CreateView):
    model = Job
    success_url = reverse_lazy("home")
    form_class = AddJobForm
    template_name = "add_job.html"

class ListJobView(ListView):
    model = Job
    template_name = "list_job.html"
    context_object_name = "jobs"




class DeleteJobView(DeleteView):
    model = Job
    template_name = "delete_job.html"
    success_url = reverse_lazy("home")
    pk_url_kwarg = "id"

class JobEditView(UpdateView):
    model = Job
    form_class = AddJobForm
    success_url = reverse_lazy("listjob")
    pk_url_kwarg = "id"
    template_name = "edit_job.html"




class CountJob(ListView):
    model = Job
    template_name = "test.html"
    context_object_name = "jobs"

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)

        totaljob=self.model.objects.all()
        context["totaljob"]=totaljob

        context["totaljob_count"]=totaljob.count()
        return context


class ViewApplications(ListView):
    model = Application
    template_name = "applications.html"
    context_object_name = "applications"


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)

        totalapplications=self.model.objects.all()
        context["totalapplications"]=totalapplications

        context["totaljob_applications"]=totalapplications.count()
        return context


