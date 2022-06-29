from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Student
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
class MyListView1(ListView):
    model = Student
    paginate_by = 2
class MyListView(ListView):
    model = Student
    paginate_by = 10
    context_object_name = 'student_list'
class StudentCreateView(CreateView):
    model=Student
    fields=['first_name','last_name','roll_number']
    # success_url = reverse_lazy('listview')
    def get_success_url(self):
        return reverse('listview')
class StudentUpdateView(UpdateView):
    model=Student
    template_name_suffix = '_update_form'
    fields=['first_name','last_name','roll_number']
    # success_url = reverse_lazy('listview')
    def get_success_url(self):
        return reverse('listview')
class StudentDeleteView(DeleteView):
    model=Student
    # success_url = reverse_lazy('listview')
    def get_success_url(self):
        return reverse('listview')