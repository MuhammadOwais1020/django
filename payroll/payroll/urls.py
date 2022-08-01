"""payroll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from payroll_app import views as pApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", pApp.home, name="home"),
    path("home", pApp.home, name="home"),
    path("admin", pApp.admin, name="admin"),
    path("admin_f", pApp.admin_f, name="admin_f"),
    path('adminLogin', pApp.adminLogin, name="adminLogin"),
    path('createUser', pApp.createUser, name="createUser"),
    path('allUsers', pApp.allUsers, name="allUsers"),
    path('userLogin', pApp.userLogin, name="userLogin"),
    path('logout', pApp.logout, name="logout"),
    path('adminLogout', pApp.adminLogout, name="adminLogout"),
    path('createBusiness', pApp.createBusiness, name='createBusiness'),
    path('payPeriod', pApp.payPeriod, name="payPeriod"),
    path('createPayPeriod', pApp.createPayPeriod, name="createPayPeriod"),
    path('businessView', pApp.businessView, name="businessView")
]
