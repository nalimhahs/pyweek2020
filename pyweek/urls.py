from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('codingcrew/', admin.site.urls),
    path('',include('pyweekapp.urls')),
]
