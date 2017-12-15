from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def home(request):
  post = Post.objects.order_by('-pub_date')

  return render(request, 'posts/home.html',{'post':post})

def post_detail(request,post_id):
  post = get_object_or_404(Post,pk=post_id)
  return render(request,'posts/post_detail.html',{'post':post})