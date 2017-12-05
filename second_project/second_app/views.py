from django.shortcuts import render
# from django.http import HttpResponse
from second_app.models import User

# Create your views here.

def index(request):
  # return HttpResponse('<em>My Second Project</em>')
  return render(request,'second_app/index.html')

# def help(request):
#   help_dict = {'help_insert':'HELP PAGE'}
#   return render(request,'second_app/help.html',context=help_dict)

def users(request):
  user_list = User.objects.order_by('first_name')
  user_dict = {'users':user_list}
  return render(request,'second_app/users.html',context=user_dict)