from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import  DeleteView,UpdateView,TemplateView,CreateView,ListView
from user.forms import UserSignupForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout
from home.models import Job,Application,HireApplication
from home.forms import AddJobForm,ApplicationForm,HireApplicationForm
from .forms import AddHireJobForm
from .filters import SearchFilter
from django.contrib import messages
from .models import HireJob

# Create your views here.

class UserHome(TemplateView):

    model = Job
    template_name = "index.html"


    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all()
        hires = HireJob.objects.all()
        context={"jobs":jobs,"hires":hires}
        return render(request,'index.html',context)






class SearchJob(TemplateView):
    model = Job
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SearchFilter(self.request.GET, queryset=self.get_queryset())
        return context



# class JobSearchView(TemplateView):
#     template_name = "search.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         f = SearchFilter(self.request.GET,queryset=Job.objects.all())
#         context["filter"]=f
#         return context

# class JobSearchView(ListView):
#     model = Job
#     template_name = 'search.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         object_list = Job.objects.filter(
#             Q(title__icontains=query)
#         )
#         return object_list


class UserSignupView(TemplateView):

    def get(self, request, *args, **kwargs):
        form=UserSignupForm()
        context={}
        context["form"]=form
        return render(request,"registration.html",context)

    def post(self,request):
        context={}
        form=UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("user registration success")
            return redirect("login")
        else:
            context["form"]=form
            return render(request,"registration.html",context)



class UserLoginView(TemplateView):
    def get(self, request, *args, **kwargs):
        form=UserLoginForm()
        context={"form":form}
        return render(request,"login.html",context)

    def post(self,request):
        form=UserLoginForm(request.POST)
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


class JobApplyView(TemplateView):
    model = Application
    form_class=ApplicationForm
    template_name = "testing.html"
    context={}

    def get(self, request, *args, **kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        job_id=kwargs["id"]
        job_item=Job.objects.get(id=job_id)


        form=self.form_class(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            location = form.cleaned_data["location"]
            experience = form.cleaned_data["experience"]
            qualification = form.cleaned_data["qualification"]
            skills= form.cleaned_data["skills"]
            income = form.cleaned_data["income"]


            application=self.model.objects.create(
                job_name=job_item,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                location=location,
                experience=experience,
                qualification=qualification,
                skills=skills,
                income=income,
            )

            application.save()
            job_item.save()


            messages.success(request,"Your Application has been submitted")
            return redirect("userhome")


class ViewApplications(ListView):
    model = Application
    template_name = "submitted.html"
    context_object_name = "applications"


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)

        totalapplications=self.model.objects.all()
        context["totalapplications"]=totalapplications

        context["totaljob_applications"]=totalapplications.count()
        return context


# hiring

class AddHireJobView(CreateView):
    model = HireJob
    success_url = reverse_lazy("userhome")
    form_class = AddHireJobForm
    template_name = "hire_add.html"

class ListHireJobView(ListView):
    model = HireJob
    template_name = "index.html"
    context_object_name = "jobs"

class MyHiringsView(ListView):
    model = HireJob
    template_name = "hire_list.html"
    context_object_name = "jobs"

class DeleteHireJobView(DeleteView):
    model = HireJob
    template_name = "hire_delete.html"
    success_url = reverse_lazy("userhome")
    pk_url_kwarg = "id"

class EditHireJobView(UpdateView):
    model = HireJob
    form_class = AddHireJobForm
    success_url = reverse_lazy("userhome")
    pk_url_kwarg = "id"
    template_name = "hire_edit.html"

class HireJobApplyView(TemplateView):
        model = HireApplication
        form_class = HireApplicationForm
        template_name = "hire_applications.html"
        context = {}

        def get(self, request, *args, **kwargs):
            form = self.form_class()
            self.context["form"] = form
            return render(request, self.template_name, self.context)

        def post(self, request, *args, **kwargs):
            job_id = kwargs["id"]
            job_item = HireJob.objects.get(id=job_id)

            form = self.form_class(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                email = form.cleaned_data["email"]
                phone = form.cleaned_data["phone"]
                location = form.cleaned_data["location"]
                experience = form.cleaned_data["experience"]
                qualification = form.cleaned_data["qualification"]
                skills = form.cleaned_data["skills"]
                income = form.cleaned_data["income"]

                application = self.model.objects.create(
                    job_name=job_item,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    location=location,
                    experience=experience,
                    qualification=qualification,
                    skills=skills,
                    income=income,
                )

                application.save()
                job_item.save()

                messages.success(request, "Your Application has been submitted")
                return redirect("userhome")


class ViewHireApplications(ListView):
    model = HireApplication
    template_name = "hire_submitted.html"
    context_object_name = "applications"
    page_kwarg = "id"


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)

        totalapplications=self.model.objects.all()
        context["totalapplications"]=totalapplications

        context["totaljob_applications"]=totalapplications.count()
        return context




