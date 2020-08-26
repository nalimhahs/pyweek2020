from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home,name="home"),
    path('signup/',views.SignUp,name="signup"),
    path('login/',views.Login,name="login"),
    path('logout/',views.Logout,name="logout"),
    path('sm/',views.StudyMaterial,name="studymaterial"),
    path('events/',views.EventRegister,name="eventregister"),
    path('confirm/',views.Confirm,name="confirm"),
    path('klepsydra/<str:val>/',views.AdminData,name="data"),
    path('guide/',views.Install,name="install"),
]
