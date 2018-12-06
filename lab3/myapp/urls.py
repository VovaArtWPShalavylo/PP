"""kalendar_application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import  LogoutView
from django.urls import include, path
from . import views

urlpatterns = [
    path(' ', views.IndexTemplateView.as_view(), name='index'),
    path('calendar', views.CalendarListView.as_view(), name='calendar'),
    path('signup', views.signup, name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout',LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('entry/<int:pk>', views.EntryDetailView.as_view(), name='details'),
    path('entry/add', views.add, name='add'),
    path('entry/delete/<int:pk>', views.delete, name='delete'),
    path('myevent',views.myevent,name = 'myevent'),

   # url(r'', views.show)
]
