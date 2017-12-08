from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy
# Create your views here.
class IndexView(TemplateView):
  template_name = 'index.html'

# # **kwargs = keyword argument except for those corresponding to the parameter as a dictionary
# # stackoverflow.com/questions/36901/what-does-double-star-and-star-do-for-parameters
#   def get_context_data(self,**kwargs):
#     context = super().get_context_data(**kwargs)
#     context['inject_me'] = 'BASIC INJECTION'
#     return context 

class SchoolListView(ListView):
  # school_list = 'schools'
  context_object_name = 'schools'
  model = models.School 
  

class SchoolDetailView(DetailView):
  context_object_name = 'school_detail'
  model = models.School
  template_name = 'cbv_app/school_detail.html'

class SchoolCreateView(CreateView):
  fields = ('name','principle','location')
  model = models.School

class SchoolUpdateView(UpdateView):
  fields = ('name','principle')
  model = models.School

class SchoolDeleteView(DeleteView):
  model = models.School
  success_url = reverse_lazy('cbv_app:list')