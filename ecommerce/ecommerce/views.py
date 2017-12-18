from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
  context = {
    'title':'Home Page!!',
    'content':'Welcome to the HOME PAGE'
  }
  return render(request,'home_page.html',context)

def about_page(request):
  context = {
    'title':'About Page!!',
    'content':'Welcome to the ABOUT PAGE'
  }
  return render(request,'home_page.html',context)

def contact_page(request):
  contact_form = ContactForm(request.POST or None)
  context = {
    'title':'Contact Page!!',
    'content':'Welcome to the CONTACT PAGE',
    'form':contact_form
  }
  if contact_form.is_valid():
    print(contact_form.cleaned_data)
  if request.method == 'POST':
    print(request.POST)
  return render(request,'contact/view.html',context)