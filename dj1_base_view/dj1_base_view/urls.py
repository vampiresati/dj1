"""dj1_base_view URL Configuration

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
from django.contrib import admin
from django.urls import path
from firstapp.views import MyView,MyTemplateView,MyRedirectView,MyListView,StudentCreateView,StudentUpdateView,StudentDeleteView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',MyView.as_view(),name='baseview'),
    path('index/<int:year>/<int:month>',MyView.as_view(),name='baseview'),
    path('mytemplate',MyTemplateView.as_view(),name='mytemplate'),
    path('redirectview', MyRedirectView.as_view(), name='redirectview'),
    path('listview', MyListView.as_view(), name='listview'),
    path('createview', StudentCreateView.as_view(), name='createview'),
    path('updateview/<pk>', StudentUpdateView.as_view(), name='updateview'),
    path('deleteview/<pk>', StudentDeleteView.as_view(), name='deleteview'),


]
