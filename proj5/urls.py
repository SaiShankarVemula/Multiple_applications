"""
URL configuration for proj5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import *
from app2.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1_String/',app1_String,name='app1_String'),
    path('app1_HTML/',app1_HTML,name='app1_HTML'),
    path('app2_String/',app2_String,name='app2_String'),
    path('app2_HTML/',app2_HTML,name='app2_HTML'),
]