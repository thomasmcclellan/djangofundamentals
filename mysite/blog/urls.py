from django.conf.urls import url 
from . import views

urlpatterns = [
  url(r'^$',views.PostListView.as_view(),name='post_list'),
  url(r'^about/$',views.AboutView.as_view(),name='about'),
  url(r'^post/(?p<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
  url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
  url(r'^post/(?p<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
  url(r'^post/(?p<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
  url(r'^drafts/$',views.DraftListView.as_view(),name='post_draft_list'),
  url(r'^post/(?p<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
  url(r'^comment/(?p<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
  url(r'^comment/(?p<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
  url(r'^post/(?p<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
]