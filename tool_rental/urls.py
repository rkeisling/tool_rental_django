from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^pricing/$', views.pricing, name='pricing'),
    url(r'^rules/$', views.rules, name='rules'),
    url(r'^tool_list/$', views.tool_list, name='tool_list'),
    url(r'^rent_tool/$', views.rent_tool, name='rent_tool'),
]
