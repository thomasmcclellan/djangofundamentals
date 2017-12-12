"""second_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.conf import settings
from second_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    # url(r'^help/',include('second_app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^users/',include('second_app.urls')),
]

if settings.DEBUG:
  import debug_toolbar
  urlpatterns = [
    url(r'^__debug__/',include(debug_toolbar.urls))
  ] + urlpatterns
