from django.urls import path
from user import views

urlpatterns=[
    path('user/home',views.UserHome.as_view(),name="userhome"),
    path('user/signup',views.UserSignupView.as_view(),name="registration"),
    path('user/signin',views.UserLoginView.as_view(),name="login"),
    path('user/signout',views.Signout,name="signout"),
    # path('search',views.SearchJob.as_view(),name="search"),
    path('search/job',views.SearchJob.as_view(),name="searching"),
    path('apply/<int:id>',views.JobApplyView.as_view(),name="apply"),
    path('submitted',views.ViewApplications.as_view(),name="submitted"),
    path('hire/add',views.AddHireJobView.as_view(),name="hireadd"),
    path('hire/list',views.MyHiringsView.as_view(),name="hirelist"),
    path('hire/delete/<int:id>',views.DeleteHireJobView.as_view(),name="hiredelete"),
    path('hire/edit/<int:id>',views.EditHireJobView.as_view(),name="hireedit"),
    path('hire/application/<int:id>',views.HireJobApplyView.as_view(),name="hireapply"),
    path('hire/submitted', views.ViewHireApplications.as_view(), name="hiresubmitted"),


]