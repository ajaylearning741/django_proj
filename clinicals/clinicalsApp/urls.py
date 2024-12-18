"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from clinicalsApp.views import PatientListView,PatientCreateView,PatientUpdateView,PatientDeleteView,addData,analyze



urlpatterns = [

    path('', PatientListView.as_view(),name='index'),
    path('create/',PatientCreateView.as_view()),
    path('update/<int:pk>/',PatientUpdateView.as_view()),
    path('delete/<int:pk>/',PatientDeleteView.as_view()),
    path('addData/<int:pk>/',addData),
    path('analyze/<int:pk>/',analyze)

]
