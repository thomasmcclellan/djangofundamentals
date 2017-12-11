from django.shortcuts import render
from .models import Post,Comment
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
class AboutView(TemplateView):
  template_name = 'about.html'

class PostListView(ListView):
  model = Post 

  def get_queryset(self):
    # __lte => for querysets, you can add actual queries
    # Here, lte = less than or equal to
    # '-published_date' => - allows you to change ascending or descending order
    return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
  model = Post 

# LoginRequiredMixin similar to decorators (@Something)
class CreatePostView(LoginRequiredMixin,CreateView):
  login_url = '/login/'
  redirect_field_name = 'blog/post_detail.html'
  form_class = PostForm
  model = Post 

class PostUpdateView(LoginRequiredMixin,UpdateView):
  login_url = '/login/'
  redirect_field_name = 'blog/post_detail.html'
  form_class = PostForm
  model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
  model = Post
  # reverse_lazy similar to async await
  success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
  login_url = '/login/'
  redirect_field_name = 'blog/post_list.html'
  model = Post 

  def get_queryset(self):
    return post.objects.filter(published_date__isnull=True).order_by('-created_date')