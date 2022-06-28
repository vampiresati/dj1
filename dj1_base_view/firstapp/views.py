from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView

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