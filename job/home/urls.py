from django.urls import path
from home import views

urlpatterns=[
    path('dashboard',views.Fun.as_view(),name="home"),
    path('admin/signup',views.AdminSignupView.as_view(),name="signup"),
    path('admin/signin',views.AdminLoginView.as_view(),name="signin"),
    path('admin/logout',views.Signout,name="logout"),
    path('job/add',views.AddJobView.as_view(),name="addjob"),
    path('job/list',views.ListJobView.as_view(),name="listjob"),
    path('job/edit/<int:id>',views.JobEditView.as_view(),name="editjob"),
    path('job/delete/<int:id>',views.DeleteJobView.as_view(),name="deletejob"),
    path('job/count',views.CountJob.as_view(),name="count"),
    path('job/applications',views.ViewApplications.as_view(),name="applications")





]