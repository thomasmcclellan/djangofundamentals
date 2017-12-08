from django.conf.urls import url 
from cbv_app import views

app_name = 'cbv_app'

urlpatterns = [
  url(r'^$',views.SchoolListView.as_view(),name='list'),
  # pk = primary key from school_list.html {{ school.id }}
  # Grab this basic app plus school id
  url(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
  url(r'^create/$',views.SchoolCreateView.as_view(),name='create'),
  url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),
  url(r'^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='delete'),
]