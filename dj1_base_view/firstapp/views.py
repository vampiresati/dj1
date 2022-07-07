from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
class MyView(View):

    def get(self, request, *args, **kwargs):
        a='Hello, World!'+str(request)+str(args)+str(kwargs)
        return HttpResponse(a)
class MyTemplateView(TemplateView):
    template_name='greeting_template.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['satvir_greeting']='hi from satvir how are you'
        return context
class MyRedirectView(RedirectView):
    """Provide a redirect on any GET request."""
    permanent = False
    url = None
    pattern_name = 'baseview'
    query_string = False

    # def get_redirect_url(self, *args, **kwargs):
    #
    #     return super().get_redirect_url(self, *args, **kwargs)


