from django.conf.urls import url
from . import views
urlpatterns = [
   # url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^$', views.get_name, name='get_name'),
    url(r'^thanks/$', views.thank_you, name='thank_you'),
    url(r'^your_name/$', views.get_name, name='get_name'),]
