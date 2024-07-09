"""
URL configuration for clinicaldataproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from clinicaldataapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.display),
    path('create/',views.Create),
    path('delete/<int:id>',views.Delete),
    path('update/<int:id>',views.Update),
    path('data/<int:id>',views.Data),
    path('report/<int:id>',views.ReportData)
]
