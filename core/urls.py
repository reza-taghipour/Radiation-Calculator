"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path , include
from calculator.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('',home_view),
    path('pdd/',Pdd.as_view()),
    path('rectangle-to-square/',rec_to_sq.as_view()),
    path('tar-to-pdd/',TarToPdd.as_view()),
    path('ssd-to-another-ssd/',SsdToSsd.as_view()),
    path('ssd-monitor-unit/',MuSsd.as_view()),
    path('sad-monitor-unit/',MuSadTechnique.as_view()),
]
