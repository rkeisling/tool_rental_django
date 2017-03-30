from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^home/$', views.rent_tool, name='home'),
    url(r'^pricing/$', views.pricing, name='pricing'),
    url(r'^rules/$', views.rules, name='rules'),
    url(r'^home/rent_tool/$', views.rent_tool, name='rent_tool'),
    url(r'^error/$', views.error, name='error   ')
]
