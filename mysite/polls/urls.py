from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
               #url('^', include('django.contrib.auth.urls')),
	url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	
	url(r'^$', views.ConnexionView.as_view(), name='connexion'),
]
