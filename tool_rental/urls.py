from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.tool_list, name='tool_list'),
]
